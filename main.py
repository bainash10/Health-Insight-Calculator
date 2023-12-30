import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight", "blue"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight", "green"
    elif 25 <= bmi < 29.9:
        return "Overweight", "orange"
    else:
        return "Obese", "red"

def calculate_calories(age, weight, gender):
    if gender.lower() == 'male':
        calories = 10 * weight + 6.25 * 170 - 5 * age + 5
    elif gender.lower() == 'female':
        calories = 10 * weight + 6.25 * 170 - 5 * age - 161
    else:
        calories = 0  # Invalid gender input

    return calories

def calculate_nutrient_intake(calories):
    fat_percentage = 0.25
    protein_percentage = 0.20

    fat_intake = calories * fat_percentage / 9
    protein_intake = calories * protein_percentage / 4

    return fat_intake, protein_intake

def calculate_hydration_limit(weight):
    hydration_limit = weight * 0.033
    return hydration_limit

def suggest_physical_activity(bmi):
    if bmi < 18.5:
        return "Consider incorporating strength training and a balanced diet to gain healthy weight."
    elif 18.5 <= bmi < 24.9:
        return "Maintain a balanced diet and regular physical activity for overall health."
    elif 25 <= bmi < 29.9:
        return "Focus on a combination of aerobic exercise and strength training to manage weight."
    else:
        return "Consult with a healthcare professional for personalized advice on weight management."

def get_random_quote(category):
    quotes = {
        "Underweight": [
            "Embrace your uniqueness. You're more than just a number on a scale.",
            "Your journey to a healthier you begins with self-love and nourishment.",
        ],
        "Normal weight": [
            "Celebrate your healthy choices. You're on the right track!",
            "Every step towards a healthier lifestyle is a step towards happiness.",
        ],
        "Overweight": [
            "Small changes lead to big results. Keep moving forward!",
            "You have the power to make positive choices for your well-being.",
        ],
        "Obese": [
            "Your health is an investment, not an expense. Take small steps for a big impact.",
            "Today's choices shape tomorrow's outcomes. Choose health and happiness.",
        ],
    }
    return random.choice(quotes.get(category, ["No specific quote for this category."]))

def calculate_and_display():
    try:
        age = int(age_entry.get())
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        gender = gender_entry.get()

        bmi = calculate_bmi(weight, height)
        interpretation, color = interpret_bmi(bmi)
        calories = calculate_calories(age, weight, gender)
        fat_intake, protein_intake = calculate_nutrient_intake(calories)
        hydration_limit = calculate_hydration_limit(weight)
        activity_suggestion = suggest_physical_activity(bmi)
        random_quote = get_random_quote(interpretation)

        result_window = tk.Toplevel(main_window)
        result_window.title("Health Calculator Results")

        # Display interpretation with colored text
        interpretation_label = ttk.Label(result_window, text=f"You are considered: {interpretation}", foreground=color)
        interpretation_label.pack(padx=10, pady=10)

        quote_label = ttk.Label(result_window, text=f"Random Quote: {random_quote}")
        quote_label.pack(padx=10, pady=10)

        fat_label = ttk.Label(result_window, text=f"Recommended daily fat intake: {fat_intake:.2f} grams")
        fat_label.pack(padx=10, pady=10)

        protein_label = ttk.Label(result_window, text=f"Recommended daily protein intake: {protein_intake:.2f} grams")
        protein_label.pack(padx=10, pady=10)

        hydration_label = ttk.Label(result_window, text=f"Recommended daily hydration limit: {hydration_limit:.2f} ml")
        hydration_label.pack(padx=10, pady=10)

        activity_label = ttk.Label(result_window, text=f"Activity Suggestion: {activity_suggestion}")
        activity_label.pack(padx=10, pady=10)

        # Button to generate a new random quote without recalculating
        new_quote_button = ttk.Button(result_window, text="Generate New Quote", command=lambda: quote_label.configure(text=f"Random Quote: {get_random_quote(interpretation)}"))
        new_quote_button.pack(pady=10)

        ok_button = ttk.Button(result_window, text="OK", command=result_window.destroy)
        ok_button.pack(pady=10)

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values for age, weight, and height.")

# Main GUI window
main_window = tk.Tk()
main_window.title("Health Calculator")

# Create and pack GUI elements with a color scheme
style = ttk.Style()
style.configure('TLabel', font=('Helvetica', 12), padding=5)
style.configure('TButton', font=('Helvetica', 12), padding=10)

main_window.configure(bg='#F0F0F0')  # Set background color

age_label = ttk.Label(main_window, text="Enter your age:")
age_label.grid(column=0, row=0, padx=10, pady=10)

age_entry = ttk.Entry(main_window)
age_entry.grid(column=1, row=0, padx=10, pady=10)

weight_label = ttk.Label(main_window, text="Enter your weight in kg:")
weight_label.grid(column=0, row=1, padx=10, pady=10)

weight_entry = ttk.Entry(main_window)
weight_entry.grid(column=1, row=1, padx=10, pady=10)

height_label = ttk.Label(main_window, text="Enter your height in meters:")
height_label.grid(column=0, row=2, padx=10, pady=10)

height_entry = ttk.Entry(main_window)
height_entry.grid(column=1, row=2, padx=10, pady=10)

gender_label = ttk.Label(main_window, text="Enter your gender (Male/Female):")
gender_label.grid(column=0, row=3, padx=10, pady=10)

gender_entry = ttk.Entry(main_window)
gender_entry.grid(column=1, row=3, padx=10, pady=10)

calculate_button = ttk.Button(main_window, text="Calculate", command=calculate_and_display)
calculate_button.grid(column=0, row=4, columnspan=2, pady=10)

main_window.mainloop()
