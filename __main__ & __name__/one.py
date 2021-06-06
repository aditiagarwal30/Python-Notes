#one.py
print('hello')

import two

print('TOP LEVEL IN ONE.PY')

two.func()

if __name__ == '__main__' :
	print('ONE.PY I BEING RUN DIRECTLY !!')
else :
	print('ONE.PY has been imported')
	



