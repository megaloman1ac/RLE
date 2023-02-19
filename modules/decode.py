import time

def decode(raw_string):
	dec=""
	
	word_count=""
	
	for i in range(0, len(raw_string)):
		if(raw_string[i].isdigit()):
			word_count += raw_string[i]
		else:
			dec += raw_string[i] * int(word_count)
			word_count=""
	return dec
