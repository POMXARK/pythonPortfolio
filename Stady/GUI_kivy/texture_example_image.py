'''
В этом примере изменяются свойства текстуры и свойства
содержащего его прямоугольника. Вы должны увидеть разноцветный
текстуру с ползунками слева и снизу и кнопками на
внизу экрана. Изображение texture_example_image.png - это
отображается в прямоугольник. Ползунки изменяют количество копий
текстура (tex_coords), размер охватывающего прямоугольника (taw_height
и taw_width), а кнопки изменяют способ рендеринга текстуры, когда больше
чем одна копия находится в прямоугольнике (
texture_wrap).

'''


from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, ListProperty, StringProperty
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.app import App # окно
from kivy.base import runTouchApp
from kivy.uix.boxlayout import BoxLayout #
class TextureAccessibleWidget(Widget):

    tex_coords = ListProperty([0, 0, 1, 0, 1, 1, 0, 1])


    def texture_init(self, *args):
        self.texture = self.canvas.children[-1].texture


Builder.load_string('''
<TextureAccessibleWidget>:
    canvas:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'texture_example_image.png'
            tex_coords: root.tex_coords


<SliderWithValue@BoxLayout>:
    min: 0.0
    max: 1.0
    value: slider.value
    Slider:
        id: slider
        orientation: root.orientation
        min: root.min
        max: root.max
        value: 1.0
    Label:
        size_hint: None, None
        size: min(root.size), min(root.size)
        text: str(slider.value)[:4]

BoxLayout:
    orientation: 'vertical'
    BoxLayout:
        SliderWithValue:
            orientation: 'vertical'
            size_hint_x: None
            width: dp(40)
            min: 0
            max: 5
            value: 1
            on_value: taw.tex_coords[5] = self.value
            on_value: taw.tex_coords[7] = self.value
        SliderWithValue:
            orientation: 'vertical'
            size_hint_x: None
            width: dp(40)
            min: 0
            max: taw_container.height
            value: 0.5*taw_container.height
            on_value: taw.height = self.value
        AnchorLayout:
            id: taw_container
            anchor_x: 'left'
            anchor_y: 'bottom'
            TextureAccessibleWidget:
                id: taw
                size_hint: None, None
    BoxLayout:
        size_hint_y: None
        height: dp(80)
        BoxLayout:
            orientation: 'vertical'
            size_hint_x: None
            width: dp(80)
            Label:
                text: 'size'
                text_size: self.size
                halign: 'right'
                valign: 'middle'
            Label:
                text: 'tex_coords'
                text_size: self.size
                halign: 'left'
                valign: 'middle'
        BoxLayout:
            orientation: 'vertical'
            SliderWithValue:
                min: 0
                max: taw_container.width
                value: 0.5*taw_container.width
                on_value: taw.width = self.value
            SliderWithValue:
                min: 0.
                max: 5.
                value: 1.
                on_value: taw.tex_coords[2] = self.value
                on_value: taw.tex_coords[4] = self.value

    BoxLayout:
        size_hint_y: None
        height: dp(50)
        Label:
            text: 'texture wrap:'
            text_size: self.size
            valign: 'middle'
            halign: 'center'
        Button:
            text: 'clamp_to_edge'
            on_press: taw.texture_wrap = 'clamp_to_edge'
        Button:
            text: 'repeat'
            on_press: taw.texture_wrap = 'repeat'
        Button:
            text: 'mirrored_repeat'
            on_press: taw.texture_wrap = 'mirrored_repeat'


''')





class SmaRT_DictorApp(App): # вызывает окно приложения
    def build(self):
        bl = BoxLayout(orientation = 'vertical')
        bl.add_widget(TextureAccessibleWidget())


        return bl
        #SmaRT_DictorApp()




if __name__ == "__main__":  # Запуск приложения
    SmaRT_DictorApp().run()