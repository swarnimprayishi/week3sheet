rows = 5
for i in range(rows):
    for j in range(i):
        print('_', end=' ')
    for k in range(rows - i):
        print('*', end=' ')
    print()  



#*   * * * *          
#_  * * * *        
#_ _ * * *         
#_ _ _*  *        

#_ _ _ _* 
