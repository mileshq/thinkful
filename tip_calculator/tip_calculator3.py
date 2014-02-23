#! /usr/local/bin/python

import sys

meal = float(sys.argv[1])
tax = float(sys.argv[2])
tip = float(sys.argv[3])

tax_value = meal * tax
meal_with_tax = meal + tax_value
tip_value = meal_with_tax * tip
total = meal_with_tax + tip_value

print "Meal: ${0:.2f}".format(meal)
print "Tax: ${0:.2f}".format(tax_value)
print "Tip: ${0:.2f}".format(tip_value)
print "Total: ${0:.2f}".format(total)
