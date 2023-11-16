from decimal import Decimal
from fractions import Fraction
import bitstring

print("----Representing 0.1 in 17 significant digits----")
print(format(0.1, '.17g')) # 17 significant digits
print("----Representing 0.1 in decimal----")
print(Decimal.from_float(0.1))
print("----Representing 0.1 in decimal using 17 significant digits----")
print(format(Decimal.from_float(0.1), '.17')) # 17 significant digits
print("----Representing 0.1 in binary----")
bits = bitstring.BitArray(float=0.1, length=64) # 64 bits
print(bits.bin)