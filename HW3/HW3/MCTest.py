#5MCTest.py
import time
import numpy as np
import math
from generator import LCG, SCG #import functions from generator.py
from point import Point

def test(gen, num_points=10000000): # Tests a generator by estimating the ratio of points that fall within a circle.
    start = time.time() #Start Counter

    it = iter(gen) #Iterate over generated numbers using LCG and SCG
    points = np.fromiter(it, float, count=num_points) #Get Points
    points = 2 * ((points - min(points)) / (max(points) - min(points))) - 1
    circle_count = 0
    for i in range(0, num_points):
            p = Point(points[i], points[i])
            circle_count += 1 if p.cal() <= 1 else 0

    end = time.time() #End Counter

    print(f'\nTested {num_points} points in {(end - start):.5f} seconds.')
    print(f'Result: {(math.pi / 4 - circle_count / num_points):.5f}\n')

if __name__ == '__main__':
    lcg = LCG(1, 1103515245, 12345, 2 ** 32)
    scg = SCG(1, 1103515245, 12345, 2 ** 32)
    print("LCG Test: ")
    test(lcg.nextNumbers(10000000))
    #Tested 10000000 points in 19.67703 seconds.
    #Result: 0.07810
    print("SCG Test: ")
    test(scg.nextNumbers(10000000))
    #Tested 10000000 points in 18.53158 seconds.
    #Result: 0.78540