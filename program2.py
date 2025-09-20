def generate_series(x):
    num=1
    for i in range(x):
        print(num,end=" ")
        num=num+2
    

# Example usage
a = int(input("Enter the Integer : "))
generate_series(a)
