n, m = map(int,input().split())
xy = [list(map(int,input().split())) for i in range(m)]

red_boxes = [False for i in range(n)]
red_boxes[0] = True
n_ball = [1 for i in range(n)]


for i in range(m):
    x_i = xy[i][0]-1
    y_i = xy[i][1]-1
    
    if n_ball[x_i] == 1:
        if red_boxes[x_i] == True:
            n_ball[x_i] -= 1
            n_ball[y_i] += 1
            red_boxes[x_i] = False
            red_boxes[y_i] = True
        
        else:
            n_ball[x_i] -= 1
            n_ball[y_i] += 1
    
    else:
        if red_boxes[x_i] == True:
            n_ball[x_i] -= 1
            n_ball[y_i] += 1
            red_boxes[y_i] = True
        
        else:
            n_ball[x_i] -= 1
            n_ball[y_i] += 1
    
    
    
print(red_boxes.count(True))