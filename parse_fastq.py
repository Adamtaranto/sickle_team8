import sys
from Bio import SeqIO
from sickle_sequence_class import OurSequence

fastq_file = sys.argv[1]

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
		print new_sequence_object.readid
		print new_sequence_object.quality
		print new_sequence_object.sequence

getSequenceObject(fastq_file)
