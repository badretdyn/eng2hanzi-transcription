import logging

logger = logging.getLogger(__name__)

class SegmentExtractor:
    def __init__(self, segments: set[str], combinations: set[str]):
        self.segments = segments
        self.combinations = combinations
        self._max_segment_length = None
        
    @property
    def max_segment_length(self) -> int:
        if self._max_segment_length is None:
            self._max_segment_length = max(len(key) for key in self.segments)
        return self._max_segment_length
    
    def split_words(self, text: str):
        return text.split(" ")

    def join_words(self, words: list[str]):
        return " ".join(words)

    def join_tokens(self, tokens):
        return " ".join("".join(sub) for sub in tokens)

    def segment_word(self, word: str) -> list[str]:
        known_segments = self.segments
        segments = []

        logger.debug("segments: %r", known_segments)
        logger.debug("word: %r", word)

        unknown_start = 0

        seg_start_i = 0
        while seg_start_i < len(word):
            logger.debug("while %r < %r", seg_start_i, len(word))

            for seg_len in range(min(len(word) - seg_start_i, self.max_segment_length), 0, -1):
                logger.debug("\tfor %r", seg_len)
                candidate = word[seg_start_i:seg_start_i+seg_len].lower()

                logger.debug("\t\tcandidate i: %r:%r", seg_start_i, seg_start_i + seg_len)
                logger.debug("\t\tcandidate: %r", candidate)

                if candidate in known_segments:
                    logger.debug("\t\t%r is in known_segments", candidate)

                    if unknown_start < seg_start_i:
                        segments.append(word[unknown_start:seg_start_i])

                    logger.debug("\t\tunder: %r:%r", unknown_start, seg_start_i)
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
        result = []

        i = 0
        while i < len(words):
            j = i + 1
            next_word = ''
            while j < len(words):
                if not words[j] == '':
                    next_word = words[j]
                    break
                j += 1
            pair = words[i] + next_word

            if words[i] == '':
                result.append([''])
            elif pair in self.combinations:
                result.append([pair])
                i = j
            else:
                result.append(self.segment_word(words[i]))
            i += 1
        return result

    def __repr__(self):
        return f"SegmentExtractor(segments: {self.segments!r})"