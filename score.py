# Prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is within range, print a grade according to the following table:
# >= 0.9 A 
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F

score = float(input("Enter Score: "))
try:
    if score >= 0.9:
        print("A")
    if score >= 0.8:
        print("B")
    if score >= 0.7:
        print("C")
    if score >= 0.6:
        print("D")
    if score < 0.6:
        print("F")
except:
    print("Sorry invalid")
