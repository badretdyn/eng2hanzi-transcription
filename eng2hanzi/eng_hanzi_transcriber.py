from to_pinyin_transcriber import ToPinyinTranscriber
from to_hanzi_transcriber import ToHanziTranscriber
from grapheme_extractor import GraphemeExtractor

class EngHanziTranscriber:
    def __init__(self, engrapheme_pinyin_transcription, pinyin_hanzi_transcription):
        self.engrapheme_pinyin_transcriber = ToPinyinTranscriber(engrapheme_pinyin_transcription)
        self.pinyin_hanzi_transcriber = ToHanziTranscriber(pinyin_hanzi_transcription)
        self.grapheme_extractor = GraphemeExtractor(set(engrapheme_pinyin_transcription))

    def is_engrapheme(self, grapheme: str) -> bool:
        return self.engrapheme_pinyin_transcriber.can_transcribe(grapheme)

    def is_pinyin(self, pinyin: str) -> bool:
        return self.pinyin_hanzi_transcriber.can_transcribe(pinyin)

    def engrapheme_to_pinyin(self, engrapheme: str):
        return self.engrapheme_pinyin_transcriber.transcribe(engrapheme)

    def engrapheme_to_hanzi(self, engrapheme: list[str]):
        pinyin = self.engrapheme_to_pinyin(engrapheme)
        return self.pinyin_hanzi_transcriber.transcribe(pinyin)

    def get_engraphemes(self, text: str) -> list[str]:
        return self.grapheme_extractor.get_graphemes(text)