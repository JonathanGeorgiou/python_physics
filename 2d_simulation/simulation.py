import sys
import pygame

from config import WIDTH, HEIGHT, FPS, SCALE

from data.bodies import earth, sun
from physics.orbital_mechanics import calculate_orbital_acceleration, update_orbital_velocity, update_orbital_position



# Set up game window with default values
def setup_screen() -> pygame.Surface:
    pygame.init()
    pygame.display.set_caption("Orbital Simulation")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    return screen

# Fill screen with static elements (background, sun)
def fill_screen(screen: pygame.Surface) -> None:
    screen.fill((0, 0, 0))

def draw_orbit_trail(screen: pygame.Surface, trail: list[tuple[float, float]], trail_length: int, orbital_position: tuple[float, float]):
    # Add to trail and keep only the last 100
    trail.append(orbital_position)
    if len(trail) > trail_length:
        trail.pop(0)

    # Draw trail
    for point in trail:
        pygame.draw.circle(screen, (200, 200, 200), (int(point[0]), int(point[1])), 1)

def main():
    screen = setup_screen()
    clock = pygame.time.Clock()
    trail = []

    # Using a large dt for the simulation
    # (e.g. 1 day per second of real time
    sim_dt = 24 * 3600 / FPS

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        fill_screen(screen)
        # Draw Sun (at centre)
        pygame.draw.circle(screen, (255, 255, 0), (WIDTH // 2, HEIGHT // 2), 15)
        update_orbital_velocity(earth, calculate_orbital_acceleration(earth, sun), sim_dt)
        update_orbital_position(earth, earth.velocity, sim_dt)

        # Calculate Earth pixels
        px = WIDTH//2 + earth.position.x * SCALE
        py = HEIGHT//2 + earth.position.y * SCALE

        # Draw orbit trail
        draw_orbit_trail(screen, trail, 1000, (px, py))

        # Draw Earth
        pygame.draw.circle(screen, (100, 149, 237), (int(px), int(py)), 5)  # Nice blue color

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
