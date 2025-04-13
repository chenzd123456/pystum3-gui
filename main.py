import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.clock import Clock
import threading
import stun

class StunGUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10
        
        # 控制按钮区域
        self.control_box = BoxLayout(size_hint=(1, 0.1))
        self.start_btn = Button(text='start check nat')
        self.start_btn.bind(on_press=self.start_stun)
        self.stop_btn = Button(text='stop', disabled=True)
        self.stop_btn.bind(on_press=self.stop_stun)
        self.control_box.add_widget(self.start_btn)
        self.control_box.add_widget(self.stop_btn)
        
        # 结果显示区域
        self.result_output = TextInput(
            text='STUN test results will appear here...',
            readonly=True,
            size_hint=(1, 0.7)
        )
        
        # 服务器配置区域
        self.config_box = BoxLayout(size_hint=(1, 0.2))
        self.config_box.add_widget(Label(text='STUN Server:'))
        self.server_input = TextInput(
            text='stun.l.google.com:19302',
            multiline=False
        )
        self.config_box.add_widget(self.server_input)
        
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
        
        server = self.server_input.text.strip()
        host, _, port = server.partition(':')
        port = int(port) if port else 3478
        
        self.stun_thread = threading.Thread(
            target=self.run_stun,
            args=(host, port),
            daemon=True
        )
        self.stun_thread.start()
    
    def stop_stun(self, instance):
        self.running = False
        self.start_btn.disabled = False
        self.stop_btn.disabled = True
        self.result_output.text += '\n检测已停止'
    
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
        self.title = 'stun GUI'
        return StunGUI()

if __name__ == '__main__':
    StunApp().run()
