from pygame_utilities import mouse_visible


class Cursor:
    def __init__(self, scr, img_default=None):
        self.scr = scr
        self.img_default = img_default
        self._img = self.img_default
        self.pos = (0, 0)
        self.active = True

    @property
    def img(self):
        return self._img

    @img.setter
    def img(self, value):
        if value is not None:
            if type(value) == str:
                self._img = value
            else:
                raise ValueError('Value must be a path to an image as a string')
        else:
            self._img = value

    def set_img(self, img=None):
        if img is None:
            self.img = self.img_default
        else:
            self.img = img

    def display(self):
        if self.active:
            mouse_visible(self.scr, image=self.img, mouse_pos=self.pos)
