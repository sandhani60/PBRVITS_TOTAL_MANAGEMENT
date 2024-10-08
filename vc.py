import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import cv2
import pyttsx3
import speech_recognition as sr
import qrcode

# Create a directory to store all data
DATA_DIR = "person_data"
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Create main application window
app = tk.Tk()
app.title("Welcome to PBRVITS")

# Set background color and font
app.configure(bg="lightgray")
app.option_add("*Font", "Arial 12")

# Welcome Page
welcome_label = tk.Label(app, text="Welcome to PBRVITS!", bg="lightgray", font=("Arial", 20, "bold"))
welcome_label.pack(pady=50)

# Branch selection variables
selected_branch = tk.StringVar()

# Function to start the application
def start_application():
    welcome_label.pack_forget()  # Remove welcome message
    select_branch_page()

start_button = tk.Button(app, text="Let's Start", bg="green", fg="white", font=("Arial", 16), command=start_application)
start_button.pack(pady=20)

# Function to display branch selection page
def select_branch_page():
    branch_window = tk.Toplevel(app)
    branch_window.title("Select Branch")
    branch_window.configure(bg="lightblue")

    # Branch selection label
    branch_label = tk.Label(branch_window, text="Select Your Branch:", bg="lightblue", font=("Arial", 14))
    branch_label.pack(pady=10)

    # Function to set selected branch
    def set_selected_branch(branch):
        selected_branch.set(branch)
        branch_window.destroy()  # Close branch selection window
        details_page()

    # Buttons for branch selection
    button_ai = tk.Button(branch_window, text="AI", bg="blue", fg="white", font=("Arial", 12),
                          command=lambda: set_selected_branch("AI"))
    button_ai.pack(pady=10)

    button_iot = tk.Button(branch_window, text="IoT", bg="blue", fg="white", font=("Arial", 12),
                           command=lambda: set_selected_branch("IoT"))
    button_iot.pack(pady=10)

    button_cse = tk.Button(branch_window, text="CSE", bg="blue", fg="white", font=("Arial", 12),
                           command=lambda: set_selected_branch("CSE"))
    button_cse.pack(pady=10)

# Function to capture voice
def capture_voice():
    try:
        recognizer = sr.Recognizer()
        mic = sr.Microphone()

        with mic as source:
            print("Speak something...")
            audio = recognizer.listen(source)

        # Save audio to a file
        audio_file = os.path.join(DATA_DIR, "audio.wav")
        with open(audio_file, "wb") as f:
            f.write(audio.get_wav_data())

        return audio_file
    except Exception as e:
        messagebox.showerror("Error", f"Failed to capture voice: {e}")
        return None

# Function to capture image
def capture_image():
    try:
        camera = cv2.VideoCapture(0)
        _, frame = camera.read()
        camera.release()

        # Save image to a file
        image_file = os.path.join(DATA_DIR, "image.jpg")
        cv2.imwrite(image_file, frame)

        return image_file
    except Exception as e:
        messagebox.showerror("Error", f"Failed to capture image: {e}")
        return None

