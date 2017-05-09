import os
import pygame
pygame.init()

SIZE = WIDTH, HEIGHT = 720, 480
FPS = 60

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()


def load_images(path):
    """
    Loads all images in directory. The directory must only contain images.

    Args:
        path: The path to the directory to load images from.

    Returns:
        List of images.
    """
    images = []
    for file in os.listdir(path):
        image = pygame.image.load(path + os.sep + file).convert()
        images.append(image)
    return images


class Sprite:

    def __init__(self, pos, images):
        """
        Animated sprite object.

        Args:
            pos: Position of the screen where Sprite should be placed at.
            images: Images to change between.
        """
        self.rect = pygame.Rect(pos, (32, 32))
        self.images = images
        self.images_right = images
        self.images_left = [pygame.transform.flip(image, True, False) for image in images]  # Flipping every image.
        self.index = 0
        self.image = images[self.index]  # 'image' is the current image of the sprite.

        self.velocity = pygame.math.Vector2(0, 0)

        self.animation_time = 0.1
        self.current_time = 0

        self.animation_frames = 6
        self.current_frame = 0

    def update1(self, dt):
        """
        Updates the image of Sprite every 0.1 second.

        Args:
            dt: Time since last call to update.

        Returns:
            None
        """
        if self.velocity[0] > 0:  # Use the right images if sprite is moving right.
            self.images = self.images_right
        elif self.velocity[0] < 0:
            self.images = self.images_left

        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

        self.rect.move_ip(*self.velocity)

    def update2(self):
        """
        Updates the image of Sprite every 6 frame (approximately every 0.1 second if frame rate is 60).

        Returns:
            None
        """
        if self.velocity[0] > 0:  # Use the right images if sprite is moving right.
            self.images = self.images_right
        elif self.velocity[0] < 0:
            self.images = self.images_left

        self.current_frame += 1
        if self.current_frame >= self.animation_frames:
            self.current_frame = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

        self.rect.move_ip(*self.velocity)


images = load_images(path='images')  # Make sure to provide the relative or full path to the images directory.
player = Sprite(pos=(100, 100), images=images)
running = True
while running:

    dt = clock.tick(FPS) / 1000  # Amount of seconds between each loop (in seconds because we're dividing with 1000).

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.velocity[0] = 5
            elif event.key == pygame.K_LEFT:
                player.velocity[0] = -5
            elif event.key == pygame.K_DOWN:
                player.velocity[1] = 5
            elif event.key == pygame.K_UP:
                player.velocity[1] = -5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                player.velocity[0] = 0
            elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                player.velocity[1] = 0

    # Update the sprite using one of the two methods. 
    player.update1(dt)
    # player.update2()

    screen.fill(pygame.Color('black'))
    screen.blit(player.image, player.rect)
    pygame.display.update()