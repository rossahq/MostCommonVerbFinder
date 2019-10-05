import io
import pathlib
import nltk

from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('tagsets')

class Main:
    def main(self):
        path = r'C:\Users\ROSSA\PycharmProjects\MostCommonVerbFinder\documents'
        filename = 'iraq_summary.pdf'

        if 'pdf' in filename:
            data = self.parse_pdf(path, filename)
        else:
            data = self.read_txt(path, filename)

        tokens = nltk.word_tokenize(data)
        tagged_tokens = nltk.pos_tag(tokens)
        verbs = [token[0] for token in tagged_tokens if token[1] in ['VB', 'VBD', 'VBP', 'VBG']]
        from nltk import FreqDist
        freq = FreqDist(verbs)
        print(freq.most_common(20))
        #print(frequency)

        #print(nltk.help.upenn_tagset())


    def split_text(self, text):
        split_text = text.split(".")
        return split_text


    def read_txt(self, path, filename):
        data = pathlib.Path(path, filename)
        fp = open(data, 'r', encoding="utf8")
        data = fp.read()
        return data


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


