from PyPDF2 import PdfReader

reader=PdfReader("AS1 ClassNotes.pdf")
for pages in reader.pages:
    print(pages.extract_text())


