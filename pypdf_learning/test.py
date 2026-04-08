from pypdf import PdfReader

reader = PdfReader("../assets/pdf_files/test.pdf")
page = reader.pages[0]

print(page.extract_text(extraction_mode="layout"))