from BezierCurve import *
import matplotlib.pyplot as plt


bezier_curve = BezierCurve(100)
bezier_curve.add_point(0.00, 0.00)
bezier_curve.add_point(0.25, 0.75)
bezier_curve.add_point(0.75, 0.05)
bezier_curve.add_point(1.00, 0.50)
curve = bezier_curve.curve()
points = bezier_curve.points()
plt.plot(curve[:, 0], curve[:, 1])
plt.plot(points[:, 0], points[:, 1], "o")
plt.show()
