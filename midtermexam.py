def Juan():
  print ("Hello, I´m your robo-asistant Juan")
  print ("I know the convertion and discounts for your machines would you like me to tell you?")
  response = input()
  if response==("no"):
    print ("Then goodbye")
  if response==("yes"):
    print ("Okay, let me tell you")
    print ("Please introduce the price of your first machine")
    machine1 = input()
    p = (float(machine1))*(float(10/100))
    ptotal = (float(machine1))-(float(p))
    print ("Acording to my calculations, the price of your machine with the 10% discount applied is",ptotal)
    print ("According to my system you had bought other 2 machines, would you like to calculate that to?")
    response2 = input()
    if response2==("no"):
      print ("Then that´s all goodbye")
    if response2==("yes"):
      print("Okay please input the second machine price")
      machine2 = input()
      print("Now the third machine price")
      machine3 = input()
      ca = (float(machine2))+(float(machine3))
      cap = (float(machine1))+(float(machine2))+(float(machine3))
      va = (float(machine2))*(float(10/100))
      ba = (float(machine3))*(float(10/100))
      va2 = (float(machine2))-(float(va))
      ba2 = (float(machine3))-(float(ba))
      vaba = (float(va2))+(float(ba2))
      vabap = (float(va2))+(float(ba2))+(float(ptotal))
      print ("Your 2 machines will cost",ca,"without the discount")
      print ("The 3 machines with no discount will cost",cap)
      print ("With the discount applied for both it will cost",vaba)
      print ("If we take in acount the first machine with a discount it will cost",vabap)
      print ("I can still convert your prices to Yen and Dollars")
      print ("Would you like me to do that?")
      response3 = input()
      if response3==("no"):
        print ("Well, that´s all thank you")
      if response3==("yes"):
        print ("Okay, let me calculate")
        yen = int((float(cap))*(float(8.37)))
        yen2 = int((float(vabap))*(float(8.37)))
        dollar = int((float(cap))*(float(0.057)))
        dollar2 = int((float(vabap))*(float(0.057)))
        print ("Calculations complete, price in yens with no discount is",yen)
        print ("Price in yens with discount is",yen2)
        print ("Price in dollars with no discount is",dollar)
        print ("Price in dollars with discount is",dollar2)
        print ("That would be everything I can do for now, Thank you :)")
    
Juan()
