import random
from math import sin, cos
from cannonball import Cannonball  # Assuming you have the Cannonball class saved as cannonball.py


class Crazyball(Cannonball):
    ## Move the crazyball with random variations if x < 400.
    def move(self, sec, grav=9.81):
        super().move(sec, grav)  # Call the original move() method from Cannonball

        # Introduce randomness in velocity if x < 400
        if self.getX() < 400:
            # Randomly adjust the velocity slightly
            self._vx += random.uniform(-1, 1)  # Small random change in vx
            self._vy += random.uniform(-1, 1)  # Small random change in vy
