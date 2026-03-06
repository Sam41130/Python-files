
def grade_s():
    math = int(input("Enter marks score in Mathematics: "))
    english = int(input("Enter marks score in English: "))
    kiswahili = int(input("Enter marks score in Kiswahili: "))

    total = math + english + kiswahili
    average = total / 3

    print("Your average score is", average)

    if 70 <= average <= 100:
        print("You have an A. Congratulations.")
    elif 60 <= average <= 69:
        print("You have a B.")
    elif 50 <= average <= 59:
        print("You have a C.")
    elif 40 <= average <= 49:
        print("You have a D.")
    elif average < 40:
        print("You have failed the test.")
    else:
        print("Enter valid marks.")

grade_s()    
