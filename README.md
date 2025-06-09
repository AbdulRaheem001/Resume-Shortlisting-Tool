# Resume Shortlisting Tool

## Overview
This project is a resume shortlisting tool that allows HR professionals to upload a Job Description (JD) and retrieve the top K matching resumes from a dataset using pure text mining techniques.

## Features
- Text preprocessing to clean and normalize resumes and JDs.
- Custom scoring mechanism to evaluate resume relevance based on keyword overlap and skill frequency.
- Top-K resume ranking based on the custom scoring.
- Candidate summaries highlighting matched skills and relevant terms.
- User-friendly interface built with Streamlit or Gradio for easy uploads and outputs.

## Project Structure
- `src/preprocessing`: Contains modules for text cleaning and tokenization.
- `src/scoring`: Implements the scoring logic and ranking functions.
- `src/utils`: Utility functions for file handling and text extraction.
- `src/interface`: User interface code for interaction.
- `src/main.py`: Entry point for the application.
- `tests`: Contains unit tests for the preprocessing and scoring modules.

## Installation
1. Clone the repository.
2. Navigate to the project directory.
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage
Run the application using:
```
python src/main.py
```
Follow the prompts in the interface to upload your Job Description and resumes.

## Contribution
Feel free to submit issues or pull requests for improvements or bug fixes.

## License
This project is licensed under the MIT License.