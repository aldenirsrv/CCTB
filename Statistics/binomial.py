from classes import Binomial

n = 8
p = 0.62

# Solicita os valores de n e p
# n = int(input("Enter the total number of items (n): "))  # Converte para inteiro
# p = float(input("Enter the success rate (p): "))  # Converte para float
# ### Exactly [P(x = y)] - Probability mass function evaluated at k
bin = Binomial(n,p)

acumum = 0
def gen_table():
    """
    param: r (range - int)
    param: k (mean)
    """
    acumum = 0
    ca = 0
    binomial = Binomial(n,p)

     # Cabeçalho da tabela
    print(f"{'Index':<10} {'P(X=k)':<12} {'less':<12} {'More':<12} {'P(x>k)':<12}")
    print("=" * 60)  # Linha separadora
    for i in range(n + 1):
        calc = binomial.calculate(i,"EXACTLY")  # Probabilidade exata de X = k
        acumum += calc  # Atualiza o acumulador
        # more = 1 - acumum  # P(X > k)
        print(f"{i:<10} {round(calc, 4):<12} {round(acumum, 4):<12} {round(1-acumum, 4):<12}")


print("### Probability table and accumulator ###")
gen_table()
print("\n#### EXERCISES ####")
k = 2
exactly = bin.calculate(k,"EXACTLY")
print(f"EXACTLY [{k}]: {exactly}")

# ### More than [P(x > y)]
k_more = 5
more_than = bin.calculate(k_more,"MORE_THAN")
print(f"MORE_THAN [{k_more}]: {more_than}")

# ### More or equal than [P(x >= y)]
k_more_equal = 3
more_or_equal = bin.calculate(k_more_equal,"MORE_OR_EQUAL")
print(f"MORE_OR_EQUAL [{k_more_equal}]: {more_or_equal}")

# ### Less than [P(x < y)]
k_less = 5
less_than = bin.calculate(k_less,"LESS_THAN")
print(f"LESS_THAN [{k_less}]: {less_than}")

# ### Less or Equal  than [P(x <= y)]
k_less_equal = 3
less_or_equal = bin.calculate(k_less_equal,"LESS_OR_EQUAL")
print(f"LESS_OR_EQUAL [{k_less_equal}]: {less_or_equal}")