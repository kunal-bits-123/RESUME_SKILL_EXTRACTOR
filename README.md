Resume Skill Extractor
======================

> Assignment Submission for CSFirst WindsurfCreated by: _\[Kunal Jain\]_Personal project for the AI Support Engineer role assignment

Project Overview
----------------

This project enables users to upload PDF resumes and automatically extract key information such as:

*   Name
    
*   Email
    
*   Phone Number
    
*   Skills
    
*   Work Experience
    

The extracted data is displayed clearly in the app and stored for future reference. Users can also filter stored resumes by skill, making it easy to search for specific expertise across uploaded resumes.

Features
--------

*   Upload multiple PDF resumes through an intuitive web interface
    
*   Robust extraction of personal info, skills, and work experience using NLP
    
*   Clear, readable summary of parsed resume data
    
*   Persistent storage of extracted results in a JSON file for later use
    
*   Filter stored resumes by skill keyword
    
*   Clean and minimal frontend using Streamlit
    

File Structure
--------------

C:.├── app.py # Main Streamlit app├── create\_resume.py # Script to generate sample fake resumes (PDFs)├── Dockerfile # Docker container setup├── extractor.py # Core resume parsing logic with spaCy├── parsed\_data.json # Stored parsed resume data (auto-generated)├── README.md # This documentation├── requirements.txt # Python dependencies├── storage.py # Data saving and loading utilities├── structure.txt # Project folder structure snapshot├── utils.py # Helper functions└── sample\_resumes # Folder containing sample PDF resumes├── resume\_1.pdf├── resume\_2.pdf└── resume\_3.pdf

Getting Started
---------------

### Prerequisites

*   Python 3.10+
    
*   pip package manager
    
*   (Optional) Docker if you want containerized deployment
    

### Installation

1.  Clone the repo or download the files to your local machine.
    
2.  (Recommended) Create and activate a virtual environment:
    

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python -m venv venv  source venv/bin/activate  # On Windows: venv\Scripts\activate   `

1.  Install required Python packages:
    

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   pip install -r requirements.txt   `

How to Run
----------

### Run Locally with Streamlit

Simply start the Streamlit app:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   streamlit run app.py   `

*   Open your browser at http://localhost:8501
    
*   Upload one or multiple PDF resumes
    
*   View parsed results displayed neatly
    
*   Use the skill filter box to search stored resumes by specific skills
    

### Using Docker

1.  Build the Docker image:
    

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   docker build -t resume-extractor-kunal-jain .   `

1.  Run the container:
    

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   docker run -p 8501:8501 resume-extractor-kunal-jain   `

1.  Access the app at http://localhost:8501
    

How It Works
------------

*   The app uploads and temporarily saves PDFs in memory for parsing
    
*   The extractor.py module uses spaCy and custom logic to extract relevant fields
    
*   Parsed data is stored in parsed\_data.json for persistence
    
*   The UI presents a clean summary of extracted data and allows filtering by skills
    

Notes and Future Improvements
-----------------------------

*   Extraction accuracy depends on the quality and formatting of resumes — improvements to the NLP model and rules can enhance this
    
*   Currently supports only PDF resumes; support for DOCX and other formats can be added
    
*   Skill filtering is case-insensitive but exact-match; could be enhanced with fuzzy matching
    
*   UI can be enhanced with better styling and visual resume previews
    

Credits
-------

Built with Python, spaCy, and Streamlit.
