from flask import Flask, render_template, request, jsonify, send_file
from werkzeug.utils import secure_filename
import os
import json
from weasyprint import HTML

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/templates')
def templates():
    return render_template('templates.html')

@app.route('/builder/<template_id>')
def builder(template_id):
    return render_template('builder.html', template_id=template_id)

@app.route('/preview', methods=['POST'])
def preview():
    data = request.json
    template_id = data.get('template_id')
    resume_data = data.get('resume_data')
    
    # Render the resume with the selected template
    html_content = render_template(f'templates/resume_{template_id}.html', **resume_data)
    
    # Save the preview
    preview_path = os.path.join(app.config['UPLOAD_FOLDER'], 'preview.html')
    with open(preview_path, 'w') as f:
        f.write(html_content)
    
    return jsonify({'success': True})

@app.route('/download', methods=['POST'])
def download():
    data = request.json
    template_id = data.get('template_id')
    resume_data = data.get('resume_data')
    format_type = data.get('format', 'pdf')
    
    # Render the resume
    html_content = render_template(f'templates/resume_{template_id}.html', **resume_data)
    
    if format_type == 'pdf':
        # Generate PDF
        pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], 'resume.pdf')
        HTML(string=html_content).write_pdf(pdf_path)
        return send_file(pdf_path, as_attachment=True, download_name='resume.pdf')
    else:
        # Return HTML
        return html_content

if __name__ == '__main__':
    app.run(debug=True) 