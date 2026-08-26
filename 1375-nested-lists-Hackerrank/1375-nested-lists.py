if __name__ == '__main__':
    l1=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l2=[name,score]
        l1.append(l2)
    a=101 
    b=101   
    for x,y in l1:
        if y<a:
            a=y
    for x,y in l1:
        if y>a and y<b:
            b=y
    l3=[]   
    for x,y in l1:
        if y==b:
            l3.append(x)
    l3=sorted(l3)
    for i in l3:
        print(i) 
            
            
        
            
        


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna