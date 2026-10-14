from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS
import pygame
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt : float):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        angle = random.uniform(20, 50)
        split1 = self.velocity.rotate(angle)
        split2 = self.velocity.rotate(-angle)

        new_rad = self.radius - ASTEROID_MIN_RADIUS

        new1 = Asteroid(self.position.x, self.position.y, new_rad)
        new2 = Asteroid(self.position.x, self.position.y, new_rad)

        new1.velocity = split1 * 1.2
        new2.velocity = split2 * 1.2
