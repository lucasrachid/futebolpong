class Ball:
    
    def __init__(self, pygame, window) -> None:
        self.pygame = pygame
        self.window = window
        self.image = self.pygame.image.load('src\\assets\\ball.png')
        self.position_x = 620
        self.position_y = 330
        self.final_position = (self.position_x, self.position_y)
        self.window.blit(self.image, self.final_position)
        
    def move_ball(self) -> None:
        self.position_x += 1
        self.window.blit(self.image, (self.position_x, self.position_y))
        