from struct import *

#Store as bytes data.
packed_data = pack('iif',6,19,4.73)
print(packed_data)

original = unpack('iif',packed_data) 
print(original)