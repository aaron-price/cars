from calculate import calculate
from cl import cars as cl_data
from hy import cars as hy_data
from atr import cars as atr_data

cl = calculate(cl_data, 'cl')
hy = calculate(hy_data, 'hy')
atr = calculate(atr_data, 'atr')
all_data = [cl['all'],hy['all'],atr['all']]
avg_data = [cl['avg'],hy['avg'],atr['avg']]

def compete(field, rev = False):
	print("FIELD",field)
	newlist = sorted(avg_data, key=lambda k: k[field], reverse=rev) 
	for l in newlist:
		print("| ",l['title'],l[field])
	print(" ")

print(avg_data[0].keys())

compete('avg_over_fmv')
compete('avg_year')
