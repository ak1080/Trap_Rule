import numpy as np

def calculate_integral(a, b, num_slices):
    def my_func(x):
        return 2 * x ** 2 - 4
    # Most important part is setting up the list of x points using linspace
    x_points = np.linspace(a,b,num_slices+1)
    # Get the slice width
    delta_x = (b-a)/num_slices

    sum = 0
    # Getting the elements in the x_points list besides endpoints. Recall for example range(0,5) would get you 0,1,2,3,4.
    for i in range(1, num_slices):
        sum += my_func(x_points[i])

    endpoints = 0.5*(my_func(x_points[0]) + my_func(x_points[num_slices]))
    integral = delta_x*(sum + endpoints)
    print(f"Integral is {integral:.2f}")

calculate_integral(a=2, b=12, num_slices=30)