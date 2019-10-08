from FrameProcessing.ShapeItem import ShapeItem
import math


class MapFrameItem(ShapeItem):
    def __init__(self, shape_type, longitude, latitude, order=1, fill_color=(255, 0, 0, 255),
                 outline_fill=(255, 0, 0, 255), outline_width=0, decay_timer=1,
                 percentage=0.001):
        super().__init__(shape_type, 0, 0, 0, 0, order, fill_color, outline_fill, outline_width)
        self.percentage = percentage
        self.longitude = longitude
        self.latitude = latitude
        self.decay_timer = decay_timer

    @property
    def percentage(self):
        return self.__percentage

    @percentage.setter
    def percentage(self, percentage):
        if percentage > 1:
            percentage = 1
        elif percentage < 0:
            percentage = 0
        self.__percentage = percentage

    @property
    def longitude(self):
        return self.__longitude

    @longitude.setter
    def longitude(self, longitude):
        # This bizarre code down calculates in case longitude is above 180 the position if it wraps around
        # falls into that location which is (longitude + 180) modulo 360 minus 180.
        longitude = ((longitude + 180) % 360) - 180
        self.__longitude = longitude

    @property
    def latitude(self):
        return self.__latitude

    @latitude.setter
    def latitude(self, latitude):
        if latitude > 90:
            latitude = 90
        elif latitude < -90:
            latitude = -90

        self.__latitude = latitude

    @property
    def decay_timer(self):
        return self.__decay_timer

    @decay_timer.setter
    def decay_timer(self, decay_timer):
        self.__decay_timer = decay_timer

    def decay(self):
        self.decay_timer -= 1

    def calculate_position(self, image_width, image_height):
        self.x = math.floor((image_width / 360) * (180 + self.longitude))
        self.y = math.floor((image_height / 180) * (90 - self.latitude))

    def calculate_size(self, image_width, image_height):
        self.width = ((image_width * image_height) * (self.percentage ** 2)) / 2
        self.height = self.width

    def render(self, image):
        self.calculate_position(image.width, image.height)
        self.calculate_size(image.width, image.height)
        super().render(image)
