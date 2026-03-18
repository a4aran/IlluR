from typing import Callable

from Illu.Settings.FrameData import FrameData


class DeltaTimer:
    def __init__(self, time: float):
        self._time = time
        self._countdown = 0
        self._running = False
        self._event = None

    def start(self):
        self._running = True

    def restart(self):
        self._countdown = 0
        self._running = True

    def stop(self):
        self._running = False

    def changeTime(self, time: float):
        self._time += time

    def changeCountdown(self, countdown: float):
        self._countdown += countdown

    def isRunning(self) -> bool:
        return self._running

    def completionPercentage(self) -> float:
        return self._countdown / self._time if self._running else 1

    def setOnCompletionEvent(self, event: Callable):
        self._event = event

    def update(self,frameData: FrameData):
        if self._running:
            self._countdown += frameData.delta_time
            if self._countdown > self._time:
                self._running = False
                self._countdown = 0
                if self._event:
                    self._event()
