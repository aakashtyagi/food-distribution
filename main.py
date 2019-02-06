""" 
a function that takes 2 arguments:
1. a dict where key => id of a food item, value => ratio of item desired
2. integer how many portions the meal should serve

it returns a dict where:
key => id of a food item
value => actual quantities for each food item

======
RULES
======

1. Assigns all portions
2. Only assigns integer for portion counts (value of the dict)
3. choose the largest remainder for allocating non-integer counts.
If no largest remainder, give to the lowest ID and then move to the next ID.

"""

import unittest

def foodQuantities(foodRatios, numberOfMeals):
	if foodRatios:
		totalFraction = sum(foodRatios.values())
		quantities = {}
		remainderValues = {}

		# Initial Distribution
		for key, value in foodRatios.iteritems():

			quantityValue = (value*numberOfMeals)/totalFraction
			quantityRemainder = (value*numberOfMeals)%totalFraction

			quantities[key] = quantityValue
			
			# if there is a remainder, store the remainder with the key
			if quantityRemainder != 0:
				remainderValues[key] = quantityRemainder
		
		# number of meals left after initial distribution
		remainingMeals = numberOfMeals - sum(quantities.values())
		
		if remainingMeals == 0:
			return quantities
		else:
			# Distribution pt.2 => find the largest remainder and follow the rules of distribution
			maxRemainder = max(remainderValues.values())
		
		# No largest remainder => means all remainders have the same value
		if remainderValues.values().count(maxRemainder) == len(remainderValues.values()):
			for key in quantities:
				if remainingMeals > 0:
					quantities[key] += 1
					remainingMeals = remainingMeals - 1
				else:
					break
		
		# there is a largest remainder(s)
		else:
			# find keys with largest remainder values
			keysWithMaxRemainder = [k for k, v in remainderValues.items() if v == maxRemainder]
			# distribute the remainingMeals among those keys
			for item in keysWithMaxRemainder:
				if remainingMeals > 0:
					quantities[item] += 1
					remainingMeals = remainingMeals - 1
				else:
					break

		return quantities
	else:
		return foodRatios


class Test(unittest.TestCase):

	def test_case_1(self):
		self.assertEqual(foodQuantities({},1), {})

	def test_case_2(self):
		self.assertEqual(foodQuantities({1:1}, 2), {1:2})

	def test_case_3(self):
		self.assertEqual(foodQuantities({1:1}, 0), {1:0})

	def test_case_4(self):
		self.assertEqual(foodQuantities({1:1, 2:1, 3:1}, 11), {1:4, 2:4, 3:3})

	def test_case_5(self):
		self.assertEqual(foodQuantities({1:10, 2:0}, 2), {1:2, 2:0})

	def test_case_6(self):
		self.assertEqual(foodQuantities({1:2, 2:4, 3:4, 4:2, 5:2, 6:2, 7:2, 8:2}, 12), {1: 1, 2: 3, 3: 3, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1})

	def test_case_7(self):
		self.assertEqual(foodQuantities({1:1, 2:2, 3:2, 4:1, 5:1, 6:1, 7:1, 8:1}, 12), {1: 1, 2: 3, 3: 3, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1})


if __name__ == "__main__":
    unittest.main()

