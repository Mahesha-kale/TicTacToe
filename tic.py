def check(player):
    if '00' in player and '11' in player and '22' in player:
        return True
    elif '00' in player and '01' in player and '02' in player:
        return True
    elif '10' in player and '11' in player and '12' in player:
        return True
    elif '20' in player and '21' in player and '22' in player:
        return True
    elif '00' in player and '10' in player and '20' in player:
        return True
    elif '01' in player and '11' in player and '21' in player:
        return True
    elif '02' in player and '12' in player and '22' in player:
        return True
    elif '02' in player and '11' in player and '20' in player:
        return True
    else:
        return False

def matt(mat):
    for j in range(3):
        for z in range(3):
            print(mat[j][z],end=' ')
        print()

print('TicTacToe Command Line')
mat = [[0,0,0],[0,0,0],[0,0,0]]
p1 = []
p2 = []
inpu = ['00','01','02','10','11','12','20','21','22']
print('p1> Player 1')
print('p2> Player 2')
print('Allowed Inputs: ',inpu)
for i in range(9):
    if i in [0,2,4,6,8]:
        #inp = list(map(int,input('p1>').strip().split()))[:2]
        inp = input('p1>')
        while inp not in inpu:
            print('Wrong Input Try Again')
            inp = input('p1>')
        flag = True
        while flag:
            if inp not in p1 and inp not in p2:
                x,y = int(inp[0]),int(inp[1])
                mat[x][y] = 'p1'
                p1.append(inp)
                flag = False
            else:
                print('Position Allredy Filled')
                inp = input('p1>')
                while inp not in inpu:
                    print('Wrong Input Try Again')
                    inp = input('p1>')
        if check(p1):
            print('Player 1 is Winner')
            matt(mat)
            break
    else:
        #inp = list(map(int,input('p2>').strip().split()))[:2]
        inp = input('p2>')
        while inp not in inpu:
            print('Wrong Input Try Again')
            inp = input('p2>')
        flag = True
        while flag:
            if inp not in p1 and inp not in p2:
                x,y = int(inp[0]),int(inp[1])
                mat[x][y] = 'p2'
                p2.append(inp)
                flag = False
            else:
                print('Position Allredy Filled')
                inp = input('p2>')
                while inp not in inpu:
                    print('Wrong Input Try Again')
                    inp = input('p2>')
        if check(p2):
            print('Player 2 is Winner')
            matt(mat)
            break
    matt(mat)
