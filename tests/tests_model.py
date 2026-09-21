from eng2hanzi.eng_hanzi_transcriber import EngHanziTranscriber
from eng2hanzi.data import engrapheme_pinyin_transcription
from eng2hanzi.data import pinyin_hanzi_transcription
from eng2hanzi.data import stable_hanzi_map

class Tests:
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
    
if __name__ == '__main__':
    user_input = input('test=')
    match user_input:
        case '1':
            Tests.transcriber_test()
        case '2':
            Tests.grex_test()