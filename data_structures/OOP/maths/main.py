from classes import Math, ParentClass
# Maths
# Has 2 properties
#     * first_operand: int
#     * second_perand: int
#     * operator: str
# if oeration == "Add"
#     return first_operand + second_perand
# if oeration == "Sub"
#     return first_operand - second_perand

# Calculate
# Has e methods
#     *add(first_operand: int, second_perand: int) -> int Value
#         return first_operand + second_perand
#     sub(first_operand: int, second_perand: int) -> int Value
#          return first_operand - second_perand

# Use both the class , get the answer of:
#     * sum of 7 and 8
#     * sum 17 minus 7

# maths = Math(7,8,'add')
m = Math()
m.set_first_operand(7)
m.set_second_operand(8)
m.set_operand("add")
print(m.get_results())

m.set_operand("sub")
print(m.get_results())

calculate = ParentClass()
print(calculate.add(7,8))
print(calculate.add(17,7))
