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
    #"鞥": Hanzi("鞥", "ēng"), # very old hanzi
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
    #"蹦": Hanzi("蹦", "bèng"), # add
    "宾": Hanzi("宾", "bīn"),
    #"冰": Hanzi("冰", "bīng"),
    #"兵": Hanzi("兵", "bīng", frozenset({HanziTag.MALE})),
    
    "普": Hanzi("普", "pǔ"),
    "帕": Hanzi("帕", "pà"),
    "佩": Hanzi("佩", "pèi"),
    "珀": Hanzi("珀", "pò"),
    "皮": Hanzi("皮", "pí"),
    "波": Hanzi("波", "bō"),
    "皮尤": Hanzi("皮尤", "píyóu"),
    "派": Hanzi("派", "pài"),
    "保": Hanzi("保", "bǎo"),
    "潘": Hanzi("潘", "pān"),
    "庞": Hanzi("庞", "páng"),
    #"盆": Hanzi("盆", "pén"),
    "彭": Hanzi("彭", "péng"),
    #"品": Hanzi("品", "pǐn"),
    "平": Hanzi("平", "píng"),
    "蓬": Hanzi("蓬", "péng"),

    "德": Hanzi("德", "dé"),
    "达": Hanzi("达", "dá"),
    "迪": Hanzi("迪", "dí"),
    "多": Hanzi("多", "duō"),
    "杜": Hanzi("杜", "dù"),
    "迪尤": Hanzi("迪尤", "díyóu"),
    "代": Hanzi("代", "dài"),
    "黛": Hanzi("黛", "dài", frozenset({HanziTag.FEMALE})),
    "道": Hanzi("道", "dào"),
    "丹": Hanzi("丹", "dān"),
    "当": Hanzi("当", "dāng"),
    "登": Hanzi("登", "dēng"),
    "丁": Hanzi("丁", "dīng"),
    "敦": Hanzi("敦", "dūn"),
    "东": Hanzi("东", "dōng"),

    "特": Hanzi("特", "tè"),
    "塔": Hanzi("塔", "tǎ"),
    "蒂": Hanzi("蒂", "dì"),
    "托": Hanzi("托", "tuō"),
    "图": Hanzi("图", "tú"),
    "蒂尤": Hanzi("蒂尤", "dìyóu"),
    "泰": Hanzi("泰", "tài"),
    "陶": Hanzi("陶", "táo"),
    "坦": Hanzi("坦", "tǎn"),
    "唐": Hanzi("唐", "táng"),
    "滕": Hanzi("滕", "téng"),
    "廷": Hanzi("廷", "tíng"),
    "通": Hanzi("通", "tōng"),
    

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
    #"ei":       ["埃"],
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
    #"eng":      ["恩"],
    "in":       ["因"],
    "ing":      ["英"],
    "un":       ["温"],
    "ung":      ["翁"],
    #"on":       ["温"],
    #"ong":      ["翁"]
}

B_INITIAL_SEGMENTS = {
    "b":         ["布"],
    "ba":        ["巴"],
    "be":        ["贝"],
    #"bei":       ["贝"],
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
    #"beng":      ["本"],
    "bin":       ["宾"],
    "bing":      ["宾"],
    "bun":       ["本"],
    "bung":      ["邦"],
    #"bon":       ["本"],
    #"bong":      ["邦"]
}

P_INITIAL_SEGMENTS = {
    "p":         ["普"],
    "pa":        ["帕"],
    "pe":        ["佩"],
    #"pei":       ["佩"],
    "peo":       ["珀"],
    "pi":        ["皮"],
    "po":        ["波"],
    "pu":        ["普"],
    "piu":       ["皮尤"],
    "pai":       ["派"],
    "pao":       ["保"],
    "pan":       ["潘"],
    "pang":      ["庞"],
    "pen":       ["彭"],
    #"peng":      ["彭"],
    "pin":       ["平"],
    "ping":      ["平"],
    "pun":       ["蓬"],
    "pung":      ["蓬"],
    #"pon":       ["蓬"], 
    #"pong":      ["蓬"]
}

D_INITIAL_SEGMENTS = {
    "d":        ["德"],
    "da":        ["达"],
    "de":        ["德"],
    #"dei":       ["德"],
    "deo":       ["德"],
    "di":        ["迪"],
    "do":        ["多"],
    "du":        ["杜"],
    "diu":       ["迪尤"],
    "dai":       ["代", "黛"],
    "dao":       ["道"],
    "dan":       ["丹"],
    "dang":      ["当"],
    "den":       ["登"],
    #"deng":      ["登"],
    "din":       ["丁"],
    "ding":      ["丁"],
    "dun":       ["敦"],
    "dung":      ["东"],
    #"don":       ["敦"],
    #"dong":      ["东"]
}

T_INITIAL_SEGMENTS = {
    "t":         ["特"],
    "ta":        ["塔"],
    "te":        ["特"],
    #"tei":       ["特"],
    "teo":       ["特"],
    "ti":        ["蒂"],
    "to":        ["托"],
    "tu":        ["图"],
    "tyu":       ["蒂尤"],
    "tai":       ["泰"],
    "tao":       ["陶"],
    "tan":       ["坦"],
    "tang":      ["唐"],
    "ten":       ["滕"],
    #"teng":      ["滕"],
    "tin":       ["廷"],
    "ting":      ["廷"],
    "tun":       ["通"],
    "tung":      ["通"],
    #"ton":       ["通"],
    #"tong":      ["通"]
}

# alias: existing
FINAL_ALIASES = {
    "ei": "e",
    "on": "un",
    "ong": "ung",
    "uo": "o",
    "eng": "en"
}

TABLE_LIST = [
    ('', NULL_INITIAL_SEGMENTS),
    ('b', B_INITIAL_SEGMENTS),
    ('p', P_INITIAL_SEGMENTS),
    ('d', D_INITIAL_SEGMENTS),
    ('t', T_INITIAL_SEGMENTS)
]

for i, table in enumerate(TABLE_LIST[:]):
    print(f"for table: {table}")
    for alias_final in FINAL_ALIASES:
        print(f"\tfor alias: {alias_final!r}")
        
        existing_final = FINAL_ALIASES[alias_final]
        print(f"\t\texisting final: {existing_final!r}")
        
        initial = table[0]
        value = ''
        new_segment = ''
        
        for segment in table[1]:
            print(f"\t\tfor segment: {segment!r}")
            
            if segment.endswith(existing_final):
                #initial = segment.replace(existing_final, '')
                value = table[1][segment]
                print(f"\t\t\tinitial: {initial!r}, value: {value!r}. break")
                
                new_segment = initial + alias_final
                print(f"\t\t\tnew segment: {new_segment!r}")
                
                if new_segment.replace(initial, "") != alias_final:
                    print(f"\t\t\t{new_segment} is not ends on {alias_final}")
                    continue
                break
        else:
            print(f"\t\t\tno segment.endswith({existing_final!r})")
            continue
            
        if new_segment in table[1]:
            print(f"\t\t{new_segment!r} is in the table already. continue")
            continue

        print(f"\t\tTABLE_LIST[{i}][{new_segment!r}] = {value!r}")
        TABLE_LIST[i][1][new_segment] = value

ALL_SEGMENTS = (
    SEGMENTS_TO_HANZI_VARIANTS
    | NULL_INITIAL_SEGMENTS
    | B_INITIAL_SEGMENTS
    | P_INITIAL_SEGMENTS
    | D_INITIAL_SEGMENTS
    | T_INITIAL_SEGMENTS
    )