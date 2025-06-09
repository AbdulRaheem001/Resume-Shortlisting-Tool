from preprocessing.cleaner import clean_text
from preprocessing.tokenizer import tokenize_text
from scoring.calculator import calculate_score
from scoring.ranker import rank_resumes
from utils.file_handler import upload_file
from utils.text_extractor import extract_text
from interface.app import run_app

def main():
    # Run the application interface
    run_app()

if __name__ == "__main__":
    main()