import pathlib
import nltk

from nltk.corpus.reader.plaintext import PlaintextCorpusReader

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('tagsets')

class Main:
    def main(self):

        corpusdir = (r'C:\Users\ROSSA\PycharmProjects\MostCommonVerbFinder\new_corpus')  # Directory of corpus.

        newcorpus = PlaintextCorpusReader(corpusdir, '.*')

        data = pathlib.Path(r'C:\Users\ROSSA\PycharmProjects\CorpusCreator\new_corpus', 'file2.txt')
        fp = open(data, 'r', encoding="utf8")
        data = fp.read()

        tokens = nltk.word_tokenize(data)
        tagged_tokens = nltk.pos_tag(tokens)
        verbs = [token[0] for token in tagged_tokens if token[1] in ['VB', 'VBD', 'VBP', 'VBG']]
        from nltk import FreqDist
        freq = FreqDist(verbs)
        print(freq.most_common(20))
        #print(frequency)

      #  print(nltk.help.upenn_tagset())

    def split_text(self, text):
        split_text = text.split(".")
        return split_text


if __name__ == '__main__':
    main = Main()
    main.main()


