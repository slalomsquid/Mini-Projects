import pygame, utils, constants

pygame.init()

WIDTH, HEIGHT = 800, 600
ORIGIN = (WIDTH//2, HEIGHT//2)
FPS = 60

def main(sides, size, start_angle, shapes):
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("N-Sided Shape")

    sides = sides
    size = size

    clock = pygame.time.Clock()
    timer = 0.0
    running = True

    while running:
        delta_time = clock.tick(FPS) / 1000.0

        timer += delta_time
        if timer >= 2:
            timer = 0.0
            print(clock.get_fps())

        shapes += 1

        size -= delta_time * 100

        start_angle -= delta_time * 100

        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    running = False

        SCREEN.fill(constants.BLACK)
        for idx, shape in enumerate(range(shapes)):
            SCREEN.blit(draw_shape(sides, size + idx * 100, start_angle + idx * 10), (0,0))
        pygame.display.flip()

def draw_shape(sides, size, start_angle):
    surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA, 32)
    last_point = None
    first_point = None
    for point in range(sides):
        angle = (360 / sides) * point
        # - size to make it upright
        end = utils.move_at_angle(ORIGIN, angle+start_angle, -size)
        # pygame.draw.line(SCREEN, WHITE, ORIGIN, end, 2)
        if first_point is None:
            first_point = end
        if last_point is not None:
            pygame.draw.line(surface, constants.WHITE, last_point, end, 2)
        last_point = end
    if first_point is not None and last_point is not None:
        pygame.draw.line(surface, constants.WHITE, last_point, first_point, 2)
    return surface

if __name__ == "__main__":
    sides = 3
    size = 100
    start_angle = 0
    shapes = 3
    main(sides, size, start_angle, shapes)