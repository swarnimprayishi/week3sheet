rows = 5
for i in range(rows):
    print('*', end=' ')
    for j in range(rows - i):
        print('_', end=' ')
    if i != rows - 1:
        print('*')
    else:
        print()


#*_ _ _ _ _*        
#*_ _ _ _*           
#*_ _ _*               
#*_ _*    
#*_*               
           

