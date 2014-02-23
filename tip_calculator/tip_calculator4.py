#! /usr/local/bin/python

from optparse import OptionParser

parser = OptionParser()

parser.add_option("-m", "--meal", dest="meal", help="Meal cost")
parser.add_option("-x", "--tax", dest="tax", help="Tax %", default="0.08")
parser.add_option("-t", "--tip", dest="tip", help="Tip %", default="0.20")

(options, args) = parser.parse_args()

if not (options.meal): 
    parser.error("You need to the meal cost with -m")

meal = float(options.meal)
tax = float(options.tax)
tip = float(options.tip)

tax_value = meal * tax
meal_with_tax = meal + tax_value
tip_value = meal_with_tax * tip
total = meal_with_tax + tip_value

print "Meal: ${0:.2f}".format(meal)
print "Tax: ${0:.2f} (@ {1}%)".format(tax_value, tax * 100)
print "Tip: ${0:.2f} (@ {1}%)".format(tip_value, tip * 100)
print "Total: ${0:.2f}".format(total)
