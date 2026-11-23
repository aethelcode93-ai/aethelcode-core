# Second quantitative script for AethelCode
# Splits a total budget into safe savings and tech investments

def split_budget(total_money):
    safe_part = total_money * 0.70
    tech_part = total_money * 0.30
    return safe_part, tech_part

# Testing with an example budget of 1000
safe, tech = split_budget(1000)
print("Safe allocation:", safe)
print("Tech allocation:", tech)
