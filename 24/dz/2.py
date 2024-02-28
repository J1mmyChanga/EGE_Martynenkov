s = open('files/24_2426.txt').readline()
s = s.replace('2', '1').replace('3', '1').replace('A', ' ').replace('B', ' ').replace('C', ' ')
print(max(len(c) for c in s.split()))