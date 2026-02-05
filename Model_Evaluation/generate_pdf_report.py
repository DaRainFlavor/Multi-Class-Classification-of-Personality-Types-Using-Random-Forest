"""
Generate PDF from Model Evaluation Report Markdown
===================================================
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
    """Generate the Model Evaluation PDF report."""
    
    output_file = 'Model_Evaluation_Report.pdf'
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
    
    subheading_style = ParagraphStyle(
        'SubHeading',
        parent=styles['Heading3'],
        fontSize=9,
        spaceBefore=4,
        spaceAfter=2,
        textColor=colors.HexColor('#4a5568')
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
    elements.append(Paragraph("Model Evaluation Report", title_style))
    elements.append(Paragraph("Multi-Class Classification of 16 MBTI Personality Types", body_style))
    elements.append(Spacer(1, 6))
    
    # 1. Evaluation Metrics
    elements.append(Paragraph("1. Evaluation Metrics Used", heading_style))
    metrics_data = [
        ['Metric', 'Purpose'],
        ['Accuracy', 'Overall percentage of correct predictions'],
        ['Top-K Accuracy', 'True label within top K predicted classes'],
        ['Macro Precision', 'Average precision across all 16 classes'],
        ['Macro Recall', 'Average recall across all 16 classes'],
        ['Macro F1-Score', 'Harmonic mean of precision & recall (primary metric)'],
        ['Weighted F1', 'F1-score weighted by class support'],
    ]
    metrics_table = Table(metrics_data, colWidths=[1.3*inch, 5.5*inch])
    metrics_table.setStyle(table_style)
    elements.append(metrics_table)
    elements.append(Spacer(1, 6))
    
    # 2. Model Comparison
    elements.append(Paragraph("2. Model Performance Comparison", heading_style))
    
    results_data = [
        ['Model', 'Test Accuracy', 'Top-3 Acc', 'Macro F1', 'Train-Test Gap'],
        ['XGBoost', '98.22%', '99.65%', '0.9822', '1.73%'],
        ['Random Forest', '97.57%', '99.41%', '0.9757', '2.42%'],
        ['Logistic Regression', '91.90%', '97.81%', '0.9189', '0.14%'],
        ['LDA', '90.56%', '97.43%', '0.9055', '0.16%'],
    ]
    results_table = Table(results_data, colWidths=[1.4*inch, 1.0*inch, 0.9*inch, 0.8*inch, 1.0*inch])
    results_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2c5282')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BACKGROUND', (0, 1), (-1, 1), colors.HexColor('#c6f6d5')),  # Highlight best
        ('ROWBACKGROUNDS', (0, 2), (-1, -1), [colors.HexColor('#f7fafc'), colors.white]),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cbd5e0')),
    ])
    results_table.setStyle(results_style)
    elements.append(results_table)
    
    elements.append(Paragraph("<b>Baseline Comparison:</b> XGBoost achieves 98.22% vs 6.25% random guess — <b>15.7× improvement</b>", small_style))
    elements.append(Spacer(1, 6))
    
    # 3. Strengths & Weaknesses
    elements.append(Paragraph("3. Strengths and Weaknesses", heading_style))
    
    sw_data = [
        ['Model', 'Strengths', 'Weaknesses'],
        ['XGBoost', 'Highest accuracy, best Top-K, handles interactions', 'Slight overfitting, complex, longer training'],
        ['Random Forest', 'Strong accuracy, feature importance, robust', 'Highest overfitting, more memory'],
        ['Logistic Reg.', 'Best generalization, interpretable, fast', 'Lower accuracy, assumes linearity'],
        ['LDA', 'Fastest training, dimensionality reduction', 'Lowest accuracy, assumes Gaussian'],
    ]
    sw_table = Table(sw_data, colWidths=[1.0*inch, 2.8*inch, 2.5*inch])
    sw_table.setStyle(table_style)
    elements.append(sw_table)
    elements.append(Spacer(1, 6))
    
    # 4. Class Imbalance
    elements.append(Paragraph("4. Handling Class Imbalance", heading_style))
    elements.append(Paragraph(
        "<b>Strategy:</b> Stratified sampling maintained class proportions across train/validation/test splits. "
        "This ensures all 16 personality types are proportionally represented. <b>Macro F1-score</b> was used "
        "as the primary metric to treat all classes equally, regardless of frequency. "
        "Result: High macro F1 (0.90-0.98) indicates good performance across all personality types.",
        small_style
    ))
    elements.append(Spacer(1, 6))
    
    # 5. Practical Implications
    elements.append(Paragraph("5. Practical Implications", heading_style))
    
    impl_data = [
        ['Finding', 'Practical Implication'],
        ['98% accuracy achievable', 'ML can reliably predict personality from surveys'],
        ['Top-3 accuracy ~99.5%', 'True type almost always in top 3 suggestions'],
        ['Ensemble methods best', 'Use XGBoost/RF for production systems'],
        ['Linear models useful', 'Use Logistic Regression for explainability'],
    ]
    impl_table = Table(impl_data, colWidths=[1.8*inch, 4.0*inch])
    impl_table.setStyle(table_style)
    elements.append(impl_table)
    elements.append(Spacer(1, 4))
    
    elements.append(Paragraph("<b>Recommended Deployment:</b>", small_style))
    recommendations = [
        "• <b>Primary:</b> XGBoost for maximum accuracy",
        "• <b>Explainability:</b> Logistic Regression coefficients for feature interpretation",
        "• <b>User Experience:</b> Show top-3 predictions with confidence probabilities"
    ]
    for rec in recommendations:
        elements.append(Paragraph(rec, small_style))
    
    elements.append(Spacer(1, 4))
    elements.append(Paragraph("<b>Limitations:</b> Models trained on self-reported surveys; 16 discrete types simplify continuous personality traits; high accuracy may reflect survey structure.", small_style))
    
    # Build PDF
    doc.build(elements)
    print(f"PDF report generated: {output_file}")
    return output_file

if __name__ == "__main__":
    create_pdf_report()
