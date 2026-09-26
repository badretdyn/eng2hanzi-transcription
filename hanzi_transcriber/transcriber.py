from .hanzi_model import Hanzi
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

    def transcribe_word(self, word: list[str]):
        result = []
        for token in word:
            logger.debug("token: %r", token)
            if self.can_get_transcriptions(token):
                # TODO: choosing variant logic here, at least variants of begining and ending of a word
                # for now it always chooses first variant
                result.append(self.get_transcriptions(token)[0])
            else:
                result.append(token)
        return result

    def transcribe_words(self, words: list[list[str]]):
        result = []
        for word in words:
            logger.debug("word: %r", word)
            result.append("".join(self.transcribe_word(word)))
        return result

    def __repr__(self):
        return f"HanziTranscriber(syllables={self.transcription_table}, variants={self.hanzi_table})"