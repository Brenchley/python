class PointWithoutSlots(object):
	"""Programs can add attributes to objects of this class"""

	def __init__(self, xValue=0.0, yValue = 0.0):
		"""Constructor for PointWithoutSlots initializes x- and y-coordinates"""

		self.x = float(xValue)
		self.y = float(yValue)


class PointWithSlots(object):
	"""Proram cannot add attributes to objects of this class"""

	# PointWithSlots object can contain only attributes x and y
	__slots__ = ["x", "y"]

	def __init__(self, xValue= 0.0, yValue = 0.0):
		"""Constructor for PointWithSlots initializes x- and y-coordinates"""

		self.x = float(xValue)
		self.y = float(yValue)

	# main program
def main():
	noSlots = PointWithoutSlots()
	slots = PointWithSlots()

	for point in [noSlots, slots]:
		print "\nProcessing an object of class",point.__class__

		print "The current value of point.x is:", point.x
		newValue = float(raw_input("Enter new x coordinate:"))
		print "Attempting to set new x-coordinate value..."

		# Logic error: create new attribute named x instead of changing  the value of attribute x
		point.x =newValue
		# output unchanged attribute x
		print "The new value of poin.x is:", point.x

	
if __name__ == "__main__":
	main()