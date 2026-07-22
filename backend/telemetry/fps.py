import time


class FPSCounter:

    def __init__(self):

        self.start = time.time()

        self.frames = 0

    def update(self):

        self.frames += 1

    def fps(self):

        elapsed = time.time() - self.start

        if elapsed == 0:

            return 0

        return self.frames / elapsed