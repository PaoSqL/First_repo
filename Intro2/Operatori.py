'''
Recap:
variabile
tipuri de date: char, string, int, double/float, boolean
operatori aritmetici: +, -, *, /, %
operatori de comparatie: <>, ==, !=, >=, <=
operatori logici:  and {si}, or {sau}, !(not)

Flow control (conditionare if/else)
'''

a = 3
b = 5
print(a+b) # 3 + 5 => 8
print(a == b) # a este egal cu b? =? False
print(a < b and a < 4) # True si True => True
print(a < b or a < 2) # True sau False => True

# cu mama sau tata sau (cu bunicu si bunica)
mama = False                               # statement
tata = True
bunicu = False
bunica = False
print(mama or tata or (bunicu and bunica)) # evaluare