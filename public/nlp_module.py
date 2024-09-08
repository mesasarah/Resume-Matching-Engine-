from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import re

# Define job roles and associated skills
job_roles = {
    "Software Engineer": ["python", "java", "c++", "javascript", "sql", "html", "css"],
    "Data Scientist": ["python", "r", "sql", "machine learning", "data analysis", "statistics"],
    "Web Developer": ["html", "css", "javascript", "react", "node.js", "sql"],
    "Product Manager": ["market research", "project management", "business analysis", "product design"],
    "UX/UI Designer": ["design thinking", "prototyping", "user research", "figma", "adobe xd"],
    "DevOps Engineer": ["docker", "kubernetes", "aws", "ci/cd", "linux", "python"],
    "Cybersecurity Analyst": ["network security", "penetration testing", "firewalls", "risk assessment"],
    "Cloud Engineer": ["aws", "azure", "gcp", "cloud architecture", "devops", "terraform"],
    "Digital Marketer": ["seo", "content marketing", "social media", "google analytics", "ppc"],
    "Business Analyst": ["data analysis", "business intelligence", "requirements gathering", "stakeholder management"]
}

# Certification links
certification_links = {
    "python": "https://www.coursera.org/specializations/python",
    "java": "https://www.coursera.org/specializations/java-programming",
    "c++": "https://www.udacity.com/course/c-plus-plus--ud258",
    "javascript": "https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/",
    "sql": "https://www.codecademy.com/learn/learn-sql",
    "html": "https://www.freecodecamp.org/learn/responsive-web-design/#basic-html-and-html5",
    "css": "https://www.freecodecamp.org/learn/responsive-web-design/#basic-css",
    "r": "https://www.coursera.org/learn/data-analysis-r",
    "machine learning": "https://www.coursera.org/learn/machine-learning",
    "data analysis": "https://www.udacity.com/course/data-analyst-nanodegree--nd002",
    "statistics": "https://www.khanacademy.org/math/statistics-probability",
    "react": "https://www.udemy.com/course/react-the-complete-guide-incl-redux/",
    "node.js": "https://www.udemy.com/course/the-complete-nodejs-developer-course-2/",
    "project management": "https://www.coursera.org/learn/project-management",
    "business analysis": "https://www.udemy.com/course/business-analysis-fundamentals/",
    "design thinking": "https://www.coursera.org/learn/design-thinking",
    "prototyping": "https://www.udemy.com/course/prototyping-with-figma/",
    "user research": "https://www.coursera.org/learn/user-research",
    "figma": "https://www.udemy.com/course/figma-for-ux-ui-design/",
    "adobe xd": "https://www.udemy.com/course/adobe-xd-cc-for-ui-ux-design/",
    "docker": "https://www.udemy.com/course/docker-mastery/",
    "kubernetes": "https://www.udemy.com/course/kubernetes-for-developers/",
    "aws": "https://www.udemy.com/course/aws-certified-solutions-architect-associate/",
    "ci/cd": "https://www.coursera.org/learn/continuous-integration",
    "linux": "https://www.udemy.com/course/linux-for-beginners/",
    "network security": "https://www.coursera.org/learn/network-security",
    "penetration testing": "https://www.udemy.com/course/penetration-testing/",
    "firewalls": "https://www.udemy.com/course/network-security-firewalls/",
    "risk assessment": "https://www.coursera.org/learn/security-risk-management",
    "azure": "https://www.udemy.com/course/azure-certified-solutions-architect/",
    "gcp": "https://www.udemy.com/course/google-cloud-platform-gcp/",
    "cloud architecture": "https://www.udemy.com/course/cloud-architecture/",
    "terraform": "https://www.udemy.com/course/learn-terraform/",
    "seo": "https://www.coursera.org/learn/seo",
    "content marketing": "https://www.udemy.com/course/content-marketing-mastery/",
    "social media": "https://www.coursera.org/learn/social-media-marketing",
    "google analytics": "https://www.udacity.com/course/google-analytics--ud257",
    "ppc": "https://www.udemy.com/course/ppc-marketing/"
}

def analyze_resume(file_path):
    try:
        # Extract text from the PDF
        text = extract_text_from_pdf(file_path)

        # Initialize vectorizer
        vectorizer = TfidfVectorizer(lowercase=True, stop_words='english')

        # Combine job roles and skill sets into a single list for TF-IDF vectorization
        job_descriptions = [' '.join(skills) for skills in job_roles.values()]

        # Add the resume text and job descriptions to the skill set for comparison
        all_texts = [text] + job_descriptions

        # Vectorize the texts
        X = vectorizer.fit_transform(all_texts)

        # Calculate cosine similarity between resume and each job description
        resume_vector = X[0]
        similarities = cosine_similarity(resume_vector, X[1:]).flatten()

        # Calculate scores based on cosine similarity
        similarity_scores = {job: round(similarity * 100, 2) for job, similarity in zip(job_roles.keys(), similarities)}

        # Find the best job match based on the highest similarity score
        recommended_job = max(similarity_scores, key=similarity_scores.get)
        total_resume_score = similarity_scores[recommended_job]

        # Prepare recommendations for certifications based on the recommended job
        job_skills = job_roles[recommended_job]
        certifications = {skill: certification_links.get(skill, "No certification available") for skill in job_skills}

        # Fetch job openings
        job_openings = fetch_job_openings(recommended_job)

        # Determine skill gaps
        skill_set = [skill for skills in job_roles.values() for skill in skills]
        resume_skills = {skill for skill in skill_set if skill in text.lower()}  # skills found in the resume text
        missing_skills = set(job_skills) - resume_skills
        recommended_skills = list(missing_skills)

        # Assess resume based on various criteria
        score_keywords = calculate_keyword_score(text, job_skills)
        score_experience = calculate_experience_score(text, job_roles[recommended_job])
        score_education = calculate_education_score(text, recommended_job)
        score_format = calculate_format_score(text)
        score_consistency = calculate_consistency_score(text)
        score_grammar = calculate_grammar_score(text)

        # Calculate overall score
        overall_score = (score_keywords + score_experience + score_education + score_format + score_consistency + score_grammar) / 6
        level = determine_level(overall_score)

        return {
            'score': round(overall_score, 2),
            'recommended_job': recommended_job,
            'certification_links': certifications,
            'job_openings': job_openings,
            'recommended_skills': recommended_skills,
            'level': level
        }

    except Exception as e:
        return {'error': str(e)}

