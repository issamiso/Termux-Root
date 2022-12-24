import os
# 
W='\33[0m'
R='\33[1;31m'
G='\33[1;32m'
O='\33[1;33m'
B='\33[1;34m'
P='\33[1;35m'
C='\33[1;36m'
GR='\33[1;37m'
xx=f"{W}[{R}✓{W}]{G} "
ss=f"{W}[{R}!{W}]{R} "
ii=f"{W}[{R}+{W}]{G} "
import time
import sys
try:
	from __root__ import __bnr__
except:
	print(ss+'Error !')
	sys.exit()
# setup root termux pro
#os.system('python3 __system__.py')
def done():
	print(xx+'Setup root ')
	time.sleep(1)
	print(xx+'pkg root')
	time.sleep(1)
	print(xx+'all pkg root')
	time.sleep(1)
	print(ss+f'update root {R}!{G}')
	time.sleep(1)
	print(ii+'Root is found restart Termux')
def setup():
	print(R+f"\n{G}info\n\n{R}basic system It is not possible\nto go back to the old tool\n"+W)
	time.sleep(2)
	os.system('cd __root__ && bash __root__.sh') 
	os.system('clear')
	__bnr__.bnr()
	print('')
	print(xx+'Loding  ',end='',flush=True)
	for mm in range(50):
		for i in r'-\|/|-/':
			print('\b',i,end='',sep='',flush=True)
			time.sleep(0.01) 
	time.sleep(1)
	print('')
	cc=os.path.exists('/data/data/com.termux/files/home/kali-fs/root')
	if cc == False:
		print(ss+R'Error system ! ')
#sys.exit()
	os.system('cd __main__ && python3 __main__.py')
	done()
def root():
	ax = os.path.exists('/data/data/com.termux/files/usr/etc')
	if ax == False:
		print(ss+'Error !')
		sys.exit()
	print(xx+'done')
	time.sleep(1)
	s1 = os.path.exists('__main__/.__net-tools__.sh')
	if s1 == False:
		print(ss+'Error !')
		sys.exit()
	print(xx+'done')
	time.sleep(1)
	s2 = os.path.exists('__main__/.bashrc')
	if s2 == False:
		print(ss+'Error !')
		sys.exit()
	print(xx+'done')
	time.sleep(1)
	s3 = os.path.exists('__main__/start-kali.sh')
	if s3 == False:
		print(ss+'Error !')
		sys.exit()
	print(xx+'done')
	time.sleep(1)
	s4 = os.path.exists('__main__/__main__.py')
	if s4 == False:
		print(ss+'Error !')
		sys.exit()
	print(xx+'done')
	time.sleep(1)
	s5 = os.path.exists('__main__/bash.bashrc')
	if s5 == False:
		print(ss+'Error !')
		sys.exit()
	print(xx+'done')
	time.sleep(1)
	s6 = os.path.exists('__root__/__bnr__.py')
	if s6 == False:
		print(ss+'Error !')
		sys.exit()
	print(xx+'done')
	time.sleep(1)
	s7 = os.path.exists('__root__/__root__.sh')
	if s7 == False:
		print(ss+'Error !')
		sys.exit()
	print(xx+'done')
	time.sleep(1)
	
	
	time.sleep(1)
	os.system('clear')
	__bnr__.bnr()
	cmd=input(f'''
{ii}setup root y/n :{W}''')
	if cmd == 'y' or cmd == 'Y':
		setup()





















try:
	root()
except:
	time.sleep(1)
	print('Exit')






