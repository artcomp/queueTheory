import math

def p0_TarefasNoSistema(p):
	return (1 - p)

def pN_TarefasNoSistema(p, n):
		return (1 - p) * ( p ** n)

def Utilization(p):
		return 1-(1 - p)
		

def EN(p):
	return (p/(1-p))

def VarN(p):
	return ( p / ( (1 - p) ** 2 ))

def p_K_jobs_na_fila(p, k):
	if k == 0:
		return (1 - (p ** 2))
	return (1 - p) * (p ** (k + 1) )

def ENq(p):
	return (p ** 2) / (1 - p)

def VarNq(p):
	a = p ** 2
	b = 1 + p - 2*p
	c = (1 - p) ** 2

	return (a * b) / c

def Er(mi, p):
	a = 1 / mi
	b = 1 - p 
	return a / b

def VARr(mi, p):
	a = (1 / mi) ** 2
	b = (1 - p) ** 2
	return a / b	

def Q_percentil_TEMPO_DE_RESPOSTA(q, er):
	a = math.log( ( 100 / ( 100 - q )  ) , math.e)
	return er * a

def Ew(mi, p):
	a = p * (1 / mi)
	b = 1 - p
	return a / b

def VARw(mi, p):
	a = (2 * p) * p
	b = (mi ** 2) * ( (1 - p) ** 2 )
	return a / b

def q_percentil_TEMPO_DE_ESPERA(q,p,ew):
	a = math.log( ( (100*p) / (100-q) )  , math.e)
	b = ew/p
	c = a * b
	return max(0, c)

def probabilityToFind_n_or_more_jobs_in_the_system(p, n):
	return p ** n


def main():
	lambdaa = 100
	S = 0.5
	mi = 1 / S
	p = lambdaa / mi
	pm= 0.833
	if p > 1:
		print("Condicao de estabilidade nao aceita")
		
	p0 = p0_TarefasNoSistema(p)
	print("P0 : %f " % p0)

	n = 1
	pn = pN_TarefasNoSistema(p,n)
	print("P%i : %f " % (n,pn))

	E_n = EN(p)
	print("E[n] : %f " % E_n)

	VAR_n = VarN(p)
	print("Var[n] : %f "  % VAR_n)

	k = 1
	p_k_jobs_na_filaa = p_K_jobs_na_fila(p, k)
	print("P%i : %f "  % (k,p_k_jobs_na_filaa))

	E_nq = ENq(p)
	print("E[nq] : %f "  % E_nq)

	VAR_nq = VarNq(p)
	print("Var[nq] : %f "  % VAR_nq)

	er = Er(mi, p)
	print("E[r] : %f "  % er)

	VAR_r = VARr(mi, p)
	print("Var[r] : %f "  % VAR_r)

	q = 90
	q_p_tp_resp =  Q_percentil_TEMPO_DE_RESPOSTA(q, er)
	print("P%i : %f "  % (q,q_p_tp_resp))


	e_w = Ew(mi, p)
	print("E[w] : %f "  % e_w)

	VAR_w = VARw(mi, p)
	print("Var[w] : %f "   % VAR_w)

	q = 90
	q_p_tp_espera = q_percentil_TEMPO_DE_ESPERA(q, p, e_w)
	print("P%i : %f "  % (q,q_p_tp_espera))


	n = 1
	prob_n_jobs_in_queue = probabilityToFind_n_or_more_jobs_in_the_system(p, n)
	print("Pn tarefas na fila : %f "  % (prob_n_jobs_in_queue))

if __name__ == '__main__':
		main()