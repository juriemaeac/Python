import math
import sys 

print("=*"*25)
print("|     /\     |      Welcome to      |      /\    |")
print("|  \ c'')    | Trigonometric Solver |   \ c'')   |")
print("|   ;-/\>    |      Created by:     |    ;-/\>   |")
print("|     ||     |   *Your Name Here*   |      ||    |")
print("=*"*25)
user = input("Enter Username: ")
print ("[Hello", user+"!]")
print("="*50)

#testing ko lng
#opposite = int (input())
#hypotenuse = int (input())
#sin =  math.asin((opposite/hypotenuse))
#deg = sin*(180/math.pi)
#print(deg)

def trigFunc(a,b,c):
  adjacent = a
  opposite = b
  hypotenuse = c
  print("-"*50)
  ''''
  print("Sine: ", round(math.asin((opposite/hypotenuse)*(180/math.pi)),4), "°")
  print("Cosine: ", round(math.acos((adjacent/hypotenuse)*(180/math.pi)),4), "°")
  print("Tangent: ", round(math.atan((opposite/adjacent)*(180/math.pi)),4), "°")
  print("Cosecant: ", round((1/math.asin((opposite/hypotenuse)*(180/math.pi))),4), "°")
  print("Secant: ", round((1/math.acos((adjacent/hypotenuse)*(180/math.pi))),4), "°")
  print("Cotangent: ", round((1/math.atan((opposite/adjacent)*(180/math.pi))),4, "°"))
 
  print("-"*50)
  
  
  trigValues = []
  trigIdentity = ["Sin: ", "Cos", "Tan: ", "Cosecant: ", "Secant: ", "Cotangent: "]
  trigValues[1] = sin*(180/math.pi)
  trigValues[2] = cos*(180/math.pi)
  trigValues[3] = tan*(180/math.pi)
  trigValues[4] = csc*(180/math.pi)
  trigValues[5] = sec*(180/math.pi)
  trigValues[6] = cot*(180/math.pi)

  for x in trigValues:
    for a in x:
      print(trigIdentity[a],trigValues[a])
  
'''
  sin= float((math.asin((opposite/hypotenuse))))
  cos= float((math.acos((adjacent/hypotenuse))))
  tan= float((math.atan((opposite/adjacent))))
  csc= float(1/sin)
  sec= float(1/cos)
  cot= float(1/tan) 
  
  print("Sine:", round(sin*(180.0/math.pi),4),"°")
  print("Cosine:", round(cos*(180.0/math.pi),4),"°")
  print("Tangent:", round(tan*(180.0/math.pi),4),"°")
  print("Cosecant:", round(csc*(180.0/math.pi),4),"°")
  print("Secant:", round(sec*(180.0/math.pi),4)+"°")
  print("Cotangent:", round(cot*(180.0/math.pi),4)+"°")

