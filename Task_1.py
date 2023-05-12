print("\n")
print("**********************// Simmple Calculater //**********************")
print("\n")
var = True
while var == True :
    print("Press 1-5 num to select an opration:-")
    print("    1. Addition")
    print("    2. Subtraction")
    print("    3. Multiplication")
    print("    4. Division")
    print("    5. Square")
    print("    6. Cube")
    print("    7. quite \n")
    opra = input() #opration variable
    if opra == "1" :        #for addition opration 
        num1 = input("Enter the first number to Addition \n")
        num2 = input("Enter the secound number to Addition \n")
        print(f"The Result of sum of both numbers are {int(num1)+int(num2)} \n")
    
    elif opra == "2" :        #for subtraction opration
        num1 = input("Enter the first number to Subtraction \n")
        num2 = input("Enter the secound number to Subtraction \n")
        print(f"The Result of Subtraction of both numbers are {int(num1)-int(num2)} \n")
    
    
    elif opra == "3" :        #for Multiplication opration
        num1 = input("Enter the first number to Multiplication \n")
        num2 = input("Enter the secound number to Multiplication \n")
        print(f"The Result of Multiplication of both numbers are {int(num1)*int(num2)} \n")
    
    
    elif opra == "4" :        #for Division opration
        num1 = input("Enter the first number to Division \n")
        num2 = input("Enter the secound number to Division \n")
        print(f"The Result of Division of both numbers are {(int(num1)/int(num2))} \n")
    
    
    elif opra == "5" :        #for square opration
        num1 = input("Enter the number for square \n")
        print(f"The result of square is {int(num1)*int(num1)} \n")
    
    
    elif opra == "6" :      #for cube opration
        num1 = input("Enter the number for Cube \n")
        print(f"The Result of Cube is {int(num1)*int(num1)*int(num1)} \n")

    elif opra == "7" :      #for quite opration
         exit()
        
    
    else : 
            print("Wrong input please try again !!!")
    
