def calculate_bmi(weight_kg, height_cm):
    """Calculate BMI given weight in kilograms and height in centimeters."""
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)

def bmi_category_and_recommendations(bmi):
    """Return BMI category and personalized recommendations for nutrients, diet, and exercise."""
    if bmi < 18.5:
        return (
            "Underweight",
            "Nutrients: Focus on calorie-dense and protein-rich foods like nuts, seeds, dairy, eggs, and lean meats.\n"
            "Diet: Eat small, frequent meals including healthy fats and smoothies with fruits and protein powders.\n"
            "Exercise: Light strength training to build muscle mass; avoid excessive cardio."
        )
    elif 18.5 <= bmi < 24.9:
        return (
            "Normal weight",
            "Nutrients: Maintain a balanced intake of carbohydrates, proteins, fats, vitamins, and minerals.\n"
            "Diet: Emphasize fruits, vegetables, whole grains, lean proteins, and stay hydrated.\n"
            "Exercise: Regular moderate aerobic exercise (like walking, jogging) and strength training for overall fitness."
        )
    elif 25 <= bmi < 29.9:
        return (
            "Overweight",
            "Nutrients: Prioritize high-fiber foods, lean proteins, and reduce intake of sugars and saturated fats.\n"
            "Diet: Reduce processed foods and sugary beverages; focus on portion control and balanced meals.\n"
            "Exercise: Increase aerobic activities like brisk walking, cycling, plus strength training to improve metabolism."
        )
    else:
        return (
            "Obesity",
            "Nutrients: Adopt a nutrient-dense, low-calorie diet rich in vegetables, lean protein, and whole grains.\n"
            "Diet: Limit high-calorie processed foods, sugary drinks, and fried items; consider professional diet guidance.\n"
            "Exercise: Start with low-impact activities such as walking or swimming; gradually increase intensity with medical advice."
        )

def get_positive_float(prompt):
    """Prompt user for positive float input safely."""
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Oops! Please enter a number greater than zero.")
        except ValueError:
            print("Hmm, that doesn't look like a valid number. Please try again.")

def main():
    print("Welcome to the Personalized BMI Calculator!")
    weight = get_positive_float("Please enter your weight in kilograms: ")
    height = get_positive_float("Please enter your height in centimeters: ")

    bmi = calculate_bmi(weight, height)
    category, recommendations = bmi_category_and_recommendations(bmi)

    print(f"\nYour BMI is: {bmi}")
    print(f"Category: {category}")
    print("Recommended Nutrients, Diet, and Exercise Tips:")
    print(recommendations)

if __name__ == "__main__":
    main()