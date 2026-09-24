from hanzi_transcriber.eng_hanzi_transcriber import EngHanziTranscriber
from hanzi_transcriber.data import engrapheme_pinyin_transcription
from hanzi_transcriber.data import pinyin_hanzi_transcription
from hanzi_transcriber.data import stable_hanzi_map

from hanzi_transcriber.transcriber import HanziTranscriber
from hanzi_transcriber.tables.en import en_table
from hanzi_transcriber.hanzi_model import *
from hanzi_transcriber.tables.en import EN_READING_TO_HANZI_VARIANTS, HANZI
from hanzi_transcriber.segment_extractor import SegmentExtractor

import logging

class Test:
    @staticmethod
    def transcriber_test():
        transcriber = EngHanziTranscriber(engrapheme_pinyin_transcription, pinyin_hanzi_transcription, stable_hanzi_map)
        engraphems = ["", "?", "b", "ba", "p", "d", "t", "g", "k", "v", "w", "f"]

        for eg in engraphems:
            if not transcriber.can_transcribe_to_pinyin(eg):
                print(f'egr: {eg!r} \tno pinyin matches')
                continue
            pysyl = transcriber.engrapheme_to_pinyin(eg)

            if not transcriber.can_transcribe_to_hanzi(pysyl):
                print(f'egr: {eg!r} \tpygr: {pysyl!r}\tno hanzi matches')
                continue
            hanzi = transcriber.pinyin_to_hanzi_candidates(pysyl)

            print(f'egr: {eg!r} \tpygr: {pysyl!r}\thanzi: {hanzi}')
    
    @staticmethod
    def grex_test():
        transcriber = EngHanziTranscriber(engrapheme_pinyin_transcription, pinyin_hanzi_transcription, stable_hanzi_map)
        text = "fbab k1t babuCoca Cola Type-A"
        graphemes = transcriber.extract_engraphemes(text)
        print(f"text={text}")
        print(f"graphemes={graphemes}")
        pinyin = transcriber.engraphemes_to_pinyin(graphemes)
        print(f"pinyin={pinyin}")
        hanzi = transcriber.pinyin_list_to_hanzi(pinyin)
        print(f"hanzi={hanzi}")
        hanzi_with_stable = transcriber.engraphemes_to_hanzi(graphemes)
        print(f"hanzi with stable={hanzi_with_stable}")
        print(f"hanzi with stable={''.join(hanzi_with_stable)}")
        custom = input("custom string=")
        print(f"{transcriber.engraphemes_to_hanzi(transcriber.extract_engraphemes(custom))}")
    
    @staticmethod
    def equals():
        hz_one = Hanzi("人", "rén", frozenset({HanziTag.END}))
        hz_other = Hanzi("人", "rén", frozenset({HanziTag.END}))
        print(f"{hz_one} == {hz_other}: {hz_one == hz_other}")
        hz_one_eval = eval(repr(hz_one), {"Hanzi": Hanzi, "HanziTag": HanziTag})
        print(f"evalable: {hz_one == hz_one_eval}")

    @staticmethod
    def tables():
        tr = HanziTranscriber(EN_READING_TO_HANZI_VARIANTS, HANZI)
        se = SegmentExtractor(EN_READING_TO_HANZI_VARIANTS)
        text = "  li ri  liri   LiRi Type Ali Lia  "
        splited = se.split_words(text)
        joined = se.join_tokens(splited)
        words = tr.transcribe_tokens(splited)
        print(f"text: {text!r}")
        print(f"splited: {splited!r}")
        print(f"joined: {joined!r}")
        print(f"text == joined: {text == joined!r}")
        print(f"words: {words}")

    @staticmethod
    def seex():
        se = SegmentExtractor(set(EN_READING_TO_HANZI_VARIANTS))
        segments = se.segment_word("alirib")
        print(segments)

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s %(name)s: %(message)s',
        datefmt='%H:%M:%S'
    )

    user_input = input('test=')
    match user_input:
        case '1':
            Test.transcriber_test()
        case '2':
            Test.grex_test()
        case '3':
            Test.equals()
        case '4':
            Test.tables()
        case '5':
            Test.seex()