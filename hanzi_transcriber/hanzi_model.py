from .hanzi_tag import HanziTag

class Hanzi:
    __slots__ = ("char", "pinyin", "tags")

    def __init__(self, char: str, pinyin: str, tags: frozenset[HanziTag] = frozenset()):
        self.char = char
        self.pinyin = pinyin
        self.tags = tags

    def has(self, tag: HanziTag):
        return tag in self.tags

    def __eq__(self, other):
        return (isinstance(other, Hanzi)
                and self.char == other.char
                and self.pinyin == other.pinyin
                and self.tags == other.tags)

    def __hash__(self):
        return hash((self.char, self.pinyin, self.tags))

    def __repr__(self):
        tags = ', '.join(f"HanziTag.{t.name}" for t in sorted(self.tags, key=lambda t: t.name))
        args = f"{self.char!r}, {self.pinyin!r}"
        if tags:
            args += f", {{{tags}}}"
        return f"Hanzi({args})"