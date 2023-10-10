import cv2
import numpy as np
from pyzbar.pyzbar import decode

# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture a single frame
    ret, frame = cap.read()

    # Decode the QR code from the frame
    decoded_objects = decode(frame)
    for obj in decoded_objects:
        # Get the QR code polygon points
        points = obj.polygon
        if len(points) == 4:
            pts = [(point.x, point.y) for point in points]
            pts = np.array(pts, dtype=np.int32)
            pts = pts.reshape((-1, 1, 2))

            # Draw the bounding box
            cv2.polylines(frame, [pts], True, (0, 255, 0), 2)

        # Get the QR code data
        data = obj.data.decode("utf-8")
        print(f"QR Code Data: {data}")

    # Show the frame with the bounding box
    cv2.imshow('QR Code Scanner', frame)

    # Close the window if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and destroy all OpenCV windows
cap.release()
cv2.destroyAllWindows()
