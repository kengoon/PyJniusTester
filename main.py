import io
import sys

from jnius import autoclass
from kivy import platform
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import OptionProperty, ColorProperty
from kivy.utils import get_color_from_hex
from traceback import format_exc

if platform == "android":
    from android.runnable import run_on_ui_thread
    activity = autoclass('org.kivy.android.PythonActivity').mActivity


Window.softinput_mode = "below_target"
kv = """
#<KvLang>
#:import KivyLexer kivy.extras.highlight.KivyLexer
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import ScrollEffect kivy.effects.scroll.ScrollEffect
BoxLayout:
    orientation: "vertical"
    Label:
        text: "Code"
        size_hint_y: None
        height: self.texture_size[1]
        bold: True
        font_size: dp(18)
    ScrollView:
        id: sv
        effect_cls: ScrollEffect
        CodeInput:
            id: code
            text: app.sample_code
            background_color: app.light_background
            foreground_color: app.light_foreground
            keyboard_suggestions: False
            size_hint_y: None
            height: max(self.minimum_height, sv.height)
    Label:
        text: "Code Logs"
        size_hint_y: None
        height: self.texture_size[1]
        bold: True
        font_size: dp(18)
    ScrollView:
        effect_cls: ScrollEffect
        do_scroll_x: False
        size_hint_y: .3
        do_scroll_y: True
        canvas.before:
            Color:
                rgba: get_color_from_hex("3f3f3f")
            Rectangle:
                size: self.size
                pos: self.pos
        Label:
            id: error
            size_hint_y: None
            height: self.texture_size[1]
            halign: "left"
            padding: 10, 10
            text_size: self.width, None
            #background_normal: ''
            color: get_color_from_hex('cccccc')
    BoxLayout:
        size_hint_y: 0.1
        Button:
            on_release: app.run_code(code.text, error)
            background_normal: ''
            bold: True
            text: 'Run pyjinus code'
            background_color: get_color_from_hex('00AA66')
        Button:
            text: "Change editor color mode"
            on_release: app.color_mode = "Dark" if app.color_mode == "Light" else "Light"
        
#</KvLang>
"""


class PyjniusTester(App):
    color_mode = OptionProperty("Light", options=["Light", "Dark"])
    light_background = ColorProperty("#e6e6e6")
    dark_background = ColorProperty('#262626')
    light_foreground = ColorProperty('#111111')
    dark_foreground = ColorProperty('#eeeeee')

    sample_code = """from jnius import autoclass, cast
from android.runnable import run_on_ui_thread
Build = autoclass("android.os.Build")
AndroidString = autoclass('java.lang.String')
VERSION = autoclass("android.os.Build$VERSION")
Device = Build.MANUFACTURER
version = int(VERSION.RELEASE[0])
Toast = autoclass('android.widget.Toast')
activity = autoclass("org.kivy.android.PythonActivity").mActivity

@run_on_ui_thread
def toast():
    global Toast, activity, cast, AndroidString, Device, version
    Toast.makeText(
            activity,
            cast('java.lang.CharSequence', AndroidString(f'{Device} android version{version}')),
            Toast.LENGTH_LONG
        ).show()
toast()
"""

    def build(self):
        return Builder.load_string(kv)

    def on_color_mode(self, *args):
        self.root.ids.code.background_color = self.light_background if self.color_mode == "Light" else self.dark_background
        self.root.ids.code.foreground_color = self.light_foreground if self.color_mode == "Light" else self.dark_foreground

    @staticmethod
    def run_code(code, error):
        try:
            old_stdout = sys.stdout
            new_stdout = io.StringIO()
            sys.stdout = new_stdout
            exec(code)
            output = new_stdout.getvalue()
            sys.stdout = old_stdout
            error.color = [0, 1, 0, 1]
            error.text = f"{output}\n\nCode ran Successfully"
        except Exception as e:
            error.color = [1, 0, 0, 1]
            error.text = f"{str(format_exc())}\nMain error is....\n{e}"


PyjniusTester().run()
