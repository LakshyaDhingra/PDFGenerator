from fpdf import FPDF


def generate_pdf(topic, pages, file_path):
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=False, margin=0)

    pdf.add_page()

    # Setting header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=topic, align="L", ln=1)
    for i in range(20, 298, 10):
        pdf.line(10, i, 200, i)

    # Setting footer for first/main page
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=12, txt=topic, align="R")

    # Adding extra pages as required
    for i in range(pages - 1):
        pdf.add_page()
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=12, txt=topic, align="R")
        for i in range(20, 298, 10):
            pdf.line(10, i, 200, i)

    pdf.output(file_path)
