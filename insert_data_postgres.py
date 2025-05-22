import json
import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="json data",
    user="postgres",
    password="1234"
)
cursor = conn.cursor()

# Create table with TEXT for nested fields
cursor.execute("""
    CREATE TABLE IF NOT EXISTS applicantsss (
        applicant_id TEXT PRIMARY KEY,
        name TEXT,
        role TEXT,
        email TEXT,
        phone TEXT,
        resume_match_score INTEGER,
        ai_interview_score INTEGER,
        role_fit_score FLOAT,
        recommended_to_hire BOOLEAN,
        skill_match INTEGER,
        experience_match INTEGER,
        relevant_experience_years FLOAT,
        industry_fit TEXT,
        personality_attributes TEXT,
        joining_probability TEXT,
        transition_behaviour TEXT,
        resume_authenticity TEXT,
        strengths TEXT,
        concerns TEXT,
        improvements TEXT,
        skill_fit INTEGER,
        cultural_fit INTEGER,
        behavior_fit INTEGER,
        company_fit INTEGER,
        candidate_demand TEXT,
        trust_score TEXT
    )
""")

# Load applicant JSON data
with open("sample_applicants_data.json", "r", encoding="utf-8") as f:
    applicants_data = json.load(f)

# Utility function to safely convert to text
def to_text(value):
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False)
    return str(value)

# Insert data
for a in applicants_data:
    cursor.execute("""
        INSERT INTO applicantsss (
            applicant_id, name, role, email, phone,
            resume_match_score, ai_interview_score, role_fit_score, recommended_to_hire,
            skill_match, experience_match, relevant_experience_years,
            industry_fit, personality_attributes,
            joining_probability, transition_behaviour, resume_authenticity,
            strengths, concerns, improvements,
            skill_fit, cultural_fit, behavior_fit, company_fit,
            candidate_demand, trust_score
        ) VALUES (%s, %s, %s, %s, %s,
                  %s, %s, %s, %s,
                  %s, %s, %s,
                  %s, %s,
                  %s, %s, %s,
                  %s, %s, %s,
                  %s, %s, %s, %s,
                  %s, %s)
        ON CONFLICT (applicant_id) DO NOTHING
    """, (
        to_text(a.get("applicant_id", "NA")),
        to_text(a.get("name", "NA")),
        to_text(a.get("role", a.get("job_title", "Unknown Role"))),
        to_text(a.get("email", "NA")),
        to_text(a.get("phone", "NA")),

        a.get("resume_match_score", 0),
        a.get("ai_interview_score", 0),
        a.get("role_fit_score", 0.0),
        a.get("recommended_to_hire", False),

        a.get("expertise", {}).get("skill_match", 0),
        a.get("expertise", {}).get("experience_match", 0),
        a.get("expertise", {}).get("relevant_experience_years", 0.0),

        to_text(a.get("industry_fit", [])),
        to_text(a.get("personality_attributes", [])),

        to_text(a.get("joining_probability", "NA")),
        to_text(a.get("transition_behaviour", "NA")),
        to_text(a.get("resume_authenticity", "NA")),

        to_text(a.get("strengths", "NA")),
        to_text(a.get("concerns", "NA")),
        to_text(a.get("areas_of_improvements", "NA")),

        a.get("fitment_overview", {}).get("skill_fit", 0),
        a.get("fitment_overview", {}).get("cultural_fit", 0),
        a.get("fitment_overview", {}).get("behavior_fit", 0),
        a.get("fitment_overview", {}).get("company_fit", 0),

        to_text(a.get("fitment_overview", {}).get("candidate_demand", {})),
        to_text(a.get("fitment_overview", {}).get("trust_score", {}))
    ))

conn.commit()
cursor.close()
conn.close()
print("All applicant data inserted successfully into PostgreSQL!")









