import cv2

# Read traffic video
cap = cv2.VideoCapture("https://github.com/AarohiSingla/Speed-detection-of-vehicles/raw/main/highway_mini.mp4?utm_source=chatgpt.com")

# Background subtractor
bg = cv2.createBackgroundSubtractorMOG2(
    history=500,
    varThreshold=50,
    detectShadows=True
)

count = 0
line_y = 300

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Resize frame
    frame = cv2.resize(frame, (800, 600))

    # Background subtraction
    mask = bg.apply(frame)

    # Remove shadows and noise
    _, mask = cv2.threshold(
        mask, 200, 255, cv2.THRESH_BINARY
    )

    kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT, (5, 5)
    )

    mask = cv2.morphologyEx(
        mask, cv2.MORPH_OPEN, kernel
    )

    mask = cv2.dilate(
        mask, kernel, iterations=2
    )

    # Find contours
    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    # Draw counting line
    cv2.line(
        frame,
        (0, line_y),
        (800, line_y),
        (0, 0, 255),
        2
    )

    # Detect vehicles
    for contour in contours:

        area = cv2.contourArea(contour)

        if area > 500:

            x, y, w, h = cv2.boundingRect(contour)

            # Draw bounding box
            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            # Vehicle center
            cx = x + w // 2
            cy = y + h // 2

            cv2.circle(
                frame,
                (cx, cy),
                5,
                (255, 0, 0),
                -1
            )

            # Count vehicle crossing the line
            if line_y - 5 < cy < line_y + 5:
                count += 1

    # Display vehicle count
    cv2.putText(
        frame,
        "Vehicle Count: " + str(count),
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 255),
        2
    )

    # Display windows
    cv2.imshow("Vehicle Detection", frame)
    cv2.imshow("Foreground Mask", mask)

    # Press Q to exit
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()