# Python-BMI-Calculator
Calculate your BMI
START

DISPLAY "BMI Calculator"

PROMPT user to enter weight in kilograms
READ weight

PROMPT user to enter height in meters
READ height

IF weight or height is not a valid number THEN
    DISPLAY "Please enter valid numerical inputs."
    END

COMPUTE BMI = weight / (height ^ 2)

IF BMI < 18.5 THEN
    category = "Underweight"
ELSE IF BMI < 24.9 THEN
    category = "Normal weight"
ELSE IF BMI < 29.9 THEN
    category = "Overweight"
ELSE
    category = "Obesity"

DISPLAY "Your BMI is: [BMI]"
DISPLAY "Category: [category]"

END
