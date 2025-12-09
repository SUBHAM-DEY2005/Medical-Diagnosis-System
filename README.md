# Medical-Diagnosis-System
A web-based medical diagnostic tool built with Flask that allows users to input patient details and symptoms, and receive possible diagnoses based on predefined rules. It also supports PDF report generation for the diagnosis results.

Features

Enter patient details: Name, Age, Gender, Temperature, Height

Select multiple symptoms from a master list

Get a list of possible diagnoses with:

Name of disease

Severity (Urgent, Moderate, Mild)

Matched symptoms

Confidence score

Description and treatment advice

Download PDF report of the diagnosis

Flash messages for validation (e.g., no symptom selected)

Clean and responsive UI using Bootstrap 5

Folder Structure
medical_diagnosis_project/
│
├── app.py                 # Flask application
├── rules.json             # JSON file containing diseases, symptoms, and treatments
├── requirements.txt       # Python dependencies
├── templates/
│   ├── index.html         # Form page
│   └── results.html       # Diagnosis results page
└── static/
    ├── custom.css         # Optional custom styles
    └── icon.png           # Optional icon/image

Installation

Clone the repository

git clone <repository-url>
cd medical_diagnosis_project


Create a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows


Install dependencies

pip install -r requirements.txt


Run the Flask app

python app.py


Open in browser

http://127.0.0.1:5000/

Usage

Fill in patient details.

Select one or more symptoms.

Click Diagnose to see possible conditions.

Click Download PDF to save a report (optional).

Dependencies

Flask
 – Web framework

ReportLab
 – PDF generation

Bootstrap 5 – Frontend styling

rules.json Format

Each disease is represented as an object:

[
  {
    "id": "d1",
    "name": "Common Cold",
    "symptoms": ["sneezing", "runny nose", "sore throat", "cough"],
    "severity": "Mild",
    "description": "A viral infection of your upper respiratory tract.",
    "treatment": "Rest, fluids, OTC pain relievers, decongestants if needed."
  }
]


symptoms → list of symptoms for the disease

severity → Urgent / Moderate / Mild

description → Short disease description

treatment → Recommended care or first aid

Hosting

You can host the app using free platforms:

Render.com

PythonAnywhere

Heroku

Make sure to set the Flask app to host="0.0.0.0" and debug=False in production.

Future Improvements

Add more diseases and symptoms to rules.json

Use a machine learning model for more accurate diagnosis

Add user authentication and patient history tracking

Enhance PDF report with better formatting and logos

Disclaimer

This tool provides possible diagnoses only and is not a substitute for professional medical advice. Always consult a licensed healthcare provider for medical concerns.
