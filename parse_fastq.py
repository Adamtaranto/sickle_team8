import sys
from Bio import SeqIO
from numpy import mean
from numpy import std
from sickle_sequence_class import OurSequence
from test_func import is_zero_len, is_allN, length_match


fastq_file = sys.argv[1]
window_size = sys.argv[2]
offset = sys.argv[3]
fastq_dict = {}

def getSummaryFile(fastq_dict):
	
	'''Take mean and standard deviation for each window position,
	create summary file for entire readset.'''
	
	#set header of file
	header = "WindowPosition,MeanQuality,SDQuality\n"
	
	#list of lists
	master_result = []
	
	#loop over each read entry
	last_window = len(fastq_dict[fastq_dict.keys()[0]].window_means)
	
	#loop over each window position in read
	for window_pos in range(0, last_window):
		mean_values = []
		
		#loop over each read in fastq_dict and pull out
		#the mean value at that window position, store
		for read in fastq_dict:
			mean_values.append(fastq_dict[read].window_mean[window_pos])
		
		#calculate mean and std at each position
		mean_at_pos = numpy.mean(mean_values)
		sd_at_pos = numpy.std(mean_values)
		
		#add window position, mean and std to master list
		master_result.append([window_pos, mean_at_pos, sd_at_pos])
	
	#create summary file
	summaryfile = header
	for i in master_result:
		summaryfile += ",".join(master_result[i]) + "\n"
	
	#write string to file
	f = open("fastq_summary_stats.csv", "w")
	f.write(summaryfile)
	f.close()
	

def makeFastqDict(sequence_object,fastq_dict):

	'''Make a dictionary where the key is the id of the read
	and the value is the OurSequence object'''
	
	#check to see if read is already in dict
	#if not, add
	if sequence_object.readid not in fastq_dict:
		fastq_dict[sequence_object.readid] = sequence_object
	else:
		pass

def getSequenceObject(fastq_file):

	'''Take each individual record in the fastq file and convert these into
	their own OurSequence objects.'''
	fastq_dict = {}
	for record in SeqIO.parse(fastq_file, "fastq"):
		
		#get identifying information
		sequence_id = record.id
		sequence = str(record.seq)
		sequence_qual = record.letter_annotations["phred_quality"]
		
		if is_zero_len(sequence):
			print "Skipping {}.".format(sequence_id)
			break
		
		if is_allN(sequence):
			print "Skipping {}.".format(sequence_id)
			break
			
		#length_match(record)
		
		#create object
		new_sequence_object = OurSequence(sequence_id, sequence, sequence_qual)

#		print new_sequence_object.readid
#		print new_sequence_object.quality
#		print new_sequence_object.sequence

		#add new sequence object to dictionary
		makeFastqDict(new_sequence_object,fastq_dict)
	return fastq_dict



if __name__=='__main__':
	
	fastq_file = sys.argv[1]
	fastq_dict = {}
	getSequenceObject(fastq_file)
	print fastq_dict

