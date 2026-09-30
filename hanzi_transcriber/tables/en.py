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

    "格": Hanzi("格", "gé"),
    "加": Hanzi("加", "jiā"),
    "盖": Hanzi("盖", "gài"),
    "吉": Hanzi("吉", "jí"),
    "戈": Hanzi("戈", "gē"),
    "果": Hanzi("果", "guǒ"),
    "古": Hanzi("古", "gǔ"),
    "久": Hanzi("久", "jiǔ"),
    "盖": Hanzi("盖", "gài"),
    "高": Hanzi("高", "gāo"),
    "甘": Hanzi("甘", "gān"),
    "冈": Hanzi("冈", "gāng"),
    "根": Hanzi("根", "gēn"),
    "金": Hanzi("金", "jīn"),
    "京": Hanzi("京", "jīng"),
    "贡": Hanzi("贡", "gòng"),

    "克": Hanzi("克", "kè"),
    "卡": Hanzi("卡", "kǎ"),
    "凯": Hanzi("凯", "kǎi"),
    "基": Hanzi("基", "jī"),
    "科": Hanzi("科", "kē"),
    "库": Hanzi("库", "kù"),
    "丘": Hanzi("丘", "qiū"),
    "凯": Hanzi("凯", "kǎi"),
    "考": Hanzi("考", "kǎo"),
    "坎": Hanzi("坎", "kǎn"),
    "康": Hanzi("康", "kāng"),
    "肯": Hanzi("肯", "kěn"),
    "昆": Hanzi("昆", "kūn"),
    "孔": Hanzi("孔", "kǒng"),
    
    "夫": Hanzi("夫", "fū"),
    "弗": Hanzi("弗", "fú", frozenset({HanziTag.START})),
    "瓦": Hanzi("瓦", "wǎ"),
    "娃": Hanzi("娃", "wá", frozenset({HanziTag.FEMALE})),
    "韦": Hanzi("韦", "wéi"),
    "维": Hanzi("维", "wéi"),
    "沃": Hanzi("沃", "wò"),
    "武": Hanzi("武", "wǔ"),
    "维尤": Hanzi("维尤", "wéiyóu"),
    "万": Hanzi("万", "wàn"),
    "旺": Hanzi("旺", "wàng"),
    "文": Hanzi("文", "wén"),
    "温": Hanzi("温", "wēn"),
    "翁": Hanzi("翁", "wēng"),

    "利": Hanzi("利", "lì"),
    "莉": Hanzi("莉", "lì", frozenset({HanziTag.FEMALE})),
    "里": Hanzi("里", "lì"),
    "丽": Hanzi("丽", "lì", frozenset({HanziTag.FEMALE})),
    #"夫": Hanzi("夫", "fū"),
    #"弗": Hanzi("弗", "fú", frozenset({HanziTag.START}))
}

MANUAL_TRANSCRIPTIONS = {
    "coca-cola": "可口可乐",
    "ping-pong": "乒乓", # +球
    "babu": "八不"
}

