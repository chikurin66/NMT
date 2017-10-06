# -*- coding: utf-8 -*-

# python3のみ対応

import sys

ASCII = 1
DIGIT = 2
KANA  = 4
ALL = ASCII | DIGIT | KANA

# list of ZENKAKU characters
z_ascii = ["ａ", "ｂ", "ｃ", "ｄ", "ｅ", "ｆ", "ｇ", "ｈ", "ｉ",
           "ｊ", "ｋ", "ｌ", "ｍ", "ｎ", "ｏ", "ｐ", "ｑ", "ｒ",
           "ｓ", "ｔ", "ｕ", "ｖ", "ｗ", "ｘ", "ｙ", "ｚ",
           "Ａ", "Ｂ", "Ｃ", "Ｄ", "Ｅ", "Ｆ", "Ｇ", "Ｈ", "Ｉ",
           "Ｊ", "Ｋ", "Ｌ", "Ｍ", "Ｎ", "Ｏ", "Ｐ", "Ｑ", "Ｒ",
           "Ｓ", "Ｔ", "Ｕ", "Ｖ", "Ｗ", "Ｘ", "Ｙ", "Ｚ",
           "！", "”", "＃", "＄", "％", "＆", "’", "（", "）",
           "＊", "＋", "，", "－", "．", "／", "：", "；", "＜",
           "＝", "＞", "？", "＠", "［", "￥", "］", "＾", "＿",
           "‘", "｛", "｜", "｝", "～", "　"]

z_digit = ["０", "１", "２", "３", "４",
       "５", "６", "７", "８", "９"]

z_kana = ["ア", "イ", "ウ", "エ", "オ",
          "カ", "キ", "ク", "ケ", "コ",
          "サ", "シ", "ス", "セ", "ソ",
          "タ", "チ", "ツ", "テ", "ト",
          "ナ", "ニ", "ヌ", "ネ", "ノ",
          "ハ", "ヒ", "フ", "ヘ", "ホ",
          "マ", "ミ", "ム", "メ", "モ",
          "ヤ", "ユ", "ヨ",
          "ラ", "リ", "ル", "レ", "ロ",
          "ワ", "ヲ", "ン",
          "ァ", "ィ", "ゥ", "ェ", "ォ",
          "ッ", "ャ", "ュ", "ョ", "ヴ",
          "ガ", "ギ", "グ", "ゲ", "ゴ",
          "ザ", "ジ", "ズ", "ゼ", "ゾ",
          "ダ", "ヂ", "ヅ", "デ", "ド",
          "バ", "ビ", "ブ", "ベ", "ボ",
          "パ", "ピ", "プ", "ペ", "ポ",
      "。", "、", "・", "゛", "゜", "「", "」", "ー"]

# list of HANKAKU characters
h_ascii = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
           "j", "k", "l", "m", "n", "o", "p", "q", "r",
           "s", "t", "", "v", "w", "x", "y", "z",
           "A", "B", "C", "D", "E", "F", "G", "H", "I",
           "J", "K", "L", "M", "N", "O", "P", "Q", "R",
           "S", "T", "", "V", "W", "X", "Y", "Z",
           "!", u'"', "#", "$", "%", "&", "'", "(", ")",
           "*", "+", ",", "-", ".", "/", ":", ";", "<",
           "=", ">", "?", "@", "[", "\\", "]", "^", "_",
           "`", "{", "|", "}", "~", " "]

h_digit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

