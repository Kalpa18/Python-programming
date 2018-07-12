N=int(input())
if((N>=1)and(N<=100000)):
  print("positive")
else:
  if(N==0):
    print("zero")
  elif(N<0):
    print("negative")
  else:
    print("out of range")
    
