def calculate_bmi(weight, height):
    """
    Calculate BMI using the formula: BMI = weight (kg) / (height (m))^2
    """
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    """
    Interpret the BMI result according to standard categories.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("BMI Calculator")
    try:
        weight = float(input("Enter your weight in kilograms (kg): "))
        height = float(input("Enter your height in meters (m): "))
        
        bmi = calculate_bmi(weight, height)
        category = interpret_bmi(bmi)
        
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Category: {category}")
    except ValueError:
        print("Please enter valid numerical inputs.")

if __name__ == "__main__":
    main()
