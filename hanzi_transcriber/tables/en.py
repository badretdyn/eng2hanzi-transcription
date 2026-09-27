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

NULL_INITIAL_SEGMENTS = {
    "a":        ["阿"],
    "e":        ["埃"],
    "eo":       ["厄"],
    "i":        ["伊"],
    "o":        ["奥"],
    "u":        ["乌"],
    "yu":       ["尤"],
    "ai":       ["艾"],
    "ao":       ["奥"],
    "an":       ["安"],
    "ang":      ["昂"],
    "en":       ["恩"],
    "eng":      ["鞥"],
    "in":       ["因"],
    "ing":      ["英"],
    "un":       ["温"],
    "ung":      ["翁"]
}

ALL_SEGMENTS = SEGMENTS_TO_HANZI_VARIANTS | NULL_INITIAL_SEGMENTS