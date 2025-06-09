from setuptools import setup, find_packages

setup(
    name="resume_shortlister",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'streamlit',
        'PyPDF2',
        'nltk',
    ],
)