
class DiscountCalculator1(object):
	def calculate_discount(cart_total, discount, discount_type):
		if discount_type == "percent" or discount_type == "%":
			return cart_total * (discount / 100)
		elif discount_type == "dollar" or discount_type == "$":
			return cart_total - discount
		else:
			raise ValueError