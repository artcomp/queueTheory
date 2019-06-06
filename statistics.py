import math

def fatorial(n):
	if n < 2:
		return 1
	return n * fatorial(n-1)

def exponencial(alpha, x):
	# alpha > 0
	# x > 0
	# E[X] = alpha
 	# Var[X] = alpha**2
	
	return ( (1/alpha) * (math.e ** (-x/alpha)) )

def accExponencial(alpha, x):
	acc = 1 - (math.e **(-x/alpha))
	complement = 1 - acc
	return (acc, complement)

def poisson(k,lamb):
	# lambda >= 0
	# E[X] = lambda
	# Var[X] = lambda
	# f(x) = P[X = k]
	#
	# print("Poisson %f" % (poisson(15,10)) )
	return ((lamb ** k) * (math.e ** (-lamb))) / fatorial(k)

def accPoisson(k, lamb):
	acc = 0
	for i in range(k):
		acc = acc + poisson(i,lamb)
	return (acc, 1-acc)

def main():

	#######  POISSON #######
	k = 15+1
	lamb = 10
	pa=accPoisson(k,lamb)

	# print("Poisson Acc = %f" % pa )

	####### EXPONENCIAL ########
	x = 1
	alpha = 36
	# print("Exponencial : %f" % exponencial(alpha, 56))
	# print("Acc_exponencial : %f\nComplemento : %f" % (accExponencial(alpha, x)[0], accExponencial(alpha, x)[1]))

	v = [30]
	k = list(map(lambda x: accExponencial(alpha, x),v))
	for i in k:
		print(i)

if __name__ == '__main__':
	main()