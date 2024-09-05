from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
import requests
from bs4 import BeautifulSoup
import re
from time import sleep
from random import randint

# Define a list of job roles and associated skill sets
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

# Certification links for improving skills
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
        pdf_reader = PdfReader(file_path)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text() or ''

        # Process the text
        text = text.lower()  

        # Initialize vectorizer
        vectorizer = TfidfVectorizer(lowercase=True, stop_words='english')

        # Combine job roles and skill sets into a single list for TF-IDF vectorization
        skill_set = [skill for skills in job_roles.values() for skill in skills]
        job_descriptions = list(job_roles.keys())

        # Add the text to the skill set for comparison
        all_texts = [text] + skill_set

        # Vectorize the texts
        X = vectorizer.fit_transform(all_texts)

        # Calculate scores for each job role
        scores = {}
        for i, job in enumerate(job_descriptions):
            job_vector = X[i + 1]  # Get the vector for the job description
            score = (X[0] @ job_vector.T).sum()  # Calculate the dot product as score
            scores[job] = score

        # Find the best job match based on score
        recommended_job = max(scores, key=scores.get)

        # Prepare recommendations for certifications
        recommendations = {skill: certification_links.get(skill, "No certification available") for skill in skill_set}

        # Fetch job openings
        job_openings = fetch_job_openings(recommended_job)

        return {
            'score': scores,
            'recommended_job': recommended_job,
            'certification_links': recommendations,
            'job_openings': job_openings
        }

    except Exception as e:
        return {'error': str(e)}

def fetch_job_openings(job_title):
    job_keys = set()
    job_openings = []
    params = {
        "q": job_title,
        "l": "United States",
        "start": 0
    }
    url = "https://www.indeed.com/jobs"
    
    for _ in range(5):  # Limit to the first 5 pages
        response = requests.get(url, params=params)
        if response.status_code != 200:
            break
        
        # Extract job keys
        jk_pattern = re.compile(r"jk:'([a-zA-Z0-9]+)'")
        keys = jk_pattern.findall(response.text)
        job_keys.update(keys)

        params['start'] += 10
        sleep(randint(1, 3))

    for key in job_keys:
        job_url = f"https://www.indeed.com/viewjob?jk={key}"
        job_response = requests.get(job_url)
        job_soup = BeautifulSoup(job_response.text, 'html.parser')
        
        try:
            job_title = job_soup.find('h1', {'class': 'jobsearch-JobInfoHeader-title'}).text.strip()
            company = job_soup.find('div', {'class': 'jobsearch-InlineCompanyRating'}).text.strip()
            location = job_soup.find('div', {'class': 'jobsearch-JobInfoHeader-subtitle'}).text.strip()
            summary = job_soup.find('div', {'id': 'jobDescriptionText'}).text.strip()
            
            job_openings.append({
                'job_title': job_title,
                'company': company,
                'location': location,
                'summary': summary,
                'url': job_url
            })
        except Exception as e:
            print(f"Error fetching details for {job_url}: {e}")

    return job_openings