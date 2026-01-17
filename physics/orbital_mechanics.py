import math

from physics.models import CelestialBody, Vector
from physics.physical_constants import G


def orbit_distance(body1: CelestialBody, body2: CelestialBody) -> float:
    return math.sqrt(
        (body1.position.x - body2.position.x) ** 2 + (body1.position.y - body2.position.y) ** 2
    )

def calculate_acceleration(body1: CelestialBody, body2: CelestialBody) -> Vector:
    r = orbit_distance(body1, body2)
    a = G * body2.mass / r ** 2
    return Vector(x = -a * body1.position.x / r,
                  y= -a * body1.position.y / r )

def calculate_orbit(body1: CelestialBody, body2: CelestialBody, total_time: int, time_step: int) -> (tuple[list[float], list[float]]):
    x_coords = []
    y_coords = []
    for _ in range(total_time):
        body1_acceleration = calculate_acceleration(body1, body2)
        body1.velocity.x += body1_acceleration.x * time_step
        body1.velocity.y += body1_acceleration.y * time_step
        body1.position.x += body1.velocity.x * time_step
        body1.position.y += body1.velocity.y * time_step
        x_coords.append(body1.position.x)
        y_coords.append(body1.position.y)

    return x_coords, y_coords