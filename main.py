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

class TypoMapper:

    def __init__(self):
        self.mapping = {}
        self.known_words = set()

    def add_fix(self, typo, correction):
        self.mapping[typo] = correction
        self.known_words.add(correction)
    
    def add_known_word(self, word):
        assert word not in self.mapping
        self.known_words.add(word)


def fix_typos_loop(words, dictionary):
    TM = TypoMapper()
    print "Initial word count: %d" % len(words)

    real_words, odd_words = partition_words_on_dictionary(words, dictionary)
    print "Partitioned word count:"
    print "-- Dictionary words:   %d" % len(real_words)
    print "-- Unrecognized words: %d" % len(odd_words)

def read_english_words(fname=DEFAULT_DICT_FILE):
    s = set()
    with open(fname, 'rb') as fin:
        for w in fin:
            s.add(str(s.strip()))
    return s
