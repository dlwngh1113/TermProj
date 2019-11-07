from pico2d import *

class Map:
    SIZE = 50
    map_source = None
    tile_image = None

    def __init__(self, filename):
        self.tile_image = load_image('C:\\Users\\dlwng\\Desktop\\2DGP\\TermProj\\image_resources\\tile_sheet.png')
        with open(filename) as data:
            self.map_source = [[int(i) for i in line.split()] for line in data.readlines()]

    def draw(self):
        for i in range(len(self.map_source)):
            for j in range(len(self.map_source[i])):
                if self.map_source[i][j] != 0:
                    self.tile_image.clip_draw(0, self.map_source[i][j] * 32, 32, 32, (j + 0.5) * self.SIZE,
                                              (len(self.map_source) - i) * self.SIZE - self.SIZE // 2, self.SIZE, self.SIZE)
        pass