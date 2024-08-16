# Доработанное. Самостоятельная работа по уроку "Произвольное число параметров".
def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.lower()
    other_words = list(other_words)
    other_words1 = list(map(str.lower, other_words))
    list_index = []
    for i in (other_words1[0:]):
        if root_word in i or i in root_word:
            list_index.append(other_words1.index(i))
        else:
            continue
    for j in list_index:
        same_words.append(other_words[j])
    return same_words


result1 = single_root_words('rich',
                            'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement',
                            'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
