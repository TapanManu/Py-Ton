morse={'a':'._','b':'_...','c':'_._.','d':'_..','e':'.'}

str="abcde"
code=[morse[i] for i in str if i in morse.keys()]
print(' '.join(code))
