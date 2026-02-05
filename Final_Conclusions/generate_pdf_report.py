"""
Generate PDF from Final Report Markdown
========================================
Creates a professional 2-page PDF report using reportlab.
"""

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
import os

def create_pdf_report():
    """Generate the Final Conclusions PDF report."""
    
    output_file = 'Final_Report.pdf'
    doc = SimpleDocTemplate(
        output_file,
        pagesize=letter,
        rightMargin=0.5*inch,
        leftMargin=0.5*inch,
        topMargin=0.4*inch,
        bottomMargin=0.4*inch
    )
    
    # Styles
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=16,
        spaceAfter=6,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#1a365d')
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=11,
        spaceBefore=8,
        spaceAfter=4,
        textColor=colors.HexColor('#2c5282')
    )
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=9,
        spaceAfter=4,
        leading=11
    )
    
    small_style = ParagraphStyle(
        'SmallBody',
        parent=styles['Normal'],
        fontSize=8,
        spaceAfter=3,
        leading=10
    )
    
    # Table styles
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2c5282')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 3),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.HexColor('#f7fafc'), colors.white]),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cbd5e0')),
    ])
    
    elements = []
    
    # Title
    elements.append(Paragraph("Final Report: Conclusions and Findings", title_style))
    elements.append(Paragraph("Multi-Class Classification of 16 MBTI Personality Types", body_style))
    elements.append(Spacer(1, 6))
    
    # 1. Main Findings
    elements.append(Paragraph("1. Main Findings and Conclusions", heading_style))
    
    results_data = [
        ['Model', 'Test Accuracy', 'Macro F1', 'Key Insight'],
        ['XGBoost', '98.22%', '0.9822', 'Best overall performer'],
        ['Random Forest', '97.57%', '0.9757', 'Strong alternative'],
        ['Logistic Regression', '91.90%', '0.9189', 'Best linear baseline'],
        ['LDA', '90.56%', '0.9055', 'Fastest training'],
    ]
    results_table = Table(results_data, colWidths=[1.3*inch, 1.0*inch, 0.8*inch, 2.0*inch])
    results_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2c5282')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (1, 0), (2, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('BACKGROUND', (0, 1), (-1, 1), colors.HexColor('#c6f6d5')),
        ('ROWBACKGROUNDS', (0, 2), (-1, -1), [colors.HexColor('#f7fafc'), colors.white]),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cbd5e0')),
    ])
    results_table.setStyle(results_style)
    elements.append(results_table)
    
    conclusions = [
        "• <b>High Accuracy Achieved:</b> 98.22% accuracy predicting 16 personality types",
        "• <b>Ensemble Methods Excel:</b> XGBoost/RF outperform linear methods by 6-8%",
        "• <b>All Types Predictable:</b> Per-class F1 scores: 0.975-0.988 (consistent)",
    ]
    for c in conclusions:
        elements.append(Paragraph(c, small_style))
    elements.append(Spacer(1, 4))
    
    # 2. Research Objectives
    elements.append(Paragraph("2. Answering Research Objectives", heading_style))
    
    obj_data = [
        ['Objective', 'Status', 'Result'],
        ['Develop Classification Model', '✓', 'XGBoost: 98.22% accuracy on 60K samples'],
        ['Identify Key Traits', '✓', 'Top features: social intro, planning, emotions'],
        ['Compare Algorithms', '✓', 'XGBoost > RF > LR > LDA ranking established'],
        ['Hard-to-predict types?', '✓', 'All 16 types similarly predictable (F1: 0.975-0.988)'],
    ]
    obj_table = Table(obj_data, colWidths=[1.8*inch, 0.5*inch, 3.5*inch])
    obj_table.setStyle(table_style)
    elements.append(obj_table)
    elements.append(Spacer(1, 4))
    
    # 3. Limitations
    elements.append(Paragraph("3. Limitations Encountered", heading_style))
    
    lim_data = [
        ['Limitation', 'Impact'],
        ['Synthetic/Survey Data', 'May not generalize to real assessments'],
        ['Self-Reported Responses', 'Subject to response bias'],
        ['16 Discrete Categories', 'Simplifies continuous personality traits'],
        ['Single Dataset', 'External validity unknown'],
    ]
    lim_table = Table(lim_data, colWidths=[1.8*inch, 4.0*inch])
    lim_table.setStyle(table_style)
    elements.append(lim_table)
    elements.append(Spacer(1, 4))
    
    # 4. Applications
    elements.append(Paragraph("4. Potential Applications", heading_style))
    
    app_data = [
        ['Application', 'Description'],
        ['Automated Assessment', 'Instant personality prediction from surveys'],
        ['HR & Team Building', 'Match team compositions by personality diversity'],
        ['Career Guidance', 'Recommend paths aligned with personality'],
        ['Personalization', 'Tailor content/recommendations to type'],
    ]
    app_table = Table(app_data, colWidths=[1.5*inch, 4.3*inch])
    app_table.setStyle(table_style)
    elements.append(app_table)
    elements.append(Spacer(1, 4))
    
    # 5. Future Work
    elements.append(Paragraph("5. Recommended Future Work", heading_style))
    
    future = [
        "• <b>Short-term:</b> Hyperparameter tuning, k-fold cross-validation, SHAP explainability",
        "• <b>Research:</b> Real-world validation, neural networks, longitudinal studies",
        "• <b>Production:</b> API deployment, user interface, model monitoring",
    ]
    for f in future:
        elements.append(Paragraph(f, small_style))
    elements.append(Spacer(1, 4))
    
    # 6. Summary
    elements.append(Paragraph("6. Final Summary", heading_style))
    elements.append(Paragraph(
        "This project demonstrated that ML can accurately predict 16 MBTI personality types with 98.22% accuracy. "
        "XGBoost significantly outperformed linear baselines. Models are reproducible (random_state=42) and ready "
        "for HR, education, and personalization applications. <b>Key Takeaway:</b> Ensemble methods are highly "
        "effective for psychometric classification, achieving near-perfect accuracy with interpretable feature importance.",
        small_style
    ))
    
    # Build PDF
    doc.build(elements)
    print(f"PDF report generated: {output_file}")
    return output_file

if __name__ == "__main__":
    create_pdf_report()
