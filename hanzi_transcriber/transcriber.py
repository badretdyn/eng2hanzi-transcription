from .hanzi_model import *
import logging

logger = logging.getLogger(__name__)

class HanziTranscriber:
    def __init__(self, transcription_table, hanzi_table, combinations):
        self.transcription_table = transcription_table | combinations
        self.hanzi_table = hanzi_table
        #self.combinations = combinations

        self._max_syllable_length = None

    def get_transcriptions(self, syllable: str) -> list[str]:
        return self.transcription_table[syllable]

    def can_get_transcriptions(self, syllable: str) -> bool:
        return syllable in self.transcription_table

    def get_hanzi(self, hanzi: str) -> Hanzi:
        return self.hanzi_table[hanzi]

    def can_get_hanzi(self, hanzi: str) -> bool:
        return hanzi in self.transcription_table

    def is_female_variant(self, hanzi: str) -> bool:
        hanzi_instance = self.get_hanzi(hanzi)
        return HanziTag.FEMALE in hanzi_instance.tags

    def is_start_variant(self, hanzi: str) -> bool:
            hanzi_instance = self.get_hanzi(hanzi)
            return HanziTag.START in hanzi_instance.tags

    def is_end_variant(self, hanzi: str) -> bool:
            hanzi_instance = self.get_hanzi(hanzi)
            return HanziTag.END in hanzi_instance.tags
        

    def transcribe_word(self, word: list[str], is_female: bool = False) -> list[str]:
        result = []
        for i, token in enumerate(word):
            logger.debug("token: %r", token)
            if self.can_get_transcriptions(token):
                # TODO: choosing variant logic here, at least variants of begining and ending of a word
                # for now it always chooses first variant
                variants = self.get_transcriptions(token)
                for v in variants:
                    try:
                        if i == 0 and self.is_start_variant(v):
                            result.append(v)
                            break
                        elif i == len(word) - 1 and self.is_end_variant(v):
                            result.append(v)
                            break
                        if is_female and self.is_female_variant(v):
                            result.append(v)
                            break
                    except KeyError as e: pass
                else:
                    result.append(variants[0])
            else:
                result.append(token)
        return result

    def transcribe_words(self, words: list[list[str]], is_female: bool = False):
        result = []
        for word in words:
            logger.debug("word: %r", word)
            result.append(self.transcribe_word(word, is_female))
        return result

    def __repr__(self):
        return f"HanziTranscriber(syllables={self.transcription_table}, variants={self.hanzi_table})"