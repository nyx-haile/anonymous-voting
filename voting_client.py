#identify self to server with some PKE
#create secret random polynomial with degree k
#recieve encryption keys from server
#send encryption of P(0) up to P(k)
#additively calculate P*() which is the sum of all polynomials
#generate table of random bits E([r_0...r_k])

import numpy as np
import random

#numbers i should probably know
k
n
p


#import libcrypto
def pseudo_encrypt(sk, m):
	return (g**(m*sk)) % p
def pseudo_decrypt(sk, c):
	return (c**((p/sk) % (p-1))) % p
def rand(table):
	random_values = [random.sample(range(?? ???), -1) for _ in range(1, j+1)] 
	random_multiplicant = random.randint(p)
	for value_list in random_values:
		value_list.append(-sum(value_list))
	#add the values and mult by random multiplicant
def increment(table):
	
	pass


poly_T = []
secret_key = random.randint(1, p-2)
public key = g**(secret_key) % p

starting_shares = []

for j in range(0, k+1):
	starting_shares.append((1/n)*poly_T[j](0)) 

#post starting shares

#await vote

vote_table = receive_vote_table()

vote = input(???)

if vote == 1:
	send_to_server(rand(inc(vote_table)))
else:
	send_to_server(rand(vote_table))

