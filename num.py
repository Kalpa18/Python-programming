N=int(input())
if((N>=1)and(N<=100000)):
  print("Positive")
else:
  if(N==0):
    print("Zero")
  elif(N<0):
    print("Negative")
  else:
    print("Out of range")
    
