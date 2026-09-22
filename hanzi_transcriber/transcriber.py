from .hanzi_model import Hanzi

class HanziTranscriber:
    def __init__(self, table):
        self.table = table

    def transcribe(self, key: str) -> Hanzi:
        return self.table[key]

    def can_transcribe(self, key: str) -> bool:
        return key in self.table