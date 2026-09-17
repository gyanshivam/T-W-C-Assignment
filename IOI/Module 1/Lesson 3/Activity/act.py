# ================================
#  MY STUDY SESSION PLANNER
#  File: my-study-session-planner.py
# ================================

# PART 1 - USER INPUT
subject = input("Enter the subject you are studying: ")
hours = float(input("Enter how many hours you plan to study: "))

# PART 2 - if STATEMENT
if hours > 4:
    print("Warning: That is a very long study session. Take breaks!")

# PART 3 - if-else
if hours >= 2:
    print("Nice! This is a solid study block.")
else:
    print("A short session is still better than none!")

# PART 4 - if-elif-else
if hours > 6:
    print("Focus Level: Marathon Mode")
elif hours > 3:
    print("Focus Level: Deep Work")
elif hours > 1:
    print("Focus Level: Quick Review")
else:
    print("Focus Level: Light Touch")

# PART 5 - datetime MODULE
import datetime
import calendar

now = datetime.datetime.now()
print("Subject:", subject)
print("Time now:", now)

print(calendar.calendar(now.year))