from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.factory import Factory
import os
import kivy
import getpass
import weakref
from kivy.app import App

from Algorithms.PedestrianDetection_Single_image import initialize_pedestrian_detection_single_image


kivy.require('2.0.0')  # replace with your current kivy version !


class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

    def getPath(self):
        return r'C:\Users\ali_a\Pictures\kivy'.format(getpass.getuser())


class Root(FloatLayout):
    loadfile = ObjectProperty(None)
    image_path = ''

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def intiate_pedestrian_detection(self):
        initialize_pedestrian_detection_single_image(self.image_path)
        self.replace_image("test.jpg")

    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            if hasattr(self.ids, 'image'):
                self.image_path = filename[0]
                self.remove_widget(self.ids.image)
                image = Image(source=filename[0])
                image.height = 400
                self.add_widget(image)
                self.make_weakref(image)
            else:
                self.image_path = filename[0]
                image = Image(source=filename[0], height=200)
                self.add_widget(image)
                self.make_weakref(image)

        self.dismiss_popup()
        self.remove_widget(self.ids.title)

    def make_weakref(self, image):
        self.ids['image'] = weakref.ref(image)

    def replace_image(self, new_image_path):
        print(new_image_path)
        new_image = Image(source=new_image_path)
        self.remove_widget(self.ids.image)
        self.add_widget(new_image)
        self.make_weakref(new_image)


class Avenue(App):
    pass


Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)
# Factory.register('SaveDialog', cls=SaveDialog)


if __name__ == '__main__':
    Avenue().run()
