from eng_hanzi_transcriber import EngHanziTranscriber
from data import engrapheme_pinyin_transcription
from data import pinyin_hanzi_transcription

def main():
    user_input = input("case=")
    transcriber = EngHanziTranscriber(engrapheme_pinyin_transcription, pinyin_hanzi_transcription)

    match user_input:
        case "1":
            # transcriber
            engraphems = ["", "?", "b", "ba", "p", "d", "t", "g", "k", "v", "w", "f"]

            for eg in engraphems:
                if not transcriber.is_engrapheme(eg):
                    print(f'egr: {eg!r} \tno pinyin matches')
                    continue
                pysyl = transcriber.engrapheme_to_pinyin(eg)

                if not transcriber.is_pinyin(pysyl):
                    print(f'egr: {eg!r} \tpygr: {pysyl!r}\tno hanzi matches')
                    continue
                hanzi = transcriber.engrapheme_to_hanzi(eg)

                print(f'egr: {eg!r} \tpygr: {pysyl!r}\thanzi: {hanzi}')
        
        case "2":
            # grapheme extractor
            text = "fbab k1t"
            graphemes = transcriber.get_engraphemes(text)
            print(f"graphemes={graphemes}")
            pinyin = [transcriber.engrapheme_to_pinyin(g) for g in graphemes[:3]]
            print(f"pinyin={pinyin}")
            # hanzi = [transcriber.engrapheme_to_hanzi(g) for g in graphemes]
            # print(f"hanzi={hanzi}")

if __name__ == '__main__':
    main()