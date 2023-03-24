n=int(input())
if(n%2==1):
    print("Weird")
elif(n%2==0 and range(2,5)):
    print("Not Weired")
elif(n%2==0 and range(6,20)):
    print("Weired")
else(n%2==0 and n>20):
    print("Not Weired")