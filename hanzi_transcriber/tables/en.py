from ..hanzi_model import Hanzi
from ..hanzi_tag import HanziTag

EN_READING_TO_HANZI_VARIANTS = {
    "li": ["利", "莉"],
    "ri": ["里", "丽"]
}

HANZI = {
    "利": Hanzi("利", "lì"),
    "莉": Hanzi("莉", "lì", frozenset({HanziTag.FEMALE})),
    "里": Hanzi("里", "lì"),
    "丽": Hanzi("丽", "lì", frozenset({HanziTag.FEMALE})),
}

COMBINATIONS = {
    "cocacola": ["可口可乐"]
}

en_table = {
    "b":    [Hanzi("布", "bù")],
    "ba":   [Hanzi("巴", "bā")],
    "v":    [Hanzi("夫", "fū"),     Hanzi("弗", "fú", "start")],
    "w":    [Hanzi("夫", "fū"),     Hanzi("弗", "fú", "start")],
    "vi":   [Hanzi("维", "wéi")],
    "wi":   [Hanzi("威", "wēi")],
    "li":   [Hanzi("利", "lì"),     Hanzi("莉", "lì", "female")],
    "ri":   [Hanzi("里", "lǐ"),     Hanzi("丽", "lì", "female")]
}