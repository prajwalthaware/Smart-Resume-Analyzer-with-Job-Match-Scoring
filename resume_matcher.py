import docx
import PyPDF2
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        return ' '.join([page.extract_text() for page in reader.pages])

def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    return ' '.join([para.text for para in doc.paragraphs])

def get_text(file_path):
    if file_path.endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith('.docx'):
        return extract_text_from_docx(file_path)
    else:
        return None

def compute_match_score(resume_text, job_text):
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf = vectorizer.fit_transform([resume_text, job_text])
    return round(cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0] * 100, 2)

# --- Example Usage ---
resume_path = "sample_resume.pdf"
job_description = """
We are looking for a Python developer with experience in machine learning,
data processing, and natural language processing (NLP). Familiarity with REST APIs,
Docker, and version control (Git) is a plus.
"""

resume_text = get_text(resume_path)
score = compute_match_score(resume_text, job_description)

print(f"Your resume matches the job description by {score}%")
