import os
import pdfplumber as pdfplumber


script_dir = os.path.dirname(__file__)
rel_path = "Product Specialist _ JD.pdf"
abs_file_path = os.path.join(script_dir, rel_path)
print("abs_file_path ::",abs_file_path)

complete_text = ''

with pdfplumber.open(abs_file_path) as pdf:
    # loop through every page and get the complete pdf into complete_text
    for pdf_page in pdf.pages:
        single_page_text = pdf_page.extract_text()
        complete_text = complete_text + single_page_text

print(complete_text)