import argparse
import sys
import logging
import os
import chardet
import re
from codeReview import gitCode
from scrapers.js_scraper import scrape_js_sync
import openai
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s')

def valid_url(url):
    """Validate the URL format."""
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # IP...
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # IPv6...
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

def analyze_files(local_repo_path):
    """Analyze files in the local repository."""
    for filename in os.listdir(local_repo_path):
        file_path = os.path.join(local_repo_path, filename)

        # Read the file as bytes
        try:
            with open(file_path, 'rb') as file:
                file_contents = file.read()

            # Detect encoding
            detected_encoding = chardet.detect(file_contents)['encoding']

            # Decode the contents
            try:
                file_contents = file_contents.decode(detected_encoding or 'utf-8')
                # Proceed with your analysis (you can call your analysis function here)
                logging.info(f"Successfully analyzed {filename}")
            except UnicodeDecodeError as e:
                logging.error(f"Error decoding {file_path}: {e}")
                continue  # Skip this file and continue with the next one

        except FileNotFoundError:
            logging.error(f"File not found: {file_path}")
            continue  # Skip this file and continue with the next one
        except IsADirectoryError:
            logging.error(f"Expected a file but found a directory: {file_path}")
            continue  # Skip this file and continue with the next one
        except Exception as e:
            logging.error(f"Error reading {file_path}: {e}")
            continue  # Skip this file and continue with the next one

def main():
    """Main function to parse arguments and execute the appropriate actions."""
    parser = argparse.ArgumentParser(
        description="Analyze code from a GitHub repository or a local path.",
        epilog="Example usage:\n  python cli.py --url https://github.com/Yash-srivastav16/Tour-Project\n  python cli.py --path /path/to/local/repo"
    )
    parser.add_argument('--url', type=str, help="The URL of the GitHub repository to analyze.")
    parser.add_argument('--path', type=str, help="The full path to the local directory to analyze.")
    parser.add_argument('--js', type=str, help="The URL to analyze JavaScript.")
    parser.add_argument('--recursive', action='store_true', help="Enable recursive scraping for JavaScript files.")
    
    try:
        args = parser.parse_args()
    except SystemExit as e:
        logging.error("Invalid arguments provided. Use --help for more information.")
        sys.exit(1)

    # Validate URL and path arguments
    if args.url and not valid_url(args.url):
        logging.error("Invalid URL format provided.")
        sys.exit(1)

    if args.path and not os.path.exists(args.path):
        logging.error("The specified path does not exist.")
        sys.exit(1)

    try:
        if args.url:
            logging.info(f"Analyzing repository at {args.url}")
            gitCode.analyze_repository(args.url)  # Ensure this function handles its own errors
        elif args.path:
            logging.info(f"Analyzing local path at {args.path}")
            analyze_files(args.path)  # Call the new function to analyze files
        elif args.js:
            logging.info(f"Scraping JavaScript from {args.js} with recursive={args.recursive}")
            scrape_js_sync(args.js, args.recursive)
        else:
            print("Please provide either a GitHub URL with --url, a JS website URL with --js, or a local path with --path.")
    except openai.error.InvalidRequestError as e:
        logging.error(f"Invalid request error: {e}")
    except openai.error.RateLimitError as e:
        logging.error(f"Rate limit exceeded: {e}")
    except KeyboardInterrupt:
        print("\nApplication interrupted by user. Exiting...")
        sys.exit()
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()