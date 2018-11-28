# class precision and recall
import math
class Result:
	recommended={}
	testing={}
	def __init__(self, recommended, testing):
		self.recommended=recommended
		self.testing = testing

	def precision(self):
		prec=len(set(self.recommended).intersection(self.testing))
		prec=prec/len(self.recommended)
		return prec

	def recall(self):
		rec=len(set(self.recommended).intersection(self.testing))
		rec=rec/len(self.testing)
		return rec

