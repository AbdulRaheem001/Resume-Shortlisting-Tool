"""
Scoring module for resume shortlisting.
Contains functionality for calculating match scores and ranking resumes.
"""

from .calculator import calculate_score
from .ranker import rank_resumes

__all__ = ['calculate_score', 'rank_resumes']

# This file initializes the scoring module.