from os import stat
from tkinter import *

class Window:
    
    def __init__(self, width, height, title):
        self.window = Tk() 
        self.window.geometry(f'{width}x{height}')
        self.title = title
        self.window.title(title)
        self.enter_state = ''
        self.state_name = ''
    
    def display(self):
        self.window.mainloop()
    
    def submit(self):
        self.state_name = self.enter_state.get().upper()
        self.window.destroy()
        
    def create_submit_page(self):
        header = Label(
            self.window, 
            text='Endangered Species\nIn Your State', 
            font=('MV Boli', 30, 'bold'), 
            fg='#046e0d'
        )
        header.place(x=10, y=10)
        header.pack()

        desc = Label(
            self.window, 
            text='This program will give you information\nabout the 10 most endangered species in your state.', 
            font=('Arial', 20, 'bold')
        )
        desc.place(x=10, y=30)
        desc.pack()

        entry_header = Label(
            self.window, 
            text='Enter your state\'s ABBREVIATION below\n(ex. NJ)', 
            font=('MV Boli', '20', 'bold')
        )
        entry_header.place(x=10, y=60)
        entry_header.pack()

        self.enter_state = Entry(
            self.window,
            font=('Arial', 40) 
        )
        self.enter_state.place(x=10, y=70)
        self.enter_state.pack(side=LEFT)

        submit_button = Button(
            self.window,
            text='Submit',
            font=('Arial', 12, 'bold'),
            command=self.submit,
            height=3,
            width=10
        )
        submit_button.place(x=60)
        submit_button.pack(side=RIGHT)
    
    def create_info_page(self, scraper):
        words = self.title.split(' ')
        state_header = Label(
            self.window,
            text=f'Information for {words[2]}',
            font=('MV Boli', 25, 'bold'),
            fg='#046e0d'
        )
        state_header.pack()
        column_headers = Label(
            self.window,
            text='Scientific Name\t\tCommon Name\t\tStatus',
            font=('Arial', 18, 'bold')
        )
        column_headers.place(y=100)
        column_headers.pack()

        s_names_txt = '\n'.join(scraper.get_col('scientific'))
        c_names_txt = '\n'.join(scraper.get_col('common'))
        status_txt = '\n'.join(scraper.get_col('status'))

        scientific_names = Label(
            self.window,
            text=s_names_txt,
            font=('Arial', 13, 'bold')
        )
        scientific_names.place(x=40, y=80)
        common_names = Label(
            self.window,
            text=c_names_txt,
            font=('Arial', 13, 'bold')
        )
        common_names.place(x=400, y=80)
        statuses = Label(
            self.window,
            text=status_txt,
            font=('Arial', 13, 'bold')
        )
        statuses.place(x=750, y=80)


 