def extract_text_from_pdf(file_path):
    text = ''
    try:
        pdf_reader = PdfReader(file_path)
        for page in pdf_reader.pages:
            text += page.extract_text() or ''
    except Exception as e:
        raise ValueError(f"Error extracting text from PDF: {e}")
    return text

def calculate_keyword_score(text, job_skills):
    keyword_count = sum(text.lower().count(skill) for skill in job_skills)
    max_keyword_count = len(job_skills) * 10
    return (keyword_count / max_keyword_count) * 100 if max_keyword_count > 0 else 0

def calculate_experience_score(text, required_experience):
    # Placeholder function, this needs actual implementation based on experience extraction logic
    return 50  # Example static value, replace with actual logic

def calculate_education_score(text, job_title):
    # Placeholder function, this needs actual implementation based on education extraction logic
    return 50  # Example static value, replace with actual logic

def calculate_format_score(text):
    # Placeholder function for resume formatting score
    return 50  # Example static value

def calculate_consistency_score(text):
    # Placeholder function for consistency score based on text checks
    return 50  # Example static value

def calculate_grammar_score(text):
    # Placeholder function for grammar score based on text checks
    return 50  # Example static value

def determine_level(score):
    if score < 40:
        return "Beginner"
    elif 40 <= score < 80:
        return "Intermediate"
    else:
        return "Advanced"

def fetch_job_openings(job_title):
    # Define static job links for different job roles
    job_links = {
        "Software Engineer": [
            "https://www.linkedin.com/jobs/view/4003668900/?alternateChannel=search&refId=AH3b8HxfrWYe%2FkBt1Z%2B2LQ%3D%3D&trackingId=GBzvUBNzjBAXgjd6bukgug%3D%3D",
            "https://in.indeed.com/jobs?q=software+engineer&l=Bengaluru%2C+Karnataka&from=searchOnHP&vjk=d87a7d0d7ef95c2d&advn=1515350661095281"
        ],
        "Data Scientist": [
            "https://www.linkedin.com/jobs/view/4001346933/?alternateChannel=search&refId=Ed6FPETLAk%2FcKEC3dWCUww%3D%3D&trackingId=3QPDZRBdkaAzszRUXPM2kQ%3D%3D",
            "https://in.indeed.com/jobs?q=data+scientist&l=Bengaluru%2C+Karnataka&from=searchOnDesktopSerp&vjk=7efb1b4bd5538e51"
        ],
        "Web Developer": [
            "https://www.linkedin.com/jobs/view/4007224594/?alternateChannel=search&refId=pFFZkPvwWk7VTA5NaDZ%2FhA%3D%3D&trackingId=8Tx5VKnMTQXAdxTvXLA0cA%3D%3D",
            "https://in.indeed.com/jobs?q=web+developer&l=Bengaluru%2C+Karnataka&from=searchOnDesktopSerp&vjk=b4e9b00af23be394"
        ],
        "Product Manager": [
            "https://www.linkedin.com/jobs/view/4011972073/?alternateChannel=search&refId=9M3mzMkK1u2fFUiHZJ2vQA%3D%3D&trackingId=dOuUetV0n8jVJTdlFrBI%2Fw%3D%3D",
            "https://in.indeed.com/jobs?q=project+manager&l=Bengaluru%2C+Karnataka&from=searchOnDesktopSerp&vjk=be12fb0eed08f2e6"
        ],
        "UX/UI Designer": [
            "https://www.indeed.com/viewjob?jk=example9",
            "https://www.linkedin.com/jobs/view/example10"
        ],
        "DevOps Engineer": [
            "https://www.indeed.com/viewjob?jk=example11",
            "https://www.linkedin.com/jobs/view/example12"
        ],
        "Cybersecurity Analyst": [
            "https://www.indeed.com/viewjob?jk=example13",
            "https://www.linkedin.com/jobs/view/example14"
        ],
        "Cloud Engineer": [
            "https://www.indeed.com/viewjob?jk=example15",
            "https://www.linkedin.com/jobs/view/example16"
        ],
        "Digital Marketer": [
            "https://www.indeed.com/viewjob?jk=example17",
            "https://www.linkedin.com/jobs/view/example18"
        ],
        "Business Analyst": [
            "https://www.indeed.com/viewjob?jk=example19",
            "https://www.linkedin.com/jobs/view/example20"
        ]
    }
    
    # Return the fixed job links for the recommended job
    return job_links.get(job_title, ["No job links available"])