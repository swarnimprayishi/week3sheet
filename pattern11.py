n = 5  
for i in range(n):
    star = n - i
    space = i * 2 + 1
    print('*' * star + ' ' * space + '*' * star)
for i in range(n):
    star = i + 1
    space = (n - i - 1) * 2 + 1
    print('*' * star + ' ' * space + '*' * star)



#********** 
#****     **** 
#***           *** 
#**                ** 
#*                     * 
#*                     * 
#**                ** 
#***           *** 
#****      **** 
#**********    