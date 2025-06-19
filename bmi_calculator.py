def calculate_bmi(weight_lbs, height_feet, height_inches):
    # Convert weight from pounds to kilograms
    weight_kg = weight_lbs * 0.453592

    # Convert height from feet and inches to meters
    total_inches = height_feet * 12 + height_inches
    height_m = total_inches * 0.0254

    # BMI formula
    bmi = weight_kg / (height_m ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("BMI Calculator (US Units)")

    try:
        weight_lbs = float(input("Enter your weight in pounds (lbs): "))
        height_feet = int(input("Enter your height - feet part (ft): "))
        height_inches = int(input("Enter your height - inches part (in): "))

        bmi = calculate_bmi(weight_lbs, height_feet, height_inches)
        category = interpret_bmi(bmi)

        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Category: {category}")

    except ValueError:
        print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    main()
