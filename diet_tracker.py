class Diet:
    def __init__(self, breakfast_cal, lunch_cal, dinner_cal, snack_cal, exercise_cal, bmr):
        self.breakfast_cal = breakfast_cal
        self.lunch_cal = lunch_cal
        self.dinner_cal = dinner_cal
        self.snack_cal = snack_cal
        self.exercise_cal = exercise_cal
        self.bmr = bmr
    
    def calorie_deficit(self):
        deficit = self.bmr + self.exercise_cal - (self.breakfast_cal + self.lunch_cal + self.dinner_cal + self.snack_cal)
        return deficit

breakfast_cal = int(input("How many calories did you have for breakfast? "))
lunch_cal = int(input("How many calories did you have for lunch? "))
dinner_cal = int(input("How many calories did you have for dinner? "))
snack_cal = int(input("How many calories did you have as snacks? "))
exercise_cal = int(input("How many calories did you burn exercising? "))
gender = str(input("Are you male or female? enter M or F."))
weight = int(input("What is your weight in kg?"))
height = int(input("What is your height in cm?"))
age = int(input("What is your age?"))

if gender == "M":
    bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
elif gender == "F":
    bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

fitness = Diet(breakfast_cal, lunch_cal, dinner_cal, snack_cal, exercise_cal, bmr)

weekly_deficit = 7 * fitness.calorie_deficit()

if weekly_deficit > 0:
    print (f"Your basal metabolic rate is {bmr} and You will lose {round(weekly_deficit / 3600, 2)} lbs per week.")
elif weekly_deficit == 0:
    print(f"Your weight will stay the same. ")
else:
    print(f"Your basal metabolic rate is {bmr} and you will gain {round(-1 * weekly_deficit / 3600, 2)} lbs per week." )
