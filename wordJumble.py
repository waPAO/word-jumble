def findCombinations(word: str, length: int) -> list:
    if len(word) == 1:
        return[word]
    
    final_combinations = []
    for i, v in enumerate(word):
        for combo in findCombinations(word[:i] + word[i+1:], length):
            check = v + combo
            if len(check) == length:
                final_combinations.append(check)
            else:
                final_combinations.append(check)
    return final_combinations


def findRealWords(combos: list, dictionary_words: list) -> list:
    checked_words = []
    for word in combos:
        if word in dictionary_words:
            checked_words.append(word)
    return checked_words

def find_message(words: list) -> str:
    letters1 = words[0][2] + words[0][4]
    letters2 = words[1][0] + words[1][1] + words[1][3]
    letters3 = words[2][4]
    letters4 = words[3][3] + words[3][4]
    secret_letters = letters1 + letters2 + letters3 + letters4
    return secret_letters
  


if __name__ == '__main__':
    
    dict_words = None
    with open('/usr/share/dict/words', 'r') as f:
        dict_words = f.read().splitlines()
    
    test_case = ['tefon', 'sokik', 'niumem', 'siconu']
    real_words = []
    for word in test_case:
      combos = findCombinations(word, len(word))
      real_words.append(findRealWords(combos, dict_words)[0])
    hidden_letters = find_message(real_words)
    print(hidden_letters)
    