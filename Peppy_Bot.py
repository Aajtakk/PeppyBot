from os import name
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def on_yes():
    messagebox.showinfo("Response", "I'm happy to chat with you!")
    root.withdraw()  # Hide the main window
    show_gender_selection()  # Start next interaction

def on_no():
    messagebox.showinfo("Response", "Okay, have a great day!")
    root.destroy()  # Close the main window

def on_male(gender_window):
    gender_window.destroy()
    messagebox.showinfo("Response", "Hey! Handsome")
    show_name_input()

def on_female(gender_window):
    gender_window.destroy()
    messagebox.showinfo("Response", "Hey, Hey Beautiful!")
    show_name_input()

def show_gender_selection():
    gender_window = tk.Toplevel(root)  # Create a new window on top of the main window
    gender_window.title("Select Your Gender")
    gender_window.geometry("300x100")

    male_button = tk.Button(gender_window, text="Male", command=lambda: on_male(gender_window))
    male_button.pack(pady=10)

    female_button = tk.Button(gender_window, text="Female", command=lambda: on_female(gender_window))
    female_button.pack(pady=10)

def show_name_input():
    name_age_window = tk.Toplevel(root)  # Create a new window
    name_age_window.title("Name and Age Input")

    name_label = tk.Label(name_age_window, text="What is your name?")
    name_label.pack(pady=10)
    name_entry = tk.Entry(name_age_window)
    name_entry.pack(pady=10)

    age_label = tk.Label(name_age_window, text="How old are you?")
    age_label.pack(pady=10)
    age_entry = tk.Entry(name_age_window)
    age_entry.pack(pady=10)

    def on_submit():
        global user_name  # Reference the global variable

        # Save the name to the global variable
        user_name = name_entry.get()
        
        age_input = age_entry.get()

        try:
            age = int(age_input)
            if age < 0 or age > 150:
                messagebox.showinfo("Invalid Age", "That doesn't seem to be a valid age. Exiting the conversation.")
                name_age_window.destroy()
                return
            elif age < 18:
                messagebox.showinfo("Youthful Phase", f"{user_name} You are in an exciting phase of learning and growth!")
            elif age > 30:
                messagebox.showinfo("Experienced Phase", f"{user_name} are now a busy and experienced individual!")
            else:
                messagebox.showinfo("Congratulations", f"Congratulations! {user_name} are now stepping into the important journey of learning life.")

            name_age_window.destroy()
            show_color_selection()
        except ValueError:
            messagebox.showinfo("Invalid Age", "That doesn't seem to be a valid age. Exiting the conversation.")
            name_age_window.destroy()

    submit_button = tk.Button(name_age_window, text="Submit", command=on_submit)
    submit_button.pack(pady=10)
    
# Create a new color window
def show_color_selection():
    color_window = tk.Toplevel(root)  
    color_window.title("Select Your Favorite Color")
    color_window.geometry("300x300")

    label = tk.Label(color_window, text=f"{user_name} Please choose your favorite color:")
    label.pack(pady=20)

    colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange", "Black", "White"]

    def on_color_choice(color):
        messagebox.showinfo("Color Choice", f"Oh, {color} is a beautiful color {user_name}.")
        color_window.destroy()
        show_hobby_selection()

    for color in colors:
        button = tk.Button(color_window, text=color, command=lambda c=color: on_color_choice(c))
        button.pack(pady=5)

# Create a new hobby window
def show_hobby_selection():
    hobby_window = tk.Toplevel(root)  
    hobby_window.title("Free Time Activity")
    hobby_window.geometry("300x200")

    label = tk.Label(hobby_window, text=f"What do you do in your free time {user_name}?")
    label.pack(pady=10)

    hobby_var = tk.StringVar(value="Your Free Time Activity")
    hobbies = ["Reading", "Painting", "Gardening", "Gaming", "Singing", "Dancing", "Sleeping", "Travelling"]
    dropdown = ttk.OptionMenu(hobby_window, hobby_var, *["Select a hobby"] + hobbies)
    dropdown.pack(pady=10)

    def display_hobby():
        selected_hobby = hobby_var.get()
        if selected_hobby != "Your Free Time Activity":
            messagebox.showinfo("Hobby Selected", f"That's awesome! {user_name}, I wish I could join you with {selected_hobby}.")
            hobby_window.destroy()
            show_music_selection()
        else:
            messagebox.showinfo("No selection made", "Please choose what you do in your free time.")

    submit_button = tk.Button(hobby_window, text="Submit", command=display_hobby)
    submit_button.pack(pady=10)

