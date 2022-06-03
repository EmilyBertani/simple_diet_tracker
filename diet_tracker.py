class Diet:
    def __init__(self, breakfast_cal, lunch_cal, dinner_cal, snack_cal, exercise_cal):
        self.breakfast_cal = breakfast_cal
        self.lunch_cal = lunch_cal
        self.dinner_cal = dinner_cal
        self.snack_cal = snack_cal
        self.exercise_cal = exercise_cal
    
    def calorie_deficit(self):
        deficit = self.exercise_cal - (self.breakfast_cal + self.lunch_cal + self.dinner_cal + self.snack_cal)
        return deficit

breakfast_cal = int(input("How many calories did you have for breakfast? "))
lunch_cal = int(input("How many calories did you have for lunch? "))
dinner_cal = int(input("How many calories did you have for dinner? "))
snack_cal = int(input("How many calories did you have as snacks? "))
exercise_cal = int(input("How many calories did you burn exercising? "))

fitness = Diet(breakfast_cal, lunch_cal, dinner_cal, snack_cal, exercise_cal)

weekly_deficit = 7 * fitness.calorie_deficit()

if weekly_deficit > 0:
    print (f"You will lose {round(weekly_deficit / 3600, 2)} lbs per week.")
elif weekly_deficit == 0:
    print(f"Your weight will stay the same. ")
else:
    print(f"You will gain {round(-1 * weekly_deficit / 3600, 2)} lbs per week." )
