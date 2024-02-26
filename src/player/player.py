class Player:
    
    def __init__(self, pygame, player, window) -> None:
        self.player = player
        self.pygame = pygame
        self.window = window
        self.image_player = 'src\\assets\\player1.png'
        self.position_x = 37
        self.position_y = 285
        self.final_position = (self.position_x, self.position_y)
        
        if self.player == 2:
            self.image_player = 'src\\assets\\player2.png'
            self.position_x = 1170
            self.position_y = 285
            self.final_position = (self.position_x, self.position_y)     
                   
        self.image = self.pygame.image.load(self.image_player)
        
    def draw_player(self) -> None:
        self.window.blit(self.image, (self.position_x, self.position_y))
        
    def move_player_up(self) -> None:
        self.position_y -= 10
        self.draw_player()
        
    def move_player_down(self) -> None:
        self.position_y += 10
        self.draw_player()