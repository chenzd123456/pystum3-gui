import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.uix.spinner import Spinner
import threading
import stun
import json

class StunGUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = '15dp'
        self.spacing = '15dp'
        
        # 控制按钮区域 - 调整为更适合触摸的尺寸
        self.control_box = BoxLayout(size_hint=(1, None), height='80dp')
        self.start_btn = Button(
            text='Start Check NAT',
            size_hint=(0.5, 1),
            font_size='18sp'
        )
        self.start_btn.bind(on_press=self.start_stun)
        self.stop_btn = Button(
            text='Stop', 
            disabled=True,
            size_hint=(0.5, 1),
            font_size='18sp'
        )
        self.stop_btn.bind(on_press=self.stop_stun)
        self.control_box.add_widget(self.start_btn)
        self.control_box.add_widget(self.stop_btn)
        
        # 结果显示区域 - 增加字体大小和行距
        self.result_output = TextInput(
            text='STUN test results will appear here...',
            readonly=True,
            size_hint=(1, 0.6),
            font_size='16sp',
            line_height=1.5,
            background_color=(0.95, 0.95, 0.95, 1)
        )
        
        # Server configuration area - 调整为更适合移动设备
        self.config_box = BoxLayout(size_hint=(1, None), height='120dp', spacing='10dp')
        
        # Load default config
        try:
            with open('config.json') as f:
                config = json.load(f)
                default_host = config['stun_server']['host']
                default_port = str(config['stun_server']['port'])
        except (FileNotFoundError, KeyError):
            default_host = 'stun.l.google.com'
            default_port = '19302'

        # Define available STUN servers
        self.servers = config.get('stun_servers', [])
        
        # Server selection and info display - 调整为移动友好布局
        server_info_layout = BoxLayout(orientation='vertical', spacing='5dp')
        
        # Server selection row - 增加字体大小和高度
        server_row = BoxLayout(size_hint=(1, None), height='50dp')
        server_row.add_widget(Label(text='Server:', font_size='16sp'))
        self.server_spinner = Spinner(
            text='Select Server',
            values=[s['name'] for s in self.servers],
            size_hint=(0.7, 1),
            font_size='16sp'
        )
        server_row.add_widget(self.server_spinner)
        server_info_layout.add_widget(server_row)
        
        # Server info display row - 增加字体大小
        info_row = BoxLayout(size_hint=(1, None), height='50dp')
        self.host_label = Label(text='Host: ', font_size='16sp')
        self.port_label = Label(text='Port: ', font_size='16sp')
        info_row.add_widget(self.host_label)
        info_row.add_widget(self.port_label)
        server_info_layout.add_widget(info_row)
        
        # Update displayed host/port when server changes
        def update_server(instance, value):
            selected = next(s for s in self.servers 
                          if s['name'] == value)
            self.host_label.text = f'Host: {selected["host"]}'
            self.port_label.text = f'Port: {selected["port"]}'
            
        self.server_spinner.bind(text=update_server)
        # Initialize with first server
        self.server_spinner.text = self.servers[0]['name']
        update_server(self.server_spinner, self.servers[0]['name'])
        
        # Add to main config box
        self.config_box.add_widget(server_info_layout)
        
        self.add_widget(self.control_box)
        self.add_widget(self.result_output)
        self.add_widget(self.config_box)
        
        self.stun_thread = None
        self.running = False
    
    def start_stun(self, instance):
        self.running = True
        self.start_btn.disabled = True
        self.stop_btn.disabled = False
        self.result_output.text = 'Detecting NAT type and public IP...'
        
        selected = next(s for s in self.servers 
                      if s['name'] == self.server_spinner.text)
        host = selected['host']
        port = selected['port']
        
        self.stun_thread = threading.Thread(
            target=self.run_stun,
            args=(host, port),
            daemon=True
        )
        self.stun_thread.start()
    
    def stop_stun(self, instance):
        self.running = False
        if self.stun_thread and self.stun_thread.is_alive():
            # 强制终止线程
            import ctypes
            import inspect
            
            try:
                tid = ctypes.c_long(self.stun_thread.ident)
                exc = ctypes.py_object(SystemExit)
                ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, exc)
            except:
                pass
            
            self.stun_thread = None
            
        self.start_btn.disabled = False
        self.stop_btn.disabled = True
        self.result_output.text += '\nstoped!'
    
    def run_stun(self, host, port):
        try:
            nat_type, external_ip, _ = stun.get_ip_info(
                stun_host=host,
                stun_port=port
            )
            if self.running:
                result = f"""
NAT Type: {nat_type}
Public IP: {external_ip}
Server: {host}:{port}
"""
                Clock.schedule_once(lambda dt: self.show_result(result))
        except Exception as e:
            if self.running:
                error_msg = f"Detection failed: {str(e)}"
                Clock.schedule_once(lambda dt: self.show_error(error_msg))
    
    def show_result(self, text):
        self.result_output.text = text.strip()
        self.start_btn.disabled = False
        self.stop_btn.disabled = True
        self.running = False
    
    def show_error(self, error):
        self.result_output.text = error
        self.start_btn.disabled = False
        self.stop_btn.disabled = True
        self.running = False

class StunApp(App):
    def build(self):
        self.title = 'Pystun GUI'
        # 添加移动端配置
        from kivy.config import Config
        Config.set('kivy', 'exit_on_escape', '0')
        Config.set('graphics', 'resizable', '0')
        Config.set('graphics', 'width', '360')
        Config.set('graphics', 'height', '640')
        return StunGUI()

if __name__ == '__main__':
    StunApp().run()
