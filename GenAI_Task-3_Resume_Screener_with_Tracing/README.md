# AI Resume Screening System (LangChain + Groq + LangSmith)

## Overview
This task is an **AI-powered Resume Screening System** that evaluates candidate resumes against a given job description using **LangChain pipelines and LLMs**.

The system:
* Extracts structured information from resumes
* Matches candidate skills with job requirements
* Assigns a score (0–100)
* Generates a detailed explanation
* Uses **LangSmith tracing** for debugging and observability

## Tech Stack
* Python
* LangChain
* Groq (LLM - LLaMA 3.1)
* LangSmith (Tracing & Debugging)
* dotenv

## Key Features
* Strict ATS-style scoring
* No hallucinated skills
* Modular LangChain architecture
* LangSmith observability
* Clean separation of concerns

## Pipeline Architecture
```
Resume → Extraction → Matching → Scoring → Explanation
```

### 1️. Extraction Chain
Extracts structured data:
* Skills
* Experience
* Tools

### 2️. Matching Chain
Compares candidate profile with job description:
* Matched requirements
* Missing requirements
* Partial matches

### 3️. Scoring Chain
Assigns a **strict score (0–100)** based on:
* Required skills (high weight)
* Preferred skills (bonus)
* No hallucination allowed

### 4️. Explanation Chain
Generates a **human-readable evaluation**:
* Strengths
* Gaps
* Final hiring recommendation

## Project Structure
```
AI-Resume-Screener/
│
├── chains/
│   ├── extraction_chain.py
│   ├── matching_chain.py
│   ├── scoring_chain.py
│   └── explanation_chain.py
│
├── prompts/
│   ├── extract_prompt.py
│   ├── match_prompt.py
│   ├── score_prompt.py
│   └── explain_prompt.py
│
├── data/
│   ├── job_description.txt
│   ├── resume_strong.txt
│   ├── resume_average.txt
│   └── resume_weak.txt
│
├── main.py
├── requirements.txt
├── .env.example
└── .gitignore
```

## Environment Setup
### 1. Clone the repository
```bash
git clone <your-repo-link>
cd GenAI_Task-3_Resume_Screener_with_Tracing
```

#### Note: Create and activate virtual environment (optional but recommended)
```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Setup environment variables
Copy the example file:
```bash
cp .env.example .env
```

### 4. Add your API keys:
```env
GROQ_API_KEY=your_key
LANGCHAIN_API_KEY=your_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=resume-screener
```

## Run the Project
```bash
python main.py
```

## LangSmith Tracing
This project uses **LangSmith** for tracing LLM workflows.

### Features:
* Full pipeline visibility
* Step-by-step debugging
* Token usage tracking

### Runs Included:
* Strong Resume
* Average Resume
* Weak Resume

## Debugging Example
### Issue Observed:
Average resume received a **higher-than-expected score**

### Root Cause:
* LLM inferred skills instead of strictly matching extracted data
* Partial matches were over-weighted
```
During testing, one incorrect output was observed where the Average Resume received an inflated score despite missing key required skills.
Using LangSmith tracing, it was identified that the scoring chain was over-weighting partial matches and inferred skills from the LLM output.
The issue was fixed by enforcing strict matching rules and ensuring scoring is based only on explicitly extracted skills.
```
### Fix Applied:
* Enforced strict prompt rules
* Removed skill inference
* Added deterministic scoring logic
