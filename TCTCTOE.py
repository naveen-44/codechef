# 1 game done, draw or win uc!=0 and win==1 or win==0 and uc==0
# 2 game not over, doable win==0 and UC!=0
# 3 not doable XC != OC, win>1

def row_win(r):
    if r[0]==r[1] and r[1]==r[2] and r[0]!="_":
        return True
    return False

def ttt_count(mat,s):
    count = 0
    for i in range(3):
        for j in range(3):
            if mat[i][j] == s:
                count+=1
    return count

def fun1(mat):
    win = []
    for i in range(3):
        if row_win(mat[i])==True:
            win.append(mat[i][0])
    for i in range(3):
        if row_win([mat[0][i],mat[1][i],mat[2][i]])==True:
            win.append(mat[0][i])
    d1,d2 = [],[]
    for i in range(3):
        d1.append(mat[i][i])
        d2.append(mat[i][2-i])
        
    if row_win(d1)==True:
        win.append(d1[0])
    if row_win(d2)==True:
        win.append(d2[0])
    return win

def fun(mat):
    
    win = fun1(mat)
    w = len(win)
    ww = len(set(win))
#     print(win,set(win))
    UC = ttt_count(mat,'_')
    XC = ttt_count(mat,'X')
    OC = ttt_count(mat,'O')
#     print("U,X,O = ",UC,XC,OC)
    if UC == 9:
        return 2
    if ww>1 :
        return 3
    if XC<OC or XC>OC+1:
        return 3
    if w == 0 and UC == 0 and XC-OC == 1:
        return 1
    if ww == 1:
        if win[0]=="X" and XC-OC == 1:
            return 1
        if win[0]=="O" and XC-OC == 0:
            return 1
        else:
            return 3
    else:
        return 2
    
    
T = int(input())
for i in range(T):
    mat = []
    for i in range(3):
        re = str(input())
        r = []
        for i in re:
            r.append(i)
        mat.append(r)
    print(fun(mat))
        
