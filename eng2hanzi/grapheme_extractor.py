class GraphemeExtractor:
    def __init__(self, graphemes : set[str]):
        self.graphemes = graphemes
        self._max_grapheme_length = None

    @property
    def max_grapheme_length(self) -> int:
        if self._max_grapheme_length is None:
            self._max_grapheme_length = max([len(g) for g in self.graphemes])
        return self._max_grapheme_length

    def is_grapheme(self, gr : str) -> bool:
        return gr in self.graphemes

    def extract_graphemes(self, text : str) -> list[str]:
        graphemes = []
        i = 0
        while i < len(text):
            matched = False
            for g in range(self.max_grapheme_length, 0, -1):
                grapheme = text[i:i+g]
                if self.is_grapheme(grapheme):
                    graphemes.append(grapheme)
                    i += len(grapheme)
                    matched = True
                    break
            if not matched:
                graphemes.append(text[i])
                i += 1
        return graphemes