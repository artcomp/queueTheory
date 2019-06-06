import math

def p0_TarefasNoSistema(m,p):
	somatorio = 0
	for n in range(1,m):
		somatorio = somatorio + (((m*p) ** n) / math.factorial(n))

	fracao = ((m * p) ** m) / (math.factorial(m) * (1 - p))

	p0 =( (1 + fracao + somatorio) ** (-1) )

	return p0

def p9_TarefasNoSistema(m, p):
	p0 = p0_TarefasNoSistema(m, p)
	return (p0 * ( (m*p) ** m ) ) / ( math.factorial(m) * (1 - p) )

def prob_of_queueing(m, p, p0):
	a = (m * p) ** m
	b = math.factorial(m) * (1 - p)

	return (a * p0) / b

def EN(m, p, n9):
	a = m * p
	b = (p * n9) / (1 - p)
	return a + b

def ENq(p, n9):
	return p * n9 / (1 - p)

def ER(mi, m , p, n9):
	a = 1 / mi
	b = n9 / ( m * (1 - p) )
	return a * (1 + b)

def EW(n9 , m, mi, p):
	a = m * mi * ( 1 - p)
	return n9 / a

def q_percentil_TEMPO_DE_RESPOSTA(q, p, ew, n9):
	a = ew/n9
	o = ( (100 * n9) / (100 - q) )
	b = math.log( o  , math.e )
	c = a*b
	return max(0, c)

def VARr(n9, mi, m, p):
	a = 1 / ( mi ** 2 )
	b = n9 * ( 2 - n9 )
	c = (m ** 2) * ( (1 - p) ** 2 )
	d = b / c

	return a * (1 + d)

def main():

	lambdaa = 0.6
	m = 7
	S = 5
	mi = 1 / S
	p = lambdaa / (m * mi)
	print("p = %f" % p)

	if p > 1:
		print("Condição de estabilidade nao aceita")

	p0 = p0_TarefasNoSistema(m,p)
	print("P0 : %f" % p0)

	p9 = p9_TarefasNoSistema(m, p)
	print("P~9 : %f" % p9)

	en = EN(m,p,p9)
	print("E[n] : %f " % en)

	enq = ENq(p, p9)
	print("E[nq] : %f " % enq)

	es = en - enq
	print("E[ns] : %f " % es)

	er = ER(mi, m , p, p9)
	print("E[r] : %f " % er)

	varr = VARr(p9, mi, m, p)
	print("Var[r] : %f " % varr)


	ew = EW(p9 , m, mi, p)
	print("E[w] : %f " % ew)

	q = 95
	q_w_90 = q_percentil_TEMPO_DE_RESPOSTA(q, p, ew, p9)
	print("Q percentil (%i) : %f " % (q,q_w_90))


if __name__ == '__main__':
	main()