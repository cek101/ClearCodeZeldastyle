import pygame
from zeldaFileSettings import *
from tile import Tile
from player import Player


class Level: 
    def _init_(self):

        #get the display surface
        self.display_surface = pygame.display.get_surface()
        
        # sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

        #sprite setup
        self.create_map()

    def create_map(self):
        for row_index, row in enumerate (WORLD_MAP):
            for col_index, col in enumerate (row):
                 x = col_index * Tilesize
                 y = row_index * Tilesize
                 if col == 'x':
                      Tile((x, y), [self.visible_sprites])
              #print(row_index)
              #print(row)
    
    def run(self):
        # update and draw the game
        self.visible_sprites.draw(self.display_surface)
            