import logging

logger = logging.getLogger(__name__)

class SegmentExtractor:
    def __init__(self, segments: set[str], manual_transcriptions: set[str]):
        self.segments = segments
        self.manual_transcriptions = manual_transcriptions
        self._max_segment_length = None
        self._max_compound_length = None
        
    @property
    def max_segment_length(self) -> int:
        if self._max_segment_length is None:
            self._max_segment_length = max(len(key) for key in self.segments)
        return self._max_segment_length

    @property
    def max_compound_length(self) -> int:
        if self._max_compound_length is None:
            self._max_compound_length = max(len(key.split(" ")) for key in self.manual_transcriptions)
        return self._max_compound_length
    
    def split_to_words(self, text: str) -> list[str]:
        """Word is a string. List of words is strings separated by spaces. Saves sonsecutive spaces so does not trims string."""
        # TODO: have to split by all whitespace characters (\n, \t) and save it
        # when joining back just replace ' \n ' with '\n'?
        return text.split(" ")

    def join_words(self, words: list[str]) -> str:
        """Joins list of words by spaces."""
        return " ".join(words)

    def join_tokens(self, tokens: list[list[str]]) -> str:
        """Joins list of string lists. Between tokens spaces, between segments empty string."""
        return " ".join("".join(sub) for sub in tokens)

    def tokenize_word(self, word: str) -> list[str]:
        """Converts word to token: splits a string to list of segments. Segments can be transcribable and not."""
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

    def tokenize_words(self, words: list[str]) -> list[list[str]]:
        """Splits every word to token and returns list of tokens. Checks neighboring words for compound word and unite it in one list with one segment"""
        tokens = []
        
        i = 0
        while i < len(words):
            logger.debug("t_ws\twhile %r < %r", i, len(words))

            compound = words[i]

            word_count_in_compound = 1
            j = i + 1
            while j < len(words) and word_count_in_compound < self.max_compound_length:
                logger.debug("t_ws\t\twhile %r < %r and %r < %r", j, len(words), word_count_in_compound, self.max_compound_length)

                next_word = words[j]
                logger.debug("t_ws\t\t\tnext_word: %r", next_word)

                compound += ' ' + next_word
                logger.debug("t_ws\t\t\tcompound: %r", compound)

                word_count_in_compound += 1
                j += 1
                if compound in self.manual_transcriptions:
                    tokens.append([compound])
                    i = j
                    break
            else:
                if words[i] == '':
                    tokens.append([''])
                elif compound in self.manual_transcriptions:
                    tokens.append([compound])
                    i = j
                else:
                    tokens.append(self.tokenize_word(words[i]))
                i += 1
        return tokens

    def __repr__(self):
        return f"SegmentExtractor(segments: {self.segments!r})"