import numpy as np

def move_at_angle(vect, angle, velocity):
    dir = angle_to_vector(angle)
    displacement = dir * velocity
    # return np.array(vect + displacement, dtype=object)
    return vect + displacement

def angle_to_vector(angle):
    """Returns a vector with a length of 1 for a given angle, <angle -> left, >angl -> right"""
    return np.round(np.array([np.cos(np.radians(angle+90)),np.sin(np.radians(angle+90))]), 4)
