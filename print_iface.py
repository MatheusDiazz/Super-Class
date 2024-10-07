from matplotlib import pyplot as plt

class Print_Iface:
    ## This class handles printing and plotting for the Cannonball class.

    def __init__(self):
        # Set up plot here if needed
        self.x_points = []
        self.y_points = []

    def print_position(self, x, y):
        # Print the current position of the cannonball
        print(f"The ball is at ({x:.1f}, {y:.1f})")

    def store_position(self, x, y):
        # Store the current position of the cannonball
        self.x_points.append(x)
        self.y_points.append(y)

    def show_plot(self):
        # Plot all stored points and display the final plot
        plt.scatter(self.x_points, self.y_points)
        plt.show()
