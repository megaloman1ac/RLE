import time

def encode(raw_string):
	enc=""
	word_count = 1
	
	for i in range(1, len(raw_string)):
		if raw_string[i] != raw_string[i-1]:
			enc += "{}{}".format(word_count, raw_string[i-1])
			word_count = 1
		else:
			word_count += 1
			
	enc += "{}{}".format(word_count, raw_string[-1])
	return enc
