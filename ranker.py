from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from extractor import clean_text, extract_skills
def rank_candidates(job_description, resumes):
    """
    resumes: list of dicts -> [{"name": "resume1.pdf", "text": "..."}, ...]
    Returns list sorted by relevance score, each with matched skills
    and up to 2 key skill gaps.
    """
    jd_clean = clean_text(job_description)
    jd_skills = set(extract_skills(job_description))
    corpus = [jd_clean] + [clean_text(r["text"]) for r in resumes]
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(corpus)
    jd_vector = tfidf_matrix[0:1]
    resume_vectors = tfidf_matrix[1:]
    scores = cosine_similarity(jd_vector, resume_vectors).flatten()
    results = []
    for i, resume in enumerate(resumes):
        resume_skills = set(extract_skills(resume["text"]))
        matched = sorted(jd_skills & resume_skills)
        gaps = sorted(jd_skills - resume_skills)[:2]
        results.append({
            "name": resume["name"],
            "score": round(float(scores[i]) * 100, 2),
            "matched_skills": matched,
            "skill_gaps": gaps,
        })
    return sorted(results, key=lambda r: r["score"], reverse=True)
