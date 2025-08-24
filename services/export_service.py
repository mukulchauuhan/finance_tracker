# services/export_service.py
import pandas as pd
from fpdf import FPDF


def export_to_csv(df: pd.DataFrame, filename: str):
    try:
        df.to_csv(filename, index=True, encoding="utf-8")
        print(f"Report exported successfully to {filename}")
    except Exception as e:
        print(f"Failed to export report to CSV: {e}")


def export_report_to_pdf(title: str, data_dict: dict, filename: str):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, title, ln=True, align="C")

    for key, value in data_dict.items():
        pdf.cell(0, 10, f"{str(key).title()}: ${value:.2f}", ln=True)

    try:
        pdf.output(filename)
        print(f"Report exported successfully to {filename}")
    except Exception as e:
        print(f"Failed to export report to PDF: {e}")
