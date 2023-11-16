import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
import tkinter.ttk
import model1
import player

if __name__ == "__main__":
   root = tk()
   root.resizeable(width=False, height=False)
   player = player.Player()
   model =  model.Model1()
   app = view(root, model, player)
   root = mainloop()

class View:
     def __init__(self, root, model, player):
        self.root = root
        self.model = model
        self .player = player
        self.create_gui()

     def create_gui(self):
         self.root.title(AUDIO_PLAYER_NAME)
         self.create_tool_display()
         self.creat_butto_frame()
         self.creat_context_menu



