alph = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о",
        "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]

word = str(input("Введите слово: "))
key_word = str(input("Введите ключевое слово: "))
c_ind = 0
result = ""


def shifr(word_symbol, key_symbol):
    try:
        tekushi_index = alph.index(word_symbol.lower())
        smesheni_index = alph.index(key_symbol.lower())
        if tekushi_index + smesheni_index >= len(alph):
            new_index = tekushi_index + smesheni_index - len(alph)
        else:
            new_index = tekushi_index + smesheni_index
        return alph[new_index]
    except ValueError:
        return word_symbol


def shifr_key():
    global c_ind
    if c_ind >= len(key_word):
        c_ind = 0
    result = key_word[c_ind]
    c_ind += 1
    return result


for symbol in word:
    result += shifr(symbol, shifr_key())

print(f"Результат: {result}")
