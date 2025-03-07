
from classes import Counting
n = 9
r = 2

## Given order of the items is important we use permutation
counting = Counting(n,r)  
p = counting.perm()

## Given order of the items is not important we use combination
c = counting.comb()

#### FEMALE PROBABILITY ####
n_f = 7
r_f = 1
## Given order of the items is important we use permutation
counting_female = Counting(n_f,r_f)  
female = counting_female.perm()

#### MALE PROBABILITY ####
n_m = 5
r_m = 1
counting_male = Counting(n_m,r_m)  
male = counting_male.perm()


