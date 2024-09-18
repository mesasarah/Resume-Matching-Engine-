# Resume-Matching Engine

## Overview

Welcome to the Resume-Matching Engine! This project is an Applicant Tracking System (ATS) designed to streamline recruitment by offering features such as job posting, resume parsing, and candidate ranking, all within a clean and responsive user interface.

The system provides an easy-to-use dashboard for recruiters, displaying job openings, top candidate matches, and detailed analytics. Our ATS goes beyond basic resume filtering by analyzing the entire resume to extract relevant skills and provide personalized recommendations for job opportunities, skills, certifications, and learning resources to help candidates improve their profiles.

The resume scoring feature offers insight into how well a resume aligns with target job roles, while real-time job openings keep candidates informed of market opportunities. Our system actively supports both recruiters and candidates in achieving more efficient and successful recruitment processes.

---

## Features

1. **Resume Upload**: Users can upload their resume in PDF format.
2. **Resume Analysis**: The system analyzes the resume to extract skills and qualifications.
3. **Scoring System**: Provides an overall score for the resume.
4. **Job Recommendations**: Suggests suitable job roles based on the extracted skills.
5. **Skill Improvement**: Recommends additional skills to improve the resume.
6. **Learning Resources**: Provides YouTube links for learning the recommended skills.
7. **Job Listings**: Shows real-time job listings for the suggested roles.
8. **Dashboard**: Offers a detailed overview of job openings, top candidate matches, and analytics.

---

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, Flask
- **NLP**: Natural Language Processing using Python libraries like `nltk`, `spacy`, and `pdfplumber`
- **Database**: SQLite (for storing job roles and corresponding skills)
- **External APIs**: YouTube Data API for fetching videos, Job listing API for fetching job posts

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
3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the Flask app:
    ```bash
    python app.py
    ```

---

## Usage

1. **Upload Resume**: Upload your resume in PDF format using the form on the homepage.
2. **Analyze Resume**: The system will analyze your resume and provide a score, job suggestions, skill improvements, and learning resources.
3. **View Job Listings**: See real-time job listings for the suggested roles.
4. **Dashboard**: Use the dashboard to get an overview of job openings, top candidate matches, and analytics.

---

## Contributing

We welcome contributions! If you have suggestions for improvement or find bugs, please open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License.
