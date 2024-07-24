import cv2
import mediapipe as mp
import pyautogui

cam = cv2.VideoCapture(0)
screen_w, screen_h = pyautogui.size()
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)

while True:
    isSuccess, frame = cam.read()
    if not isSuccess:
        print('ERROR: Webcam not found.')
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape

    if landmark_points:
        landmarks = landmark_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
            if id == 1:
                screen_x = int(landmark.x * screen_w)
                screen_y = int(landmark.y * screen_h)
                pyautogui.moveTo(screen_x, screen_y)

        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
        if (left[0].y - left[1].y) < 0.007:
            pyautogui.click()
            pyautogui.sleep(1)

    cv2.imshow('WebCam', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
