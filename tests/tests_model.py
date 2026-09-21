from eng2hanzi.eng_hanzi_transcriber import EngHanziTranscriber
from eng2hanzi.data import engrapheme_pinyin_transcription
from eng2hanzi.data import pinyin_hanzi_transcription

class Tests:
    @staticmethod
    def transcriber_test():
        transcriber = EngHanziTranscriber(engrapheme_pinyin_transcription, pinyin_hanzi_transcription)
        engraphems = ["", "?", "b", "ba", "p", "d", "t", "g", "k", "v", "w", "f"]

        for eg in engraphems:
            if not transcriber.can_transcribe_to_pinyin(eg):
                print(f'egr: {eg!r} \tno pinyin matches')
                continue
            pysyl = transcriber.engrapheme_to_pinyin(eg)

            if not transcriber.can_transcribe_to_hanzi(pysyl):
                print(f'egr: {eg!r} \tpygr: {pysyl!r}\tno hanzi matches')
                continue
            hanzi = transcriber.engrapheme_to_hanzi_candidates(eg)

            print(f'egr: {eg!r} \tpygr: {pysyl!r}\thanzi: {hanzi}')
    
    @staticmethod
    def grex_test():
        transcriber = EngHanziTranscriber(engrapheme_pinyin_transcription, pinyin_hanzi_transcription)
        text = "fbab k1t"
        graphemes = transcriber.extract_engraphemes(text)
        print(f"graphemes={graphemes}")
        pinyin = transcriber.engraphemes_to_pinyin(graphemes)
        print(f"pinyin={pinyin}")
        hanzi = transcriber.pinyin_list_to_hanzi(pinyin)
        print(f"hanzi={hanzi}")
    
if __name__ == '__main__':
    user_input = input('test=')
    match user_input:
        case '1':
            Tests.transcriber_test()
        case '2':
            Tests.grex_test()