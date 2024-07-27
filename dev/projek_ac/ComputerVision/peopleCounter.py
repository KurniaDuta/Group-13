import cv2
import numpy as np
import requests
import time

# Load YOLO
net = cv2.dnn.readNet(
    "dev/projek_ac/ComputerVision/yolov3.weights",
    "dev/projek_ac/ComputerVision/yolov3.cfg",
)
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

with open("dev/projek_ac/ComputerVision/coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Define the in-out line positions (middle of the frame)
line_position_in = 400
line_position_out = 250

person = 0
count_out = 0
previous_centers = {}

send_interval = 5
last_send_time = time.time()

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    
    height, width, channels = frame.shape

    # Detecting objects
    blob = cv2.dnn.blobFromImage(
        frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False
    )
    net.setInput(blob)
    outs = net.forward(output_layers)

    # Showing information on the screen
    class_ids = []
    confidences = []
    boxes = []
    centers = []

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5 and class_id == 0:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
                centers.append((center_x, center_y))

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    current_ids = []
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = confidences[i]
            color = (0, 255, 0)
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(
                frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2
            )

            center = centers[i]
            current_ids.append(center)

            if i in previous_centers:
                prev_center = previous_centers[i]
                if prev_center[0] < line_position_in <= center[0]:
                    person += 1
                elif prev_center[0] > line_position_out >= center[0]:
                    count_out += 1
                    person = max(person - 1, 0)

    previous_centers = {i: center for i, center in enumerate(centers)}

    # Draw in-out lines
    cv2.line(frame, (line_position_in, 0), (line_position_in, height), (255, 0, 0), 2)
    cv2.line(frame, (line_position_out, 0), (line_position_out, height), (0, 0, 255), 2)

    # Display counts
    cv2.putText(
        frame, f"In: {person}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2
    )
    cv2.putText(
        frame,
        f"Out: {count_out}",
        (10, 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2,
    )

    cv2.imshow("Image", frame)
    
    current_time = time.time()
    if current_time - last_send_time >= send_interval:
        url = "https://api-9928.vercel.app/person"
        data = {"person": person}
        try:
            response = requests.post(url, json=data)
            if response.status_code == 200:
                print(f"Successfully sent person: {person}")
            else:
                print(f"Failed to send person: {person}")
        except Exception as e:
            print(f"Error sending person: {e}")
        last_send_time = current_time

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()