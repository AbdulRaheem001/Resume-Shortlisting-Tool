from typing import List, Tuple

def rank_resumes(resumes: List[Tuple[str, str]], scores: List[float], top_k: int) -> List[Tuple[str, str, float]]:
    """
    Rank resumes based on their scores and return top K matches.
    
    Args:
        resumes: List of tuples containing (resume_name, resume_text)
        scores: List of scores corresponding to each resume
        top_k: Number of top matches to return
    
    Returns:
        List of tuples containing (resume_name, resume_text, score) sorted by score
    """
    # Combine resumes with their scores
    ranked_resumes = list(zip(resumes, scores))
    
    # Sort by score in descending order
    ranked_resumes.sort(key=lambda x: x[1], reverse=True)
    
    # Take top K results
    top_k_resumes = ranked_resumes[:top_k]
    
    # Format results with name, text, and score
    return [(name, text, score) for (name, text), score in top_k_resumes]