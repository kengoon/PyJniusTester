import io
import sys
import threading

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.codeinput import CodeInput
from kivy import platform
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import OptionProperty, ColorProperty, BooleanProperty
from kivy.uix.popup import Popup
from kivymd.app import MDApp
from kivymd.uix.button import MDTextButton
from kivymd.uix.textfield import MDTextField
from kivy.utils import get_color_from_hex
from kivy.uix.label import Label
from traceback import format_exc
from kivy.clock import Clock
from datetime import datetime
from os.path import join

from client import SharedCode

if platform == "android":

    from androidstorage4kivy import SharedStorage, Chooser
    from android.runnable import run_on_ui_thread
    from android import cast, autoclass, api_version, mActivity
    activity = autoclass('org.kivy.android.PythonActivity').mActivity
    AndroidString = autoclass('java.lang.String')
    Toast = autoclass('android.widget.Toast')

    @run_on_ui_thread
    def toast(chars):
        Toast.makeText(activity,cast('java.lang.CharSequence', AndroidString(chars)),
            Toast.LENGTH_LONG
        ).show()
    
    def get_app_name():
        ''' 
        get the title of the application (defined in spec file)
        '''
        context = mActivity.getApplicationContext()
        appinfo = context.getApplicationInfo()
        if appinfo.labelRes:
            name = context.getString(appinfo.labelRes)
        else:
            name = appinfo.nonLocalizedLabel.toString()
        return name

Window.softinput_mode = "below_target"
kv = """
#<KvLang>
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
        MyCodeInput:
            id: code
            text: app.sample_code
            background_color: app.light_background
            foreground_color: app.light_foreground
            size_hint_y: None
            input_type: "text"
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
            color: '#cccccc'
    BoxLayout:
        size_hint_y: 0.1
        Button:
            text: 'Run'
            text_size: self.width, None
            halign: 'center'
            background_normal: ''
            bold: True
            background_color: '#00AA66'
            on_release: 
                app.run_code(code.text, error)
        Button
            text: "Change color"
            text_size: self.width, None
            halign: 'center'
            on_release: 
                app.color_mode = "Dark" if app.color_mode == "Light" else "Light"
        Button:
            text: "Open"
            text_size: self.width, None
            halign: 'center'
            on_release: 
                app.laoding_without_adding = True
                app.open_file()
        Button:
            text: "Add"
            text_size: self.width, None
            halign: 'center'
            on_release: 
                app.laoding_without_adding = False
                app.open_file()
        Button:
            text: "Save"
            text_size: self.width, None
            halign: 'center'
            on_release: 
                app.save_file()
        Button:
            text: "Connect to pc"
            text_size: self.width, None
            halign: 'center'
            on_release:
                app.connection_dialog()
        
#</KvLang>
"""
class MyCodeInput(CodeInput):
        
    def on_triple_tap(self):
        self.focus = True
        Clock.schedule_once(lambda dt: self.select_all())

class ConnectionBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        host_input = MDTextField(mode="rectangle", hint_text="Ip address")
        port_input = MDTextField(mode="rectangle", hint_text="Port")
        self.add_widget(host_input)
        self.add_widget(port_input)

        sub_container = BoxLayout(orientation='horizontal')
        accept_button = MDTextButton(text="Accept", color='blue', on_release=lambda x: threading.Thread(
            target=lambda: TesterApp.rewire_data(host=host_input.text, port=port_input.text)
        ).start())
        sub_container.add_widget(accept_button)
        self.add_widget(sub_container)


class PyjniusTester(MDApp):
    color_mode = OptionProperty("Light", options=["Light", "Dark"])
    light_background = ColorProperty("#e6e6e6")
    dark_background = ColorProperty('#262626')
    light_foreground = ColorProperty('#111111')
    dark_foreground = ColorProperty('#eeeeee')
    laoding_without_adding = BooleanProperty(True)

    sample_code = """from android import autoclass, cast
from android.runnable import run_on_ui_thread
Build = autoclass("android.os.Build")
AndroidString = autoclass('java.lang.String')
VERSION = autoclass("android.os.Build$VERSION")
Device = Build.MANUFACTURER
version = int(VERSION.RELEASE[:])
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

    def connection_dialog(self):
        connection_dialog = Popup(title='Test popup', size_hint_y = 0.5, content=ConnectionBox())
        connection_dialog.open()

    def update_code(self, operator):
        self.root.ids['code'].text = operator.get_data()

    def rewire_data(self, host, port):
        operator = SharedCode(host, port)
        print("in")
        while True:
            operator.data_pull()
            Clock.schedule_once(lambda x: self.update_code(operator), 0.1)



    def open_file(self):
        '''
        Calls Android Chooser to pick a file and then chooser_callback
        '''
        if platform == "android":
            Chooser(lambda files: self.chooser_callback(files[0])).choose_content()

    def chooser_callback(self,uri):
        reading = ""
        '''
        Using chooser from androidstorage4kivy to read file content.
        Limits : Can retrieve only txt file, sure there is a way to
        retrieve others extension files
        '''
        try:
            ss = SharedStorage()
            # copy to private cache
            path = ss.copy_from_shared(uri[0])
            
            #read content from cache
            with open(path,'r',encoding = 'utf-8') as fread:
                reading = fread.read()

            #Clock is needed otherwise throw thread error
            Clock.schedule_once(lambda dt: self.populate_label(reading))

        except (FileNotFoundError, UnicodeError) as e:
            toast(f"1.cannot open file path : {str(path)}  because : {str(e)}")

    def populate_label(self,reading):

        if self.laoding_without_adding:
            self.root.ids.code.text = reading
        else:
            self.root.ids.code.text += "\n" + reading

    def save_file(self):
        '''
        Here the saving process could be optimize with 
        a Chooser and a popup to enter the filename
        '''

        if platform == "android":
            # 1. save file to private storage:
            time = datetime.now().strftime("%d_%m_%d_%H_%M_%S")
            file_name = "jnius_code_"+ time +".txt"
            with open(join(".",file_name),'w',encoding= 'utf-8') as fwrite:
                fwrite.write(self.root.ids.code.text)

            #2. Copy the filename to sharedstorage in "Documents/appnamefolder/"
            ss = SharedStorage()
            shared = ss.copy_to_shared(file_name) #

            #3. toast the saving path
            app_name = get_app_name()
            toast(f"File saved to Documents/{app_name}/{file_name}")
            
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
TesterApp = PyjniusTester()
TesterApp.run()
