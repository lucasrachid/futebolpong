import pygame
from src.field.field import Field
from src.ball.ball import Ball
from src.player.player import Player
from src.config.setup import Setup
from pygame.locals import (
    QUIT,
    KEYDOWN,
    K_ESCAPE,
    K_UP,
    K_DOWN,
    K_s,
    K_w
)

class Game:
    
    def __init__(self) -> None:
        self.setup = Setup(pygame)
        self.is_running = True
        self.field = Field(pygame, self.setup.window)
        self.player_1 = Player(pygame, 1, self.setup.window)
        self.player_2 = Player(pygame, 2, self.setup.window)
        self.ball = Ball(pygame, self.setup.window)
        
    def update_player_position(self, event_key) -> None:
        if event_key == K_UP:
            self.player_1.move_player_up()
        
        if event_key == K_DOWN:
            self.player_1.move_player_down()
            
        if event_key == K_w:
            self.player_2.move_player_up()
            
        if event_key == K_s:
            self.player_2.move_player_down() 
            
    def run_game(self) -> None:
        while self.is_running:
            
            events = pygame.event.get() 
            for event in events:
                if event.type == QUIT:
                    self.is_running = False
                if event.type == KEYDOWN:
                    
                    if event.key == K_ESCAPE:
                        self.is_running = False
                    
                    self.update_player_position(event.key)
                    
            self.field.draw_field()  
            self.ball.move_ball()
            self.player_1.draw_player()
            self.player_2.draw_player()
            pygame.display.update()