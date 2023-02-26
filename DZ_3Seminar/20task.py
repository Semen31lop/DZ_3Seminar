
eng = {1:'A, E, I, O, U, L, N, S, T, R',
      	2:' D, G',
      	3:' B, C, M, P',
      	4:'F, H, V, W, Y',
      	5:' K',
      	8:' J, X ',
      	10:'Q, Z'}
rus = {1:' А, В, Е, И, Н, О, Р, С, Т ',
      	2:'Д, К, Л, М, П, У',
      	3:' Б, Г, Ё, Ь, Я',
      	4:'Й, Ы',
      	5:'Ж, З, Х, Ц, Ч',
      	8:'Ш, Э, Ю',
      	10:'Ф, Щ, Ъ '}
N = int(input('0=rus;1=eng: '))
word =str( input('Введите слово: '))
if N == 1:
	print(f'{word} -> {sum([t for i in word for t , f in eng.items() if i in f])} очков')
elif N == 0:
	print(f'{word} -> {sum([t for i in word for t , f in rus.items() if i in f])} очков ')