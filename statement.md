# STATEMENT OF PROJECT: PERSONALIZED BMI CALCULATOR

## 🎯 Problem Statement

The goal is to provide users with a **simple, accurate, and accessible tool** to calculate their Body Mass Index (BMI) and, more importantly, to deliver **immediately actionable, personalized health and lifestyle recommendations** based on their specific BMI category. Existing BMI calculators often provide only the numerical result and category, lacking tailored guidance on nutrients, diet, and exercise that are crucial for promoting a healthier lifestyle.

---

## 🧭 Scope of the Project

The scope of this project, implemented in the provided Python script, is limited to:

1.  **Input Handling:** Safely accepting and validating positive numerical inputs for weight (kilograms) and height (centimeters).
2.  **Core Calculation:** Accurately calculating the BMI using the standard formula.
3.  **Classification:** Mapping the calculated BMI to one of the four recognized categories (Underweight, Normal weight, Overweight, Obesity).
4.  **Recommendation Generation:** Returning pre-defined, category-specific recommendations for nutrition, diet, and exercise.

**Out of Scope:**
* Advanced body composition analysis (e.g., body fat percentage).
* Storage of user data or history.
* Medical diagnosis or professional consultation.

---

## 👥 Target Users

The primary target users are individuals seeking a quick and informative assessment of their weight status and general health guidance.

* **Individuals focused on fitness** who want to monitor their progress.
* **Health-conscious individuals** looking for general, category-based advice on diet and exercise.
* **Students or educators** needing a simple, functional example of conditional logic applied to a public health metric.

---

## ✅ High-Level Features

| Feature | Description |
| :--- | :--- |
| **Robust Input Validation** | Ensures user input is a positive number, preventing calculation errors and crashes. |
| **Accurate BMI Calculation** | Converts centimeters to meters and calculates BMI based on the standard formula. |
| **BMI Categorization** | Assigns the result to one of four internationally recognized weight categories. |
| **Personalized Recommendations** | Delivers unique, text-based advice covering **Nutrients**, **Diet**, and **Exercise** for each category. |
| **Command Line Interface (CLI)** | Provides a simple, text-based interface for easy execution in any standard terminal. |
