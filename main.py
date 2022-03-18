from english_words import english_words_set

result = []
# Function to swap two characters in a character array
def swap(ch, i, j):

    temp = ch[i]
    ch[i] = ch[j]
    ch[j] = temp


# Recursive function to generate all permutations of a string
def permutations(ch, curr_index=0):
    ch = list(ch)

    if curr_index == len(ch) - 1:
        x = ''.join(ch)
        if x not in result:
            result.append(x)

    for i in range(curr_index, len(ch)):
        swap(ch, curr_index, i)
        permutations(ch, curr_index + 1)
        swap(ch, curr_index, i)

def normalizer(word):
    return word.lower().strip()


def checker(word, map):
    ll = []
    permutations(word)

    for w in result:
        if w in map:
            ll.append(w)

    return ll


def final(word):

    word = normalizer(word)
    eng_words = [normalizer(el) for el in english_words_set]
    res = checker(word, eng_words)

    print(' '.join(res))

final('fingre')

