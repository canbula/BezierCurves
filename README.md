# BezierCurves
Python code to generate 2d Bezier Curves.

## Import
from BezierCurve import *

## Initialize
bezier_curve = BezierCurve(100) # 100 steps between t=0 and t=100

bezier_curve.add_point(0, 0) # Add points

bezier_curve.add_point(0, 1)

bezier_curve.add_point(1, 0)

## Generate Curve
curve = bezier_curve.curve() # Method returns with a numpy array

## Get the Points (Optional)
points = bezier_curve.points() # Method returns with a numpy array
