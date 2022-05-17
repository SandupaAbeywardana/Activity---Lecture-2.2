count = 1

while count <= 5:
  mark = int(input("Enter Mark "))
  
  if(mark>75):
      print("Grade is A")
  elif(mark>=65 and mark<=75):
      print("Grade is B")
  elif(mark>=55 and mark<=64):
      print("Grade is C")
  elif(mark>=45 and mark<=54):
      print("Grade is S")
  elif(mark<45):
      print("Grade is F")
    
  count = count + 1
