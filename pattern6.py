n = int(input("Enter no of rows : "))

for i in range(1, n+1):
    print("*", end=" ")
    for j in range(n - i+1):
        print(" ", end="")  
    print("*")


#*_ _ _ _ _*        
#*_ _ _ _*           
#*_ _ _*               
#*_ _*    
#*_*               
           


