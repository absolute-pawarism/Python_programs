sample=['p','q']
number=int(input("Enter the number: "))
nl=[y+str(x) for x in range(1,number+1) for y in sample]
print(nl)
