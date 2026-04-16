from dotenv import load_dotenv
import time
import re

# Load API keys from .env
load_dotenv()

from chains.extraction_chain import extraction_chain
from chains.matching_chain import matching_chain
from chains.scoring_chain import scoring_chain
from chains.explanation_chain import explanation_chain

print("==================== RESUME SCREENING SYSTEM ====================")

def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def run_resume_screening(resume_text, job_description):

    extracted = extraction_chain.invoke({
        "resume": resume_text,
        "job_description": job_description
    })

    matched = matching_chain.invoke({
        "extracted_data": extracted,
        "job_description": job_description
    })

    score_raw = scoring_chain.invoke({
        "matched_data": matched,
        "job_description": job_description
    }).strip()

    # Extract first valid number from output
    match = re.search(r"\d+", score_raw)

    if match:
        score = int(match.group())
    else:
        score = 0  # fallback safe value

    explanation = explanation_chain.invoke({
        "score": score,
        "matched_data": matched
    }).strip()

    return score, explanation


# ---------------- MAIN EXECUTION ---------------- #

job_description = read_file("data/job_description.txt")

resumes = {
    "Strong Resume": "data/resume_strong.txt",
    "Average Resume": "data/resume_average.txt",
    "Weak Resume": "data/resume_weak.txt"
}

for name, path in resumes.items():

    print(f"\n==================== {name} ====================")

    resume_text = read_file(path)

    score, explanation = run_resume_screening(resume_text, job_description)

    print("✅ Final Score:", score)
    print("\n Explanation:\n", explanation)

    time.sleep(10)