import itertools


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
    for n in range(11,12):
        # generate all bitstrings of length n
        min_weight = 6
        words = ["".join(seq) for seq in itertools.product("012", repeat=n)]
        print "There are {} total words of length {}".format(len(words), n)
        words = filter(lambda i: weight(i) >= min_weight, words)
        print "There are {} total words of length {} and weight at least {}".format(len(words), n, min_weight)
        bad_words = set()
        m = 30
        for M in range(m,m+1):
            for d in range(5,6):
                # initialize code to 0 vector WLOG
                code = [words[0]]
                second_word = "00000011111"
                code.append(second_word)
                # construct a binary (n,M,d)-code
                exists = construct_code()
                if not exists:
                    print "I didn't find a binary [",n,"|",M,"|",d,"] code!"
                else:
                    print "Here is a binary [",n,"|",M,"|",d,"] code:",code

