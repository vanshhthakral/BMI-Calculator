# BMI-Calculator
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

root = Tk()
root.title("Body mass index Calculator")
root.geometry("650x680+300+200")
root.resizable(False, False)
root.configure(bg="#f0f1f5")

def BMI():
    h = float(Height.get())
    w = float(Weight.get())
    a = float(Age.get())

    # convert height into meter
    m = h / 100
    bmi = round(float(w / m ** 2), 1)
    label1.config(text=bmi)

    save_data(height, weight, age, bmi)

    if bmi <= 18.5:
        label2.config(text="Underweight!")
        label3.config(text="YOU have lower weight then normal body!")
    elif bmi > 18.5 and bmi <= 25:
        label2.config(text="Normal!")
        label3.config(text="IT indicates that you are healthy!")
    elif bmi > 25 and bmi <= 30:
        label2.config(text="Overweight!")
        label3.config(text="It indicates that a person is \n slightly overweight! \n A doctor may advice to lose some \n weight for health reasons!")
    else:
        label2.config(text="Obes!")
        label3.config(text="Health may be at risk , if they do not \n lose weight")


image_icon = PhotoImage(file="icon.png")
root.iconphoto(False, image_icon)

# top
top = PhotoImage(file="top.png")
top_image = Label(root, image=top, background="#f0f1f5")
top_image.place(width=650, height=100)

# bottom box
Label(root, width=100, height=32, bg="light green").pack(side=BOTTOM)

# twoboxes
box = PhotoImage(file="box.png")
Label(root, text="Weight (in kg)", font="arial 20 bold", fg="black").place(x=255, y=100)
Label(root, text="Height (in cm)", font="arial 20 bold", fg="black").place(x=35, y=100)
Label(root, text="Age", font="arial 20 bold", fg="black").place(x=475, y=100)

# scale
scale = PhotoImage(file="scale.png")
Label(root, image=scale, bg="light green").place(x=20, y=330)

########SLIDER 1 #############
current_value = tk.DoubleVar()


def get_current_value():
    return '{: .2f}'.format(current_value.get())


def slider_changed(event):
    Height.set(get_current_value())

    size = int(float(get_current_value()))
    img = Image.open("man.png")
    resized_image = img.resize((50, 10 + size))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.place(x=70, y=550 - size)
    secondimage.image = photo2


# command to change background color of scale
style = ttk.Style()
style.configure("TScale", background="white")

slider = ttk.Scale(root, from_=0, to=220, orient='horizontal', style="TScale", command=slider_changed,
                   variable=current_value)

slider.place(x=80, y=250)

###########################################


##@@@@@@@@@@@@@SLIDER 2 @@@@@@@@@@@@@

current_value2 = tk.DoubleVar()


def get_current_value2():
    return '{: .2f}'.format(current_value2.get())


def slider_changed2(event):
    Weight.set(get_current_value2())

    size = int(float(get_current_value2()))


# command to change background color of scale
style2 = ttk.Style()
style2.configure("TScale", background="white")

slider2 = ttk.Scale(root, from_=0, to=220, orient='horizontal', style="TScale", command=slider_changed2,
                    variable=current_value2)

slider2.place(x=300, y=250)

##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#slider3##
current_value3 = tk.DoubleVar()


def get_current_value3():
    return '{: .1f}'.format(current_value3.get())


def slider_changed3(event):
    Age.set(get_current_value3())

    size = int(float(get_current_value3()))


# command to change background color of scale
style3 = ttk.Style()
style3.configure("TScale", background="white")

slider3 = ttk.Scale(root, from_=0, to=220, orient='horizontal', style="TScale", command=slider_changed3,
                    variable=current_value3)

slider3.place(x=490, y=250)


# entry box
Height = StringVar()
Weight = StringVar()
Age = StringVar()
height = Entry(root, textvariable=Height, width=5, font='arial 50', bg="#fff", fg="#000", bd=0, justify=CENTER)
# TO ALIGN THE TEXT IN CENTER
height.place(x=35, y=160)
# Height.set(get_current_value)

weight = Entry(root, textvariable=Weight, width=5, font='arial 50', bg="#fff", fg="#000", bd=0, justify=CENTER)
weight.place(x=255, y=160)
# Weight.set(get_current_value2)

age = Entry(root, textvariable=Age, width=5, font='arial 50', bg="#fff", fg="#000", bd=0, justify=CENTER)
# TO ALIGN THE TEXT IN CENTER
age.place(x=475, y=160)
# Age.set(get_current_value)

# man image
secondimage = Label(root, bg="light green")
secondimage.place(x=5, y=600)

Button(root, text="View Report", width=15, height=2, font="arial 10 bold", bg="#1f6e68", fg="white", command=BMI).place(
    x=480, y=340)

