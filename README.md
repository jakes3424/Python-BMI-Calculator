START

DISPLAY "BMI Calculator (US Units)"

PROMPT user to enter weight in pounds
READ weight_lbs

PROMPT user to enter height in feet
READ height_feet

PROMPT user to enter height in inches
READ height_inches

IF any input is invalid THEN
    DISPLAY "Invalid input. Please enter numbers only."
    END

CONVERT weight_lbs to kilograms:
    weight_kg = weight_lbs × 0.453592

CONVERT height_feet and height_inches to total inches:
    total_inches = (height_feet × 12) + height_inches

CONVERT total_inches to meters:
    height_m = total_inches × 0.0254

CALCULATE BMI:
    bmi = weight_kg / (height_m ^ 2)

IF bmi < 18.5 THEN
    category = "Underweight"
ELSE IF bmi < 24.9 THEN
    category = "Normal weight"
ELSE IF bmi < 29.9 THEN
    category = "Overweight"
ELSE
    category = "Obesity"

DISPLAY "Your BMI is: [bmi]"
DISPLAY "Category: [category]"

END
