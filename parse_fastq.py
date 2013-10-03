import sys
from Bio import SeqIO
from sickle_sequence_class import OurSequence
from test_func import is_zero_len, is_allN, length_match

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

