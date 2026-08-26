if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l=list(arr)
    a=-100
    b=-100
    for i in l:
        if i>a:
            a=i
    for i in l:
        if i>b and i<a:
            b=i
    print(b)        
            
            
            


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna