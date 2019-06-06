import math

def p0_TarefasNoSistema(p, B, m):
    s = 0
    for n in range(1,m):
        s = s + (  ((m * p) ** n) / math.factorial(n) )

    frac = ( (1 - (p ** (B-m+1)) )  * (m*p)**m ) / (math.factorial(m) * (1 - p) )

    value = 1 + frac + s

    return  value ** (-1)


def pN_TarefasNoSistema(p, B, m, n):
    p0 = p0_TarefasNoSistema(p,B,m)
    if n < m:
        value = (p0 * ( (m*p) ** n)  ) / math.factorial(n)
        return value
    else:
        value = ( p0 * (p ** n) * (m ** m )  ) / (math.factorial(m))    
        return value


def EN(B, list_pn):
    en = 0
    for i in range(1,B+1):
        en = en + i*list_pn[i-1]
    return en


def ENq(B, m, list_pn):
    enq = 0
    for n in range(m, B+1):
        enq = enq +  (n - m) * list_pn[n-1]
    return enq


def efective_arrival_rate(lambdaa, pb):
    return lambdaa * (1 - pb)

def avg_U_for_each_server(p, pb):
    return p * (1 - pb)

def ER(en, ear):
    return en / ear

def MeanWaitingTime(er, mi):
    return er - (1 / mi)

def lossRate(lambdaa, pb):
    return lambdaa * pb

def VARn(B, list_pn):
    en = 0
    for i in range(1,4+1):
        en = en + i**2 *list_pn[i-1]
    return en - (EN(B, list_pn) ** 2 )


def l_print(l):
    print("\n")
    for i in range(len(l)):
        print("P %i : %f" % (i+1, l[i]))
    print("\n")

def pn_erlang(m,p):
    a = ((m * p) ** m) / math.factorial(m)

    s = 0
    for j in range(m+1):
        s = s + ((m * p) ** j) / math.factorial(j)

    return a/s

def aux():

    lambdaa = 1
    B = 3
    m = 2
    p = 0.5
    S = 1
    mi = 1 / S
    p = lambdaa / (m * mi)
    p = 0.5

    print("P : %f " % p)
    print("B : %f " % B)
    print("M : %f " % m)

    p0 = p0_TarefasNoSistema(p, B, m)
    print("P0 : %f " % p0)
    
    v = [1,2,3]
    list_pn = list(map( lambda x: pN_TarefasNoSistema(p,B,m,x), v))
    
    l_print(list_pn)

    pb = list_pn[-1]


    en = EN(B,list_pn)
    print("E[n] : %f" % en)

    # varn = VARn(B,list_pn)
    # print("Var[n] : %f" % varn)

    enq = ENq(B,m, list_pn)
    print("E[nq] : %f" % enq)

    efec_arr_rate = efective_arrival_rate(lambdaa, pb)
    print("Effective Arrival Rate : %f " % efec_arr_rate)

    avg_u_per_server = avg_U_for_each_server(p, pb) 
    print("Avg Utilization of each server : %f " % avg_u_per_server)

    er = ER(en, efec_arr_rate)
    print("E[r] : %f " % er)

    mwt = MeanWaitingTime(er, mi)
    print("Mean waiting time : %f " % mwt)

    loss_rate = lossRate(lambdaa, pb)
    print("Loss Rate : %f " % loss_rate)

    pm_erlang = pn_erlang(m, p)
    print("Pm Erlang : %f " % pm_erlang)


def main():
    aux()

if __name__ == '__main__':
    main()
