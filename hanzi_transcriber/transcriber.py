from .hanzi_model import Hanzi

class HanziTranscriber:
    def __init__(self, transcription_table, hanzi_table):
        self.transcription_table = transcription_table
        self.hanzi_table = hanzi_table

        self._max_syllable_length = None

    def get_transcriptions(self, syllable: str) -> list[str]:
        return self.transcription_table[syllable]

    def can_get_transcriptions(self, syllable: str) -> bool:
        return syllable in self.transcription_table

    def transcribe_token(self, token: str):
        # TODO: chooses variant based on HanziType
        pass

    def transcribe_tokens(self, tokens: list[str]):
        # TODO: uses transcribe_token for every token
        
        #transcribed_tokens = []
        # print(f"ht.tr\ttokens: {tokens!r}")
        # for token in tokens:
        #     other = ''
        #     print(f"ht.tr\tfor token: {token!r}")
        #     i = 0
        #     while i < len(token):
        #         matched = False
        #         last_match_i = 0
        #         other = token[last_match_i:]
        #         print(f"ht.tr\t\tfor i: {i!r}")
        #         for chunk_len in range(self.max_syllable_length, 0, -1):
        #             print(f"ht.tr\t\t\tchunk_len: {chunk_len!r}")
        #             chunk = token[i:chunk_len+i].lower()
        #             print(f"ht.tr\t\t\tchunk: {chunk}")
        #             if self.can_get_variants(chunk):
        #                 transcribed_tokens.append(self.get_variants(chunk))
        #                 print(f"ht.tr\t\t\t{chunk!r} can be transcribed")
        #                 i += len(chunk)
        #                 last_match_i = i
        #                 other = token[last_match_i:]
        #                 matched = True
        #                 break
        #         print(f"ht.tr\t\t\tlast_match_i: {last_match_i}, other: {other!r}")
        #         if not matched:
        #             i += 1
        #     if not other == '':
        #         transcribed_tokens.append(other)
        #return transcribed_tokens
        pass

    def __repr__(self):
        return f"HanziTranscriber(syllables={self.transcription_table}, variants={self.hanzi_table})"