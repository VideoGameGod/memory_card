#Great app!


#create a memory card application
from PyQt5.QtCore import Qt
from random import shuffle
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton,  QPushButton, QLabel)
app=QApplication([])
main_win = QWidget()
main_win.move(400, 300)
main_win.resize(400, 300)
correct_answers = 0
label1 = QLabel("A very difficult question.")
gbox1 = QGroupBox("Answer options")
gbox2 = QGroupBox("Test Result:")
label2 = QLabel("Correct/Incorrect")
label3 = QLabel("The answer will be here!")
label4 = QLabel(str(correct_answers))
v4 = QVBoxLayout()
v4.addWidget(label2, alignment = Qt.AlignLeft)
v4.addWidget(label3, alignment = Qt.AlignCenter)
gbox2.setLayout(v4)
but1 = QPushButton("Answer")
main_win.current_qst = -1
RadioGroup = QButtonGroup()
b1 = QRadioButton("Option 1")
b2 = QRadioButton("Option 2")
b3 = QRadioButton("Option 3")
b4 = QRadioButton("Option 4")
RadioGroup.addButton(b1)
RadioGroup.addButton(b2)
RadioGroup.addButton(b3)
RadioGroup.addButton(b4)
answers = [b1, b2, b3, b4]
v1 = QVBoxLayout()
v2 = QVBoxLayout()
v3 = QVBoxLayout()
h1 = QHBoxLayout()
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
q1 = Question("In what year was the great fire of London?", "1666", "1999", "1062", "666")
q2 = Question("What module was used to create this?", "PyQt", "Pygame", "Python_module", "Python")
q3 = Question("How old is the Universe?", "between 10 billion and 20 billion years old", "between 10 thousand and 20 thousand years old", "between 10 million and 20 million years old", "between 10 trillion and 20 trillion years old")
q4 = Question("In what year was Moscow founded?", "1047", "1666", "147", "2012")
q5 = Question("What is Force divided by mass?", "accelaration", "distance", "power", "speed")
q6 = Question("What is the national language of Brazil?", "Portuguese", "Spanish", "Italian", "Brazilian")
q7 = Question("Which nationality does not exist?", "Smurfs", "Enets", "Chulyms", "Aleuts")
q8 = Question("What number should be called when in danger?", "999", "900", "998", "499")
q9 = Question("How many days are in a leap year?", "366", "365", "367", "364")
q10 = Question("What is 9 x 8?", "72", "81", "63", "80")
q_list = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
def show_ans():
    global correct_answers
    if but1.text() == "Answer":
        gbox1.hide()
        gbox2.show()
        but1.setText("Next question")
        if answers[0].isChecked():
            label2.setText("Correct!")
            correct_answers += 1
            label4.setText(str(correct_answers))
        else:
            label2.setText("Incorrect, sorry.")
def show_qst():
    gbox1.show()
    gbox2.hide()
    but1.setText("Answer")
    RadioGroup.setExclusive(False)
    b1.setChecked(False)
    b2.setChecked(False)
    b3.setChecked(False)
    b4.setChecked(False)
    RadioGroup.setExclusive(True)
def test():
    if but1.text() == "Finish":
        quit()
    elif but1.text() == "Answer":
        show_ans()
    else:
        next_qst()
def ask(q: Question):
    shuffle(answers)
    label1.setText(q.question)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    label3.setText(q.right_answer)
    show_qst()
def next_qst():
    if len(q_list) >= 1:
        main_win.current_qst += 1
        if main_win.current_qst >= len(q_list):
            main_win.current_qst = 0
        shuffle(q_list)
        q = q_list[main_win.current_qst]
        ask(q)
        q_list.remove(q)
    else:
        label3.setText(f"The have completed the quiz! Your score was {correct_answers}/10.")
        but1.setText("Finish")
v1.addWidget(label1)
v1.addWidget(label4, alignment = Qt.AlignRight)
v1.addWidget(gbox1)
v1.addWidget(gbox2)
v1.addWidget(but1)
main_win.setLayout(v1)
v2.addWidget(b1)
v2.addWidget(b2)
v3.addWidget(b3)
v3.addWidget(b4)
h1.addLayout(v2)
h1.addLayout(v3)
gbox1.setLayout(h1)
gbox2.hide()
but1.clicked.connect(test)
next_qst()
main_win.show()
app.exec_()
