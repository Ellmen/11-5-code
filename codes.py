import itertools
from random import shuffle


def weight(word):
    # return weight of a codeword (number of non-zero entries)
    return sum([1 if i != "0" else 0 for i in word])

def dist(word1, word2):
    # return distance of a codeword (number of entries that disagree)
    return sum([1 if i != j else 0 for i, j in zip(word1, word2)])

def check_dist(w,partial_code):
    '''
        returns True if a word w has distance >= d to every word in partial_code;
        otherwise, returns False
    '''
    global d, bad_words
    for codeword in partial_code:
        # count distance of codeword with w
        if (dist(codeword, w) < d):
            bad_words.add(codeword)
            return False
    return True

def construct_code():
    '''
        a backtracking routine that searches for a binary (n,M,d)-code
        the routine  maintains a global list (code) that is a partial code that contains candidate codewords
        for a binary (n,M,d)-code.
    '''
    global words, bad_words, M, d, code

    if len(code) == M:
        return True
    for w in words:
        # we skip w if it is already in the partial code or if
        # it is already distance < 5 from an existing code_word
        if w in code or w in bad_words:
            continue
        # check if d(w,c) >= d for all c in the partial code
        if check_dist(w, code):
            # if this is true, then add w to the partial code
            code.append(w)
            # recurse with new partial code and check if it was
            # completed to (n,M,d)-code. if it wasn't, remove w from code
            if not construct_code():
                code.remove(w)
            else:
                # if it was completed to a (n,M,d)-code, return True
                return True

if __name__ == '__main__':
    # we are looking for an (n, M, d) code
    n = 11
    M = 90
    d = 5

    # generate all bitstrings of length n
    words = ["".join(seq) for seq in itertools.product("012", repeat=n)]
    print "There are {} total words of length {}".format(len(words), n)

    # filter words with weight < d
    min_weight = 5
    words = filter(lambda i: weight(i) >= min_weight, words)
    print "There are {} total words of length {} and weight at least {}".format(len(words), n, min_weight)

    # shuffle words since they are generated in an order where they are close to each other
    shuffle(words)

    # create list of words to ignore once they are distance < d to the code
    bad_words = set()

    # initialize code to 0 vector and (0, 11111) WLOG
    first_word = "00000000000"
    second_word = "00000011111"

    code = [first_word, second_word]
    # construct a binary (n,M,d)-code
    exists = construct_code()
    print "There are {} words that were rejected and could be skipped".format(len(bad_words))
    if not exists:
        print "I didn't find a ternary [",n,"|",M,"|",d,"] code!"
    else:
        print "Here is a ternary [",n,"|",M,"|",d,"] code:",code

