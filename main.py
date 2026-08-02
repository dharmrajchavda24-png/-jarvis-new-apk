from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class JarvisApp(App):
    def build(self):
        self.title = "JARVIS AI"
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Title Label
        self.header_label = Label(
            text="JARVIS AI Companion[span_1](start_span)[span_1](end_span)\nStatus: Online & Ready, Boss!", 
            font_size=22, 
            halign='center',
            valign='middle'
        )
        self.header_label.bind(size=self.header_label.setter('text_size'))
        layout.add_widget(self.header_label)
        
        # Command Input Box
        self.user_input = TextInput(
            hint_text='Enter your command here, Boss...', 
            size_hint=(1, 0.2),
            multiline=False
        )
        layout.add_widget(self.user_input)
        
        # Execute Button
        self.btn = Button(
            text='Run Command', 
            size_hint=(1, 0.2),
            background_color=(0.1, 0.6, 0.9, 1)
        )
        self.btn.bind(on_press=self.on_execute)
        layout.add_widget(self.btn)
        
        return layout

    def on_execute(self, instance):
        text = self.user_input.text
        if text:
            self.header_label.text = f"Command Executed:\n{text}"
        else:
            self.header_label.text = "Please enter a valid command, Boss!"

if __name__ == '__main__':
    JarvisApp().run()
  
