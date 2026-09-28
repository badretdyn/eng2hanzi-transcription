from .hanzi_model import *
from .segment_extractor import SegmentExtractor
import logging

logger = logging.getLogger(__name__)

class HanziTranscriber:
    def __init__(self, segments: set[str], hanzi_table: set[str], manual_transcriptions: set[str]):
        self.segments = segments
        self.hanzi_table = hanzi_table
        self.manual_transcriptions = manual_transcriptions
        
        self._segex = SegmentExtractor(self.segments, self.manual_transcriptions)

    def get_hanzi_variants(self, segment: str) -> list[str]:
        return self.segments[segment]

    def has_hanzi_variants(self, segment: str) -> bool:
        return segment in self.segments

    def get_hanzi(self, hanzi: str) -> Hanzi:
        return self.hanzi_table[hanzi]

    def has_hanzi(self, hanzi: str) -> bool:
        return hanzi in self.hanzi_table

    def get_manual(self, segment: str) -> str:
        return self.manual_transcriptions[segment]

    def has_manual(self, segment: str) -> bool:
        return segment in self.manual_transcriptions

    def has_female_tag(self, hanzi: str) -> bool:
        hanzi_instance = self.get_hanzi(hanzi)
        return HanziTag.FEMALE in hanzi_instance.tags

    def has_start_tag(self, hanzi: str) -> bool:
        hanzi_instance = self.get_hanzi(hanzi)
        return HanziTag.START in hanzi_instance.tags

    def has_end_tag(self, hanzi: str) -> bool:
        hanzi_instance = self.get_hanzi(hanzi)
        return HanziTag.END in hanzi_instance.tags
        

    def transcribe_token(self, token: list[str], is_female: bool = False) -> list[str]:
        transcription_token = []
        for i, segment in enumerate(token):
            logger.debug("token: %r", segment)
            if self.has_manual(segment):
                transcription_token.append(self.get_manual(segment))
                continue
            if self.has_hanzi_variants(segment):
                variants = self.get_hanzi_variants(segment)
                for v in variants:
                    try:
                        if i == 0 and self.has_start_tag(v):
                            transcription_token.append(v)
                            break
                        if i == len(token) - 1 and self.has_end_tag(v):
                            transcription_token.append(v)
                            break
                        if is_female and self.has_female_tag(v):
                            transcription_token.append(v)
                            break
                    except KeyError:
                        logger.debug("KeyError while checking tags for variant %r", v)
                        continue
                else:
                    transcription_token.append(variants[0])
            else:
                transcription_token.append(segment)
        return transcription_token

    def transcribe_tokens(self, tokens: list[list[str]], is_female: bool = False) -> list[list[str]]:
        transcribed_tokens = []
        for token in tokens:
            logger.debug("word: %r", token)
            transcribed_tokens.append(self.transcribe_token(token, is_female))
        return transcribed_tokens

    def transcribe_text(self, text, is_female = False):
        words = self._segex.split_to_words(text)
        tokens = self._segex.tokenize_words(words)
        transcribed_tokens = self.transcribe_tokens(tokens, is_female)
        transcribed_text = self._segex.join_tokens(transcribed_tokens)
        return transcribed_text

    def __repr__(self):
        return f"HanziTranscriber(syllables={self.segments}, variants={self.hanzi_table})"