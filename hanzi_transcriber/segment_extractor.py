class SegmentExtractor:
    def __init__(self, transcription_table: set[str, list[str]]):
        self.transcription_table = transcription_table

    def get_words(self, text: str):
        return text.split(" ")

    def join(self, tokens: list[str]):
        return " ".join(tokens)

    def tokenize_word(self):
        # TODO: return list of tokens. for string 'alib' returns ['a', '[利, 莉]', 'b'] for now
        pass

    def tokenize_words(self):
        # TODO: uses tokenize_word for every word from method get_words
        pass

    def __repr__(self):
        return f"SegmentExtractor(syllables: {self.transcription_table})"