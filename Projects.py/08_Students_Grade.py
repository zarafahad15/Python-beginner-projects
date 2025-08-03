perc = int(input("Enter your percentage: "))

if perc >= 90 and perc <= 100:
    print("Grade: A+🎉")
elif perc >= 80 and perc < 90:
    print("Grade: A🎉")
elif perc >= 60 and perc < 80:
    print("Grade: B")
elif perc >= 50 and perc < 60:
    print("Grade: C")
elif perc >= 40 and perc < 50:
    print("Grade: D")
elif perc >= 0 and perc < 40:
    print("Grade: F")
else:
    print("Invalid percentage entered!")


