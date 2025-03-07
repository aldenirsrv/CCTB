from classes import Poisson
from scipy.stats import binom, poisson




def gen_table(r,k):
    """
    param: r (range - int)
    param: k (mean)
    """
    acumum = 0
    poi = Poisson(k)
     # Cabeçalho da tabela
    print(f"{'Index':<10} {'P(X=k)':<12} {'P(x=<k)':<12} {'P(x>=k)':<12} {'P(x>k)':<12}")
    print("=" * 60)  # Linha separadora
    for k, i in enumerate(range(r)):
        calc = poi.calculate(i, 'EXACTLY')
        equal_or_more = 1 - acumum
        acumum += calc
        more = 1 - acumum
        print(f"{i:<10} {round(calc, 4):<12} {round(acumum, 4):<12} {round(equal_or_more, 4):<12} {round(more, 4):<12}")

def calc_poi(mean, k, type):
    new_instance = Poisson(mean)
    return new_instance.calculate(k,type)


mean = 11
print("### Probability table and accumulator for mean {mean} ###")
gen_table(8,mean)

k_a = 6
calc_1 = calc_poi(mean, k_a, "EXACTLY")
print(calc_1)

print("### Probability table and accumulator for mean {mean}/2 ###")
gen_table(8,mean/2)

k_b = 3
calc_2 = calc_poi(mean/2, k_b, "EXACTLY")
print(calc_2)
k_c = 7

calc_3 = calc_poi(mean, k_c, "MORE_OR_EQUAL")
print(calc_3)


