#takes screenshots per frame
#could be used in image proccessing
import cv2
import threading
import os

#path should change
video1_path = "paper_craft1.mp4"
video2_path = "paper_craft2.mp4"
output_directory = "screenshots"


def take_screenshot(video_path, output_file):

    cap = cv2.VideoCapture(video_path)

    if cap.isOpened():

        frame_num = 0
        while True:

            ret, frame = cap.read()
            if not ret:
                break

            screenshot_path = os.path.join(output_directory, output_file.format(frame_num))
            cv2.imwrite(screenshot_path, frame)
            print(f"{screenshot_path} kaydedildi.")
            frame_num += 1

    cap.release()


thread1 = threading.Thread(target=take_screenshot, args=(video1_path, "screenshot1_{:04d}.png"))
thread2 = threading.Thread(target=take_screenshot, args=(video2_path, "screenshot2_{:04d}.png"))


thread1.start()
thread2.start()


thread1.join()
thread2.join()

print("İşlem tamamlandı.")
