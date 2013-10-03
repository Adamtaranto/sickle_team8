import math

class OurSequence:
	'''
	This class will keep track of a read quality scores.
	'''
	def __init__(self, readid, sequence, quality):

		self.readid = readid
		self.sequence = sequence
		self.quality = quality
		self.meanq = self.mean()

	def mean(self):

		'''Calculate the mean quality score for an entire read.'''

		#get total number of quality scores and
		#sum quality scores together
		total_len = len(self.quality)
		total_sum = sum(self.quality)

		#calculate mean
		mean_read = float(total_sum) / total_len
		return mean_read

	def sd(self):

		'''Calculate the standard deviation of the quality socres
		for an entire read.'''

		#list to store variance values in
		new_variance = []

		#loop over quality scores and calculate variance
		for i in self.quality:
			variance = pow((i - self.meanq), 2)
			new_variance.append(variance)

			#sum the variance values together
			variance_sum = sum(new_variance)
			#get the number of variance values
			variance_total = len(new_variance)

			#caluculate the standard deviation
			standard_dev = float(variance_sum) / variance_total
		return standard_dev

	def window_mean(self,window_size, offset):
		
		'''Calculate the mean quality score at incremented windows 
		across the length of a read.'''

		#Initialize empty dictionary
		quality_means = {}
		#Set to position of last value in list
		seq_end = len(self.quality)
		#Initialize window boundaries and window instance
		window_start = 0
		window_end = (offset - 1)
		window_count = 1

		# While current window range does not run over the length of the 'self.quality' 
		# list, calculate window mean, and increment window by offset.
		while window_end <= seq_end:
			#Returns sublist with range of current window
			window_values = [self.quality[i] for i in range(window_start, window_end+1)]
			#Calculate mean of values in sublist, assumes they are all ints
			window_mean = reduce(lambda x, y: x + y, window_values) / len(window_values)
			#Save position and mean into dictionary
			quality_means[window_count] = window_mean
			#Increment window count and boundaries
			window_count += 1
			window_start += offset
			window_end += offset