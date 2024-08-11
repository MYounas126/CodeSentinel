import streamlit as st
import os
from codeReview.gitCode import analyze_repository, output_messages
from scrapers.js_scraper import scrape_js_sync
import chardet

def analyze_uploaded_file(uploaded_file):
    # Read the contents of the uploaded file
    try:
        # Read the file as bytes
        file_contents = uploaded_file.read()
        
        # Detect encoding
        detected_encoding = chardet.detect(file_contents)['encoding']
        
        # Decode the contents
        file_contents = file_contents.decode(detected_encoding or 'utf-8')
        
        # Perform your analysis on the decoded contents
        # For example, you could call a function here to analyze the contents
        # analyze_file_contents(file_contents)
        
        st.write("File analysis complete. Here are the contents:")
        st.text(file_contents)  # Display the contents or results of the analysis
        
    except UnicodeDecodeError as e:
        st.error(f"Error decoding the uploaded file: {e}")
    except Exception as e:
        st.error(f"An error occurred while analyzing the file: {e}")

def main():
    st.title('Secure Eye App')

    # Create a text input for the GitHub URL or Local Path
    url = st.text_input('Enter the GitHub URL or Local path:')

    # Create a file uploader for local files
    uploaded_file = st.file_uploader('Or upload a file:', type=['zip', 'py', 'js', 'html', 'css'])

    # Add a checkbox for recursive scraping
    recursive = st.checkbox('Enable recursive scraping for JS')

    # Create a button to trigger the analysis
    if st.button('Analyze'):
        if url:
            # If a URL is provided, analyze the GitHub repository or scrape JS
            st.write('Analyzing...')
            if url.endswith('.git'):
                analyze_repository(url)  # Call your analysis function for GitHub repository
            else:
                scrape_js_sync(url, recursive)  # Call the JS scraping function
            
            for message in output_messages:
                st.write(message)
            output_messages.clear()
            st.write('Analysis complete.')  # Show the results here
            
            # Display markdown reports
            report_path = f"report/{url.split('/')[-1].replace('.git', '')}" if 'http' in url else f"report/{os.path.basename(url)}"
            if os.path.exists(report_path):
                reports = [f for f in os.listdir(report_path) if f.endswith('.md')]
                selected_report = st.selectbox('Select a report:', ['Select...'] + reports)
                if selected_report != 'Select...':
                    with open(os.path.join(report_path, selected_report), 'r') as file:
                        st.markdown(file.read())
        elif uploaded_file:
            # If a file is uploaded, analyze the local file
            st.write('Analyzing the uploaded file...')
            analyze_uploaded_file(uploaded_file)  # Call the function to analyze the uploaded file
        else:
            st.warning('Please enter a GitHub URL or upload a file.')

if __name__ == '__main__':
    main()