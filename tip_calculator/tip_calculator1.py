#! /usr/local/bin/python

meal = 44.50
tax = 0.08
tip = 0.2

tax_value = meal * tax
meal_with_tax = meal + tax_value
tip_value = meal_with_tax * tip
total = meal_with_tax + tip_value

print "Meal: {:.2f}".format(meal)
print "Tax: {:.2f}".format(tax_value)
print "Tip: {:.2f}".format(tip_value)
print "Total: {:.2f}".format(total)
