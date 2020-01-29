
def main():
    #Array for Binary Input 
    arr = [[0,0],[0,1],[1,0],[1,1]]
      
    #Target array for Binary Input 
    t = [0,1,1,1]   
    # Considering learning rate = 1 
    alp = 1 
  
    #yi = input, yo = output 
    w1 = 0
    w2 = 0
    b = 0
    count = 0
         
    while(1):
        print('x1  x2  b  yi   yo  t  dw1  dw2  db  w1  w2   b')

        for i in range (4):
            # Calaulating Input 
            yi = arr[i][0] * w1 + arr[i][1] * w2 + b; 
            if yi >= 0: 
                yo = 1
            else:
                yo = 0
            if t[i] == yo:
                count+=1 
                dw1 = 0 
                dw2 = 0 
                db = 0 
            # Calaulating Change in Weight 
            else:
                dw1 = alp*(t[i] - yo) * arr[i][0] 
                dw2 = alp*(t[i] - yo) * arr[i][1] 
                db = alp*(t[i] - yo) 
           
            w1 = w1 + dw1 
            w2 = w2 + dw2 
            b = b + db
            print(arr[i][0]," ",arr[i][1]," ",1,"",yi,"  ",yo," ",t[i]," ",dw1," ",dw2,"  ",db," ",w1," ",w2," ",b)
                    
        print('\n')
        if count == 4: 
            return 0
        else:
            count = 0      

if __name__ == "__main__": 
    main() 