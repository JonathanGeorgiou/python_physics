from physics.models import CelestialBody, Vector

earth = CelestialBody(
    name="Earth",
    mass=5.972e24,
    position=Vector(x=1.496e11, y=0),
    velocity=Vector(x=0, y=29780)
)

sun = CelestialBody(
    name="Sun",
    mass=1.989e30,
    position=Vector(x=0, y=0),
    velocity=Vector(x=0, y=0)
)