while True: 
  print("\n                  [Options Menu]") 
  print("-"*50)
  print("[1] Open Trigonometric Calculator.")
  print("[2] Open Trigonometric Solver for Math Problems. ")
  print("[3] Exit.")
  print("-"*50)
  choiceMenu = int(input("What do you want to do?: "))
  
  if choiceMenu == 1:
      print ("")
      #repeating 
      print("   || Trigonometric Calculator ||  ")
      print("===========================================")
      print("| [1] Given: Angle and Side of a Triangle |")
      print("| [2] Given: Two Sides of a Triangle      |")
      print("| [3] Evaluate Angle                      |")
      print("| [4] Exit.                               |")     
      print("===========================================")
      opt1 = int(input("Option: "))
      #####################################################################
      if opt1 == 1:
        print ("\n[Choose which side is given]\n 1. Adjacent   2. Opposite  3. Hypotenuse")
        print ("")
        opt2 = int(input("Option: "))
        if opt2 == 1:
          adjacent = int(input("Input adjacent side: "))
          degrees = int(input("Input angle in degrees: "))
          print("-"*50)
          print ("hypotenuse: ", round(adjacent*(math.cos(degrees*(math.pi/180))),4))
          print ("opposite: ", round(adjacent*(math.tan(degrees*(math.pi/180))),4))
          
        elif opt2 == 2:
          opposite = int(input("Input opposite side: "))
          degrees = int(input("Input angle in degrees: "))
          print("-"*50)
          print ("hypotenuse: ", round(opposite*(math.sin(degrees*(math.pi/180))),4))
          print ("adjacent: ", round(opposite*(math.tan(degrees*(math.pi/180))),4)) #not sure di ko alam

        elif opt2 == 3:
          hypotenuse = int(input("Input hypotenuse: "))
          degrees = int(input("Input angle in degrees: "))
          print("-"*50)
          print ("opposite: ", round(hypotenuse*(math.sin(degrees*(math.pi/180))),4))
          print ("adjacent: ", round(hypotenuse*(math.cos(degrees*(math.pi/180))),4))

        else:
          print("[!]Invalid")
      #####################################################################
      elif opt1 == 2:
        print ("\n[Choose which side to find]\n 1. Adjacent   2. Opposite  3. Hypotenuse")
        side = int(input("What side do you want to solve: "))

        if side == 1:
          hypotenuse = int(input("Enter hypotenuse side: "))
          opposite = int(input("Enter opposite side: "))
          adjacent = math.sqrt((hypotenuse**2) - (opposite**2))
          print("-"*50)
          print("Adjacent: ", adjacent)
          trigFunc(adjacent, opposite, hypotenuse)#ampota bakit nawala alin?
          
        elif side == 2:
          adjacent = int(input("Enter adjacent side: "))
          hypotenuse = int(input("Enter hypotenuse side: "))
          opposite = math.sqrt((hypotenuse**2) - (adjacent**2))
          print("-"*50)
          print ("Opposite : ", opposite)
          trigFunc(adjacent, opposite, hypotenuse) 
          
        elif side == 3:
          adjacent = int(input("Enter adjacent side: "))
          opposite = int(input("Enter opposite side: "))
          hypotenuse =   math.sqrt((adjacent**2) + (opposite**2))
          print("-"*50)
          print ("Hypotenuse : ", hypotenuse)
          trigFunc(adjacent, opposite, hypotenuse)

        else:
          print("[!]Invalid")
      #####################################################################
      elif opt1 == 3:
        noQuadrant=[0.0,90.0,180.0,270.0,360.0,0,90,180,270,360]
        angle = int(input("Input angle: "))
        basis = angle
        angle %= 360.
        if (angle < 0): 
          angle += 360.0;
        if angle in noQuadrant:
          if angle == 0.0 or angle == 360.0: 
            print("Angle in +x axis")
            print("Special Angle")
          elif angle == 180.0:
            print("Angle in -x axis")
            print("Special Angle")
          elif angle == 90.0:
            print("Angle in +y axis")
            print("Special Angle")
          elif angle == 270.0:
            print("Angle in -y axis")  
            print("Special Angle")
          else:
            print("[!]Angle cannot be classified.")
        
        else:
          quadrant = int((angle/90) % 4 + 1)
          quadrantList = ["I", "II", "III", "IV"]
          print("-"*50)
          print("Angle",basis, "is in", "quadrant", quadrantList[quadrant-1])
          print("-"*50)  
      #####################################################################
      elif opt1 == 4:
        print("Exiting Trigonometric Calculator")
        break

      else:
        print("[!]Invalid input.")
      #####################################################################
    
  elif choiceMenu == 2:
    print ("") 
    print("\n || Trigonometric Solver for Math Problems ||  \n")
    print("           _________________________            ") 
    print("           |    [Illustration]     |            ")
    print("           |=======================|            ")         
    print("           |       ~~              |            ")
    print("           |      ~                |            ")
    print("           |   _u__                |            ")       
    print("           |  /____\>              |            ")
    print("           |  |[][]| \  <--Ladder  |            ")    
    print("           | _|[]..|__\            |            ") 
    print("           |  '--'''               |            ")
    print("           |_______________________|            ")    
    print("===============[Given Question]=================")
    print("| A 36ft ladder is inclined 60° to the ground. |")
    print("| Suppose the ladder is leaned against a house |")
    print("| at this angle, find the distance from the    |")
    print("| base of the house to the foot of the ladder  |")
    print("| and the height reached by the ladder.        |")                      
    print("================================================")
    print("Given")
    hypotenuse = int(input("Input hypotenuse (length of ladder): "))
    degrees = int(input("Input angle in degrees: "))
    print("-"*50)
    if hypotenuse == 36 & degrees == 60:
      print ("Height: ", round(hypotenuse*(math.sin(degrees*(math.pi/180))),4))
      print ("Distance: ", round(hypotenuse*(math.cos(degrees*(math.pi/180))),4))
    else:
      print("[!]Invalid value please check the problem.")
    print("-"*50)
   
    print("")
    print("________________________________________________") 
    print("|               [ Illustration ]               |")
    print("|==============================================|")   
    print("|                            ,-.               |") 
    print("|                 __,.      /  /               |")  
    print("|                 ; \____,-==-._  )            |") 
    print("|                 //__   `----' {+>            |") 
    print("|               /|`   '--/  /-'`(              |") 
    print("|              / | _    /  /                   |") 
    print("|             /  |  |   `='                    |") 
    print("|            /   |  |                          |")
    print("|           /    |  3                          |")
    print("|          /     |  0                          |")
    print("|         /      |  0                          |")
    print("|        /       |  m              _u__        |")
    print("|       /        |  |             /____\       |")
    print("|      /         |  |             |[][]|       |")
    print("|     /         _| _|            _|[]..|_      |")
    print("|    /_________|_|                '--'''       |")
    print("|==============[Given Question]================|")
    print("| Find the angle of elevation of the plane     |")
    print("| from the ground (Point A). Given that the    |")
    print("| height of the plane is 300 meters with       |")
    print("| distance of 400 meters.                      |")
    print("================================================")
    print("Given")
    h = int(input("Enter height: "))
    w = int(input("Enter distance: "))
    if h == 300 & w == 400:
      tan= float((math.atan((h/w))))
      print("Angle of elevation: ", round(tan*(180/math.pi)),4)
    else:
      print("[!]Invalid value, please check the problem.")
    print("-"*50)
 
  elif choiceMenu == 3:
    print("=*"*25)
    print("\t\t\t\tGoodbye ",user)
    print("=*"*25)
    sys.quit()


