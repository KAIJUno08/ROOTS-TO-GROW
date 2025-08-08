from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from database import crear_base, registrar_usuario, validar_credenciales, obtener_usuarios

class LoginScreen(Screen): pass
class RegistroScreen(Screen): pass
class InicioAdminScreen(Screen): pass
class InicioDespachoScreen(Screen): pass
class NovedadesScreen(Screen): pass
class ControlUsuariosScreen(Screen): pass
class ResultadosScreen(Screen): pass
class PlanificacionScreen(Screen): pass
class RemisionesScreen(Screen): pass
class DespachoScreen(Screen): pass

class ControlUsuariosScreen(Screen):
    def on_pre_enter(self):
        self.ids.lista_usuarios.clear_widgets()
        for nombre, apellido, tipo in obtener_usuarios():
            self.ids.lista_usuarios.add_widget(
                MDLabel(text=f"{nombre} {apellido} - {tipo.capitalize()}", halign="center")
            )

class MainApp(MDApp):
    def build(self):
        crear_base()
        return Builder.load_file("main.kv")

    def registrar(self, nombre, apellido, usuario, clave, tipo):
        if all([nombre.strip(), apellido.strip(), usuario.strip(), clave.strip()]):
            if registrar_usuario(nombre, apellido, usuario, clave, tipo):
                self.ir_a_login()
            else:
                print("⚠️ Usuario ya existe.")
        else:
            print("⚠️ Todos los campos son obligatorios.")

    def iniciar_sesion(self, usuario, clave):
        tipo = validar_credenciales(usuario, clave)
        if tipo:
            if tipo == "admin":
                self.root.current = "admin"
            elif tipo == "despachador":
                self.root.current = "despacho"
        else:
            print("⚠️ Credenciales incorrectas.")

    def ir_a_login(self): self.root.current = "login"
    def ir_a_registro(self): self.root.current = "registro"
    def ir_a_admin(self): self.root.current = "admin"
    def ir_a_despacho(self): self.root.current = "despacho"
    def ir_a_novedades(self): self.root.current = "novedades"
    def ir_a_control(self): self.root.current = "control"
    def ir_a_resultados(self): self.root.current = "resultados"
    def ir_a_planificacion(self): self.root.current = "planificacion"
    def ir_a_remisiones(self): self.root.current = "remisiones"

MainApp().run()