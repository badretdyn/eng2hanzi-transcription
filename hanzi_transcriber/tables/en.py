from ..hanzi_model import Hanzi
from ..hanzi_tag import HanziTag

SEGMENTS_TO_HANZI_VARIANTS = {
    "li": ["利", "莉"],
    "ri": ["里", "丽"],
    "v": ["夫", "弗"]
}

HANZI_BY_CHAR = {
    "阿": Hanzi("阿", "ā"),
    "埃": Hanzi("埃", "āi"),
    "厄": Hanzi("厄", "è"),
    "伊": Hanzi("伊", "yī"),
    "奥": Hanzi("奥", "奥"),
    "乌": Hanzi("乌", "wū"),
    "尤": Hanzi("尤", "yóu"),
    "艾": Hanzi("艾", "ài"),
    "安": Hanzi("安", "ān"),
    "昂": Hanzi("昂", "áng"),
    "恩": Hanzi("恩", "ēn"),
    "鞥": Hanzi("鞥", "ēng"), # very old hanzi
    "因": Hanzi("因", "yīn"),
    "英": Hanzi("英", "yīng"),
    "温": Hanzi("温", "wēn"),
    "翁": Hanzi("翁", "wēng"),
    
    "布": Hanzi("布", "bù"),
    "巴": Hanzi("巴", "bā"),
    "贝": Hanzi("贝", "bèi"),
    "伯": Hanzi("伯", "bó"),
    "比": Hanzi("比", "bǐ"),
    "博": Hanzi("博", "bó"),
    "比尤": Hanzi("比尤", "bǐyóu"),
    "拜": Hanzi("拜", "bài"),
    "鲍": Hanzi("鲍", "bào"),
    "班": Hanzi("班", "bān"),
    "邦": Hanzi("邦", "bāng"),
    "本": Hanzi("本", "běn"),
    "蹦": Hanzi("蹦", "bèng"), # add
    "宾": Hanzi("宾", "bīn"),
    "冰": Hanzi("冰", "bīng"),
    "兵": Hanzi("兵", "bīng", frozenset({HanziTag.MALE})),
    
    "普": Hanzi("普", "pǔ"),
    "帕": Hanzi("帕", "pà"),
    "佩": Hanzi("佩", "pèi"),
    "珀": Hanzi("珀", "pò"),
    "皮": Hanzi("皮", "pí"),
    "波": Hanzi("波", "bō"),
    "普": Hanzi("普", "pǔ"),
    "皮尤": Hanzi("皮尤", "píyóu"),
    "派": Hanzi("派", "pài"),
    "保": Hanzi("保", "bǎo"),
    "潘": Hanzi("潘", "pān"),
    "庞": Hanzi("庞", "páng"),
    "盆": Hanzi("盆", "pén"),
    "彭": Hanzi("彭", "péng"),
    "品": Hanzi("品", "pǐn"),
    "平": Hanzi("平", "píng"),
    "蓬": Hanzi("蓬", "péng"),

    "利": Hanzi("利", "lì"),
    "莉": Hanzi("莉", "lì", frozenset({HanziTag.FEMALE})),
    "里": Hanzi("里", "lì"),
    "丽": Hanzi("丽", "lì", frozenset({HanziTag.FEMALE})),
    "夫": Hanzi("夫", "fū"),
    "弗": Hanzi("弗", "fú", frozenset({HanziTag.START}))
}

MANUAL_TRANSCRIPTIONS = {
    "coca-cola": "可口可乐",
    "ping-pong": "乒乓", # +球
    "babu": "八不"
}

NULL_INITIAL_SEGMENTS = {
    "a":        ["阿"],
    "e":        ["埃"],
    "ei":       ["埃"],
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
    "eng":      ["鞥"], # add
    "in":       ["因"],
    "ing":      ["英"],
    "un":       ["温"],
    "ung":      ["翁"],
    "on":       ["温"], # add
    "ong":      ["翁"] # add
}

B_INITIAL_SEGMENTS = {
    "b":         ["布"],
    "ba":        ["巴"],
    "be":        ["贝"],
    "bei":       ["贝"],
    "beo":       ["伯"],
    "bi":        ["比"],
    "bo":        ["博"],
    "bu":        ["布"],
    "biu":       ["比尤"],
    "bai":       ["拜"],
    "bao":       ["鲍"],
    "ban":       ["班"],
    "bang":      ["邦"],
    "ben":       ["本"],
    "beng":      ["蹦"], # add
    "bin":       ["宾"],
    "bing":      ["冰", "兵"], # add
    "bun":       ["本"],
    "bung":      ["邦"],
    "bon":       ["本"], # add
    "bong":      ["邦"] # add
}

P_INITIAL_SEGMENTS = {
    "p":         ["普"],
    "pa":        ["帕"],
    "pe":        ["佩"],
    "pei":       ["佩"],
    "peo":       ["珀"],
    "pi":        ["皮"],
    "po":        ["波"],
    "pu":        ["普"],
    "piu":       ["皮尤"],
    "pai":       ["派"],
    "pao":       ["保"],
    "pan":       ["潘"],
    "pang":      ["庞"],
    "pen":       ["盆"], # add
    "peng":      ["彭"],
    "pin":       ["品"], # add
    "ping":      ["平"],
    "pun":       ["盆"], # changed
    "pung":      ["蓬"],
    "pon":       ["盆"], # add
    "pong":      ["蓬"] # add
}

ALL_SEGMENTS = SEGMENTS_TO_HANZI_VARIANTS | NULL_INITIAL_SEGMENTS | B_INITIAL_SEGMENTS | P_INITIAL_SEGMENTS | P_INITIAL_SEGMENTS