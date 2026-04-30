import math

print("--- BPO Training Assistant ---")

# 1. Input Training/Shift Data
total_shift_hours = 7.5
name = input("Enter employee name: ")
cases_resolved = int(input("How many cases have you resolved so far? "))
hours_worked = float(input("How many hours have you been on shift? "))

# 2. Calculations (Target is 5 cases per hour)
target_cases = hours_worked * 5
productivity = (cases_resolved / target_cases) * 100 if target_cases > 0 else 0

# Shift progress
progress = (hours_worked / total_shift_hours) * 100
remaining_hours = total_shift_hours - hours_worked

# 3. Output Results
print(f"\n--- Progress Report for {name} ---")
print(f"Shift Progress: {progress:.1f}% (Remaining: {remaining_hours}h)")
print(f"Productivity Score: {math.floor(productivity)}%")

if productivity >= 100:
    print("Status: ✅ Target Met! Great job.")
else:
    print(f"Status: ⚠️ Below Target. You need {math.ceil(target_cases - cases_resolved)} more cases to catch up.")
