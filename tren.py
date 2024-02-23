pos = [0, 0]
n = 1
in_cycle = False
st = input()

def command(st):
    k = 1
    if '()' not in st:
        k = int(st[st.find('(') + 1:st.find(')')])
    if 'right' in st:
        pos[0] += k
    elif 'left' in st:
        pos[0] -= k
    elif 'up' in st:
        pos[1] += k
    elif 'down' in st:
        pos[1] -= k

while '#' not in st:
    k = 1
    if 'move' in st:
        if st.startswith(' '):
            in_cycle = True
        else:
            in_cycle = False
            n = 1
        for i in range(n):
            command(st)
    elif st.startswith('for '):
        n = int(st[st.find('(') + 1:st.find(')')])
        in_cycle = True
    st = input()

if pos == [0, 0]:
    print('')
else:
    if pos[0] != 0:
        if pos[0] > 0:
            if pos[0] == 1:
                print('move_right()')
            else:
                print(f'move_right({abs(pos[0])})')
        else:
            if pos[0] == -1:
                print('move_left()')
            else:
                print(f'move_left({abs(pos[0])})')

    if pos[1] != 0:
        if pos[1] > 0:
            if pos[1] == 1:
                print('move_up()')
            else:
                print(f'move_up({abs(pos[1])})')
        else:
            if pos[1] == -1:
                print('move_down()')
            else:
                print(f'move_down({abs(pos[1])})')