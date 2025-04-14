
# Facial-Based Attendance System

A facial recognition-based attendance system using computer vision techniques and machine learning. This system can recognize faces and automatically mark attendance, making it ideal for schools, colleges, and workplaces.

## Features

- **Face Recognition**: Detects and recognizes faces using pre-trained models.
- **Attendance Marking**: Automatically marks attendance when a recognized face is detected.
- **Database Integration**: Saves the attendance data in a structured format.
- **Real-Time Processing**: Uses webcam or camera feed to capture and recognize faces in real time.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/viany7799/Facial-Attendance.git
   ```
2. Navigate to the project folder:
   ```bash
   cd Facial-Attendance
   ```
3. Create and activate a virtual environment:
   - For Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - For macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. To train the model (encode faces), run:
   ```bash
   python encode_faces.py
   ```

2. To start the attendance system, run:
   ```bash
   python mark_attendance.py
   ```

3. The system will use the webcam to capture faces, compare them with the encoded faces, and mark attendance in the system.

## Project Structure

```
Facial-Attendance/
│
├── encode_faces.py       # Script to encode the faces
├── mark_attendance.py    # Script to mark attendance using face recognition
├── requirements.txt      # List of project dependencies
├── README.md             # Project documentation
└── images/               # Folder to store face images
```

## Dependencies

- **face_recognition**: A library for recognizing and manipulating faces.
- **opencv-python**: OpenCV library for image processing.
- **numpy**: A package for scientific computing.

You can install these dependencies by running:
```bash
pip install face_recognition opencv-python numpy
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
