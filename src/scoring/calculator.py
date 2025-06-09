import re
from collections import Counter
from typing import List, Dict, Set

def preprocess_text(text: str) -> str:
    """Clean and preprocess text for scoring."""
    text = text.lower()
    text = re.sub(r'[^\w\s]', ' ', text)
    return ' '.join(text.split())

def extract_keywords(text: str) -> List[str]:
    """Extract keywords from text using simple tokenization."""
    return preprocess_text(text).split()

def keyword_overlap(jd_keywords: List[str], resume_keywords: List[str]) -> float:
    """Calculate the keyword overlap score between job description and resume."""
    jd_set = set(jd_keywords)
    resume_set = set(resume_keywords)
    overlap = len(jd_set.intersection(resume_set))
    total_keywords = len(jd_set)
    return (overlap / total_keywords * 40) if total_keywords > 0 else 0  # 40% weight

def skill_frequency_weighting(resume_keywords: List[str], job_related_terms: Set[str]) -> float:
    """Calculate score based on frequency of job-related terms in resume."""
    if not job_related_terms:
        return 0
    
    counter = Counter(resume_keywords)
    score = sum(counter[term] for term in job_related_terms if term in counter)
    return min(score * 2, 30)  # 30% weight, capped

def phrase_match_bonus(resume_text: str, jd_phrases: List[str]) -> float:
    """Calculate bonus points for matching exact phrases."""
    if not jd_phrases:
        return 0
    
    matches = sum(1 for phrase in jd_phrases if phrase in resume_text.lower())
    return (matches / len(jd_phrases) * 30)  # 30% weight

def calculate_score(job_description: str, resume: str) -> float:
    """Calculate the overall score for a resume based on the job description."""
    # Preprocess texts
    jd_processed = preprocess_text(job_description)
    resume_processed = preprocess_text(resume)
    
    # Extract keywords
    jd_keywords = extract_keywords(jd_processed)
    resume_keywords = extract_keywords(resume_processed)
    
    # Common technical skills and experience keywords
    technical_skills = {
        'python', 'java', 'javascript', 'react', 'angular', 'vue', 
        'node', 'django', 'flask', 'sql', 'mongodb', 'postgresql',
        'aws', 'azure', 'gcp', 'docker', 'kubernetes', 'ci/cd',
        'git', 'agile', 'scrum', 'rest', 'api', 'microservices'
    }
    
    # Important phrases to look for
    key_phrases = [
        'years experience', 'team lead', 'project manager',
        'software engineer', 'developer', 'full stack',
        'backend', 'frontend', 'devops', 'machine learning'
    ]
    
    # Calculate individual scores
    overlap_score = keyword_overlap(jd_keywords, resume_keywords)
    frequency_score = skill_frequency_weighting(resume_keywords, technical_skills)
    phrase_score = phrase_match_bonus(resume, key_phrases)
    
    # Calculate total score (max 100)
    total_score = overlap_score + frequency_score + phrase_score
    
    return min(100, total_score)