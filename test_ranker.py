from ranker import rank_candidates
jd = "Looking for a Python developer with Flask, SQL, and Docker experience."
resumes = [
    {"name": "candidate_a.pdf", "text": "Experienced in Python, Flask, SQL, Git"},
    {"name": "candidate_b.pdf", "text": "Java developer with React and AWS"},
]
for r in rank_candidates(jd, resumes):
    print(r)
