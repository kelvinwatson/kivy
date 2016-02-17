__version__ = "1.0"
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label

kivy.require('1.0.6')

class KivyHowToApp(App):
  pass  
  #def build(self):
  #  btn=Button(text='Hello Android!!!')
  #  return btn
  #  #return Label(text='Hello world')
  
if __name__ == '__main__':
  KivyHowToApp().run()
