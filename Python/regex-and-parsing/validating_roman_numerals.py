import re

thousands = 'M{0,3}'
# C[MD] is equal to CM|CD
hundreds = '(C[MD]|D?C{0,3})'
tens = '(X[CL]|L?X{0,3})'
digits = '(I[VX]|V?I{0,3})'

# Use the $ to match the end of the string
regex_pattern = thousands + hundreds + tens + digits + '$'

print(str(bool(re.match(regex_pattern, input()))))