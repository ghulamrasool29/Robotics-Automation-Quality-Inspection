# Automated Quality Inspection Using OpenCV

## About the Project

This project was completed as part of my Robotics & Automation Internship.

The goal of this project is to inspect images using basic image processing techniques in OpenCV. Instead of checking images manually, the program processes the image and highlights the detected objects automatically.

The project follows a simple OpenCV pipeline and was created for learning the fundamentals of industrial image inspection.

---

## What the Program Does

- Reads images from the `input_images` folder.
- Converts each image to grayscale.
- Applies Gaussian Blur to reduce noise.
- Uses thresholding to separate objects from the background.
- Detects objects using contours.
- Draws bounding boxes around detected objects.
- Displays the inspection result.
- Saves the processed images in the `output` folder.

---

## Tools Used

- Python
- OpenCV
- NumPy
- Visual Studio Code

---

## Project Folder

```
Robotics & Automation Project 2
│
├── inspection.py
├── README.md
├── requirements.txt
│
├── input_images
│   ├── sample1.jpg
│   └── sample2.jpg
│
└── output
    ├── sample1_result.jpg
    └── sample2_result.jpg
```

---

## How to Run

1. Install the required libraries.

```bash
pip install -r requirements.txt
```

2. Run the project.

```bash
python inspection.py
```

3. The processed images will be saved automatically inside the **output** folder.

---

## Sample Output

The program displays:

- Original image
- Threshold image
- Final inspection result
- Number of detected objects
- PASS / FAIL status

---

## What I Learned

While working on this project, I learned how to:

- Read images using OpenCV
- Convert images to grayscale
- Apply Gaussian Blur
- Perform thresholding
- Detect contours
- Draw bounding boxes
- Save processed images automatically

This project also helped me understand the basic workflow of image processing used in quality inspection systems.

---

## Author

**Ghulam Rasool**

Robotics & Automation Internship Project
