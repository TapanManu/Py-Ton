morse={'a':'._','b':'_...','c':'_._.','d':'_..','e':'.','f':'.._.','g':'__.','h':'.....','i':'..','j':'.___',
'k':'_._','l':'._..','m':'__','n':'_.','o':'___','p':'.__.','q':'__._','r':'._.','s':'...','t':'_',
'u':'.._','v':'..._','w':'.__','x':'_.._','y':'_.__','z':'__..'}

def no_asterick(str):
	ls=[x for x in str if x != '*']
	return ''.join(ls)

def decode(morse,*keys):
	dec=[]
	for k in keys:
		p = ' '.join(k)
		k = no_asterick(p)
		dec= [''.join([ m for m in morse if j in morse.values() and j == morse[m]])for j in k.split(' ')]
	return dec

#print(no_asterick('*abcd'))


# * each character  # each word
str="#*_...  *._  *_ *__ *._ *_. #*_ *..... *. #*_.. *._ *._. *_._ #*_._ *_. *.. *__. *..... *_"
str1="#*_ *..... *. #*_.. *._ *._. *_._ #*_._ *_. *.. *__. *..... *_  #*._. *.. *... *. *..."
for i in str.split('#'):
	print(''.join(decode(morse,i.split(' '))),end=' ')
print()
for i in str1.split('#'):
	print(''.join(decode(morse,i.split(' '))),end=' ')



