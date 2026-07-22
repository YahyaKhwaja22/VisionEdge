import cv2


class VideoReader:

    def __init__(self, path):

        self.cap = cv2.VideoCapture(path)

        if not self.cap.isOpened():

            raise Exception("Cannot open video.")

    def read(self):

        return self.cap.read()

    def release(self):

        self.cap.release()