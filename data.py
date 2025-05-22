import json
import random
from faker import Faker

fake = Faker()

# Generate sample data for 10 applicants
def generate_applicant(applicant_id):
    return {
        "applicant_id": applicant_id,
        "name": fake.name(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "position": "Software Programmer",
        "resume_match_score": random.randint(70, 90),
        "ai_interview_score": random.randint(80, 95),
        "role_fitment_score": round(random.uniform(7.5, 9.5), 1),
        "fitment_recommendation": "Recommended to Hire" if random.random() > 0.2 else "Consider with Reservations",
        "expertise": {
            "skill_match": random.randint(75, 95),
            "experience_match": random.randint(2, 6),
            "required_experience": 3
        },
        "industry_fit": random.sample(["Ed-Tech", "Digital Marketing", "IT", "Software", "Healthcare", "FinTech"], 3),
        "personality_attributes": random.sample([
            "self-awareness", "eagerness", "committed", "solid understanding", 
            "quick understanding", "empathy", "adaptability", "team player"
        ], 5),
        "fitment_overview": {
            "skill_fit": random.randint(75, 95),
            "cultural_fit": random.randint(75, 95),
            "behavioral_fit": random.randint(75, 95),
            "company_fit": random.randint(75, 95),
            "candidate_demand": random.choice(["High", "Moderate", "Low"]),
            "trust_score": random.choice(["High", "Medium", "Low"])
        },
        "joining_probability": {
            "salary_expectation": random.choice(["Below the range", "Within the range", "Above the range"]),
            "notice_period": random.choice(["Immediate", "1 Month", "2 Months"]),
            "offer_in_hand": random.choice(["Yes", "No"]),
            "location_preference": random.choice(["Flexible", "Remote", "On-site"])
        },
        "transition_behavior": {
            "any_duration_in_roles": random.choice(["1-2 years", "2-3 years", "3-5 years"]),
            "duration_in_recent_company": f"{random.randint(1, 5)} years"
        },
        "resume_authenticity": {
            "score": random.randint(70, 95),
            "comment": "Resume aligns with verbal responses"
        },
        "strengths": random.sample([
            "Strong PM skills", "Fast learner", "Excellent communicator", 
            "Team player", "Culturally aligned", "Strategic thinker"
        ], 3),
        "concerns_risks": random.sample([
            "No prior experience in large corporates", 
            "Potential return to entrepreneurship", 
            "Overqualified for narrow roles",
            "Learning curve in technical domains"
        ], 2),
        "areas_of_improvement": random.sample([
            "Adjustment in large corporates", 
            "Monitor engagement in entrepreneurial mindset", 
            "Improve communication clarity"
        ], 2)
    }

# Create list of applicants
applicants_data = [generate_applicant(1000 + i) for i in range(10)]

# Save to file
file_path = "C:/power bi dashboard for persimmon/sample_applicants_data.json"
with open(file_path, "w") as f:
    json.dump(applicants_data, f, indent=2)

file_path
