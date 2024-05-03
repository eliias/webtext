from webtext import WebText


class TestWebText:
    def test_paragraphs(self):
        text = WebText("This is some text.\n\nAnother paragraph.")

        for paragraph in text.paragraphs():
            print(f"paragraph=`{paragraph}`")
            
    def test_sentences(self):
        text = WebText("This is some text.\n\nAnother paragraph.")

        for sentence in text.sentences():
            print(f"sentence=`{sentence}`")

    def test_words(self):
        text = WebText("This is some text.\n\nAnother paragraph.")
        
        for word in text.words():
            print(f"word=`{word}`")
