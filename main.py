
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



