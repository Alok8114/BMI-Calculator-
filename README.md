# Personalized BMI Calculator 📊

This Python script calculates the **Body Mass Index (BMI)** based on user input (weight in kilograms and height in centimeters) and provides personalized health recommendations tailored to the resulting BMI category.

---

## ✨ Features

* **BMI Calculation:** Accurately calculates BMI using the standard formula.
* **Input Validation:** Uses the `get_positive_float` function to ensure safe and positive numerical input from the user.
* **Category Classification:** Classifies the BMI into standard categories: **Underweight**, **Normal weight**, **Overweight**, and **Obesity**.
* **Personalized Recommendations:** Provides specific advice for **Nutrients**, **Diet**, and **Exercise** based on the identified BMI category.

---

## 🚀 How to Run the Script

### Prerequisites

You need **Python 3** installed on your system.

### Execution

1.  **Save the Code:** Save the provided code into a file named `bmi_calculator.py`.
2.  **Open Terminal:** Open your terminal or command prompt.
3.  **Run the Script:** Execute the file using the Python interpreter:

    ```bash
    python bmi_calculator.py
    ```

4.  **Follow Prompts:** The script will prompt you to enter your weight in kilograms (kg) and your height in centimeters (cm).

---

## 💻 Code Overview

The script is divided into four main functions:

### `calculate_bmi(weight_kg, height_cm)`

Calculates the BMI. It first converts the height from centimeters to meters.

$$\text{BMI} = \frac{\text{weight in kg}}{(\text{height in cm} / 100)^2}$$

### `bmi_category_and_recommendations(bmi)`

Takes the calculated BMI and returns the corresponding category and a string containing tailored health recommendations (Nutrients, Diet, Exercise).

| BMI Range | Category |
| :--- | :--- |
| **< 18.5** | Underweight |
| **18.5 – 24.9** | Normal weight |
| **25.0 – 29.9** | Overweight |
| **$\ge$ 30.0** | Obesity |

### `get_positive_float(prompt)`

A robust utility function that handles user input. It ensures the user enters a **valid positive number** and reprompts them if the input is invalid (non-numeric or zero/negative).

### `main()`

The primary function that orchestrates the program flow:
1.  Collects user input for weight and height.
2.  Calls `calculate_bmi`.
3.  Calls `bmi_category_and_recommendations`.
4.  Prints the final results clearly to the console.

---

## 💡 Example Usage
