import mmh3
bit_vector = [0]*20
a = mmh3.hash('Picachu') % 20
b = mmh3.hash('Charmander') %20

bit_vector[a] = 1
bit_vector[b] = 1
print(bit_vector)

r = mmh3.hash('Picachu') %20
if bit_vector[r] == 1:
    print(False)
else:
    print(True)