label1 = Label(root, font="arial 40 bold", bg="lightgreen", fg="#fff")
label1.place(x=220, y=350)

label2 = Label(root, font="arial 20 bold", bg="lightgreen", fg="#3b3a3a")
label2.place(x=220, y=440)

label3 = Label(root, font="arial 10 bold", bg="lightgreen")
label3.place(x=220, y=500)


def DIETCHART():
    bmi = float(label1.cget("text"))
    diet_text = ""

    if bmi <= 18.5:
        diet_text = ("Breakfast: Bagel with cream cheese and avocado\n"
                     "Lunch: Grilled chicken salad with olive oil dressing\n"
                     "Dinner: Salmon, quinoa, and steamed vegetables\n"
                     "Snacks: Nuts, yogurt, or fruit smoothies")
    elif 18.5 <= bmi < 25:
        diet_text = ("Breakfast: Oatmeal with fruits and nuts\n"
                     "Lunch: Turkey sandwich with whole grain bread and a side salad\n"
                     "Dinner: Grilled fish with sweet potato and greens\n"
                     "Snacks: Carrot sticks with hummus, fresh fruits")
    elif 25 <= bmi < 30:
        diet_text = ("Breakfast: Greek yogurt with sliced strawberries and a sprinkle of flaxseed\n"
                     "Lunch: Vegetable soup with a side of whole grain rolls\n"
                     "Dinner: Chicken breast with cauliflower rice and mixed vegetables\n"
                     "Snacks: Apple slices with almond butter, air-popped popcorn")
    else:
        diet_text = ("Breakfast: Smoothie with spinach, protein powder, and a banana\n"
                     "Lunch: Salad with mixed greens, chickpeas, and light vinaigrette\n"
                     "Dinner: Baked tofu with broccoli and brown rice\n"
                     "Snacks: Cucumber slices with low-fat cheese, berries")

    # Create a new window for displaying the diet chart
    diet_chart_window = tk.Toplevel(root)
    diet_chart_window.title("Diet Chart")

    # Create a label to display the diet chart text
    label_diet_chart = Label(diet_chart_window, text=diet_text, font="Arial 12", justify=LEFT, bg="#f0f1f5")
    label_diet_chart.pack(padx=10, pady=10)





Button(root, text="View Diet Chart", width=15, height=2, font="arial 10 bold", bg="#1f6e68", fg="white",
       command=DIETCHART).place(x=480, y=400)
label4 = Label(root, font="arial 10 bold", bg="lightgreen")
label4.place(x=400, y=500)

def save_data(height, weight, bmi, age):
    data = pd.DataFrame({
        'Date': [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        'Height': [height],
        'Weight': [weight],
        'BMI': [bmi],
        'Age': [age]
    })
    try:
        df = pd.read_csv('bmi_data.csv')
        df = pd.concat([df, data], ignore_index=True)
    except FileNotFoundError:
        df = data
    df.to_csv('bmi_data.csv', index=False)

    #Function to plot graph

def plot_trends():
    try:
        df = pd.read_csv('bmi_data.csv')
        plt.figure(figsize=(10, 5))
        plt.plot(pd.to_datetime(df['Date']), df['BMI'], marker='o')
        plt.title('BMI Trends Over Time')
        plt.xlabel('Date')
        plt.ylabel('BMI')
        plt.grid(True)
        plt.show()
    except FileNotFoundError:
        print("Data file not found.")

 # Function to plot Age vs BMI
# Function to plot Age vs BMI
def plot_age_vs_bmi():
    try:
        df = pd.read_csv('bmi_data.csv')
        df['BMI'] = pd.to_numeric(df['BMI'], errors='coerce')  # Convert 'BMI' to numeric
        plt.figure(figsize=(10, 5))
        scatter = plt.scatter(df['Age'], df['BMI'], c=df['BMI'], cmap='viridis', alpha=0.6)
        plt.colorbar(scatter)
        plt.title('Age vs BMI Scatter Plot')
        plt.xlabel('Age')
        plt.ylabel('BMI')
        plt.grid(True)
        plt.show()
    except FileNotFoundError:
        print("Data file not found.")




# Button to show BMI trends
plot_button = tk.Button(root, text="Show BMI Trends", command=plot_trends, width=15, height=2, font="arial 10 bold", bg="#1f6e68", fg="white").place(x=480, y=520)

#button for age vs bmi
plot_button = tk.Button(root, text="Show Age vs BMI", command=plot_age_vs_bmi, width=15, height=2, font="arial 10 bold", bg="#1f6e68", fg="white").place(x=480, y=460)


# Set up the main window
root.mainloop()
