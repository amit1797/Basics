print("Welcome to Leap Year Checker")
year = int(input("Which year do you want to Check: "))
if year % 4== 0:
  if year % 100 != 0:
    print("Leap Year")
  else:
    if year % 400 == 0:
      print("Leap Year")
    else:
      print("Not Leap year")
     
else:
  print("Not Leap Year")

    
  
    
  
