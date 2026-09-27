from hanzi_transcriber.transcriber import HanziTranscriber
from hanzi_transcriber.hanzi_model import *
from hanzi_transcriber.tables.en import HANZI_BY_CHAR, ALL_SEGMENTS, MANUAL_TRANSCRIPTIONS
from hanzi_transcriber.segment_extractor import SegmentExtractor

import logging

class Test:
    @staticmethod
    def equals():
        hz_one = Hanzi("人", "rén", frozenset({HanziTag.END}))
        hz_other = Hanzi("人", "rén", frozenset({HanziTag.END}))
        print(f"{hz_one} == {hz_other}: {hz_one == hz_other}")
        hz_one_eval = eval(repr(hz_one), {"Hanzi": Hanzi, "HanziTag": HanziTag})
        print(f"evalable: {hz_one == hz_one_eval}")

    @staticmethod
    def seex():
        se = SegmentExtractor(set(ALL_SEGMENTS), set(MANUAL_TRANSCRIPTIONS))
        tr = HanziTranscriber(ALL_SEGMENTS, HANZI_BY_CHAR, MANUAL_TRANSCRIPTIONS)
        segments = se.tokenize_word("_liri_LIRI_")
        print(f"segments: {segments}")
        print(f"transcribed segments: {tr.transcribe_token(segments, True)}")

        text = "TypeA liRiB coca  cola  cocacola coca cola ba bu babu bab u"
        print(f"text: {text!r}")
        words = se.split_to_words(text)
        print(f"words: {words!r}")
        tokens = se.tokenize_words(words)
        print(f"tokens: {tokens!r}")
        #print(f"cocacola: {tr.get_hanzi_variants("cocacola")}")
        transcribed = tr.transcribe_tokens(tokens, True)
        print(f"transcribed: {transcribed!r}")
        joined_transcribed = se.join_tokens(transcribed)
        print(f"joined trasncribed: {joined_transcribed!r}")

    @staticmethod
    def hz_variants():
        tr = HanziTranscriber(ALL_SEGMENTS, HANZI_BY_CHAR, MANUAL_TRANSCRIPTIONS)
        token = tr.transcribe_token(["v", "a", "li", "v"], True)
        print(f"token: {token}")

    @staticmethod
    def null_initial():
        tr = HanziTranscriber(ALL_SEGMENTS, HANZI_BY_CHAR, MANUAL_TRANSCRIPTIONS)
        se = SegmentExtractor(ALL_SEGMENTS, MANUAL_TRANSCRIPTIONS)
        token = tr.transcribe_token(["a", "u", "e", "en"], True)
        token_se = tr.transcribe_token(se.tokenize_word("aueen"))
        print(f"{token} == {token_se}: {token == token_se}")

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.WARNING,
        format='%(asctime)s %(levelname)s %(name)s: %(message)s',
        datefmt='%H:%M:%S'
    )

    user_input = input('test=')
    match user_input:
        case '1':
            Test.equals()
        case '2':
            Test.seex()
        case '3':
            Test.hz_variants()
        case '4':
            Test.null_initial()