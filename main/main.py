import io
import pathlib
import nltk
from nltk.corpus import stopwords
from nltk import FreqDist

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('tagsets')
nltk.download('stopwords')


class Main:
    def main(self):
        path = r'C:\Users\ROSSA\PycharmProjects\MostCommonVerbFinder\documents'
        filename = 'huttonreport.pdf'

        if 'pdf' in filename:
            data = self.parse_pdf(path, filename)
        else:
            data = self.read_txt(path, filename)

        data = self.clean_pdf(data)

        data = str(data)

        tokens = nltk.word_tokenize(data)
        tagged_tokens = nltk.pos_tag(tokens)
        verbs = [token[0] for token in tagged_tokens if token[1] in ['VB', 'VBD', 'VBP', 'VBG', 'VBN']]
        freq = FreqDist(verbs)
        freq_verb = freq.most_common(50)
        print(type(freq_verb))
        print(freq_verb)

    def split_text(self, text):
        split_text = text.split(".")
        return split_text

    def remove_stopwords(self, text):
        stop_words = stopwords.words('english')
        text = [w for w in text if w not in stop_words]
        return text


    def read_txt(self, path, filename):
        data = pathlib.Path(path, filename)
        fp = open(data, 'r', encoding="utf8")
        data = fp.read()
        return data

    def clean_pdf(self, text):
        text = text.replace("\n", " ")
        return text.encode('ascii', 'ignore')

    def parse_pdf(self, path, filename):
        data = pathlib.Path(path, filename)
        fp = open(data, 'rb')
        rsrcmgr = PDFResourceManager()
        retstr = io.StringIO()
        codec = 'utf-8'
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
        # Create a PDF interpreter object.
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        # Process each page contained in the document.

        for page in PDFPage.get_pages(fp):
            interpreter.process_page(page)
            data = retstr.getvalue()

        return data



if __name__ == '__main__':
    main = Main()
    main.main()