h_kana = ["ｱ", "ｲ", "ｳ", "ｴ", "ｵ",
          "ｶ", "ｷ", "ｸ", "ｹ", "ｺ",
          "ｻ", "ｼ", "ｽ", "ｾ", "ｿ",
          "ﾀ", "ﾁ", "ﾂ", "ﾃ", "ﾄ",
          "ﾅ", "ﾆ", "ﾇ", "ﾈ", "ﾉ",
          "ﾊ", "ﾋ", "ﾌ", "ﾍ", "ﾎ",
          "ﾏ", "ﾐ", "ﾑ", "ﾒ", "ﾓ",
          "ﾔ", "ﾕ", "ﾖ",
          "ﾗ", "ﾘ", "ﾙ", "ﾚ", "ﾛ",
          "ﾜ", "ｦ", "ﾝ",
          "ｧ", "ｨ", "ｩ", "ｪ", "ｫ",
          "ｯ", "ｬ", "ｭ", "ｮ", "ｳﾞ",
          "ｶﾞ", "ｷﾞ", "ｸﾞ", "ｹﾞ", "ｺﾞ",
          "ｻﾞ", "ｼﾞ", "ｽﾞ", "ｾﾞ", "ｿﾞ",
          "ﾀﾞ", "ﾁﾞ", "ﾂﾞ", "ﾃﾞ", "ﾄﾞ",
          "ﾊﾞ", "ﾋﾞ", "ﾌﾞ", "ﾍﾞ", "ﾎﾞ",
          "ﾊﾟ", "ﾋﾟ", "ﾌﾟ", "ﾍﾟ", "ﾎﾟ",
      "｡", "､", "･", "ﾞ", "ﾟ", "｢", "｣", "ｰ"]

# maps of ascii
zh_ascii = {}
hz_ascii = {}

for i in range(len(z_ascii)):
    zh_ascii[z_ascii[i]] = h_ascii[i]
    hz_ascii[h_ascii[i]] = z_ascii[i]

del z_ascii, h_ascii

# maps of digit
zh_digit = {}
hz_digit = {}

for i in range(len(z_digit)):
    zh_digit[z_digit[i]] = h_digit[i]
    hz_digit[h_digit[i]] = z_digit[i]

del z_digit, h_digit

# maps of KANA
zh_kana = {}
hz_kana = {}

for i in range(len(z_kana)):
    zh_kana[z_kana[i]] = h_kana[i]
    hz_kana[h_kana[i]] = z_kana[i]

del z_kana, h_kana



def Zen2Han(text="", mode=ALL, ignore=()):
    result = list()

    for c in text:
        if c in ignore:
            result.append(c)

        elif (mode in (1, 3, 5, 7)) and (c in zh_ascii):
            result.append(zh_ascii[c])

        elif (mode in (2, 3, 6, 7)) and (c in zh_digit):
            result.append(zh_digit[c])

        elif (mode in range(4, 8)) and (c in zh_kana):
            result.append(zh_kana[c])

        else:
            result.append(c)

    return "".join(result)



def Han2Zen(text, mode=ALL, ignore=()):
    result = list()
    i = 0
    size = len(text)

    while i < size:
        if i < size - 1:
            if text[i:i+2] in ignore:
                result.append(text[i:i+2])
                i += 2
                continue

            elif (mode in range(4, 8)) and (text[i:i+2] in hz_kana):
                result.append(hz_kana[text[i:i+2]])
                i += 2
                continue

        if text[i:i+1] in ignore:
            result.append(text[i:i+1])

        elif (mode in (1, 3, 5, 7)) and (text[i:i+1] in hz_ascii):
            result.append(hz_ascii[text[i:i+1]])

        elif (mode in (2, 3, 6, 7)) and (text[i:i+1] in hz_digit):
            result.append(hz_digit[text[i:i+1]])

        elif (mode in range(4, 8)) and (text[i:i+1] in hz_kana):
            result.append(hz_kana[text[i:i+1]])

        else:
            result.append(text[i:i+1])

        i += 1

    return "".join(result)



if __name__ == "__main__":

    for line in sys.stdin:
        line = Zen2Han(line, ASCII | DIGIT )
        line = Han2Zen(line, KANA)
        print(line, end='')

'''
    teststr = "abcＤＥＦ123４５６ｱｶﾞｻダナバビﾌﾟﾍﾟ"

    print("original:", teststr)
    print("Han2Zen : ascii only:", Han2Zen(teststr, ASCII))
    print("Han2Zen : ascii and kana:", Han2Zen(teststr, ASCII|KANA))
    print("Zen2Han : digit only:", Zen2Han(teststr, DIGIT))
    print("Zen2Han : digit and kana:", Zen2Han(teststr, DIGIT|KANA))
    print("Zen2Han : digit and kana, except '５':", Zen2Han(teststr, DIGIT|KANA, ("５")))
'''
