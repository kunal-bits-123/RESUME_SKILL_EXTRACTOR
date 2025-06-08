# Resume Skill Extractor

**Project for the AI Support Engineer role assignment at CSFirst Windsurf**

Created by: **Kunal Jain**

---

## Project Overview

The **Resume Skill Extractor** is a powerful and intuitive web application designed to streamline the process of extracting key information from PDF resumes. Built with Python, this tool leverages Natural Language Processing (NLP) to automatically parse resumes, identify crucial details like name, email, phone number, skills, and work experience, and present them in a clear, organized manner.

Beyond simple extraction, the application also stores this data persistently, enabling users to easily search and filter uploaded resumes by specific skills. This makes it an invaluable asset for recruiters, hiring managers, or anyone needing to quickly identify candidates with particular expertise.

---

## Features

* **Effortless PDF Uploads:** Upload single or multiple PDF resumes through a user-friendly web interface.
* **Robust Data Extraction:** Utilizes advanced NLP techniques (powered by spaCy) and custom logic to accurately extract:
    * Name
    * Email Address
    * Phone Number
    * Skills
    * Work Experience
* **Clear Data Summaries:** View a clean and readable summary of all parsed resume data directly within the application.
* **Persistent Storage:** Extracted resume data is automatically saved to a `parsed_data.json` file, allowing for future reference and analysis.
* **Skill-Based Filtering:** Easily search and filter stored resumes by entering specific skill keywords, simplifying the discovery of relevant candidates.
* **Clean User Interface:** A minimal and intuitive frontend built with Streamlit ensures a smooth user experience.

---

## File Structure
---

- **resume_skill_extractor/**  
  Main project folder containing the following files and directories:

  - `app.py`  
    Main Streamlit application.

  - `create_resume.py`  
    Helper script for resume creation (if applicable).

  - `extractor.py`  
    Core logic for extracting resume data.

  - `storage.py`  
    Handles data storage and retrieval (e.g., JSON files).

  - `utils.py`  
    Utility functions used throughout the project.

  - `parsed_data.json`  
    Stores all extracted resume data persistently.

  - `requirements.txt`  
    List of Python dependencies.

  - `Dockerfile`  
    Docker configuration file for containerized deployment (to be added).

  - **sample_resumes/**  
    Directory containing sample PDF resumes:
    - `resume_1.pdf`
    - `resume_2.pdf`
    - `resume_3.pdf`

---


## Getting Started

Follow these steps to get the Resume Skill Extractor up and running on your local machine.

### Prerequisites

* **Python 3.10+**
* **pip** (Python package installer)
* **(Optional) Docker:** If you prefer a containerized deployment.

### Installation

1.  **Clone the repository** or download the project files to your local system:

    ```bash
    git clone [https://github.com/your-username/resume-skill-extractor.git](https://github.com/your-username/resume-skill-extractor.git)
    cd resume_skill_extractor
    ```

2.  **(Recommended) Create and activate a virtual environment:** This isolates your project's dependencies.

    ```bash
    python -m venv venv
    # On macOS/Linux:
    source venv/bin/activate
    # On Windows:
    .\venv\Scripts\activate
    ```

3.  **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

---

## How to Run

You have two primary options for running the application: locally with Streamlit or via Docker.

### Run Locally with Streamlit

1.  Ensure your virtual environment is activated (if you created one).
2.  Start the Streamlit application:

    ```bash
    streamlit run app.py
    ```

3.  Open your web browser and navigate to `http://localhost:8501`.
4.  You can now:
    * Upload one or multiple PDF resumes.
    * View the neatly parsed results.
    * Use the skill filter box to search stored resumes by specific skills.

### Using Docker (Containerized Deployment)

For a more isolated and portable deployment, you can use Docker.

1.  **Build the Docker image:**

    ```bash
    docker build -t resume-extractor-kunal-jain .
    ```

2.  **Run the Docker container:**

    ```bash
    docker run -p 8501:8501 resume-extractor-kunal-jain
    ```

3.  Access the application in your browser at `http://localhost:8501`.

---

## How It Works

The Resume Skill Extractor operates through a series of logical steps:

1.  **PDF Upload and Parsing:** The application accepts PDF resume uploads, temporarily saving them in memory for processing.
2.  **Information Extraction:** The `extractor.py` module, powered by the `spaCy` NLP library and custom rules, meticulously parses the PDF content to identify and extract key fields such as name, email, phone number, skills, and work experience.
3.  **Data Persistence:** The extracted and structured data for each resume is then stored in the `parsed_data.json` file, ensuring that the information is available for future sessions.
4.  **User Interface & Filtering:** The Streamlit-based UI (`app.py`) presents a clean and organized summary of the extracted data. It also provides a dedicated input field that allows users to filter the stored resumes instantly by specific skill keywords.

---

## Notes and Future Improvements

* **Extraction Accuracy:** While robust, extraction accuracy can vary based on the quality and formatting of the uploaded resumes. Future work will focus on enhancing the NLP model and refining extraction rules for improved performance across diverse resume layouts.
* **Document Format Support:** Currently, the application exclusively supports PDF resumes. Expanding support to include other popular formats like DOCX would significantly broaden its utility.
* **Skill Filtering Enhancement:** The current skill filtering mechanism performs a case-insensitive, exact-match search. Implementing fuzzy matching would allow for more flexible and forgiving searches, accommodating variations in skill terminology.
* **UI/UX Enhancements:** The user interface can be further refined with better styling, visual cues, and potentially even direct resume previews for a more engaging and informative user experience.

---

## Credits

This project was built with the power of:

* **Python**
* **spaCy** (for Natural Language Processing)
* **Streamlit** (for the web application frontend)
