# Resume-Matching Engine

[![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/) 
[![Flask](https://img.shields.io/badge/Flask-2.3-orange?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/) 
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML) 
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS) 
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://www.javascript.com/) 
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/) 

---

## Overview

The **Resume-Matching Engine** is an **Applicant Tracking System (ATS)** designed to streamline recruitment by offering features such as **job posting, resume parsing, and candidate ranking** through a clean and responsive dashboard.

It goes beyond basic filtering by analyzing resumes for **skills, experience, and qualifications**, providing **personalized recommendations** for job roles, skill improvement, certifications, and learning resources.

---

## Features

- **Resume Upload**: Upload resumes in PDF format.  
- **Resume Analysis**: Extracts skills, experience, and qualifications using NLP.  
- **Resume Scoring**: Evaluates how well a resume aligns with target job roles.  
- **Job Recommendations**: Suggests suitable roles based on extracted skills.  
- **Skill Improvement**: Recommends additional skills to enhance resumes.  
- **Learning Resources**: Provides YouTube links for suggested skills.  
- **Job Listings**: Displays real-time job openings for suggested roles.  
- **Dashboard**: Visualizes analytics, top candidate matches, and job openings.

---

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: Python, Flask  
- **NLP**: `nltk`, `spacy`, `pdfplumber`  
- **Database**: SQLite  
- **External APIs**: YouTube Data API, Job Listing API  

---

## Installation

### Prerequisites

- Python 3.x  
- pip (Python package manager)  

### Steps

1. Clone the repository:  
    ```bash
    git clone https://github.com/your-username/Resume-Matching-Engine.git
    ```
2. Navigate into the project directory:  
    ```bash
    cd Resume-Matching-Engine
    ```
3. Install dependencies:  
    ```bash
    pip install -r requirements.txt
    ```
4. Run the Flask app:  
    ```bash
    python app.py
    ```

---

## Usage

1. Upload your resume in PDF format.  
2. Analyze the resume to get a **score, job suggestions, skill improvements, and learning resources**.  
3. Explore real-time job listings for recommended roles.  
4. Use the **dashboard** for analytics and top candidate matches.

---

## Contributing

Contributions are welcome! If you find bugs or have suggestions, please open an issue or submit a pull request.

---

## License

This project is licensed under the **MIT License**.
