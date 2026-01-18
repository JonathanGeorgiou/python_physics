import matplotlib.pyplot as plt

from data.bodies import earth, sun
from physics.orbital_mechanics import calculate_orbit

def plot_earth_orbit():
    x_coords, y_coords = calculate_orbit(body1=earth, body2=sun, total_time=365 * 24, time_step=3600)
    plt.plot(x_coords, y_coords, label="Earth Orbit")
    plt.scatter(0, 0, color="yellow", label="Sun")
    plt.gca().set_aspect("equal")
    plt.show()

def main():
  pass

if __name__ == "__main__":
    main()


