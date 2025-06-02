#CODE-1--to create a csv file

import csv
import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
csv_file = "data.csv"
data = [
    ["Date", "Product", "Units Sold", "Revenue"],
    ["01-06-2025", "Product A", 10, 1000],
    ["02-05-2025", "Product B", 5, 500],
    ["03-05-2025", "Product A", 8, 800],
    ["04-05-2025", "Product C", 12, 1800],
    ["05-05-2025", "Product B", 7, 700]
]
with open(csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
print(f"CSV file '{csv_file}' created successfully!")
def read_data(file_path):
    df = pd.read_csv(file_path)
    return df.describe()  # Basic statistics
data_summary = read_data(csv_file)
def generate_pdf_report(data_summary, output_pdf):
    c = canvas.Canvas(output_pdf, pagesize=A4)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 800, "Automated Report Generation")
    c.setFont("Helvetica", 12)
    y_position = 760
    # Add Column Headers
    c.drawString(100, y_position, "Statistic")
    c.drawString(250, y_position, "Value")
    y_position -= 30
    for row in data_summary.itertuples():
        c.drawString(100, y_position, f"{row.Index}")  # Statistic Name
        c.drawString(250, y_position, f"{row[1]:.2f}")  # Value
        y_position -= 20
    c.save()
pdf_output = "report.pdf"
generate_pdf_report(data_summary, pdf_output)
print(f"PDF report '{pdf_output}' generated successfully!")



#code-2--to generate a pdf through file

import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
def read_data(file_path):
    df = pd.read_csv(file_path)
    return df
csv_file = "data.csv"  # Ensure this file exists
data = read_data(csv_file)
def generate_pdf_report(data, output_pdf):
    c = canvas.Canvas(output_pdf, pagesize=A4)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 800, "Sales Report")
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, 770, "Date")
    c.drawString(150, 770, "Product")
    c.drawString(250, 770, "Units Sold")
    c.drawString(350, 770, "Revenue")
    c.setFont("Helvetica", 12)
    y_position = 750
    for index, row in data.iterrows():
        c.drawString(50, y_position, str(row["Date"]))
        c.drawString(150, y_position, str(row["Product"]))
        c.drawString(250, y_position, str(row["Units Sold"]))
        c.drawString(350, y_position, f"₹{row['Revenue']:,.2f}")
        y_position -= 20
    c.save()
pdf_output = "sales_report.pdf"
generate_pdf_report(data, pdf_output)
print(f"PDF report '{pdf_output}' generated successfully!")
