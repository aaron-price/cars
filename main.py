from calculate import calculate
from cl import cars as cl_data
from hy import cars as hy_data
from atr import cars as atr_data

cl = calculate(cl_data, 'cl')
hy = calculate(hy_data, 'hy')
atr = calculate(atr_data, 'atr')
all_data = [cl['all'],hy['all'],atr['all']]
avg_data = [cl['avg'],hy['avg'],atr['avg']]

def compete(data, field, rev = False):
	print("FIELD",field)
	newlist = sorted(data, key=lambda k: k[field], reverse=rev) 
	for l in newlist:
		print("| ",l['title'],l[field])
	print(" ")

# Available average data
print(avg_data[0].keys())

# avg_over_fmv = "Price" - "fair market value" (according to motortrends.com)
compete(avg_data, 'avg_over_fmv')

compete(all_data[0], 'price')
compete(all_data[0], 'over_fmv')