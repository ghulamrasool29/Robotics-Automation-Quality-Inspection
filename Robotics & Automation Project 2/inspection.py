import cv2
import os

# ==============================
# CONFIGURATION
# ==============================
INPUT_FOLDER = "input_images"
OUTPUT_FOLDER = "output"

EXPECTED_OBJECTS = 4
AREA_THRESHOLD = 3000

os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def preprocess_image(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    _, threshold = cv2.threshold(
        blur,
        120,
        255,
        cv2.THRESH_BINARY_INV
    )

    kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT,
        (5, 5)
    )

    cleaned = cv2.morphologyEx(
        threshold,
        cv2.MORPH_OPEN,
        kernel
    )

    return gray, cleaned


def detect_objects(image, binary):

    contours, _ = cv2.findContours(
        binary,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    detected = 0

    for contour in contours:

        area = cv2.contourArea(contour)

        if area < AREA_THRESHOLD:
            continue

        detected += 1

        x, y, w, h = cv2.boundingRect(contour)

        cv2.rectangle(
            image,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        cv2.putText(
            image,
            f"Object {detected}",
            (x, y - 20),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 0, 0),
            2
        )

    return detected


def inspect_image(image_path):

    print("=" * 50)
    print("Processing:", image_path)

    image = cv2.imread(image_path)

    if image is None:
        print("Image could not be loaded.")
        return

    original = image.copy()

    gray, threshold = preprocess_image(image)

    detected = detect_objects(image, threshold)

    brightness = gray.mean()

    if detected >0:

        status = "PASS"
        color = (0, 255, 0)

    else:

        status = "FAIL"
        color = (0, 0, 255)

    cv2.putText(
        image,
        status,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        color,
        3
    )

    cv2.putText(
        image,
        f"Detected : {detected}",
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 0),
        2
    )

    cv2.putText(
        image,
        f"Expected : {EXPECTED_OBJECTS}",
        (20, 115),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 0),
        2
    )

    filename = os.path.basename(image_path)

    name = os.path.splitext(filename)[0]

    save_path = os.path.join(
        OUTPUT_FOLDER,
        f"{name}_result.jpg"
    )
        # -----------------------------
    # Save Result Image
    # -----------------------------
    saved = cv2.imwrite(save_path, image)

    print("-" * 50)
    print("Detected Objects :", detected)
    print("Expected Objects :", EXPECTED_OBJECTS)
    print("Brightness       :", round(brightness, 2))
    print("Final Status     :", status)

    if saved:
        print("Result Saved     :", save_path)
    else:
        print("ERROR : Image could not be saved!")

    print("-" * 50)

    # Show Images
    cv2.imshow("Original Image", original)
    cv2.imshow("Threshold", threshold)
    cv2.imshow("Inspection Result", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# ===========================================
# MAIN PROGRAM
# ===========================================

def main():

    print("=" * 60)
    print(" AUTOMATED QUALITY INSPECTION SYSTEM ")
    print("=" * 60)

    if not os.path.exists(INPUT_FOLDER):
        print(f"ERROR: '{INPUT_FOLDER}' folder not found.")
        return

    image_files = []

    for file in os.listdir(INPUT_FOLDER):

        if file.lower().endswith((".jpg", ".jpeg", ".png")):
            image_files.append(file)

    if len(image_files) == 0:
        print("No images found inside input_images folder.")
        return

    print(f"Total Images Found : {len(image_files)}")

    for file in image_files:

        image_path = os.path.join(INPUT_FOLDER, file)

        inspect_image(image_path)

    print("=" * 60)
    print("Inspection Completed Successfully.")
    print(f"Processed Images are saved inside '{OUTPUT_FOLDER}' folder.")
    print("=" * 60)


if __name__ == "__main__":
    main()