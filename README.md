# 🧠 Smart Resume Analyzer – Python Project

## Overview

This Python project analyzes resumes against job descriptions to generate a **match score** using Natural Language Processing (NLP). It helps job seekers understand how closely their resume aligns with a job posting and what keywords they may be missing.

## Key Features

- 📄 Supports PDF and DOCX resume files
- 🧠 Uses TF-IDF and cosine similarity for matching
- 🚨 Highlights missing keywords or skills
- ✅ Customizable job description input

## Technologies

- Python
- PyPDF2 & python-docx
- scikit-learn (TF-IDF, cosine similarity)
- Regular expressions & text cleaning

## How it Works

1. Extracts text from the uploaded resume.
2. Compares it to a user-provided job description.
3. Calculates a similarity score based on content relevance.
4. Outputs a percentage match score.


## Sample Output

Your resume matches the job description by 78.23%
