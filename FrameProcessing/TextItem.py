from FrameProcessing.FrameItem import FrameItem
from PIL import ImageFont


# Direction on text don't work right now!

class TextItem(FrameItem):
    def __init__(self, text, font_path, x=0, y=0, font_size=10,
                 fill_color=(255, 255, 255, 255), spacing=0, align="center", direction="ltr"):
        super().__init__(0, 0, x, y)
        self.text = text
        self.font_size = font_size
        if font_path[-3:] == 'ttf':
            self.font = ImageFont.truetype(font_path, self.font_size)
        elif font_path[-3:] == 'otf':
            self.font = ImageFont.FreeTypeFont(font_path, self.font_size)
        self.fill_color = fill_color
        self.spacing = spacing
        self.align = align
        self.direction = direction

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text):
        self.__text = text

    @property
    def font(self):
        return self.__font

    @font.setter
    def font(self, font):
        self.__font = font

    @property
    def spacing(self):
        return self.__spacing

    @spacing.setter
    def spacing(self, spacing):
        self.__spacing = spacing

    @property
    def align(self):
        return self.__align

    @align.setter
    def align(self, align):
        self.__align = align

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction):
        self.__direction = direction

    @property
    def font_size(self):
        return self.__font_size

    @font_size.setter
    def font_size(self, font_size):
        self.__font_size = font_size

    def render(self, image):
        pass