from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename
from nlp_module import analyze_resume

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if file and file.filename.endswith('.pdf'):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Perform NLP analysis on the uploaded resume
        analysis_result = analyze_resume(filepath)

        # Pass the results to the result page
        return render_template('results.html', analysis=analysis_result)
    else:
        return jsonify({'error': 'Invalid file type, please upload a PDF'}), 400

if __name__ == '__main__':
    app.run(debug=True)
