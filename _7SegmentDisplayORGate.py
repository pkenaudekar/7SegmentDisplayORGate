
def main():
    #Array for Binary Input 
    arr = [[1,1,1,1,1,1,1,0],
           [1,1,1,0,0,0,0,0],
           [1,0,1,0,1,1,0,1],
           [1,1,1,1,1,0,0,1],
           [1,0,1,1,0,0,1,1],
           [1,1,0,1,1,0,1,1],
           [1,1,0,1,1,1,1,1],
           [1,1,1,1,0,0,0,0],
           [1,1,1,1,1,1,1,1],
           [1,1,1,1,1,0,1,1]]
      
    #Target array for Binary Input 
    t = [[1,0,0,0,0,0,0,0,0,0],
         [0,1,0,0,0,0,0,0,0,0],
         [0,0,1,0,0,0,0,0,0,0],
         [0,0,0,1,0,0,0,0,0,0],
         [0,0,0,0,1,0,0,0,0,0],
         [0,0,0,0,0,1,0,0,0,0],
         [0,0,0,0,0,0,1,0,0,0],
         [0,0,0,0,0,0,0,1,0,0],
         [0,0,0,0,0,0,0,0,1,0],
         [0,0,0,0,0,0,0,0,0,1]]   

    # Considering learning rate = 1 
    alp = 1 

    #Select target from between 0 to 9
    tr = 0
  
    #yi = input, yo = output 
    w0 = 1
    w1 = 0
    w2 = 0
    w3 = 0
    w4 = 0
    w5 = 0
    w6 = 0
    w7 = 0
    b = 0
    count = 0
         
    while(1):
        print('x0  x1  x2  x3  x4  x5  x6  x7  b  yi   yo  t  dw0  dw1  dw2  dw3  dw4  dw5  dw6  dw7  db  w0  w1  w2  w3  w4  w5  w6  w7   b')

        for i in range (10):
            # Calaulating Input 
            yi = arr[i][0] * w0 + arr[i][1] * w1 + arr[i][2] * w2 + arr[i][3] * w3 + arr[i][4] * w4 + arr[i][5] * w5 + arr[i][6] * w6 + arr[i][7] * w7 + b; 
            if yi >= 0: 
                yo = 1
            else:
                yo = 0
            if t[tr][i] == yo:
                count+=1 
                dw0 = 0 
                dw1 = 0 
                dw2 = 0 
                dw3 = 0 
                dw4 = 0 
                dw5 = 0 
                dw6 = 0 
                dw7 = 0 
                db = 0 
            # Calaulating Change in Weight 
            else:
                dw0 = alp*(t[0][i] - yo) * arr[i][0] 
                dw1 = alp*(t[0][i] - yo) * arr[i][1] 
                dw2 = alp*(t[0][i] - yo) * arr[i][2] 
                dw3 = alp*(t[0][i] - yo) * arr[i][3] 
                dw4 = alp*(t[0][i] - yo) * arr[i][4] 
                dw5 = alp*(t[0][i] - yo) * arr[i][5] 
                dw6 = alp*(t[0][i] - yo) * arr[i][6] 
                dw7 = alp*(t[0][i] - yo) * arr[i][7] 
                db = alp*(t[0][i] - yo) 
           
            w0 = w0 + dw0 
            w1 = w1 + dw1 
            w2 = w2 + dw2
            w3 = w3 + dw3
            w4 = w4 + dw4
            w5 = w5 + dw5
            w6 = w6 + dw6
            w7 = w7 + dw7
            b = b + db
            print(arr[i][0]," ",arr[i][1]," ",arr[i][2]," ",arr[i][3]," ",arr[i][4]," ",arr[i][5]," ",arr[i][6]," ",arr[i][7]," ",1,"",yi,"  ",yo," ",t[tr][i]," ",dw0," ",dw1," ",dw2," ",dw3," ",dw4," ",dw5," ",dw6," ",dw7,"  ",db," ",w0," ",w1," ",w2," ",w3," ",w4," ",w5," ",w6," ",w7," ",b)
                    
        print('\n')
        if count == 10: 
            return 0
        else:
            count = 0      

if __name__ == "__main__": 
    main() 