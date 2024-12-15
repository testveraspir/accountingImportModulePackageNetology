from datetime import datetime
from tkinter import Tk, Label
from emoji import emojize
from application.salary import calculate_salary
from application.db.people import get_employees

if __name__ == '__main__':
    cur_date = datetime.now()
    print(cur_date.strftime("Сегодня: %d число %m месяц %Y год\nВремя: %H:%M"))
    calculate_salary()
    get_employees()
    window = Tk()
    label = Label(text=emojize(":beaming_face_with_smiling_eyes:"))
    label.place(relx=0.5, rely=0.5, anchor="center")
    window.mainloop()
