
class DiscountCalculator(object):
	
	def calculate_discount(self, cart_total, discount, discount_type):
		if discount_type == "%" and discount <= 100:
			return cart_total * (discount / 100.0)
		elif discount_type == "$" and discount <= cart_total:
			return cart_total - discount
		else:
			raise ValueError("Invalid discount type or value.")