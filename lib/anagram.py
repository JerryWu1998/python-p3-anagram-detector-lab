# your code goes here!


class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, list):
        result = []
        for vocab in list:
            sort_vocab = sorted(vocab)
            if sort_vocab == sorted(self.word):
                result.append(vocab)

        return result
