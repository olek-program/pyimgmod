import png


class Image:
    def __init__(self, filename):
        self.filename = filename
        self.width = 0
        self.height = 0
        self.pixels = []

    def new(self, width, height, red=0, green=0, blue=0):
        self.width = width
        self.height = height

        color = (red, green, blue)
        self.pixels = [[color] * width for _ in range(height)]

    def save(self):
        with open(self.filename, 'wb') as f:
            writer = png.Writer(self.width, self.height, alpha=False)
            writer.write(f, self.pixels)
