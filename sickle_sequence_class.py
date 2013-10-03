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
		
		quality_means = {}
		seq_end = len(self.quality)
		window_start = 0
		window_end = (offset - 1) 
		window_count = 1


		while window_end <= seq_end: 
			window_values = [self.quality[i] for i in range(window_start, window_end+1)] #returns [0,1,2,3,4]
			window_mean = reduce(lambda x, y: x + y, window_values) / len(window_values)
			quality_means = {window_count : window_mean}
			window_count += 1
			window_start += offset
			window_end += offset

		print quality_means


		