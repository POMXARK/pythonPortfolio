from kivy.app import App
from kivy.uix.slider import Slider
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import NumericProperty
import kivy
kivy.require('1.10.0')


class Container(BoxLayout):

    slider_val = NumericProperty(0)

    def __init__(self, *args, **kwargs):
        super(Container, self).__init__(*args, **kwargs)
        self.orientation = 'vertical'

        slide = Slider(min=-100, max=100, value=0)
        slide.fbind('value', self.on_slider_val)

        self.label = Label(text=str(self.slider_val))

        self.add_widget(slide)
        self.add_widget(self.label)

    def on_slider_val(self, instance, val):
        self.label.text = str(val)


class app(App):

    def build(self):
        return Container()


app().run()