def show_music_selection():
    music_window = tk.Toplevel(root)  # Create a new window
    music_window.title("Music Genre Selection")
    music_window.geometry("300x200")

    label = tk.Label(music_window, text=f"What kind of music do you like {user_name}?")
    label.pack(pady=10)

    music_var = tk.StringVar(value="Select a genre")
    music_genres = ["Rock", "Pop", "Jazz", "Classical", "Hip-Hop"]
    music_dropdown = ttk.OptionMenu(music_window, music_var, *["Select a genre"] + music_genres)
    music_dropdown.pack(pady=10)

    def display_music():
        selected_music = music_var.get()
        if selected_music != "Select a genre":
            messagebox.showinfo("Music Selected", f"{user_name}, I love the idea of listening to {selected_music} music.")
            music_window.destroy()
            show_week_feedback()
        else:
            messagebox.showinfo("No selection made", "Please select a music genre.")

    submit_button = tk.Button(music_window, text="Submit", command=display_music)
    submit_button.pack(pady=10)

def show_week_feedback():
    feedback_window = tk.Toplevel(root)  # Create a new window
    feedback_window.title("Your Week Feedback")
    feedback_window.geometry("300x200")

    label = tk.Label(feedback_window, text=f"{user_name} How was your week?")
    label.pack(pady=20)

    def on_feedback(choice):
        if choice == "Great":
            messagebox.showinfo("Feedback", f"{user_name} That's amazing! I'm glad to hear you had a great week!")
        elif choice == "Worst":
            messagebox.showinfo("Feedback", f"{user_name} I'm sorry to hear that. I hope next week is much better for you.")
        feedback_window.destroy()
        show_weekend_plans()  # Proceed to the next question

    great_button = tk.Button(feedback_window, text="Great", command=lambda: on_feedback("Great"))
    great_button.pack(side="left", padx=20)

    worst_button = tk.Button(feedback_window, text="Worst", command=lambda: on_feedback("Worst"))
    worst_button.pack(side="right", padx=20)

def show_weekend_plans():
    plans_window = tk.Toplevel(root)  # Create a new window
    plans_window.title("Weekend Plans")
    plans_window.geometry("300x200")

    label = tk.Label(plans_window, text=f"{user_name} Do you have any fun plans for the weekend?")
    label.pack(pady=20)

    def submit_plans(response):
        if response == "Yes":
            messagebox.showinfo("Plans", f"I hope you have a wonderful time {user_name} with your weekend plans!")
        elif response == "No":
            messagebox.showinfo("No Plans", f"No plans? That's okay too {user_name}, enjoy your relaxing weekend!")
        plans_window.destroy()
        show_travel_feedback()  # Proceed to the next question

    yes_button = tk.Button(plans_window, text="Yes", command=lambda: submit_plans("Yes"))
    yes_button.pack(side="left", padx=20)

    no_button = tk.Button(plans_window, text="No", command=lambda: submit_plans("No"))
    no_button.pack(side="right", padx=20)

# Create a new travel window
def show_travel_feedback():
    travel_window = tk.Toplevel(root)  
    travel_window.title("Travel Feedback")
    travel_window.geometry("300x200")

    label = tk.Label(travel_window, text=f"{user_name} Have you traveled anywhere exciting recently?")
    label.pack(pady=20)

   

    def submit_travel(travel):
        if travel == "Yes":
            messagebox.showinfo("Travel", f"{user_name} Traveling is always exciting! I'd love to hear more about your trip.")
        elif travel == "No":
            messagebox.showinfo("No Travel", f"No recent travels? That's fine {user_name}; home is where the heart is!")
        travel_window.destroy()
        show_thanks_message()  # Call the final thank you message
        
    yes_button = tk.Button(travel_window, text="Yes", command=lambda: submit_travel("Yes"))
    yes_button.pack(side="left", padx=20)

    no_button = tk.Button(travel_window, text="No", command=lambda: submit_travel("No"))
    no_button.pack(side="right", padx=20)
    
def show_thanks_message():
    messagebox.showinfo("Thanks!", f"Thanks for your time {user_name}, Have a great day ahead!")
    root.quit()  # Close the main window

# Create the main window
root = tk.Tk()
root.title("Welcome!")
root.geometry("300x200")

label = tk.Label(root, text="Would you like to answer a few questions?")
label.pack(pady=10)

yes_button = tk.Button(root, text="Yes", command=on_yes)
yes_button.pack(side="left", padx=20, pady=10)

no_button = tk.Button(root, text="No", command=on_no)
no_button.pack(side="right", padx=20, pady=10)

root.mainloop()