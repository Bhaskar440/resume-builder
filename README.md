# Resume Builder

A modern and user-friendly resume builder application that helps job seekers create professional resumes quickly and easily.

## Features

- Multiple professional resume templates
- Real-time preview of changes
- Export to PDF or HTML formats
- Responsive design for all devices
- Easy-to-use form interface
- Dynamic sections for work experience and education
- Skills management with tags

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd resume-builder
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask development server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

## Usage

1. Choose a template from the available options
2. Fill in your personal information
3. Add your work experience
4. Add your education history
5. List your skills
6. Preview your resume
7. Download in your preferred format (PDF or HTML)

## Project Structure

```
resume-builder/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── static/
│   └── css/
│       └── style.css  # Custom styles
├── templates/         # Jinja2 templates
│   ├── base.html     # Base template
│   ├── index.html    # Home page
│   ├── builder.html  # Resume builder form
│   └── resume_1.html # Professional resume template
└── uploads/          # Temporary storage for generated files
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 