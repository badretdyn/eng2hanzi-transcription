class ToPinyinTranscriber:
    def __init__(self, table: dict[str, str]):
        self.table = table

    def can_transcribe_to_pinyin(self, engrapheme: str) -> bool:
        return engrapheme in self.table

    def transcribe(self, engrapheme: str) -> str:
        return self.table[engrapheme]
    
    def transcribe_many(self, engraphemes: list[str]) -> list[str]:
        "Convert each grapheme to pinyin if a mapping exists; otherwise keep it unchanged."
        pinyin = []
        for e in engraphemes:
            if self.can_transcribe_to_pinyin(e):
                pinyin.append(self.transcribe(e))
            else:
                pinyin.append(e)
        return pinyin