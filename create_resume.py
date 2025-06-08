from faker import Faker
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from reportlab.lib.units import inch
import os
import random

fake = Faker()

skills_list = [
    "Python", "Machine Learning", "Data Analysis", "SQL", "Deep Learning",
    "Project Management", "Communication", "Cloud Computing", "Docker",
    "Kubernetes", "JavaScript", "React", "AWS", "Azure"
]

def generate_basic_info():
    return {
        "name": fake.name(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "address": fake.address().replace('\n', ', '),
        "job_title": fake.job(),
        "summary": fake.paragraph(nb_sentences=3),
        "experience_years": random.randint(1, 10),
        "education": f"{fake.company()} University, B.Sc. in {fake.job().split()[0]}",
        "skills": ', '.join(fake.random_elements(elements=skills_list, length=5, unique=True))
    }

def resume_format_1(data, filename):
    # Simple vertical layout with bold headers
    c = canvas.Canvas(filename, pagesize=LETTER)
    width, height = LETTER

    c.setFont("Helvetica-Bold", 20)
    c.drawString(72, height - 72, data['name'])

    c.setFont("Helvetica", 12)
    c.drawString(72, height - 100, f"{data['job_title']}")
    c.drawString(72, height - 115, f"Email: {data['email']}")
    c.drawString(72, height - 130, f"Phone: {data['phone']}")
    c.drawString(72, height - 145, f"Address: {data['address']}")

    y = height - 180
    c.setFont("Helvetica-Bold", 14)
    c.drawString(72, y, "Professional Summary")
    c.setFont("Helvetica", 12)
    text = c.beginText(72, y - 15)
    for line in data['summary'].split('\n'):
        text.textLine(line)
    c.drawText(text)

    y = y - 70
    c.setFont("Helvetica-Bold", 14)
    c.drawString(72, y, "Experience")
    c.setFont("Helvetica", 12)
    c.drawString(72, y - 15, f"{data['experience_years']} years of experience in related field.")

    y = y - 50
    c.setFont("Helvetica-Bold", 14)
    c.drawString(72, y, "Education")
    c.setFont("Helvetica", 12)
    c.drawString(72, y - 15, data['education'])

    y = y - 50
    c.setFont("Helvetica-Bold", 14)
    c.drawString(72, y, "Skills")
    c.setFont("Helvetica", 12)
    c.drawString(72, y - 15, data['skills'])

    c.save()

def resume_format_2(data, filename):
    # Use ReportLab platypus for paragraph styling, two columns style simulation
    doc = SimpleDocTemplate(filename, pagesize=LETTER, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=72)
    styles = getSampleStyleSheet()

    # Custom styles
    title_style = styles['Title']
    header_style = styles['Heading2']
    normal_style = styles['BodyText']

    elements = []

    # Name centered and big
    elements.append(Paragraph(data['name'], title_style))
    elements.append(Paragraph(data['job_title'], normal_style))
    elements.append(Spacer(1, 12))

    contact_info = f"Email: {data['email']}<br/>Phone: {data['phone']}<br/>Address: {data['address']}"
    elements.append(Paragraph(contact_info, normal_style))
    elements.append(Spacer(1, 12))

    # Summary with indentation
    elements.append(Paragraph("Professional Summary", header_style))
    elements.append(Paragraph(data['summary'], normal_style))
    elements.append(Spacer(1, 12))

    # Education then Experience
    elements.append(Paragraph("Education", header_style))
    elements.append(Paragraph(data['education'], normal_style))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("Experience", header_style))
    elements.append(Paragraph(f"{data['experience_years']} years of experience in related field.", normal_style))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("Skills", header_style))
    elements.append(Paragraph(data['skills'], normal_style))

    doc.build(elements)

def resume_format_3(data, filename):
    # More creative layout: name on top left, job title top right, skills as bullet points, summary boxed
    
    c = canvas.Canvas(filename, pagesize=LETTER)
    width, height = LETTER

    # Header
    c.setFont("Courier-Bold", 22)
    c.drawString(72, height - 72, data['name'])
    c.setFont("Courier-Oblique", 14)
    c.drawRightString(width - 72, height - 72, data['job_title'])

    # Contact info below name
    c.setFont("Courier", 10)
    c.drawString(72, height - 90, f"Email: {data['email']}")
    c.drawString(72, height - 105, f"Phone: {data['phone']}")
    c.drawString(72, height - 120, f"Address: {data['address']}")

    # Draw box for summary
    box_x = 72
    box_y = height - 200
    box_width = width - 144
    box_height = 60
    c.roundRect(box_x, box_y, box_width, box_height, 10, stroke=1, fill=0)
    c.setFont("Courier-Bold", 12)
    c.drawString(box_x + 10, box_y + box_height - 15, "Professional Summary:")
    c.setFont("Courier", 10)
    text = c.beginText(box_x + 10, box_y + box_height - 30)
    for line in data['summary'].split('\n'):
        text.textLine(line)
    c.drawText(text)

    # Skills as bullets
    c.setFont("Courier-Bold", 12)
    c.drawString(72, box_y - 20, "Skills:")
    c.setFont("Courier", 10)
    skills = data['skills'].split(', ')
    skill_y = box_y - 35
    bullet = u"\u2022"  # bullet point
    for skill in skills:
        c.drawString(80, skill_y, f"{bullet} {skill}")
        skill_y -= 15

    # Education and Experience side by side
    left_x = 72
    right_x = width / 2 + 20
    y_start = skill_y - 30
    c.setFont("Courier-Bold", 12)
    c.drawString(left_x, y_start, "Education:")
    c.setFont("Courier", 10)
    c.drawString(left_x, y_start - 15, data['education'])

    c.setFont("Courier-Bold", 12)
    c.drawString(right_x, y_start, "Experience:")
    c.setFont("Courier", 10)
    c.drawString(right_x, y_start - 15, f"{data['experience_years']} years of experience")

    c.save()

def save_resumes(directory):
    os.makedirs(directory, exist_ok=True)
    for i in range(1, 4):
        data = generate_basic_info()
        filename = os.path.join(directory, f"resume_{i}.pdf")
        if i == 1:
            resume_format_1(data, filename)
        elif i == 2:
            resume_format_2(data, filename)
        else:
            resume_format_3(data, filename)
        print(f"Saved {filename}")

if __name__ == "__main__":
    save_dir = "./sample_resumes"  # Change to your preferred directory
    save_resumes(save_dir)
