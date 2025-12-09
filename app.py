from flask import Flask, render_template, request, redirect, url_for, flash, send_file
import json
import os
from operator import itemgetter
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET', 'dev-secret')

RULES_PATH = os.path.join(os.path.dirname(__file__), 'rules.json')


def load_rules():
    with open(RULES_PATH, 'r', encoding='utf-8') as f:
        rules = json.load(f)
    for r in rules:
        r['symptoms'] = [s.strip().lower() for s in r.get('symptoms', [])]
    return rules


@app.route('/', methods=['GET'])
def index():
    rules = load_rules()
    master_symptoms = sorted({s for r in rules for s in r['symptoms']})
    return render_template('index.html', symptoms=master_symptoms)


@app.route('/diagnose', methods=['POST'])
def diagnose():
    # Patient details
    name = request.form.get('name')
    age = request.form.get('age')
    gender = request.form.get('gender')
    temperature = request.form.get('temperature')
    height = request.form.get('height')

    # Symptom selection
    selected = request.form.getlist('symptom')
    selected = [s.lower().strip() for s in selected]

    if not selected:
        flash('Please select at least one symptom.', 'warning')
        return redirect(url_for('index'))

    rules = load_rules()
    results = []

    for r in rules:
        disease_symptoms = r.get('symptoms', [])
        matched = len(set(disease_symptoms) & set(selected))
        if matched > 0:
            score = matched / len(disease_symptoms)
            results.append({
                'id': r['id'],
                'name': r['name'],
                'severity': r.get('severity', 'Unknown'),
                'matched': matched,
                'total_symptoms': len(disease_symptoms),
                'score': score,
                'description': r.get('description', ''),
                'treatment': r.get('treatment', ''),
                'matched_symptoms': sorted(list(set(disease_symptoms) & set(selected)))
            })

    results = sorted(results, key=itemgetter('score', 'matched'), reverse=True)

    return render_template(
        'results.html',
        results=results,
        selected=selected,
        name=name,
        age=age,
        gender=gender,
        temperature=temperature,
        height=height
    )


@app.route('/download_pdf', methods=['POST'])
def download_pdf():
    results_text = request.form.get('results')
    if not results_text:
        return redirect(url_for('index'))

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    p.setFont("Helvetica", 12)
    p.drawString(100, 750, "Medical Diagnostic Report")
    p.line(100, 745, 500, 745)

    y = 720
    p.drawString(100, y, "Selected Symptoms: ")
    y -= 20
    p.drawString(120, y, results_text)

    p.showPage()
    p.save()
    buffer.seek(0)
    return send_file(buffer, as_attachment=True,
                     download_name="diagnosis_report.pdf",
                     mimetype='application/pdf')




if __name__ == '__main__':
    app.run(debug=True)
