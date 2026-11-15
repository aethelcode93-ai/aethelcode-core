# First risk model I built for AethelCode
# Checking if a stock is too risky to invest right now

def calculate_risk(price, volatility):
    if volatility > 5.0:
        return "HIGH RISK"
    else:
        return "SAFE INVESTMENT"

# Testing the function with my own numbers
result = calculate_risk(240, 6.8)
print(result)
