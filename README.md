# PBRVITS_TOTAL_MANAGEMENT
 PBRVITS Application
Description
The PBRVITS Application is an interactive tool designed for educational institutions, specifically aimed at managing student data, including personal details and attendance. This application allows users to capture and store vital information such as names, ages, sections, and parent details, alongside audio recordings and images of the students. With features for voice recognition and QR code generation, the application enhances student management and attendance tracking, making it an efficient solution for schools and colleges.

Key Features
User-Friendly Interface: Built using tkinter, the application offers an intuitive interface for users to input and manage student details easily.
Branch Selection: Users can select their respective branches (AI, IoT, CSE) to organize student data effectively.
Voice Capture: Captures audio recordings of students for personal notes or attendance verification.
Image Capture: Allows users to take and store images of students using their webcam.
Data Storage: All information is saved in structured directories, making it easy to retrieve and manage student data.
QR Code Generation: Automatically generates QR codes for each student's details, enabling quick access and sharing of information.
Details Retrieval: Users can retrieve and view stored details by entering a student's name or roll number, including their audio recordings and images.
Technologies Used
Python: The primary programming language used to develop the application.
Tkinter: A GUI toolkit for creating the application's interface.
OpenCV: Used for capturing images from the webcam.
Pillow (PIL): For image handling and display.
SpeechRecognition: For capturing and processing audio input.
pyttsx3: For text-to-speech capabilities, providing vocal feedback.
qrcode: To generate QR codes for student details.
OS: For file and directory management.
How It Works
Data Directory: The application creates a designated directory (person_data) to store all student-related information, including images, audio files, and QR codes.
User Interaction: Upon launching the application, users can select their branch, enter student details, and capture voice and image data.
Data Storage: Captured information is saved in text files, and QR codes are generated for quick access to the student's data.
Retrieval: Users can retrieve details by name or roll number, displaying the student’s information along with their audio and image.
Setup and Installation
To run the PBRVITS Application locally, follow these steps:
![Screenshot 2024-10-08 102346](https://github.com/user-attachments/assets/a41b14ef-2c58-4f04-8521-ca8e0f3e161d)
![Screenshot 2024-10-08 102336](https://github.com/user-attachments/assets/50cf6e49-d0f3-439a-90b0-e55b8baf1439)
![Screenshot 2024-10-08 102330](https://github.com/user-attachments/assets/c3275bde-0f50-46ad-b2c8-a00617774457)
![Screenshot 2024-10-08 102323](https://github.com/user-attachments/assets/7fff3a4e-c2e1-4cb4-baa1-ebce9c8a8638)
![Screenshot 2024-10-08 102304](https://github.com/user-attachments/assets/f4e55628-688d-4041-8b5c-83b756855f49)
![Screenshot 2024-10-08 102502](https://github.com/user-attachments/assets/5f819fef-0c26-459d-93d9-70166c54474f)
![Screenshot 2024-10-08 102446](https://github.com/user-attachments/assets/b4f85177-3c27-4001-8207-2949c6ee8529)
![Screenshot 2024-10-08 102437](https://github.com/user-attachments/assets/50a9af64-d119-4531-8b19-8a3d6aedd656)
![Screenshot 2024-10-08 102413](https://github.com/user-attachments/assets/06b6cbfd-5660-48ea-9aed-6e61420fbc14)
![Screenshot 2024-10-08 102355](https://github.com/user-attachments/assets/563fb517-bfd8-43d5-9a03-7545f6f1a6b2)

Clone the Repository:


git clone https://github.com/yourusername/pbrvits-application.git
Navigate to the Project Directory:


cd pbrvits-application
Install Required Packages: Make sure you have Python installed, then install the required libraries:


pip install opencv-python pillow pyttsx3 speechrecognition qrcode
Run the Application: Execute the main script:


python main.py
Future Enhancements
Database Integration: Implement a database for better data management and retrieval.
Mobile Compatibility: Develop a mobile version of the application to facilitate data entry and access on-the-go.
Advanced Reporting: Include features to generate reports on student attendance and performance.
Contact
For any questions or suggestions, feel free to reach out:

Email: sandhani82@gmail.com
GitHub: sandhani60