NULL_INITIAL_SEGMENTS = {
    "a":        ["阿"],
    #"ya":            ["亚"],
    "e":        ["埃"],
    #"ye":            ["耶"],
    #"ei":       ["埃"],
    "eo":       ["厄"],
    "i":        ["伊"],
    #"yi":        ["伊"],
    "o":        ["奥"],
    "uo":           ["乌奥"],
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
    #"bia":        ["比亚"],
    "ba":        ["巴"],
    "be":        ["贝"],
    #"bie":        ["比耶"],
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
    #"pia":        ["皮亚"],
    "pe":        ["佩"],
    #"pie":        ["皮耶"],
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
    #"dia":        ["迪亚"],
    "de":        ["德"],
    #"die":        ["迪耶"],
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
    #"tia":        ["蒂亚"],
    "te":        ["特"],
    #"tie":        ["蒂耶"],
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

G_INITIAL_SEGMENTS = {
    "g":        ["格"],
    "ga":       ["加"],
    #"gia":       ["吉亚"],
    "ge":       ["盖"],
    #"gie":       ["吉耶"],
    "geo":      ["格"],
    "gi":       ["吉"],
    "go":       ["戈"],
    "guo":          ["果"],
    "gu":       ["古"],
    "giu":      ["久"],
    "gai":      ["盖"],
    "gao":      ["高"],
    "gan":      ["甘"],
    "gang":     ["冈"],
    "gen":      ["根"],
    "gin":      ["金"],
    "ging":     ["京"],
    "gun":      ["贡"],
    "gung":     ["贡"],
}

K_INITIAL_SEGMENTS = {
    "k":         ["克"],
    "ka":        ["卡"],
    #"kia":        ["基亚"],
    "ke":        ["凯"],
    #"kie":        ["基耶"],
    "keo":       ["克"],
    "ki":        ["基"],
    "ko":        ["科"],
    "kuo":          ["库奥"],
    "ku":        ["库"],
    "kiu":       ["丘"],
    "kai":       ["凯"],
    "kao":       ["考"],
    "kan":       ["坎"],
    "kang":      ["康"],
    "ken":       ["肯"],
    "kin":       ["金"],
    "king":      ["金"],
    "kun":       ["昆"],
    "kung":      ["孔"]
}

V_INITIAL_SEGMENTS = {
    "v":        ["夫", "弗"],
    "va":       ["瓦", "娃"],
    #"via":       ["维亚"],
    "ve":       ["韦"],
    #"vie":       ["维耶"],
    "veo":      ["弗"],
    "vi":       ["维"],
    "vo":       ["沃"],
    "vu":       ["武"],
    "viu":      ["维尤"],
    "vai":      ["韦"],
    "vao":      ["沃"],
    "van":      ["万"],
    "vang":     ["旺"],
    "ven":      ["文"],
    "vin":      ["温"],
    "ving":     ["温"],
    "vun":      ["文"],
    "vung":     ["翁"]
}

# alias: existing
_FINAL_ALIASES = {
    "ei": "e",
    "on": "un",
    "ong": "ung",
    "uo": "o",
    "eng": "en",
    #"io": "iu"
}

_TABLE_LIST = [
    ('', NULL_INITIAL_SEGMENTS),
    ('b', B_INITIAL_SEGMENTS),
    ('p', P_INITIAL_SEGMENTS),
    ('d', D_INITIAL_SEGMENTS),
    ('t', T_INITIAL_SEGMENTS),
    ('g', G_INITIAL_SEGMENTS),
    ('k', K_INITIAL_SEGMENTS),
    ('v', V_INITIAL_SEGMENTS)
]

def _build_tables(table_list, final_aliases):
    for i, table in enumerate(table_list[:]):
        #print(f"for table: {table}")
        for alias_final in final_aliases:
            #print(f"\tfor alias: {alias_final!r}")
            
            existing_final = final_aliases[alias_final]
            #print(f"\t\texisting final: {existing_final!r}")
            
            initial = table[0]
            value = ''
            new_segment = ''
            
            for segment in table[1]:
                #print(f"\t\tfor segment: {segment!r}")
                
                segment_wo_init = segment.replace(initial, "", 1)
                if segment_wo_init == existing_final:
                    #initial = segment.replace(existing_final, '')
                    value = table[1][segment]
                    #print(f"\t\t\tsegment: {segment!r}, value: {value!r}")
                    
                    new_segment = initial + alias_final
                    #print(f"\t\t\tnew segment: {new_segment!r}")

                    #print(f"\t\t\t{new_segment.replace(initial, "", 1)} != {alias_final}")
                    if new_segment.replace(initial, "", 1) != alias_final:
                        #print(f"\t\t\t{new_segment!r} is not ends on {alias_final!r}. continue")
                        continue

                    #print("\t\t\tbreak")
                    break
            else:
                #print(f"\t\t\tno segment.endswith({existing_final!r})")
                continue
                
            if new_segment in table[1]:
                #print(f"\t\t{new_segment!r} is in the table already. continue")
                continue

            #print(f"\t\tTABLE_LIST[{i}][{new_segment!r}] = {value!r}")
            table_list[i][1][new_segment] = value

    all_segments = dict()
    for t in table_list:
        all_segments = all_segments | t[1]

    return all_segments

_ALL_SEGMENTS = None

def get_all_segments():
    global _ALL_SEGMENTS
    if _ALL_SEGMENTS is None:
        _ALL_SEGMENTS = _build_tables(_TABLE_LIST, _FINAL_ALIASES)

        # all_segments = (
        #     SEGMENTS_TO_HANZI_VARIANTS
        #     | NULL_INITIAL_SEGMENTS
        #     | B_INITIAL_SEGMENTS
        #     | P_INITIAL_SEGMENTS
        #     | D_INITIAL_SEGMENTS
        #     | T_INITIAL_SEGMENTS
        #     | G_INITIAL_SEGMENTS
        #     )

    return _ALL_SEGMENTS
