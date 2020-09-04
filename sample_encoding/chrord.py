# encoding strings
lst=[x for x in 'python']
print(''.join([chr(ord(x)+1) for x in lst]))
