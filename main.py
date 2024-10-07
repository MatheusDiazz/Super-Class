from math import sin, cos, radians
import random
# Import Print_Iface
from print_iface import Print_Iface

# Ask the user for the angle and velocity
def get_user_input():
    angle = radians(float(input("Enter starting angle in degrees: ")))
    velocity = float(input("Enter initial velocity: "))
    return angle, velocity

# Menu for selecting gravity and trajectory type
def main_menu():
    print("Select an option:")
    print("1. Earth Gravity")
    print("2. Moon Gravity")
    print("3. Crazy Trajectory")
    print("4. Quit")

class Cannonball:
    ## Create a new cannonball at the provided x position.
    def __init__(self, x):
        self._x = x
        self._y = 0
        self._vx = 0
        self._vy = 0
        # Create an instance of Print_Iface
        self.printer = Print_Iface()     ## Move the cannonball, using its current velocities.
    def move(self, sec, grav=9.81):
        dx = self._vx * sec
        dy = self._vy * sec
        self._vy = self._vy - grav * sec
        self._x = self._x + dx
        self._y = self._y + dy

    ## Get the current x position of the ball.
    def getX(self):
        return self._x

    ## Get the current y position of the ball.
    def getY(self):
        return self._y

    ## Shoot the cannonball.
    def shoot(self, angle, velocity, user_grav):
        self._vx = velocity * cos(angle)
        self._vy = velocity * sin(angle)
        self.move(0.1, user_grav)

        while self.getY() > 1e-14:
            # Use Print_Iface to print and store the position
            self.printer.print_position(self.getX(), self.getY())
            self.printer.store_position(self.getX(), self.getY())
            self.move(0.1, user_grav)

        # Show the final plot
        self.printer.show_plot()

# Crazyball inherits from Cannonball and adds randomness to the trajectory
class Crazyball(Cannonball):
    def __init__(self, x):
        super().__init__(x)

    def move(self, sec, grav=9.81):
        dx = self._vx * sec
        dy = self._vy * sec
        self._vy = self._vy - grav * sec

        # Adding randomness to the trajectory when the ball is under 400
        if self._x < 400:
            dx += random.uniform(-1, 1)
            dy += random.uniform(-1, 1)

        self._x = self._x + dx
        self._y = self._y + dy


# Main function to handle user selection and execute the program
if __name__ == "__main__":
    while True:
        main_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:  # Earth Gravity
            angle, velocity = get_user_input()
            c = Cannonball(0)
            c.shoot(angle, velocity, 9.81)

        elif choice == 2:  # Moon Gravity
            angle, velocity = get_user_input()
            c = Cannonball(0)
            c.shoot(angle, velocity, 1.625)

        elif choice == 3:  # Crazy Trajectory
            angle, velocity = get_user_input()
            crazy_ball = Crazyball(0)
            crazy_ball.shoot(angle, velocity, 9.81)

        elif choice == 4:  # Quit
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")
            30



