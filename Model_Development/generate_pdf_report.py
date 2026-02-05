"""
Generate PDF from Model Development Report Markdown
====================================================
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
    """Generate the Model Development PDF report."""
    
    output_file = 'Model_Development_Report.pdf'
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
    
    # Table style
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2c5282')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 8),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 3),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f7fafc')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.HexColor('#f7fafc'), colors.white]),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cbd5e0')),
    ])
    
    elements = []
    
    # Title
    elements.append(Paragraph("Model Development Report", title_style))
    elements.append(Paragraph("Multi-Class Classification of 16 MBTI Personality Types", body_style))
    elements.append(Spacer(1, 8))
    
    # 1. Description
    elements.append(Paragraph("1. Description", heading_style))
    elements.append(Paragraph(
        "Four machine learning models were trained to classify 16 MBTI personality types using 60 survey questions. "
        "The dataset contains ~66,000 samples with personality trait responses as features.",
        small_style
    ))
    
    # 2. Models Trained
    elements.append(Paragraph("2. Models Trained & Rationale", heading_style))
    models_data = [
        ['Model', 'Rationale'],
        ['XGBoost', 'Gradient boosting ensemble; excellent for tabular data with complex patterns'],
        ['Random Forest', 'Bagging ensemble; robust to noise, provides feature importance'],
        ['Logistic Regression', 'Linear baseline; interpretable coefficients, multinomial softmax'],
        ['LDA', 'Dimensionality reduction classifier; finds class-separating linear combinations'],
    ]
    models_table = Table(models_data, colWidths=[1.3*inch, 5.5*inch])
    models_table.setStyle(table_style)
    elements.append(models_table)
    elements.append(Spacer(1, 6))
    
    # 3. Hyperparameters
    elements.append(Paragraph("3. Hyperparameter Choices", heading_style))
    
    hyper_data = [
        ['Model', 'Key Parameters'],
        ['XGBoost', 'n_estimators=500, learning_rate=0.1, max_depth=6, subsample=0.8, early_stopping=15'],
        ['Random Forest', 'n_estimators=100, max_depth=20, min_samples_split=5, max_features=sqrt'],
        ['Logistic Regression', 'multi_class=multinomial, solver=lbfgs, max_iter=1000, C=1.0'],
        ['LDA', 'solver=svd, n_components=15 (auto), tol=1e-4'],
    ]
    hyper_table = Table(hyper_data, colWidths=[1.3*inch, 5.5*inch])
    hyper_table.setStyle(table_style)
    elements.append(hyper_table)
    elements.append(Spacer(1, 6))
    
    # 4. Training Iterations
    elements.append(Paragraph("4. Training Iterations", heading_style))
    iter_data = [
        ['Model', 'Iterations/Trees', 'Notes'],
        ['XGBoost', '~100-150 (early stopped)', 'Stopped early from max 500 based on validation loss'],
        ['Random Forest', '100 trees', 'Full ensemble trained in parallel'],
        ['Logistic Regression', '~200-400 iterations', 'Converged before max_iter (1000)'],
        ['LDA', 'Single pass', 'Analytical solution via SVD, no iterations needed'],
    ]
    iter_table = Table(iter_data, colWidths=[1.3*inch, 1.3*inch, 4.2*inch])
    iter_table.setStyle(table_style)
    elements.append(iter_table)
    elements.append(Spacer(1, 6))
    
    # 5. Validation Strategy
    elements.append(Paragraph("5. Validation Strategy", heading_style))
    elements.append(Paragraph(
        "<b>Stratified Hold-Out Split (70/15/15):</b> Training (70%, ~46,200 samples), Validation (15%, ~9,900 samples), "
        "Test (15%, ~9,900 samples). Stratification maintained class proportions. All models used identical splits "
        "(random_state=42) for fair comparison. Validation set used for early stopping and model selection.",
        small_style
    ))
    elements.append(Spacer(1, 6))
    
    # 6. Training Results
    elements.append(Paragraph("6. Training Results", heading_style))
    results_data = [
        ['Model', 'Test Accuracy', 'Macro F1', 'Train Accuracy', 'Overfit Gap'],
        ['XGBoost', '98.22%', '0.9822', '99.95%', '1.73%'],
        ['Random Forest', '97.57%', '0.9757', '99.99%', '2.42%'],
        ['Logistic Regression', '91.90%', '0.9189', '92.04%', '0.14%'],
        ['LDA', '90.56%', '0.9055', '90.72%', '0.16%'],
    ]
    results_table = Table(results_data, colWidths=[1.3*inch, 1.0*inch, 0.9*inch, 1.1*inch, 0.9*inch])
    results_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2c5282')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 3),
        ('BACKGROUND', (0, 1), (4, 1), colors.HexColor('#c6f6d5')),  # Highlight best
        ('ROWBACKGROUNDS', (0, 2), (-1, -1), [colors.HexColor('#f7fafc'), colors.white]),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cbd5e0')),
    ])
    results_table.setStyle(results_style)
    elements.append(results_table)
    elements.append(Paragraph("<b>Best Model:</b> XGBoost achieved highest test accuracy (98.22%) with minimal overfitting.", small_style))
    elements.append(Spacer(1, 6))
    
    # 7. Computational Resources
    elements.append(Paragraph("7. Training Time & Computational Resources", heading_style))
    compute_data = [
        ['Model', 'Training Time', 'Hardware Utilization'],
        ['XGBoost', '~2-3 minutes', 'Multi-core CPU (n_jobs=-1)'],
        ['Random Forest', '~1-2 minutes', 'Multi-core CPU (n_jobs=-1)'],
        ['Logistic Regression', '~30-60 seconds', 'Multi-core CPU (n_jobs=-1)'],
        ['LDA', '~5-10 seconds', 'Single-core (analytical solution)'],
    ]
    compute_table = Table(compute_data, colWidths=[1.3*inch, 1.3*inch, 2.2*inch])
    compute_table.setStyle(table_style)
    elements.append(compute_table)
    elements.append(Paragraph(
        "<b>Environment:</b> Python 3.x with scikit-learn, XGBoost on standard desktop hardware. "
        "Total training time: ~5 minutes for all four models.",
        small_style
    ))
    elements.append(Spacer(1, 6))
    
    # 8. Key Findings
    elements.append(Paragraph("8. Key Findings", heading_style))
    findings = [
        "<b>Ensemble methods outperform linear models:</b> XGBoost and Random Forest achieved >97% accuracy vs ~91% for linear models.",
        "<b>Gradient boosting is optimal:</b> XGBoost's sequential error correction captures subtle personality patterns best.",
        "<b>Linear models generalize better:</b> Smaller train-test gap (0.14-0.16%) but lower overall accuracy.",
        "<b>Efficient training:</b> All models trained in under 5 minutes combined on standard hardware."
    ]
    for finding in findings:
        elements.append(Paragraph(f"• {finding}", small_style))
    
    # Build PDF
    doc.build(elements)
    print(f"PDF report generated: {output_file}")
    return output_file

if __name__ == "__main__":
    create_pdf_report()
