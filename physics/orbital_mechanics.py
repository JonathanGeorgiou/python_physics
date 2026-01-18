import math

from physics.models import CelestialBody, Vector
from physics.physical_constants import G


def orbit_distance(body1: CelestialBody, body2: CelestialBody) -> float:
    return math.sqrt(
        (body1.position.x - body2.position.x) ** 2 + (body1.position.y - body2.position.y) ** 2
    )

def calculate_orbital_acceleration(body1: CelestialBody, body2: CelestialBody) -> Vector:
    r = orbit_distance(body1, body2)
    a = G * body2.mass / r ** 2
    return Vector(x = -a * body1.position.x / r,
                  y= -a * body1.position.y / r )

def update_orbital_velocity(body: CelestialBody, acceleration: Vector, time_step: float) -> None:
    body.velocity.x += acceleration.x * time_step
    body.velocity.y += acceleration.y * time_step

def update_orbital_position(body: CelestialBody, velocity: Vector, time_step: float) -> None:
    body.position.x += velocity.x * time_step
    body.position.y += velocity.y * time_step

def calculate_orbit(body1: CelestialBody, body2: CelestialBody, total_time: float, time_step: float) -> (tuple[list[float], list[float]]):
    x_coords = []
    y_coords = []
    for _ in range(total_time):
        update_orbital_velocity(body1, calculate_orbital_acceleration(body1, body2), time_step)
        update_orbital_position(body1, body1.velocity, time_step)

        x_coords.append(body1.position.x)
        y_coords.append(body1.position.y)

    return x_coords, y_coords