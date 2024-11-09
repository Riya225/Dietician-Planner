from tkinter import *
from random import randint
from tkinter import messagebox

# Main window setup
root = Tk()
root.title('The Dietician - Health & Nutrition Planner')
root.configure(bg="#e0f7fa")
root.geometry("700x800")

# Calculate BMI and display BMI category
def calculate_BMI():
    try:
        weight = float(weight_var.get())
        height = float(height_var.get()) / 100  # Convert height to meters
        bmi = weight / (height ** 2)
        
        # Set BMI category
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"
        
        bmi_result.set(f"BMI: {bmi:.1f} ({category})")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for weight and height.")

# Function to calculate BMR and generate a meal plan
def calculate_BMR_and_meal_plan():
    try:
        weight = float(weight_var.get())
        height = float(height_var.get())
        age = int(age_var.get())
        gender = gender_listbox.get(ACTIVE)
        activity = activity_listbox.get(ACTIVE)

        # BMR Calculation
        if gender == 'Male':
            bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
        else:
            bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

        # Activity level multiplier
        activity_multiplier = {
            'Sedentary': 1.2,
            'Lightly active': 1.375,
            'Moderately active': 1.55,
            'Very active': 1.725,
            'Super active': 1.9
        }
        
        total_calories = bmr * activity_multiplier.get(activity, 1.2)
        
        # Generate meal plan based on calories
        meal_plan.set(f"Your daily caloric needs: {int(total_calories)} kcal\n\n"
                      f"Suggested Meal Plan:\n"
                      f"Breakfast: {protein_options[randint(0, 4)]} + {fruit_options[randint(0, 4)]}\n"
                      f"Lunch: {protein_options[randint(0, 4)]} + {vegetable_options[0]} + {grain_options[randint(0, 4)]}\n"
                      f"Snack: {snack_options[randint(0, 4)]} + {vegetable_options[0]}\n"
                      f"Dinner: {protein_options[randint(0, 4)]} + {vegetable_options[0]} + {grain_options[randint(0, 4)]}\n"
                      f"Evening Snack: {fruit_options[randint(0, 4)]}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for weight, height, and age.")

# Food options for meal plan
protein_options = ['Yogurt (1 cup)', 'Cooked meat (3 oz)', 'Cooked fish (4 oz)', '1 whole egg + 4 egg whites', 'Tofu (5 oz)']
fruit_options = ['Berries (80g)', 'Apple', 'Orange', 'Banana', 'Dried Fruits (Handful)', 'Fruit Juice (125ml)']
vegetable_options = ['Mixed vegetables (80g)']
grain_options = ['Cooked Grain (150g)', 'Whole Grain Bread (1 slice)', 'Half Large Potato (75g)', 'Oats (250g)', '2 Corn Tortillas']
snack_options = ['Soy Nuts (1 oz)', 'Low-fat milk (250ml)', 'Hummus (4 tbsp)', 'Cottage cheese (125g)', 'Flavored yogurt (125g)']

# Frames and UI elements
header = Label(root, text="The Dietician - Health & Nutrition Planner", font=("Arial", 24, "bold"), bg="#00796b", fg="white")
header.pack(fill="x", pady=10)

# BMI Section
bmi_frame = LabelFrame(root, text="BMI Calculator", padx=20, pady=10, bg="#e0f7fa", font=("Arial", 14, "bold"))
bmi_frame.pack(pady=10, fill="both")

Label(bmi_frame, text="Weight (kg):", bg="#e0f7fa").grid(row=0, column=0, sticky=W)
Label(bmi_frame, text="Height (cm):", bg="#e0f7fa").grid(row=1, column=0, sticky=W)
weight_var = StringVar()
height_var = StringVar()
Entry(bmi_frame, textvariable=weight_var, width=30).grid(row=0, column=1)
Entry(bmi_frame, textvariable=height_var, width=30).grid(row=1, column=1)
Button(bmi_frame, text="Calculate BMI", command=calculate_BMI, bg="#00796b", fg="white").grid(row=2, columnspan=2, pady=10)
bmi_result = StringVar()
Label(bmi_frame, textvariable=bmi_result, bg="#e0f7fa", font=("Arial", 12, "bold")).grid(row=3, columnspan=2, pady=5)

# BMR and Meal Plan Section
meal_plan_frame = LabelFrame(root, text="Daily Caloric Needs & Meal Plan", padx=20, pady=10, bg="#e0f7fa", font=("Arial", 14, "bold"))
meal_plan_frame.pack(pady=10, fill="both")

Label(meal_plan_frame, text="Age:", bg="#e0f7fa").grid(row=0, column=0, sticky=W)
Label(meal_plan_frame, text="Gender:", bg="#e0f7fa").grid(row=1, column=0, sticky=W)
Label(meal_plan_frame, text="Activity Level:", bg="#e0f7fa").grid(row=2, column=0, sticky=W)
age_var = StringVar()
Entry(meal_plan_frame, textvariable=age_var, width=30).grid(row=0, column=1)

# Gender Listbox
gender_listbox = Listbox(meal_plan_frame, height=2, width=20)
gender_listbox.insert(1, 'Male')
gender_listbox.insert(2, 'Female')
gender_listbox.grid(row=1, column=1)

# Activity Level Listbox
activity_listbox = Listbox(meal_plan_frame, height=5, width=30)
activity_levels = ['Sedentary', 'Lightly active', 'Moderately active', 'Very active', 'Super active']
for level in activity_levels:
    activity_listbox.insert(END, level)
activity_listbox.grid(row=2, column=1)

# Calculate Button
Button(meal_plan_frame, text="Calculate BMR & Generate Meal Plan", command=calculate_BMR_and_meal_plan, bg="#00796b", fg="white").grid(row=3, columnspan=2, pady=15)

# Display Meal Plan
meal_plan = StringVar()
Label(meal_plan_frame, textvariable=meal_plan, bg="#e0f7fa", font=("Arial", 12), justify=LEFT, wraplength=500).grid(row=4, columnspan=2)

root.mainloop()
