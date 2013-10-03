import sys
from Bio import SeqIO
from sickle_sequence_class import OurSequence

fastq_file = sys.argv[1]
fastq_dict = {}

def makeFastqDict(sequence_object):

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
	
	for record in SeqIO.parse(fastq_file, "fastq"):
		
		#get identifying information
		sequence_id = record.id
		sequence = record.seq
		sequence_qual = record.letter_annotations["phred_quality"]
		
		#create object
		new_sequence_object = OurSequence(sequence_id, sequence, sequence_qual)

#		print new_sequence_object.readid
#		print new_sequence_object.quality
#		print new_sequence_object.sequence

		#add new sequence object to dictionary
		makeFastqDict(new_sequence_object)

getSequenceObject(fastq_file)
print fastq_dict
