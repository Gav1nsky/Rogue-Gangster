import libtcodpy as libtcod

#Game sizes
GAME_WIDTH = 800
GAME_HEIGHT = 600
CELL_WIDTH = 32
CELL_HEIGHT = 32

#FPS LIMIT
GAME_FPS = 60

#MAP VARS
MAP_WIDTH = 20
MAP_HEIGHT = 20

#Color definitions
COLOR_BLACK = (0,0,0)
COLOR_WHITE = (255,255,255)
COLOR_GREY = (100,100,100)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)

#Game colors
COLOR_DEFAULT_BG = COLOR_GREY

#FOV SETTINGS
FOV_ALGO = libtcod.FOV_BASIC
FOV_LIGHT_WALLS = True
TORCH_RADIUS = 10

#MESSAGE DEFAULTS
NUM_MESSAGES = 4