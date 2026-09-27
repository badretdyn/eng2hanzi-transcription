from .hanzi_model import *
import logging

logger = logging.getLogger(__name__)

class HanziTranscriber:
    def __init__(self, transcription_table, hanzi_table, manual_transcriptions):
        self.transcription_table = transcription_table
        self.hanzi_table = hanzi_table
        self.manual_transcriptions = manual_transcriptions

    def get_hanzi_variants(self, syllable: str) -> list[str]:
        return self.transcription_table[syllable]

    def has_hanzi_variants(self, syllable: str) -> bool:
        return syllable in self.transcription_table

    def get_hanzi(self, hanzi: str) -> Hanzi:
        return self.hanzi_table[hanzi]

    def has_hanzi(self, hanzi: str) -> bool:
        return hanzi in self.hanzi_table

    def get_manual(self, manual: str) -> str:
        return self.manual_transcriptions[manual]

    def has_manual(self, manual: str) -> bool:
        return manual in self.manual_transcriptions

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
        result = []
        for i, token in enumerate(token):
            logger.debug("token: %r", token)
            if self.has_manual(token):
                result.append(self.get_manual(token))
                continue
            if self.has_hanzi_variants(token):
                variants = self.get_hanzi_variants(token)
                for v in variants:
                    try:
                        if i == 0 and self.has_start_tag(v):
                            result.append(v)
                            break
                        elif i == len(token) - 1 and self.has_end_tag(v):
                            result.append(v)
                            break
                        if is_female and self.has_female_tag(v):
                            result.append(v)
                            break
                    except KeyError as e: pass
                else:
                    result.append(variants[0])
            else:
                result.append(token)
        return result

    def transcribe_tokens(self, tokens: list[list[str]], is_female: bool = False):
        result = []
        for token in tokens:
            logger.debug("word: %r", token)
            result.append(self.transcribe_token(token, is_female))
        return result

    def __repr__(self):
        return f"HanziTranscriber(syllables={self.transcription_table}, variants={self.hanzi_table})"