from hanzi_transcriber.transcriber import HanziTranscriber
from hanzi_transcriber.hanzi_model import *
from hanzi_transcriber.tables.en import EN_READING_TO_HANZI_VARIANTS, HANZI, COMBINATIONS, ALL_SETS
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
        se = SegmentExtractor(set(ALL_SETS))
        tr = HanziTranscriber(ALL_SETS, HANZI)
        segments = se.segment_word("_liri_LIRI_")
        print(f"segments: {segments}")
        print(f"transcribed segments: {tr.transcribe_word(segments, True)}")

        text = "TypeA liRiB coca  cola  cocacola"
        print(f"text: {text!r}")
        words = se.split_words(text)
        print(f"words: {words!r}")
        tokens = se.segment_words(words)
        print(f"tokens: {tokens!r}")
        print(f"cocacola: {tr.get_transcriptions("cocacola")}")
        transcribed = tr.transcribe_words(tokens, True)
        print(f"transcribed: {transcribed!r}")
        joined_transcribed = se.join_tokens(transcribed)
        print(f"joined trasncribed: {joined_transcribed!r}")

    @staticmethod
    def hz_variants():
        tr = HanziTranscriber(ALL_SETS, HANZI)
        token = tr.transcribe_word(["v", "a", "li", "v"], True)
        print(f"token: {token}")

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