# 📊 End-to-End Applicant Analytics: Python + PostgreSQL + Power BI

This project demonstrates a complete workflow for generating, storing, and visualizing applicant data using Python, PostgreSQL, and Power BI. It includes dataset generation, database insertion, and a browser-based embedded dashboard for recruiters to filter insights by applicant ID.

---

## 🧰 Tech Stack

- **Python** – for data generation and database insertion  
- **PostgreSQL** – as the backend database  
- **Power BI** – for data visualization  
- **HTML** – to embed Power BI dashboard interactively

---

## 🗂️ Project Files

├── data.py # Generates synthetic applicant data (JSON)
├── sample_applicants_data.json # Output dataset with mock applicant info
├── insert_data_postgres.py # Inserts JSON data into PostgreSQL DB
├── embed_dashboard.html # HTML file to embed Power BI with filter




---

## 📌 Project Workflow

1. **Generate Data**  
   Uses `Faker` to create realistic applicant profiles.  
   Output: `sample_applicants_data.json`

   ```bash
   python data.py

##Insert into PostgreSQL
Creates table applicantsss if not present
Converts nested fields to text
Inserts all JSON records using psycopg2

#Bash#
python insert_data_postgres.py

### Visualize with Power BI

Dashboard created using Power BI Desktop
Embed the dashboard into a browser via embed_dashboard.html
To embed: Replace "YOUR_EMBED_LINK_HERE" inside embed_dashboard.html with your actual Power BI public link.
Open it in any browser to view and filter by applicant ID.


Sai Kumar Thomburapu
Aspiring Data Analyst & AI Developer | Building practical tools with open-source technologies
