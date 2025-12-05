from fpdf import FPDF

def text_to_pdf(text: str, output_path: str):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.set_auto_page_break(auto=True, margin=15)

    # Split text into lines and write each line
    for line in text.split("\n"):
        pdf.multi_cell(0, 8, line)

    pdf.output(output_path)
    return output_path
