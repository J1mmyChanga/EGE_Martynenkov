from ipaddress import *

print('.'.join(f'{x:>08b}' for x in [255, 224, 0, 0]))
print('.'.join(f'{x:>08b}' for x in [117, 32, 0, 0]))