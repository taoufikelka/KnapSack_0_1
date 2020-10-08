'''
	0/1 knaosack probleme solver
'''

m = 15				# Maximum weight 
P = [10,15,8,11,10,20,25,18,21,20]		# Profits
W = [ 1, 5,3, 9,10, 2, 5, 8, 6,10]		# Weights


V = []				# Table
maxw = []			# list of weights to max
S = [0] * len(P)		# Solutions list


#fonction to initiate variables
def init():
	# initiate table with 0
	for a in range(len(P)):
		V.append(0)
		V[a] = []
		for b in range(m+1):
			V[a].append(0)
	
	# Fill maxw with possible weights
	for i in range(m+1):
		maxw.append(i)

# fonction to print results
def prnt(T, M):
	print("\n\t[+]Table :\n")
	print ("\tP\tW\tL\t",maxw,"\n")
	for c in range(len(T)):
		print("\t",P[c],"\t",W[c],"\t",c,"\t",T[c])
	print("\n\t[+]Solusion :")
	print("\n\tObj\tP\tW")
	pro = mwei = 0
	for i in range(len(M)):
		if M[i] == 1:
			print("\t",i,"\t",P[i],"\t",W[i])
			pro = pro + P[i]
			mwei = mwei + W[i]
	print("\n[+]Max weight :",mwei,"\n[+]Total profit :",pro)

#fonction to find solution
def solution(T):
	mx = max(max(T))			#find max profit in table
	imx = V.index(max(T))			#index of max profit
	nx = mx - P[imx]			#max profit - profit of item with same index as max
	S[imx] = 1				#add solution

	while nx != 0:				#loop till n = 0
		imx = indx(imx, nx)		#calling fonction indx
		nx = nx - P[imx]		#reset n with value
	return S

# fonction to find next max profit and add solution
def indx(im, n):
	for i in range(im):
		if n in V[i]:
			S[i] = 1
			return i
			break

#fonction to fill table
def fillTab(T):
	for i in range(len(P)):			#loop for lines
		for w in maxw:			#loop for columns
			s = w-W[i]		#current weight - item (line) weight
			if s >= 0:		#if s >= 0 then the profit is the max of (previous line, same column's profit ; previous line, s column's profit)
				T[i][w] = max(T[i-1][w], (T[i-1][s]+P[i]))
			else :			#else profit is previous line's profit
				T[i][w] = T[i-1][w]

#initiate variables
init()
#calculate table values
fillTab(V)
#print results
prnt(V, solution(V))
