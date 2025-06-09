import nltk
import os
import sys

def download_nltk_data():
    """Download required NLTK packages to a project-specific directory."""
    # Create a local nltk_data directory in the project
    current_dir = os.path.dirname(os.path.abspath(__file__))
    nltk_data_dir = os.path.join(current_dir, 'nltk_data')
    os.makedirs(nltk_data_dir, exist_ok=True)
    
    required_packages = ['punkt', 'stopwords', 'averaged_perceptron_tagger']
    
    print(f"Downloading NLTK data to: {nltk_data_dir}")
    
    for package in required_packages:
        try:
            print(f"Downloading {package}...")
            nltk.download(package, download_dir=nltk_data_dir)
            print(f"Successfully downloaded {package}")
        except Exception as e:
            print(f"Error downloading {package}: {str(e)}", file=sys.stderr)
            
    print("\nNLTK data download complete!")

if __name__ == "__main__":
    download_nltk_data()