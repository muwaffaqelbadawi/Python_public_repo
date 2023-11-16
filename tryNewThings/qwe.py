import operator as op
from itertools import compress

names = ['Muwaffuq', 'Muwazzur', 'Maeen', 'Moyassar', 'Ammar']

# filt = [name for name in names if names.index(name) in [1, 3]]

simpleFilt = op.itemgetter(1, 3)(names)

choosen = [1, 1, 0, 1, 0]

compressedData = compress(names, choosen)

print(list(compressedData))


# print(simpleFilt)


# start_time = time.time()
# print("\n\n--- %s seconds ---" % (time.time() - start_time))
