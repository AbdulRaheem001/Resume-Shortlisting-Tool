# Resume Shortlisting Tool - Final Report

## 1. Scoring System Design (40%)

Our custom scoring system evaluates resumes against job descriptions using three main components:

### 1.1 Keyword Overlap Score (40%)
- Extracts keywords from both JD and resume
- Calculates intersection of keywords
- Score = (matched keywords / total JD keywords) * 40
- Emphasizes presence of required skills and qualifications

### 1.2 Skill Frequency Analysis (30%)
- Measures frequency of technical skills in resume
- Focuses on common industry terms like:
  - Programming languages (Python, Java, JavaScript)
  - Frameworks (Django, Flask, React)
  - Tools (Git, Docker, AWS)
- Score = min(frequency_sum * 2, 30)
- Rewards depth of experience in key areas

### 1.3 Phrase Match Scoring (30%)
- Identifies complete phrase matches
- Targets important phrases like:
  - "years experience"
  - "team lead"
  - "software engineer"
- Score = (matched phrases / total key phrases) * 30
- Values contextual relevance

## 2. Sample Results

### 2.1 Job Description
```
Software Developer Position
- Python programming (5+ years experience)
- Web development with Django or Flask
- Experience with RESTful APIs
- Database design and SQL
- Git version control
```

### 2.2 Top 3 Resume Matches

1. **Michael Wilson (Score: 89.5/100)**
   - High keyword overlap (35/40)
   - Strong skill frequency (28/30)
   - Good phrase matches (26.5/30)
   - Key Matches: Python, Django, SQL, Git, 7+ years experience

2. **John Doe (Score: 78.2/100)**
   - Good keyword overlap (32/40)
   - Moderate skill frequency (25/30)
   - Average phrase matches (21.2/30)
   - Key Matches: Python, Flask, REST APIs, 6 years experience

3. **Alice Smith (Score: 45.7/100)**
   - Limited keyword overlap (18/40)
   - Low skill frequency (15/30)
   - Few phrase matches (12.7/30)
   - Key Matches: Basic Python, REST APIs

## 3. Challenges and Solutions

### 3.1 Text Preprocessing
- **Challenge**: Inconsistent formatting in PDFs and text files
- **Solution**: Implemented robust text cleaning:
  - Case normalization
  - Special character handling
  - Whitespace standardization

### 3.2 Skill Recognition
- **Challenge**: Multiple ways to refer to same skill
- **Solution**: Created comprehensive skill mapping
  - Technical skill aliases
  - Common abbreviations handling
  - Phrase variations

### 3.3 Score Calibration
- **Challenge**: Balancing component weights
- **Solution**: Iterative testing with sample data
  - 40/30/30 split based on importance
  - Capped subscores to prevent inflation
  - Normalized final scores to 0-100 range

## 4. Limitations

1. **Language Dependency**
   - Current implementation optimized for English
   - Limited support for multilingual resumes

2. **Format Constraints**
   - Best results with structured formats
   - May miss context in creative layouts

3. **Domain Specificity**
   - Technical skill focus
   - May need adaptation for other industries

## 5. Future Improvements

1. Add support for multiple languages
2. Implement semantic similarity matching
3. Expand industry-specific terminology
4. Add customizable scoring weights
5. Include experience level analysis
