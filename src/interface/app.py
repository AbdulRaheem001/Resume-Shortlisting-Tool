import streamlit as st
import os
import sys
import PyPDF2
from typing import List, Tuple

# Add the project root to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
if project_root not in sys.path:
    sys.path.append(project_root)

from src.scoring.calculator import calculate_score
from src.scoring.ranker import rank_resumes

def read_pdf(file):
    try:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        st.error(f"Error reading PDF: {str(e)}")
        return None

def read_text(file):
    try:
        return file.getvalue().decode("utf-8")
    except Exception as e:
        st.error(f"Error reading text file: {str(e)}")
        return None

def process_file(file):
    if file.type == "application/pdf":
        return read_pdf(file)
    elif file.type == "text/plain":
        return read_text(file)
    else:
        st.error(f"Unsupported file type: {file.type}")
        return None

def main():
    st.title("Resume Shortlisting Tool")
    
    # Upload Job Description
    st.header("Upload Job Description")
    jd_file = st.file_uploader("Upload Job Description", type=["pdf", "txt"])
    
    if jd_file:
        with st.spinner("Processing Job Description..."):
            jd_text = process_file(jd_file)
            if jd_text:
                st.success("Job Description processed successfully!")
                with st.expander("View Job Description"):
                    st.write(jd_text)
    
    # Upload Resumes
    st.header("Upload Resumes")
    resume_files = st.file_uploader("Upload Resumes", type=["pdf", "txt"], accept_multiple_files=True)
    
    if resume_files and jd_text:
        resumes = []
        with st.spinner("Processing Resumes..."):
            for resume in resume_files:
                resume_text = process_file(resume)
                if resume_text:
                    resumes.append((resume.name, resume_text))
        
        if resumes:
            st.success(f"Successfully processed {len(resumes)} resumes!")
            
            # Calculate scores
            scores = [calculate_score(jd_text, resume_text) for _, resume_text in resumes]
            
            # Parameters for ranking
            k = st.slider("Select number of top matches to display", 1, len(resumes), 3)
            
            if st.button("Rank Resumes"):
                # Get ranked resumes
                ranked_results = rank_resumes(resumes, scores, k)
                
                # Display results
                st.header("Top Matching Resumes")
                for i, (name, text, score) in enumerate(ranked_results, 1):
                    with st.expander(f"#{i}: {name} (Score: {score:.1f}/100)"):
                        st.write("Match Score Components:")
                        st.progress(score/100)
                        st.write(text)

if __name__ == "__main__":
    main()