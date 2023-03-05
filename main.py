import tkinter as tk

class Application(tk.Frame):

    def __init__(self,master):
        self.master = master
        tk.Frame.__init__(self)
        self.pack()
        self.count = 1
        self._after_id = None
        self.text_box = tk.Text(self, width=90, height=20, font=('Yu Gothic Semibold', 20), bg='#D7D9D9', fg='#3C3F40')
        self.text_box.pack()
        self.text_box.bind('<Key>', self.reset)

    def reset(self, event):
        # cancel the old job
        if self._after_id is not None:
            self.count = 1
            self.after_cancel(self._after_id)
        else:
        # create a new job
            self._after_id = self.after(1, self.timer)

    def timer(self):
        self.count += 1
        print(self.count)
        if self.count == 6:
            self.text_box.config(fg='#636566')
        elif self.count == 7:
            self.text_box.config(fg='#7d7f80')
        elif self.count == 8:
            self.text_box.config(fg='#a3a6a6')
        elif self.count == 9:
            self.text_box.config(fg='#bdbfc0')
        elif self.count == 10:
            self.text_box.delete(1.0, "end")
            self.text_box.config(fg='#3C3F40')
        self.after(1000, self.timer)

root = tk.Tk()
app = Application(root)
app.mainloop()