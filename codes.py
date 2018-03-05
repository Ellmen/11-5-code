import itertools

def check_dist(w,partial_code):
    '''
        returns True if a word w has distance >= d to every word in partial_code;
        otherwise, returns False
    '''
    global d
    for codeword in partial_code:
        # perform bitwise XOR on codeword and w
        xor = int(codeword,2) ^ int(w,2)
        # turn the bitstring into a string, count num 1's
        if "{0:b}".format(xor).count("1") < d:
            return False
    return True

def construct_code():
    '''
        a backtracking routine that searches for a binary (n,M,d)-code
        the routine  maintains a global list (code) that is a partial code that contains candidate codewords
        for a binary (n,M,d)-code.
    '''
    global words, M, d, code

    if len(code) == M:
        return True
    for w in words:
        # we skip w if it is already in the partial code
        if w in code:
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
        words = ["".join(seq) for seq in itertools.product("01", repeat=n)]
        for M in range(16,17):
            for d in range(5,6):
                # initialize code to 0 vector WLOG
                code = [words[0]]
                # construct a binary (n,M,d)-code
                exists = construct_code()
                if not exists:
                    print "I didn't find a binary [",n,"|",M,"|",d,"] code!"
                else:
                    print "Here is a binary [",n,"|",M,"|",d,"] code:",code

