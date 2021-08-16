'''
A Hamming number is a positive integer of the form 2i3j5k, for some non-negative integers i, j, and k.

Write a function that computes the nth smallest Hamming number.

Specifically:

The first smallest Hamming number is 1 = 203050
The second smallest Hamming number is 2 = 213050
The third smallest Hamming number is 3 = 203150
The fourth smallest Hamming number is 4 = 223050
The fifth smallest Hamming number is 5 = 203051
The 20 smallest Hamming numbers are given in example test fixture.

Your code should be able to compute all of the smallest 5,000 (Clojure: 2000, NASM: 13282) Hamming numbers without timing out.
'''


n = 10
def hamming(n):
    # Base values and exponent
    base = [2, 3, 5]
    exp = [0, 0, 0]
    # Get list of hamming numbers
    # hamming(0) = 1
    ham_ls = [1]
    # Loop
    for _ in range(1, n):
        # Calculate list of 3 next hamming numbers 
        next_hamms = [base[i] * ham_ls[exp[i]] for i in range(3)]
        # Get the smallest number in this list
        next_hamm = min(next_hamms)
        # Append to list of hamming number
        ham_ls.append(next_hamm)
        # Assign value to exponent list with this smallest number
        for i in range(3):
            exp[i] += int(next_hamms[i] == next_hamm)
    # return the last number in hamming list
    return ham_ls[-1]

print(hamming(10))