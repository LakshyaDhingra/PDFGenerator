from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    topic = row["Topic"]

    pages = row["Pages"]

    pdf.add_page()

    # Setting header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=topic, align="L", ln=1)
    pdf.line(10, 21, 200, 21)

    # Setting footer for first/main page
    pdf.ln(260)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=12, txt=str(index + 1), align="R")

    for i in range(pages - 1):
        pdf.add_page()

pdf.output("output.pdf")
