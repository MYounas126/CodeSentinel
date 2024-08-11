# CodeSentinel: A Powerful AI-Driven Tool for Secure Code Review

CodeSentinel is a cutting-edge, AI-powered tool designed to streamline and enhance the security of your codebase. It leverages advanced artificial intelligence algorithms to perform comprehensive assessments of your code, pinpointing potential vulnerabilities and security risks. By employing CodeSentinel, you can proactively identify and address security concerns before they become exploitable weaknesses.

# Key Features

## Vulnerability Detection:

 CodeSentinel meticulously examines your code to uncover a wide range of vulnerabilities (Specially OWASP Top 10), including prevalent attack vectors such as SQL injection, Cross-Site Scripting (XSS), buffer overflows, remote code execution and more.

## Secure Coding Practices Evaluation: 

Beyond vulnerability detection, CodeSentinel analyzes your codebase for adherence to secure coding practices. This includes scrutinizing aspects like input validation, output sanitization, robust authentication and access control mechanisms, and proper error handling.

## Detailed Reporting: 

Following a thorough analysis, CodeSentinel generates in-depth reports that provide valuable insights for developers and security professionals. These reports encompass:
- Clear descriptions of each identified vulnerability
- Assigned severity levels to prioritize critical issues
- Affected code snippets
- Actionable Recommendations for improving security posture

## Mitigation Guidance: 

CodeSentinel goes beyond simply identifying vulnerabilities. It empowers developers by offering step-by-step guidance on how to mitigate these issues. This includes providing code snippets that illustrate both the vulnerable code and the recommended secure refactoring.

## Installation

Getting started with CodeSentinel is a breeze. Follow these simple steps to set up and run the tool:

## Prerequisites:

- Python 3.6+
- Virtual environment (recommended)

# Steps:

### 1.Clone the repository

```bash
git clone https://github.com/MYounas126/CodeSentinel.git
```
### 2. Create a Virtual Environment:
It's highly recommended to create a virtual environment to isolate SecureEye's dependencies from your system-wide Python installations. You can achieve this using the following commands:

```bash
python3 -m venv venv
source ./venv/bin/activate  # On Windows use: .\venv\Scripts\activate 
```

### 3. Install Dependencies
After activiting virtual environment on your system, follow this command

```bash
python3 -m pip install -r requirements.txt
```

## Usage
You can use CodeSentinel in two ways:

### 1. Command Line Interface
For users who prefer the command line, CodeSentinel provides a user-friendly CLI interface. To run CodeSentinel using CLI, execute the following command:
```bash 
python3 cli.py --url <repository-url> #Find vulnerability in a Codebase of github repo
```
Replace <repository-url> with the actual URL of the code repository you want to analyze.
There are some other options as well like as we can also use to analyze a --js and --path options for finding vulnerabilities in JS website URL, or a local path respectivley.

### 2. Web Application
CodeSentinel also offers a web application interface for a more interactive experience. To run CodeSentinel as a web application, use the following command:
```bash
streamlit run app.py
```
This will launch the CodeSentinel web interface, allowing you to analyze code repositories through a user-friendly GUI.

![image](https://github.com/MYounas126/CodeSentinel/blob/main/Screenshot%202024-08-11%20130809.png)

## Example Output
Upon analyzing your code, CodeSentinel will generate a comprehensive report that details the identified vulnerabilities. Here's an example of what you might expect:

# Output
Here I have analyze a random github repo and here is the report that CodeSentinel have generate.

![image](https://github.com/MYounas126/CodeSentinel/blob/main/Screenshot%202024-08-11%20141130.png)

![image](https://github.com/MYounas126/CodeSentinel/blob/main/Screenshot%202024-08-11%20141151.png)

This example showcases how CodeSentinel not only identifies an unvalidated input vulnerability but also provides concrete mitigation steps with the corresponding secure code snippet.

## Contributing
CodeSentinel welcomes contributions from the developer community! Feel free to submit a pull request to propose enhancements or bug fixes.

## License
CodeSentinel is licensed under the permissive MIT License. Refer to the LICENSE file for more details.
