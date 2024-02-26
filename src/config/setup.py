class Setup:
    
    def __init__(self, pygame) -> None:
        pygame.init()
        self.width = 1280
        self.height = 720
        self.game_name = 'Futebol Pong'
        self.window = pygame.display.set_mode((self.width, self.height))