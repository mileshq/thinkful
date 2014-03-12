import sys
from tip_calculator_as_functions import calculate_rate, calculate_meal_costs

try:
	meal = float(sys.argv[1])
except (ValueError, IndexError):
	print "Sorry, you must supply numbers for all input parameters to this script."
	meal = float(raw_input("Enter meal cost: "))

try:
	tax = float(sys.argv[2])
except (ValueError, IndexError):
	print "Sorry, you must supply numbers for all input parameters to this script."
	tax = float(raw_input("Enter tax % (as decimal): "))

try:
	tip = float(sys.argv[3])
except (ValueError, IndexError):
	print "Sorry, you must supply numbers for all input parameters to this script."
	tip = float(raw_input("Enter tip % (as decimal): "))

meal_info = calculate_meal_costs(meal, tax, tip)

for k, v in meal_info.iteritems():
	print "{0}: {1}".format(k, v)
