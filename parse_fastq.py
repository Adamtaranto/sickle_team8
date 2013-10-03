import sys
from Bio import SeqIO
from sickle_sequence_class import OurSequence
from test_func import is_zero_len, is_allN, length_match

fastq_file = sys.argv[1]
fastq_dict = {}

def makeFastqDict(sequence_object):
	if sequence_object.readid not in fastq_dict:
		fastq_dict[sequence_object.readid] = sequence_object
	else:
		pass

def getSequenceObject(fastq_file):
	'''Take each individual record in the fastq file and convert these into
	their own OurSequence objects.'''
	for record in SeqIO.parse(fastq_file, "fastq"):
		
		#get identifying information
		sequence_id = record.id
		sequence = record.seq
		sequence_qual = record.letter_annotations["phred_quality"]
		
		if is_zero_len(sequence):
			break
		
		if is_allN(sequence):
			break
			
		if match_len
		
		#create object
		new_sequence_object = OurSequence(sequence_id, sequence, sequence_qual)
#		print new_sequence_object.readid
#		print new_sequence_object.quality
#		print new_sequence_object.sequence
		makeFastqDict(new_sequence_object)

getSequenceObject(fastq_file)
print fastq_dict
