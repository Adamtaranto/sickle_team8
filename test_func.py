from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import generic_dna
import doctest

'''
Here are some functions to test out our sequences before executing sickle
'''

def is_zero_len(sequence):
	'''
	Test if the sequence of zero length, if so return True else False
	
	>>> is_zero_len('')
	True
	>>> is_zero_len('ATCG')
	False
	'''
	assert type(sequence) == str
	if sequence == '':
		return True
	if len(sequence) > 0:
		return False
		
def is_allN(sequence,proportion=None):
	'''
	Test if the whole sequence is composed only of N. Return True is yes, False otherwise.
	As option, if proportion is set, check if the proportion of 'N' in sequence is equal to our larger than <proportion>. If so, return True, else return False
	
	>>> is_allN('ATCG')
	False
	>>> is_allN('ATNG')
	False
	>>> is_allN('NNNN')
	True
	>>> is_allN('')
	False
	>>> is_allN('AANN',proportion=0.5)
	True
	>>> is_allN('AATTN',proportion=0.5)
	False
	'''
	
	if sequence == '':
		return False
	
	sequence = sequence.upper()
	#print sequence.count('N')/float(len(sequence))
	
	if 'N' in set(sequence):
		if proportion == None:
			if len(sequence) == sequence.count('N'):
				return True
			else:
				return False
		else:
			if sequence.count('N')/float(len(sequence)) >= proportion:
				return True
			else:
				return False
	else:
		return False

class lengthException(Exception):
	pass

def length_match(seq_rec):
	'''
	Test if the length of the sequence is the same as the length of the quality string. If not, raise an exception.
	
	>>> test = SeqRecord(Seq("NACGTACGTA", generic_dna), id="Test", description="Made up!")
	>>> test.letter_annotations["phred_quality"] = [0,1,2,3,4,5,10,20,30,40]
	>>> length_match(test)
	'''

	seq_len = len(seq_rec.seq)
	qual_len = len(seq_rec.letter_annotations['phred_quality'])
	
	if seq_len != qual_len:
		raise lengthException("The read {} has different quality score string length to the read length".format(seq_rec.id))
	else:
		return

if __name__=='__main__':
	doctest.testmod()
