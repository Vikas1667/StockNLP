from text_to_pdf import text_to_pdf
import fitz
from text_summarizer import pdf_text_parser,summarizer

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input_pdf_path = "./input_pdf/FoodWastage.pdf"
    text = pdf_text_parser(input_pdf_path)

    summarize_text = summarizer(text)
    print(summarize_text)

    output_filename = './output_pdf/output.pdf'

    # input_filename = 'myfile.txt'
    # file = open(input_filename, encoding='latin1')
    # text = file.read()
    # file.close()

    # text_to_pdf(text, output_filename)

