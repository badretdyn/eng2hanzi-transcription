class ToHanziTranscriber:
    def __init__(self, table: dict[str, list[str]]):
        self.table = table

    def can_transcribe(self, key: str) -> bool:
        return key in self.table

    def transcribe(self, key: str) -> list[str]:
        return self.table[key]