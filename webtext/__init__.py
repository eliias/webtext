import re
from functools import lru_cache

import nltk
from nltk import PunktSentenceTokenizer, TreebankWordTokenizer

nltk.download('punkt')


class WebText(str):
    def __new__(cls, value=""):
        return super(WebText, cls).__new__(cls, value)

    @lru_cache(maxsize=None)
    def paragraphs(self) -> list['Paragraph']:
        tokens = re.split(r'\n{2,}', self)

        paragraphs = []
        start = 0
        for paragraph in tokens:
            start = self.find(paragraph, start)
            end = start + len(paragraph)
            paragraphs.append(Paragraph(self, start, end))

        return paragraphs

    def sentences(self) -> list['Sentence']:
        return [sentence for paragraph in self.paragraphs() for sentence in paragraph.sentences()]

    def words(self):
        return [word
                for paragraph in self.paragraphs()
                for sentence in paragraph.sentences()
                for word in sentence.words()]


class Paragraph:
    def __init__(self, text: WebText, start: int, end: int):
        self.text = text
        self.start = start
        self.end = end

    def __str__(self):
        return self.text[self.start:self.end]

    @lru_cache(maxsize=None)
    def sentences(self):
        text = self.__str__()
        tokenizer = PunktSentenceTokenizer()
        tokens = tokenizer.tokenize(text)

        # Find and store the indices of each sentence
        sentences = []
        start = 0
        for sentence in tokens:
            start = text.find(sentence, start)
            end = start + len(sentence)
            sentences.append(Sentence(self, self.start + start, self.start + end))
            start = end

        return sentences

    def words(self):
        return [word
                for sentence in self.sentences()
                for word in sentence.words()]


class Sentence:
    def __init__(self, paragraph: Paragraph, start: int, end: int):
        self.paragraph = paragraph
        self.start = start
        self.end = end

    def __str__(self):
        return self.paragraph.text[self.start:self.end]

    @lru_cache(maxsize=None)
    def words(self) -> list['Word']:
        text = self.__str__()
        tokenizer = TreebankWordTokenizer()
        tokens = tokenizer.tokenize(text)

        words = []
        start = 0
        for word in tokens:
            start = text.find(word, start)
            end = start + len(word)
            words.append(Word(self, self.start + start, self.start + end))
            start = end

        return words
        

class Word:
    def __init__(self, sentence: Sentence, start: int, end: int):
        self.sentence = sentence
        self.start = start
        self.end = end

    def __str__(self):
        return self.sentence.paragraph.text[self.start:self.end]
