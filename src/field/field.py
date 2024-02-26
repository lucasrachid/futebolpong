class Field:
    
    def __init__(self, pygame, window) -> None:
        self.pygame = pygame
        self.window = window
        self.image = self.pygame.image.load('src\\assets\\field.png')
        self.position_x = 0
        self.position_y = 0
        self.final_position = (self.position_x, self.position_y)
        self.window.blit(self.image, self.final_position)
        
    def draw_field(self) -> None:
        self.window.blit(self.image, self.final_position)