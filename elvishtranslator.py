# MCB185 final
# Plausible elvish 

# When writing fantasy novels, authors must somehow come up with new names that sound like they come from a different language. Make a language generator using Nth-order Markov models. For example, generate Elvish words from a mixture of Finnish and Welsh (or whatver you think Elivsh is supposed to look like) 

import random 

def generate_language(text, order, length):
	
	transitions = {}
	
	words = text.split()
	
	for i in range(len(words)-order):
		current_state = ''.join(words[i:i+order])
		next_state = words[i+order]
		if current_state not in transitions:
			transitions[current_state] = {}
		if next_state not in transitions[current_state]:
			transitions[current_state][next_state] = 0
		transitions[current_state][next_state] +=1

	current_state = random.choice(list(transitions.keys()))
	new_text = current_state + ''
	for i in range(length):
		if current_state not in transitions:
			break
		next_state = max(transitions[current_state], key = transitions[current_state].get)
		current_state = ''.join(current_state.split()[1:])+ ''+ next_state
		new_text += next_state + ''
	return new_text
	
with open('input.txt', 'r') as f:
	text = f.read()

new_text = generate_language(text, 5, 100)
print(new_text)




"""
def init(letter, n):
	letter.n = n
	letter.prefixes = {}
	letter.suffixes = {}

def train(letter, text):
	words = text.split()
	for i in range(len(words)-letter.n):
		prefix = tuple(words[i:i+letter.n])
		suffix = words[i+letter.n]
		if prefix not in letter.prefixes:
			letter.prefixes[prefix] = []
		letter.prefixes[prefix].append(suffix)
	prefix = tuple(words[-letter.n])
	if prefix not in letter.prefixes:
		letter.prefixes[prefix] = []

def generate(letter, length):
	prefix = random.choice(list(letter.prefixes.keys()))
	words = list(prefix)
	for i in range(length):
		if prefix not in letter.prefixes:
			break
		suffix = random.choice(letter.prefixes[prefix])
		words.appedn(suffix)
		prefix = tuple(words[-self.n:])
	return "".join(words)
	
print(letter)
"""

