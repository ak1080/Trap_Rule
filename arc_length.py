import numpy as np

def calculate_arc_length(a, b, num_slices):
    def my_func(x):
        # Can make this any function I want.
        return x**2 - 0.4*x
    # Most important part is setting up the list of x points using linspace.
    num_points = num_slices +1
    x_points = np.linspace(a,b,num_points)
    # Get the slice width
    delta_x = (b-a)/num_slices

    arc_length = 0
    for i in range(0, num_slices):
        # Pythagorean theorem for calculating each element ds along the path.
        arc_length += ((my_func(x_points[i]) - my_func(x_points[i+1]))**2 + delta_x**2)**0.5

    print(f"Arc length is {arc_length:.2f}")

calculate_arc_length(a=0, b=10, num_slices=10)