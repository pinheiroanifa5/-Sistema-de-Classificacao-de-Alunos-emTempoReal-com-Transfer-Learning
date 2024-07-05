import cv2


class Video(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        ret, frame = self.video.read()
        if not ret:
            return None

        ret, jpg = cv2.imencode('.jpg', frame)
        if not ret:
            return None

        return jpg.tobytes()