# Function to save person details along with voice and image
def save_details(name, age, section, father_name, mother_name, aadhar_number):
    try:
        branch = selected_branch.get()
        person_dir = os.path.join(DATA_DIR, branch)
        if not os.path.exists(person_dir):
            os.makedirs(person_dir)

        # Capture voice and image
        voice_file = capture_voice()
        image_file = capture_image()

        if voice_file and image_file:
            # Save details to a text file
            details_file = os.path.join(person_dir, f"{name}_details.txt")
            with open(details_file, "w") as f:
                f.write(f"Name: {name}\n")
                f.write(f"Age: {age}\n")
                f.write(f"Branch: {branch}\n")
                f.write(f"Section: {section}\n")
                f.write(f"Father's Name: {father_name}\n")
                f.write(f"Mother's Name: {mother_name}\n")
                f.write(f"Aadhar Card Number: {aadhar_number}\n")
                f.write(f"Voice File: {voice_file}\n")
                f.write(f"Image File: {image_file}\n")

            # Generate and save QR code for details
            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
            qr.add_data(details_file)
            qr.make(fit=True)

            qr_image = qr.make_image(fill_color="black", back_color="white")
            qr_image.save(os.path.join(person_dir, f"{name}_details_qr.png"))

            messagebox.showinfo("Success", "Details saved successfully!")
        else:
            messagebox.showwarning("Error", "Failed to save details. Please try again.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to display details entry page
def details_page():
    details_window = tk.Toplevel(app)
    details_window.title("Enter Details")
    details_window.configure(bg="lightgreen")

    # Entry fields
    label_name = tk.Label(details_window, text="Name:", bg="lightgreen")
    label_name.pack(pady=10)
    entry_name = tk.Entry(details_window)
    entry_name.pack(pady=5)

    label_age = tk.Label(details_window, text="Age:", bg="lightgreen")
    label_age.pack(pady=10)
    entry_age = tk.Entry(details_window)
    entry_age.pack(pady=5)

    label_section = tk.Label(details_window, text="Section:", bg="lightgreen")
    label_section.pack(pady=10)
    entry_section = tk.Entry(details_window)
    entry_section.pack(pady=5)

    label_father_name = tk.Label(details_window, text="Father's Name:", bg="lightgreen")
    label_father_name.pack(pady=10)
    entry_father_name = tk.Entry(details_window)
    entry_father_name.pack(pady=5)

    label_mother_name = tk.Label(details_window, text="Mother's Name:", bg="lightgreen")
    label_mother_name.pack(pady=10)
    entry_mother_name = tk.Entry(details_window)
    entry_mother_name.pack(pady=5)

    label_aadhar = tk.Label(details_window, text="Aadhar Card Number:", bg="lightgreen")
    label_aadhar.pack(pady=10)
    entry_aadhar = tk.Entry(details_window)
    entry_aadhar.pack(pady=5)

    # Save Button
    button_store = tk.Button(details_window, text="Save Details", bg="green", fg="white",
                             command=lambda: save_details(entry_name.get(), entry_age.get(),
                                                          entry_section.get(), entry_father_name.get(),
                                                          entry_mother_name.get(), entry_aadhar.get()))
    button_store.pack(pady=20)

    # Retrieve Button with name/roll entry field
    retrieve_frame = tk.Frame(details_window, bg="lightgreen")
    retrieve_frame.pack(pady=20)

    retrieve_label = tk.Label(retrieve_frame, text="Retrieve by Name or Roll Number:", bg="lightgreen")
    retrieve_label.pack(side=tk.LEFT)

    retrieve_entry = tk.Entry(retrieve_frame)
    retrieve_entry.pack(side=tk.LEFT, padx=10)

    button_retrieve = tk.Button(retrieve_frame, text="Retrieve", bg="blue", fg="white",
                                 command=lambda: retrieve_details(retrieve_entry.get()))
    button_retrieve.pack(side=tk.LEFT)

# Function to retrieve details and display image
def retrieve_details(name):
    try:
        if not name:
            messagebox.showwarning("Error", "Please enter a name or roll number for retrieval.")
            return

        branch = selected_branch.get()
        person_dir = os.path.join(DATA_DIR, branch)
        details_file = os.path.join(person_dir, f"{name}_details.txt")

        if os.path.exists(details_file):
            with open(details_file, "r") as f:
                details = f.readlines()
                messagebox.showinfo("Person Details", "\n".join(details))

                # Display image
                image_file = details[-1].split(": ")[1].strip()
                display_image(image_file)

                # Play voice
                voice_file = details[-2].split(": ")[1].strip()
                play_voice(voice_file)

                # Display QR code
                qr_file = os.path.join(person_dir, f"{name}_details_qr.png")
                if os.path.exists(qr_file):
                    qr_img = Image.open(qr_file)
                    qr_img.show()
                else:
                    messagebox.showwarning("Warning", "QR code not found.")
        else:
            messagebox.showwarning("Error", f"No data found for {name}.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to play voice
def play_voice(voice_file):
    try:
        if os.path.exists(voice_file):
            engine = pyttsx3.init()
            engine.say("Playing voice recording.")
            engine.runAndWait()

            os.system(f'start {voice_file}')  # Play using default system player
        else:
            messagebox.showwarning("Warning", "Voice file not found.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to play voice: {e}")

# Function to display image
def display_image(image_path):
    try:
        img = Image.open(image_path)
        img.show()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to display image: {e}")

# Run the application
app.mainloop()
