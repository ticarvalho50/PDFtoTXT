import pdfplumber

pdf_files = [r'pdf path'
    ]

max_pages = '' # number of pages you want to extract from the pdf

for i, pdf_file in enumerate(pdf_files):
    extracted_text = ""

    with pdfplumber.open(pdf_file) as pdf:
        num_pages = min(len(pdf.pages), max_pages)

        for page_number in range(num_pages):
            page = pdf.pages[page_number]
            text_page = page.extract_text()
            extracted_text += text_page

    txt_file = 'txt path.txt'
    with open(txt_file, 'w', encoding='utf-8') as txt:
        txt.write(extracted_text)

    print(f'Text from PDF {pdf_file} saved in {txt_file}')
