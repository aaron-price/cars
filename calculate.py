def calculate(cars, title):

	def add_field(index, key, value):
		car = cars[index]
		car[key] = value

	def mean(numbers):
		return sum(numbers) / len(numbers)

	all_year = []
	all_price = []
	all_odo = []
	all_age = []
	all_msrp = []
	all_fmv = []
	all_price_to_year = []
	all_odo_to_year = []
	all_odo_to_age = []

	for i, car in enumerate(cars):
		all_year.append(car['year'])
		all_price.append(car['price'])
		all_odo.append(car['odo'])
		all_age.append(car['age'])
		all_msrp.append(car['msrp'])
		all_fmv.append(car['fmv'])

		p_to_y = car['price'] / (car['year'] - 2000)
		all_price_to_year.append(p_to_y)
		add_field(i, 'price_to_year', p_to_y)

		o_to_y = car['odo'] / (car['year'] - 2000)
		all_odo_to_year.append(o_to_y)
		add_field(i, 'odo_to_year', o_to_y)

		o_to_a = car['odo'] / car['age']
		all_odo_to_age.append(o_to_a)
		add_field(i, 'odo_to_age', o_to_a)

	averages = {
		"avg_year": mean(all_year),
		"avg_price": mean(all_price),
		"avg_odo": mean(all_odo),
		"avg_age": mean(all_age),
		"avg_msrp": mean(all_msrp),
		"avg_fmv": mean(all_fmv),
		"avg_price_to_year": mean(all_price_to_year),
		"avg_odo_to_year": mean(all_odo_to_year),
		"avg_odo_to_age": mean(all_odo_to_age)
	}

	all_over_fmv = []
	for i, car in enumerate(cars):
		over_fmv = car['price'] - car['fmv']
		add_field(i, 'over_fmv', over_fmv)
		all_over_fmv.append(over_fmv)
	averages['avg_over_fmv'] = mean(all_over_fmv)


	def get_condition(car):
		odo_to_age = car['odo_to_age']
		return averages['avg_odo_to_age'] - odo_to_age

	def value_offset(car):
		ofm = car['over_fmv']
		return averages['avg_over_fmv'] - ofm
	def cond_value(car):
		cond = car['condition']
		val = car['val_offset']
		return val / cond
	def get_title(car):
		return str(car['year']) + " " + str(car['make']) + " " + str(car['model'])


	for i, car in enumerate(cars):
		add_field(i, 'condition', get_condition(car))
		add_field(i, 'val_offset', value_offset(car))
		add_field(i, 'cond_val', cond_value(car))
		add_field(i, 'title', get_title(car))
	averages['avg_over_fmv'] = mean(all_over_fmv)
	averages['title'] = title

	return {
		'avg': averages,
		'all': cars
	}