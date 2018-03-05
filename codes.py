import itertools


#################
# functions
#################

def check_dist(w,partial_code):
	'''
		returns True if a word w has distance >= d to every word in partial_code;
		otherwise, returns False
	'''
	global d
	for codeword in partial_code:				# go through each codeword of partial_code
		xor = int(codeword,2) ^ int(w,2)		# perform bitwise XOR on codeword and w
		if "{0:b}".format(xor).count("1") < d:		# turn the bitstring into a string, count num 1's
			return False
	return True

def construct_code():
	'''
		a backtracking routine that searches for a binary (n,M,d)-code
		the routine  maintains a global list (code) that is a partial code that contains candidate codewords
		for a binary (n,M,d)-code.
	'''
	global words, M, d, code				# state which variables are global

	if len(code) == M:					# check if the candidate codewords are (n,Md)-code
		return True					
	for w in words:						# go through all bitstrings of length n
		if w in code:					# we skip w if it is already in the partial code
			continue
		if check_dist(w, code):				# check if d(w,c) >= d for all c in the partial code 
			code.append(w)				# if this is true, then add w to the partial code
			if not construct_code():		# recurse with new partial code and check if it was
				code.remove(w)			# completed to (n,M,d)-code. if it wasn't, remove w from code 
			else:	
				return True			# if it was completed to a (n,M,d)-code, return True



####################
#  driver code
####################


for n in range(11,12):									# specify range of n values
	words = ["".join(seq) for seq in itertools.product("01", repeat=n)]		# generate all bitstrings of length n
	for M in range(16,17):								# specify range of num code words
		for d in range(5,6):							# specify range of min distance
			code = [words[0]]						# initialize code to 0 vector WLOG
			exists = construct_code()					# construct a binary (n,M,d)-code
			if not exists:							# if no code was found, say so
				print "I didn't find a binary [",n,"|",M,"|",d,"] code!"
			else:								# otherwise, print code
				print "Here is a binary [",n,"|",M,"|",d,"] code:",code

