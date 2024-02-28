s = open('files/24_2420.txt').readline()
s = s.replace('C', ' ').replace('D', ' ')
print(max(len(c) for c in s.split()))