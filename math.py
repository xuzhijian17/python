# -*- coding: utf-8 -*-


init = 6
total = 42
step = 5
l = ['+6','-6','*4']

def cl(l, step):
	tl = []
	if step == 2:
		for x in l:
			for y in l:
				tl.append([x,y])
	elif step == 3:
		for x in l:
			for y in l:
				for z in l:
					tl.append([x,y,z])
	elif step == 4:
		for x in l:
			for y in l:
				for z in l:
					for m in l:
						tl.append([x,y,z,m])
	elif step == 5:
		for x in l:
			for y in l:
				for z in l:
					for m in l:
						for n in l:
							tl.append([x,y,z,m,n])
	return tl


def main(init, total, step, cl):
	while True:
		for y in cl:
			sn = init
			for x in range(step):
				n = int(y[x][1:])
				if y[x][0] == '+':
					sn += n
				elif y[x][0] == '-':
					sn -= n
				elif y[x][0] == '*':
					sn *= n
				elif y[x][0] == '/':
					sn /= n

			print(y,sn)
			
			if sn == total:
				print('\n\t\tSuccess Done!')
				print('=============================================================')
				print(y,sn)
				print('=============================================================')
				exit()

if __name__ == '__main__':
	cl = cl(l,step)
	main(init, total, step, cl)