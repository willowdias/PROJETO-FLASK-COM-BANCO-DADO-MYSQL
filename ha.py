import time
test=int(str(input('\033[0;31;44m digita algo\033[m '+'='*50)))
print('='*50,' \033[1;1;44m loading... \033[m','='*50)
print('='*50,' \033[1;1;44m loading... \033[m','='*50)
time.sleep(1)
print('='*50,' \033[1;1;41m loading... \033[m','='*50)
print('='*50,' \033[1;1;41m loading... \033[m','='*50)
time.sleep(1)
print('='*50,' \033[1;1;42m loading... \033[m','='*50)
print('='*50,' \033[1;1;42m loading... \033[m','='*50)
time.sleep(1)
print('='*50,' \033[1;1;43m loading... \033[m','='*50)
print('='*50,' \033[1;1;43m loading... \033[m','='*50)
time.sleep(1)
print('='*50,' \033[1;1;40m loading... \033[m','='*50)
print('='*50,' \033[1;1;40m loading... \033[m','='*50)
time.sleep(1)
print('='*50,' \033[1;1;40m loading... \033[m','='*50)
print('='*50,' \033[1;1;40m loading... \033[m','='*50)

while test:
    	
	print(f'\033[1;1;40m o numero digitado foi {test}\033[m')
	if int(test>= 50 and test <= 100): 
			print(f'\033[1;1;34m bom dia {test} parabens \033[m')
	elif int(test>=100 and test<=200):
		print(f'\033[0;31;40m {test} esse numero muito alto\033[m')
	else:
		print(f'\033[0;31;40m {test} voce perdeu\033[m')
	break