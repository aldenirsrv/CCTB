vancouver = {
    'Great': 14,
    'Good': 31,
    'Ok': 20,
    'Bad': 11
}
burnaby ={
    'Great': 30,
    'Good': 38,
    'Ok': 16,
    'Bad': 5
}

total_vancouver = sum(vancouver.values())
total_burnaby = sum(burnaby.values())
total_clients = total_vancouver + total_burnaby

p_burnaby = (total_burnaby/total_clients) * 100
print()
p_good = ((burnaby['Good'] + vancouver['Good']) / total_clients) * 100
p_good_2 = ((burnaby['Good']/total_clients) + (vancouver['Good'] / total_clients)) * 100
p_vancouver_good = ( vancouver['Good'] / total_clients) * 100

p_burnaby_or_great= ((total_burnaby / total_clients) + (vancouver['Great'] + burnaby['Great']) / total_clients - (burnaby['Great'] / total_clients)) * 100
p_burnaby_or_great2= ((total_burnaby / total_clients) + (vancouver['Great']) / total_clients) * 100
p_okay_given_vancouver = (vancouver['Ok'] / total_vancouver) * 100

 
# Resultados
print(f"a. Percentual de clientes que visitaram a cafeteria em Burnaby: {p_burnaby:.2f}%")
print(f"b. Percentual de clientes que classificaram como Good: {p_good:.2f}%")
print(f"b. Percentual de clientes que classificaram como Good 2: {p_good_2:.2f}%")
print(f"c. Percentual de clientes que visitaram Vancouver e classificaram como Good: {p_vancouver_good:.2f}%")
print(f"d. Percentual de clientes que visitaram Burnaby ou classificaram como Great: {p_burnaby_or_great:.2f}%")
print(f"d. Percentual de clientes que visitaram Burnaby ou classificaram como Great2: {p_burnaby_or_great2:.2f}%")
print(f"e. Percentual de clientes que classificaram como Okay, dado que visitaram a cafeteria em Vancouver: {p_okay_given_vancouver:.2f}%")