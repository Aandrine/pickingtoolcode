import customtkinter as ctk

ctk.set_appearance_mode('System')

ctk.set_default_color_theme('green')

class App(ctk.CTk):
    def __init__(self, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.title("app")
        self.geometry('200x200')

        self.nameLabel = ctk.CTkLabel(self,text='name')
        self.nameLabel.grid(row=0,column=0,padx=20,pady=20,sticky='ew')

        self.nameEntry = ctk.CTkEntry(self,placeholder_text='teja')
        self.nameEntry.grid(row=0,column=0,padx=20,pady=20,sticky='ew')
        self.entered = self.nameEntry.get()        

if __name__=='__main__':
    app = App()
    app.mainloop()

    print(app.entered)
