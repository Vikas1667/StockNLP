# Load Pkgs
import fitz,sys
import glob
from tqdm import tqdm
import sumy

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer



# Parsing From String
import nltk
nltk.download('punkt')



def pdf_text_parser(input_pdf_path):
    text = ""
    pdf = fitz.open(input_pdf_path)
    print(pdf.pageCount)

    for page in pdf:
        text = text + str(page.get_text())
    print(text)
    return text


def summarizer(text):
    parser = PlaintextParser.from_string(text,Tokenizer("english"))
    # Get The Text
    parser.document
    # Get The Sentence Text
    parser.document.sentences
    # Get Word Tokens
    parser.document.words
    txtRank = TextRankSummarizer()
    summary_4 = txtRank(parser.document,4)
    summaize_text=""

    for summary in tqdm(summary_4):
        summaize_text=summaize_text+str(summary)

    return summaize_text
