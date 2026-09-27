from ..hanzi_model import Hanzi
from ..hanzi_tag import HanziTag

SEGMENTS_TO_HANZI_VARIANTS = {
    "li": ["利", "莉"],
    "ri": ["里", "丽"],
    "v": ["夫", "弗"]
}

HANZI_BY_CHAR = {
    "利": Hanzi("利", "lì"),
    "莉": Hanzi("莉", "lì", frozenset({HanziTag.FEMALE})),
    "里": Hanzi("里", "lì"),
    "丽": Hanzi("丽", "lì", frozenset({HanziTag.FEMALE})),
    "夫": Hanzi("夫", "fū"),
    "弗": Hanzi("弗", "fú", frozenset({HanziTag.START}))
}

MANUAL_TRANSCRIPTIONS = {
    "coca cola": "可口可乐",
    "babu": "八不",
    "ba bu": "八不"
}

ALL_SEGMENTS = SEGMENTS_TO_HANZI_VARIANTS