

kata_input = input("masukan kata per kata bebas = ").split()

kamus ={}

for kata in kata_input:
    kamus[kata] = kamus.get(kata, 0)+1

print(kamus)