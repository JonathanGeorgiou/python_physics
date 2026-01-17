from pydantic import BaseModel

class Vector(BaseModel):
    x: float
    y: float

class CelestialBody(BaseModel):
    name: str
    mass: float
    position: Vector
    velocity: Vector