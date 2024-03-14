import math
import random

import pygame
from src.models.player_model import Player
from src.models.utils_models import Point
from src.models.enemy_model import Enemy
from src.utils.map_variables import MAP_VARIABLES, TILES_GRID_COL_ROW
import src.utils.map_utils as map_utils
from src.helpers.resources_helper import EnemyList
from src.models.tile_model import Tile
from src.models.fps import FPS
from src.helpers.resources_helper import RESOURCES, get_scaled_image, GeneralTextures
from src.models.map_object_model import MapObject

class Map():
    _tiles_info: dict[str, Tile] = {}
    _enemies: list[Enemy] = []
    _my_player: Player = None
    _hovered_tile: Tile = None
    _tilemap = None
    _auxiliar_texts: dict[str, str] = {}
    _draw_grid = False
    _tiles_grid_col_row = TILES_GRID_COL_ROW
    
    def __init__(self):
        pass
    
    def initialize(self):
        # Set the tiles info
        for row in range(1, TILES_GRID_COL_ROW.y + 1, 1):
            for col in range(1, TILES_GRID_COL_ROW.x + 1, 1):
                tile = Tile(Point(col, row))
                tile.subscribe(self.on_tile_updated)
                self._tiles_info[self.get_tile_key(col, row)] = tile
        
        for i in range(Enemy.initial_enemies):
            available_enemies = list(EnemyList)
            enemy_name = random.choice(available_enemies).value.name
            
            # enemy_name = f"enemy_{random.randint(1, Enemy.types)}"
            random_tile = self.get_random_tile(True)
            self._enemies.append(Enemy(random_tile, enemy_name))
        
        self._my_player = Player(self.get_center_tile(), "player_1")
        
        
    # region EVENTS
    def on_tile_updated(self, tile: Tile):
        self._refresh_tilemap()
        print(f"tilemap was updated! {tile._position.x}, {tile._position.y}")        
    # endregion
        
    # region GETTERS
    def get_tile_key(self, col: int, row: int):
        return f"{col}_{row}"
    def get_tile_info(self, position: Point):
        return self._tiles_info[f"{position.x}_{position.y}"]
    def get_enemies(self):
        return self._enemies
    def get_my_player(self):
        return self._my_player
    def get_random_tile(self, validate_blocked_tiles: bool = False):
        available_keys = list(self._tiles_info.keys())
        if validate_blocked_tiles:
            available_keys = [key for key, value in self._tiles_info.items() if not value._blocked]
        random_key = random.choice(available_keys)
        return self._tiles_info[random_key]
    def get_center_tile(self):
        center_tile = Point(math.ceil(TILES_GRID_COL_ROW.x / 2), math.ceil(TILES_GRID_COL_ROW.y / 2))
        return self._tiles_info[self.get_tile_key(center_tile.x, center_tile.y)]
        
    # endregion
    
    # region SETTERS
    def set_tile_hovered(self):
        mouse_position = map_utils.get_fixed_mouse_position()
        hovered_tile_x = int(mouse_position.x / MAP_VARIABLES.tile_size.x) + 1
        hovered_tile_y = int(mouse_position.y / MAP_VARIABLES.tile_size.y) + 1
        hovered_tile = self.get_tile_info(Point(hovered_tile_x, hovered_tile_y))
        # self._auxiliar_texts["mouse_position"] = f"x: {mouse_position.x}, y: {mouse_position.y}"
        self._auxiliar_texts["hovered_tile"] = f"x: {hovered_tile._position.x}, y: {hovered_tile._position.y}"
        self._hovered_tile = hovered_tile
        
        # self._tile_hovered = 
    
    # endregion
    
    def update(self):
        FPS.set_fps()
        self.set_tile_hovered()

        for enemy in self._enemies:
            enemy.update()

        self._my_player.update()
        
    def draw(self):
        self._draw_terrain()
        
        map_objects_group = pygame.sprite.Group()
        for obj in self._get_ordered_map_objects():
            obj.draw(map_objects_group)
        
        if self._hovered_tile:
            map_objects_group.add(self._hovered_tile._sprite)
        
        for index, (key, value) in enumerate(self._auxiliar_texts.items()):
            text = MAP_VARIABLES.font.render(f"{key}: {value}", True, (255, 255, 255))
            MAP_VARIABLES.surface.blit(text, (10, 10 + index * 30))
            
        map_objects_group.draw(MAP_VARIABLES.surface)
    
    def handle_events(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                # self.on_right_click()
                pass
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                self._draw_grid = not self._draw_grid
                self._refresh_tilemap()
            if event.key == pygame.K_e:
                tile = self._tiles_info[self.get_tile_key(5, 5)]
                tile.set_blocked(not tile._blocked)
    
    def _draw_terrain(self):
        if self._tilemap is None:
            self._refresh_tilemap()
        MAP_VARIABLES.surface.blit(self._tilemap, (0, 0))
        
    def _refresh_tilemap(self):
        # Crear una nueva superficie para el tilemap
        tilemap = pygame.Surface((MAP_VARIABLES.TILES_GRID_COL_ROW.x * MAP_VARIABLES.tile_size.x, MAP_VARIABLES.TILES_GRID_COL_ROW.y * MAP_VARIABLES.tile_size.y))

        # Dibujar cada tile en la superficie del tilemap
        scale_tile = 1
        scaled_tile_size_x = MAP_VARIABLES.tile_size.x * scale_tile
        scaled_tile_size_y = MAP_VARIABLES.tile_size.y * scale_tile
        grass = get_scaled_image(GeneralTextures.GRASS.name, scaled_tile_size_x, scaled_tile_size_y)
        square = get_scaled_image(GeneralTextures.SQUARE.name, scaled_tile_size_x, scaled_tile_size_y)
        for x in range(int(MAP_VARIABLES.TILES_GRID_COL_ROW.x / scale_tile)):
            for y in range(int(MAP_VARIABLES.TILES_GRID_COL_ROW.y / scale_tile)):
                rect = pygame.Rect(x * scaled_tile_size_x, y * scaled_tile_size_y, scaled_tile_size_x, scaled_tile_size_y)
                MAP_VARIABLES.surface.blit(grass, rect)
                tilemap.blit(grass, rect)
                if self._draw_grid:
                    pygame.draw.rect(MAP_VARIABLES.surface, (0, 0, 0), rect, 1)
                    tilemap.blit(square, rect)
                tile_key = self.get_tile_key(x + 1, y + 1)
                if self._tiles_info[tile_key]._blocked:
                    pygame.draw.rect(MAP_VARIABLES.surface, (255, 0, 0), rect, 1)
                    tilemap.blit(square, rect)

        # Devolver la superficie del tilemap
        self._tilemap = tilemap
    
    def _get_ordered_map_objects(self):
        objects: list[MapObject] = []
        for enemy in self._enemies:
            objects.append(enemy)
        objects.append(self._my_player)

        ordered_list = sorted(objects, key=lambda obj: (obj._tile_in._position.y, obj._tile_in._position.x))

        return ordered_list
    
MAP = Map()
