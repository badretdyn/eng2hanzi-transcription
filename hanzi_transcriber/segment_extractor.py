import logging

logger = logging.getLogger(__name__)

class SegmentExtractor:
    def __init__(self, segments: set[str]):
        self.segments = segments
        self._max_segment_length = None
        
    @property
    def max_segment_length(self) -> int:
        if self._max_segment_length is None:
            self._max_segment_length = max(len(key) for key in self.segments)
        return self._max_segment_length
    
    def split_words(self, text: str):
        return text.split(" ")

    def join_tokens(self, tokens: list[str]):
        return " ".join(tokens)

    def segment_word(self, word: str) -> list[str]:
        known_segments = self.segments
        segments = []

        logger.debug("segments: %r", known_segments)
        print(f"se.tw\tkeys:{known_segments!r}")
        print(f"se.tw\tword:{word!r}")

        unknown_start = 0

        seg_start_i = 0
        while seg_start_i < len(word):
            print(f'se.tw\twhile {seg_start_i} < {len(word)}')

            for seg_len in range(min(len(word) - seg_start_i, self.max_segment_length), 0, -1):
                print(f'se.tw\t\tfor {seg_len}')
                candidate = word[seg_start_i:seg_start_i+seg_len]

                print(f"se.tw\t\t\t{seg_start_i}:{seg_start_i+seg_len}")
                print(f"se.tw\t\t\tchunk: {candidate}")

                if candidate in known_segments:
                    print(f'se.tw\t\t\t{candidate} is in keys')

                    if unknown_start < seg_start_i:
                        segments.append(word[unknown_start:seg_start_i])

                    print(f'se.tw\t\t\tundef: {unknown_start}:{seg_start_i}')
                    segments.append(candidate)

                    seg_start_i += seg_len
                    unknown_start = seg_start_i
                    break
            else:
                seg_start_i += 1

        if unknown_start < len(word):
            segments.append(word[unknown_start:])

        return segments

    def segment_words(self, words):
        # TODO: uses tokenize_word for every word from method get_words
        result = []
        for word in words:
            result.extend(self.segment_word(word))
        return result

    def __repr__(self):
        return f"SegmentExtractor(segments: {self.segments!r})"