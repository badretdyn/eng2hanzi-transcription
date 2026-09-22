class ToHanziTranscriber:
    def __init__(self, table: dict[str, list[str]]):
        self.table = table

    def can_transcribe_to_hanzi(self, pinyin: str) -> bool:
        return pinyin in self.table

    def transcribe_candidates(self, pinyin: str) -> list[str]:
        return self.table[pinyin]

    def transcribe(self, pinyin: str) -> str:
        return self.table[pinyin][0]

    def transcribe_many_candidates(self, pinyin_list: list[str]) -> list[list[str]]:
        "Convert each pinyin to hanzi if a mapping exists; otherwise keep it unchanged."
        hanzi = []
        for p in pinyin_list:
            if self.can_transcribe_to_hanzi(p):
                hanzi.append(self.transcribe_candidates(p))
            else:
                hanzi.append(list(p))
        return hanzi

    def transcribe_many(self, pinyin_list: list[str]) -> list[str]:
        hanzi = []
        for p in pinyin_list:
            if self.can_transcribe_to_hanzi(p):
                hanzi.append(self.transcribe(p))
            else:
                hanzi.append(p)
        return hanzi