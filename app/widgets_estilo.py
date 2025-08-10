from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.screenmanager import Screen
from kivy.graphics import Rectangle




class EtiquetaNegra(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color = (0, 0, 0, 1)  # Texto
        
        self.font_size = 18
        
        self.halign = 'left'  # Alineación a la izquierda
        
        self.valign = 'middle'  # Alineación vertical al centro
        
        self.size_hint_y = None
        self.height = 40  # Altura fija para la etiqueta
        self.bind(size=self._actualizar_texto)
        
    def _actualizar_texto(self, *args):
        # Aseguramos que el texto se ajuste al tamaño de la etiqueta
        self.text_size = self.size



class BotonBonito(Button):
    def __init__(self, **kwargs):
        kwargs.setdefault('background_normal', '')
        kwargs.setdefault('background_down', '')
        kwargs.setdefault('background_color', (0, 0, 0, 0))  # Hacemos fondo transparente
        kwargs.setdefault('color', (0, 0, 0, 1))              # Texto blanco
        kwargs.setdefault('font_size', 16)
        kwargs.setdefault('size_hint_y', None)
        kwargs.setdefault('height', 50)
        super().__init__(**kwargs)

        with self.canvas.before:
            self.bg_color = Color(0.8, 0.6, 0.2, 1)  # amarillo mostaza
            self.bg_rect = RoundedRectangle(radius=[25], size=self.size, pos=self.pos)

        self.bind(pos=self._actualizar_fondo, size=self._actualizar_fondo)

    def _actualizar_fondo(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size
        


class FileChooserBonito(FileChooserIconView):
    def __init__(self, **kwargs):
        kwargs.setdefault('font_size', 18)
        kwargs.setdefault('background_color', (1, 1, 1, 1))
        kwargs.setdefault('color', (0, 0, 0, 1))
        super().__init__(**kwargs)
        
from kivy.uix.filechooser import FileChooserIconView

class FileChooserBonito(FileChooserIconView):
    def __init__(self, **kwargs):
        # Elimina estas dos líneas:
        # kwargs.setdefault('background_color', (1, 1, 1, 1))
        # kwargs.setdefault('color', (0, 0, 0, 1))

        kwargs.setdefault('size_hint', (1, 0.8))
        kwargs.setdefault('filters', ['*.csv', '*.xlsx'])

        super().__init__(**kwargs)

        # Estas sí están permitidas después de inicializar
        self.font_size = 18
        self.background_color = (1, 1, 1, 1)
        self.color = (0, 0, 0, 1)
        
from kivy.uix.image import Image

class PantallaAzul(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(0.1, 0.4, 0.8, 1)  # Fondo azul
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self._actualizar_rect, size=self._actualizar_rect)

        # Agregar el logo centrado
        self.logo = Image(source='logo.png', size_hint=(None, None), size=(300, 300))
        self.add_widget(self.logo)
        self.bind(size=self._centrar_logo, pos=self._centrar_logo)

    def _actualizar_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def _centrar_logo(self, *args):
        self.logo.center = self.center
        
        
        
# archivo_estilo.py (puedes cambiar el nombre si lo prefieres)

from kivy.uix.screenmanager import Screen
from kivy.graphics import Color, Rectangle

class PantallaBlanca2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(1, 1, 1, 1)  # Fondo blanco
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self._actualizar_rect, size=self._actualizar_rect)

    def _actualizar_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
        
from kivy.uix.label import Label

class EtiquetaTitulo(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color = (0, 0, 0, 1)        # Texto negro
        self.font_size = 28              # Tamaño grande para títulos
        self.halign = 'center'
        self.valign = 'middle'
        self.size_hint_y = None
        self.height = 60
        self.bind(size=self._actualizar_texto)

    def _actualizar_texto(self, *args):
        self.text_size = self.size