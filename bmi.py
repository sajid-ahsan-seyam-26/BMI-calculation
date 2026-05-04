import tkinter as tk

def calculate_bmi():
    weight = float(weight_entry.get())
    height_text = height_entry.get().lower()

    # Example input: 5 feet 10 inch
    height_text = height_text.replace("feet", "")
    height_text = height_text.replace("foot", "")
    height_text = height_text.replace("inch", "")
    height_text = height_text.replace("inches", "")

    parts = height_text.split()

    feet = float(parts[0])
    inches = float(parts[1])

   
    total_inches = (feet * 12) + inches


    height_meter = total_inches * 0.0254

   
    bmi = weight / (height_meter * height_meter)
    bmi = round(bmi, 2)

    result_label.config(text=f"Your BMI is: {bmi}")

    if bmi < 18.5:
        category_label.config(text="Category: Underweight")
    elif bmi >= 18.5 and bmi < 25:
        category_label.config(text="Category: Normal Weight")
    elif bmi >= 25 and bmi < 30:
        category_label.config(text="Category: Overweight")
    else:
        category_label.config(text="Category: Obese")



window = tk.Tk()
window.title("BMI Calculator")
window.geometry("450x430")
window.config(bg="black")


title_label = tk.Label(
    window,
    text="BMI Calculator",
    font=("Arial", 22, "bold"),
    bg="black",
    fg="white"
)
title_label.pack(pady=20)


weight_label = tk.Label(
    window,
    text="Enter Weight in KG:",
    font=("Arial", 14),
    bg="black",
    fg="white"
)
weight_label.pack()


weight_entry = tk.Entry(window, font=("Arial", 14))
weight_entry.pack(pady=10)

height_label = tk.Label(
    window,
    text="Enter Height like: 5 feet 10 inch",
    font=("Arial", 14),
    bg="black",
    fg="white"
)
height_label.pack()


height_entry = tk.Entry(window, font=("Arial", 14), width=25)
height_entry.pack(pady=10)


calculate_button = tk.Button(
    window,
    text="Calculate BMI",
    font=("Arial", 14, "bold"),
    bg="white",
    fg="black",
    command=calculate_bmi
)
calculate_button.pack(pady=20)


result_label = tk.Label(
    window,
    text="",
    font=("Arial", 14),
    bg="black",
    fg="yellow"
)
result_label.pack(pady=10)


category_label = tk.Label(
    window,
    text="",
    font=("Arial", 14),
    bg="black",
    fg="lightgreen"
)
category_label.pack()


window.mainloop()