class Hanzi:
    def __init__(self, char: str, pinyin: str, role: str = "common"):
        self.char = char
        self.pinyin = pinyin
        self.role = role # common, start, end, female

    def __repr__(self):
        return f"Hanzi(char={self.char}, pinyin={self.pinyin}, role={self.role})"