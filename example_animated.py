from BezierCurve import *
import time
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class AnimatedBezier(BezierCurve):
    def __init__(self, n, points):
        super().__init__(n)
        for p in points:
            super().add_point(p[0], p[1])
        self.bezier_curve = super().curve()
        self.bezier_points = super().points()
        self.i = 0
        self.t_end = 0
        self.done = False
        matplotlib.use("TkAgg")
        plt.rcParams["figure.figsize"] = [24, 18]
        self.fig, self.ax = plt.subplots()

    def start_timer(self):
        self.t_end = time.time()

    def end_timer(self):
        if self.done and time.time() - self.t_end > 3:
            quit()

    def update(self, _):
        if self.i == self.bezier_curve.shape[0] and not self.done:
            self.done = True
            self.start_timer()
        self.ax.clear()
        self.ax.set_title(f"Bezier Curve")
        self.ax.plot(self.bezier_curve[0:self.i, 0], self.bezier_curve[0:self.i, 1], linewidth=2, color="red")
        self.ax.plot(self.bezier_points[:, 0], self.bezier_points[:, 1], "o", markersize=10, color="black")
        self.i = min(self.i + 1, self.bezier_curve.shape[0])
        self.end_timer()

    def draw(self):
        _ = FuncAnimation(self.fig, self.update, interval=100)
        plt.show()


def main():
    animated_bezier = AnimatedBezier(100, [[0.0, 0.0], [0.2, 0.8], [0.8, 0.1], [1.0, 0.5]])
    animated_bezier.draw()


if __name__ == "__main__":
    main()
