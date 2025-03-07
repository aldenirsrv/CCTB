import math
from scipy.stats import binom, poisson
from enum import Enum

round_size = 6
class Counting:
    def __init__(self, total_itens, items_to_choose)  -> float:
        self.total_itens = total_itens
        self.items_to_choose = items_to_choose
        # print(f"""\n### Class instantiated with the following parameters\nTotal_items (n): {self.total_itens}\nitams_to_chose(r): {self.items_to_choose}
        # """)

    def perm(self):
        result =  math.perm(self.total_itens,self.items_to_choose)
        print(f"Calculated using [PERMUTION]: {result}")
        return result
   
    def comb(self):
        result =  math.comb(self.total_itens,self.items_to_choose)
        print(f"Calculated using [Combination]: {result}")
        return result
    
    def student_details(self):
        return f'id [{self.student_id}] {self.name}'

# Definindo as condições usando Enum
class Condition(Enum):
    EXACTLY = "EXACTLY"
    MORE_THAN = "MORE_THAN"
    MORE_OR_EQUAL = "MORE_OR_EQUAL"
    LESS_THAN = "LESS_THAN"
    LESS_OR_EQUAL = "LESS_OR_EQUAL"

class Binomial:
    def __init__(self, sample, success_rate )  -> float:
        """
        Initializes the parameters for the binomial distribution calculation.

        :param sample: Total number of items (n).
        :param success_rate: Success rate (p) for the binomial calculation.
        :param  events: Number of events which we want to calculate the probability
        """
      
        self.sample = sample
        self.success_rate = success_rate
        
        mean = self.sample * self.success_rate
        sigma = math.sqrt(self.sample* self.success_rate*(1- self.success_rate))
        print(f"\nmean: {mean}\nStandard Derivation: {round(sigma,3)}")
        print("-------")
        

    def calculate(self,events, type:Condition) -> float:
        """
        Calculate the Binomial distribution

        :param events: Number of events which we want to calculate the probability.
        :param Type Enum: EXACTLY|MORE_THAN|MORE_OR_EQUAL|LESS_THAN|LESS_OR_EQUAL.
        """
        try:
            if type == None:
                raise ValueError("You need to pass a type")
        
            if events == None:
                raise ValueError("You need to pass a type")
            
            if type == 'EXACTLY':
                result = binom.pmf(events,self.sample,self.success_rate)
                # print(f'EXACTLY {result * 100:.2f}%')
                return round(result,round_size)
            elif type == 'MORE_THAN':
                result =  1 - binom.cdf(events,self.sample,self.success_rate)
                # print(f'MORE_THAN {result * 100:.2f}%')
                return round(result,round_size)
            elif type == 'MORE_OR_EQUAL':
                result =  1 - sum(binom.pmf(k,self.sample,self.success_rate) for k in range(events+1))
                # print(f'MORE_OR_EQUAL {result * 100:.2f}%')
                return round(result,round_size)
            elif type == 'LESS_THAN':
                result =  sum(binom.pmf(k,self.sample,self.success_rate) for k in range(events))
                # print(f'LESS_THAN {result * 100:.2f}%')
                return round(result,round_size)
            elif type == 'LESS_OR_EQUAL':
                result = sum(binom.pmf(k,self.sample,self.success_rate) for k in range(events+1))
                # print(f'LESS_OR_EQUAL {result * 100:.2f}%')
                return round(result,round_size)
            else:
                raise ValueError("""Opção inválida!\nChoose: EXACTLY | MORE_THAN | MORE_OR_EQUAL |  LESS_THAN | LESS_OR_EQUAL
                """)
        except ValueError as err:
            print(err)


class Poisson:
    def __init__(self, mean)  -> float:
        """
        Initializes the parameters for the binomial distribution calculation.

        :param mean:mean
        """
        self.mean = mean
        eurlers = 2.71828

        try:
            if mean == None:
                raise ValueError("You need to pass a mean")
            
            
        except ValueError as err:
            print(err)
    def calculate(self, k, type: Condition):
        if type == 'EXACTLY':
                #  ((self.mean ** k) * math.exp(-self.mean)) / math.factorial(k)
                result = poisson.pmf(k,self.mean)
                # print(f'EXACTLY {result * 100:.2f}%')
                return result
        elif type == 'MORE_THAN':
            result =  1 - poisson.cdf(k,self.mean)
            # print(f'MORE_THAN {result * 100:.2f}%')
            return round(result,round_size)
        elif type == 'MORE_OR_EQUAL':
            result =  1 - sum(poisson.pmf(k,self.mean) for k in range(k))
            # print(f'MORE_OR_EQUAL {result * 100:.2f}%')
            return round(result,round_size)
        elif type == 'LESS_THAN':
            result =  sum(poisson.pmf(k,self.mean) for k in range(k+1))
            # print(f'LESS_THAN {result * 100:.2f}%')
            return round(result,round_size)
        elif type == 'LESS_OR_EQUAL':
            result = sum(poisson.pmf(k,self.mean) for k in range(k))
            # print(f'LESS_OR_EQUAL {result * 100:.2f}%')
            return round(result,round_size)
        else:
            raise ValueError("""Opção inválida!\nChoose: EXACTLY | MORE_THAN | MORE_OR_EQUAL |  LESS_THAN | LESS_OR_EQUAL
            """)
        