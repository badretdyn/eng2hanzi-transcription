from .to_pinyin_transcriber import ToPinyinTranscriber
from .to_hanzi_transcriber import ToHanziTranscriber
from .grapheme_extractor import GraphemeExtractor

class EngHanziTranscriber:
    def __init__(self, engrapheme_pinyin_transcription, pinyin_hanzi_transcription):
        self.engrapheme_pinyin_transcriber = ToPinyinTranscriber(engrapheme_pinyin_transcription)
        self.pinyin_hanzi_transcriber = ToHanziTranscriber(pinyin_hanzi_transcription)
        self.grapheme_extractor = GraphemeExtractor(set(engrapheme_pinyin_transcription.keys()))

    def can_transcribe_to_pinyin(self, grapheme: str) -> bool:
        return self.engrapheme_pinyin_transcriber.can_transcribe(grapheme)

    def can_transcribe_to_hanzi(self, pinyin: str) -> bool:
        return self.pinyin_hanzi_transcriber.can_transcribe(pinyin)

    def engrapheme_to_pinyin(self, engrapheme: str) -> str:
        return self.engrapheme_pinyin_transcriber.transcribe(engrapheme)

    def engraphemes_to_pinyin(self, engraphemes: list[str]) -> list[str]:
        "Convert each grapheme to pinyin if a mapping exists; otherwise keep it unchanged."
        pinyin = []
        for e in engraphemes:
            if self.can_transcribe_to_pinyin(e):
                pinyin.append(self.engrapheme_to_pinyin(e))
            else:
                pinyin.append(e)
        return pinyin

    def pinyin_to_hanzi_candidates(self, pinyin: str) -> list[str]:
        return self.pinyin_hanzi_transcriber.transcribe(pinyin)

    def pinyin_list_to_hanzi(self, pinyin: list[str]) -> list[list[str]]:
        hanzi = []
        for p in pinyin:
            if self.can_transcribe_to_hanzi(p):
                hanzi.append(self.pinyin_to_hanzi_candidates(p))
            else:
                hanzi.append(list(p))
        return hanzi

    def engrapheme_to_hanzi_candidates(self, engrapheme: str) -> list[str]:
        pinyin = self.engrapheme_to_pinyin(engrapheme)
        return self.pinyin_to_hanzi_candidates(pinyin)

    def extract_engraphemes(self, text: str) -> list[str]:
        return self.grapheme_extractor.extract_graphemes(text)