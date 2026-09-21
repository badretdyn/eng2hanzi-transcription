from .to_pinyin_transcriber import ToPinyinTranscriber
from .to_hanzi_transcriber import ToHanziTranscriber
from .grapheme_extractor import GraphemeExtractor

class EngHanziTranscriber:
    def __init__(self, engrapheme_pinyin_map, pinyin_hanzi_map, stable_hanzi_map):
        self.engrapheme_pinyin_transcriber = ToPinyinTranscriber(engrapheme_pinyin_map)
        self.pinyin_hanzi_transcriber = ToHanziTranscriber(pinyin_hanzi_map)
        self.stable_hanzi_map = stable_hanzi_map
        all_graphemes = set(self.stable_hanzi_map.keys()) | set(engrapheme_pinyin_map.keys())
        self.grapheme_extractor = GraphemeExtractor(all_graphemes)

    def _normalize(text: str) -> str:
        return text.replace(' ', '').lower()

    def can_transcribe_to_pinyin(self, grapheme: str) -> bool:
        return self.engrapheme_pinyin_transcriber.can_transcribe_to_pinyin(grapheme)

    def can_transcribe_to_hanzi(self, pinyin: str) -> bool:
        return self.pinyin_hanzi_transcriber.can_transcribe_to_hanzi(pinyin)

    def engrapheme_to_pinyin(self, engrapheme: str) -> str:
        return self.engrapheme_pinyin_transcriber.transcribe(engrapheme)

    def engraphemes_to_pinyin(self, engraphemes: list[str]) -> list[str]:
        return self.engrapheme_pinyin_transcriber.transcribe_many(engraphemes)

    def pinyin_to_hanzi_candidates(self, pinyin: str) -> list[str]:
        return self.pinyin_hanzi_transcriber.transcribe_candidates(pinyin)

    def pinyin_to_hanzi(self, pinyin: str) -> str:
        return self.pinyin_to_hanzi_candidates(pinyin)[0]

    def pinyin_list_to_hanzi_candidates(self, pinyin_list: list[str]) -> list[list[str]]:
        return self.pinyin_hanzi_transcriber.transcribe_many_candidates(pinyin_list)

    def pinyin_list_to_hanzi(self, pinyin_list: list[str]) -> list[str]:
        return self.pinyin_hanzi_transcriber.transcribe_many(pinyin_list)

    def engraphemes_to_hanzi(self, engraphemes: list[str]) -> list[str]:
        result: list[str] = []
        for e in engraphemes:
            if self.is_stable_transcription(e):
                result.append(self.stable_engrapheme_to_hanzi(e))
            elif self.can_transcribe_to_pinyin(e):
                pinyin = self.engrapheme_to_pinyin(e)
                result.append(self.pinyin_to_hanzi(pinyin))
            else:
                result.append(e)
        return result

    def extract_engraphemes(self, text: str) -> list[str]:
        return self.grapheme_extractor.extract_graphemes(text)

    def is_stable_transcription(self, text: str) -> bool:
        return text in self.stable_hanzi_map

    def stable_engrapheme_to_hanzi(self, engrapheme: str) -> str:
        return self.stable_hanzi_map[engrapheme]