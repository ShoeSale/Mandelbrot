from dataclasses import dataclass
from PIL import Image


@dataclass
class Viewport:
    '''Class for managing the size of the output display'''

    image: Image.Image
    center: complex
    width: float

    @property
    def scale(self):
        return self.width / self.image.width

    @property
    def offset(self):
        return self.center + complex(-self.width, self.height) / 2

    @property
    def height(self):
        return self.scale * self.image.height

    def __iter__(self):
        for y in range(self.image.height):
            for x in range(self.image.width):
                yield Pixel(self, x, y)

@dataclass
class Pixel:
    '''
        Class for converting the complex matrix into a color value based
    on location on the Viewport and scale
    '''
    viewport: Viewport
    x: int
    y: int

    @property
    def color(self):
        return  self.viewport.image.getpixel((self.x, self.y))

    @color.setter
    def color(self, value):
        self.viewport.image.putpixel((self.x, self.y), value)

    def __complex__(self):
        return (
            complex(self.x, -self.y)
            * self.viewport.scale
            + self.viewport.offset
            )
