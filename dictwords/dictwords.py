DEFAULT_DICT_FILE = "/usr/share/dict/words"

def partition_words_on_dictionary(words, dictionary):

    real_words = set()
    odd_words = set()
    for w in words:
        if w in dictionary:
            real_words.add(w)
        else:
            odd_words.add(w)

    return real_words, odd_words

def read_english_words(fname=DEFAULT_DICT_FILE):
    s = set()
    with open(fname, 'rb') as fin:
        for w in fin:
            s.add(str(s.strip()))
    return s
