#начни тут создавать приложение с умными заметfrom PyQt5.QtCore import Qt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import  (QApplication, QWidget, QPushButton, QLabel,QVBoxLayout,QHBoxLayout,QRadioButton,QMessageBox,QGroupBox,QButtonGroup,QLineEdit, QTextEdit, QListWidget, QInputDialog)
import json
app=QApplication([])
notes={'Добро пожаловать':{'текст':'Это самое лучшее приложение в мире!','теги':['добро','инструкция']}}
with open ('notes_data.json','w') as file:
    json.dump(notes, file)

notes_win=QWidget()
notes_win.setWindowTitle('Умные заметки')
notes_win.resize(900,600)
list_notes=QListWidget()
list_notes_label=QLabel('Список заметок')  
button_note_create=QPushButton('Создать заметку')
button_note_del=QPushButton('Удалить заметку')
button_note_save=QPushButton('Сохранить заметку')
list_tag=QListWidget()
list_tag_label=QLabel('Список тегов')
tag_line=QLineEdit(' ')
tag_line.setPlaceholderText('Введите тег: ')
button_tag_add=QPushButton('Добавить к заметкие')
button_tag_del=QPushButton('Открепить')
button_tag_search=QPushButton('Искать')
file_text=QTextEdit()
file_text.setText('Текст заметки')
laytout_1=QVBoxLayout()
laytout_2=QVBoxLayout()
laytout_1.addWidget(file_text)
laytout_2.addWidget(list_notes_label)
laytout_2.addWidget(list_notes)
laytout_2.addWidget(button_note_create)
laytout_2.addWidget(button_note_del)
laytout_2.addWidget(button_note_save)
laytout_2.addWidget(list_tag_label)
laytout_2.addWidget(list_tag)
laytout_2.addWidget(button_tag_add)
laytout_2.addWidget(button_tag_del)
laytout_2.addWidget(button_tag_search)
laytout_3=QHBoxLayout()
laytout_3.addLayout(laytout_1)
laytout_3.addLayout(laytout_2)
notes_win.setLayout(laytout_3)
def show_note():
    key=list_notes.selectedItems()[0].text()
    print(key)
    file_text.setText(notes[key]['текст'])
    list_tag.clear()
    list_tag.addItems(notes[key]['теги'])
list_notes.itemClicked.connect(show_note)
def add_note():
    note_name, ok=QInputDialog.getText(notes_win,"Добавить заметку", "Название заметки:")
    if ok and note_name != '':
        notes[note_name]={'текст': '', 'теги':[]}
        list_notes.addItem(note_name)
        list_tag.addItems(notes[note_name]['теги'])
        print(notes)

def del_note():
    if list_notes.selectedItems():
        key=list_notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        list_tag.clear()
        file_text.clear()
        list_notes.addItems(notes)
        with open ('notes_data.json', 'w') as file:
            json.dump(notes, file, sort_keys=True)
    else:
        print('Вы не выделили заметку')

def save_note():
    if list_notes.selectedItems():
        key=list_notes.selectedItems()[0].text()
        notes[key]['текст']=file_text.toPlainText()
       
        with open ('notes_data.json', 'w') as file:
            json.dump(notes, file, sort_keys=True)
    else:
        print('Вы не выделили заметку')

def add_tag():
    if list_notes.selectedItems():
        key=list_notes.selectedItems()[0].text()
        tag=tag_line.text()
        if not tag in notes[key]['теги']:
            notes[key]['теги'].append(tag)
        list_tag.addItem(tag)
        tag_line.clear()
        with open ('notes_data.json', 'w') as file:
            json.dump(notes, file, sort_keys=True)
    else:
        print('Вы не выделили заметку')

def del_tag():
    if list_notes.selectedItems():
        key=list_notes.selectedItems()[0].text()
        key=list_tag.text()
        notes [key]['теги'].remove(tag)
        list_tag.clear()
        list_tag.addItems(notes[key]['теги'])
        with open ('notes_data.json', 'w') as file:
            json.dump(notes, file, sort_keys=True)
    else:
        print('Вы не выделили заметку')

def search_tag():
    tag=list_tag.text()
    if button_tag_search.text()== "Искать заметки по тегу" and tag:
        notes_filtered={}
        for note in notes:
            if tag in notes [note]['теги']:
                notes_filtered[note]=notes[note]
        button_tag_search.setText('Сбросить поиск')
        list_notes.clear()
        list_tag.clear()
        list_notes.addItems(notes_filtered)
    elif button_tag_search.text()=='Сбросить  поиск':
        tag_line.clear()
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes)
        button_tag_search.setText('Искать заметку по тегу')
    else:
        pass
button_note_create.clicked.connect(add_note)
button_note_del.clicked.connect(del_note)
button_note_save.clicked.connect(save_note)
button_tag_add.clicked.connect(add_tag)
button_tag_del.clicked.connect(del_tag)
button_tag_search.clicked.connect(search_tag)
notes_win.show()
with open ('notes_data.json','r') as file:
    notes=json.load(file)
list_notes.addItems(notes)
app.exec()




