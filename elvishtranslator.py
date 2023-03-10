#!/usr/bin/env python3
# MCB185 final
# Plausible elvish 

# When writing fantasy novels, authors must somehow come up with new names that sound like they come from a different language. Make a language generator using Nth-order Markov models. For example, generate Elvish words from a mixture of Finnish and Welsh (or whatver you think Elivsh is supposed to look like) 

# prob of a single double triple in separate dictionaries, read them out to develop a model, then generating a language model. 

import random 
import re

# Start off by converting certain punctuations into spaces
punc = '~`1234567890!@#$%^&*()-_+=[]\{}|:;",./<>?'
spaces = ''*len(punc)

f = open('Finnishlang.txt', 'r')
fin = f.read()
w = open('Welshlang.txt', 'r')
wel = w.read()
words = fin + wel

lang = []

for text in words:
	text = re.sub(r'[^a-z\s]', '',text.lower())
	
	words = text.split()
	lang.extend(words)


order = 3
model = {}

for i in range(len(lang)-order):
	prefix = tuple(lang[i:i+order])
	suffix = lang[i+order]
	if prefix not in model:
		model[prefix] = {}
	if suffix not in model[prefix]:
		model[prefix][suffix] = 0
	model[prefix][suffix] += 1
	
def gen_sent():
	seed = random.randint(0, len(lang) - order - 1)
	prefix = tuple(lang[seed:seed+order])
	sentence = list(prefix)
	while len(sentence) < 20:
		if prefix not in model:
			break
		choices = []
		weights = []
		for suffix in model[prefix]:
			choices.append(suffix)
			weights.append(model[prefix][suffix])
		if not choices:
			break
		suffix = random.choices(choices, weights = weights)[0]
		sentence.append(suffix)
		prefix = tuple(sentence[-order:])
	return ''.join(sentence)

for i in range(10):
	print(gen_sent())
		



"""
finnish_model = {}

# Test 3: fail, just...fail
with open('Finnishlang.txt', 'r') as f:
	text = f.read()
with open('Welshlang.txt', 'r') as q:
	test = q.read()
	
n = 3
fin_mod = {}
wel_mod = {}

for word in fin:
	for i in range(len(word) - n):
		seq = word[i:i+n]
		next_char = word[i+n]
		if seq not in fin_mod:
			fin_mod[seq][next_char] = 0
		fin_mod[seq][next_char] += 1

for word in wel:
	for i in range(len(word) -n):
		seq = word[i:i+n]
		next_char = word[i+n]
		if seq not in wel_mod:
			wel_mod[seq] = {}
		if next_char not in wel_mod[seq]:
			wel_mod[seq][next_char] = 0
		wel_mod[seq][next_char] += 1

num_words = 10
word_len = 5

for i in range(num_words):
	if random.random() <0.5:
		model = fin_mod
	else:
		model = wel_mod
	
	word = ''
	seq = random.choice(list(model.keys()))
	word += seq
	for j in range(word_len -n):
		if seq not in model:
			breal
		choices = list(model[seq].keys())
		weights = list(model[seq].values())
		next_char = random.choices(choices, weights = weights)[0]
		word += next_char
		seq = seq[1:] + next_char
	print(word)
"""

"""
# Test run 2: worked, however, only produced one long word
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
	
with open('Finnishlang.txt', 'r') as f:
	text = f.read()
with open('Welshlang.txt', 'r') as q:
	test = q.read()

new_text = generate_language(text, 2, 100)
print(new_text)
"""

"""
# Test run 1: failed to produce cohesive words 
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

