class OurSequence:
	'''
	This class will keep track of a read quality scores.
	'''
	def __init__(self, readid, sequence, quality):
		
		self.readid = readid
		self.sequence = sequence
		self.quality = quality
	
	def mean(self):
		pass
	
	def sd(self):
		pass
	
	def window_mean(self,window_size, offset):
		pass
	
	
