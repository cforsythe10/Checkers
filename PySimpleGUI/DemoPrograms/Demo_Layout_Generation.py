import PySimpleGUI as sg

"""
    PySimpleGUI is designed & authored in Python to take full advantage the awesome Python constructs & capabilities.
    Layouts are represented as lists to PySimpleGUI. Lists are fundamental in Python and have a number of powerful
    capabilities that PySimpleGUI exploits.
       
    Many times PySimpleGUI programs can benefit from using CODE to GENERATE your layouts.  This Demo illustrates
    a number of ways of "building" a layout. Some work on 3.5 and up.  Some are basic and show concatenation of rows
    to build up a layout.  Some utilize generators.
    
    These 8 "Constructs" or Design Patterns demonstrate numerous ways of "generating" or building your layouts
    0 - A simple list comprehension to build a row of buttons
    1 - A simple list comprehension to build a column of buttons
    2 - Concatenation of rows within a layout
    3 - Concatenation of 2 complete layouts [[ ]] + [[ ]] = [[ ]]
    4 - Concatenation of elements to form a single row [ [] + [] + [] ] = [[ ]]
    5 - Questionnaire - Using a double list comprehension to build both rows and columns in a single line of code
    6 - Questionnaire - Unwinding the comprehensions into 2 for loops instead
    7 - Using the * operator to unpack generated items onto a single row 
"""

"""
    Construct #0 - List comprehension to generate a row of Buttons

    Comprehensions are super-powers of Python.  In this example we're using a comprehension to create 4 buttons that
    are all on the same row.
"""


def layout0():
    layout = [[sg.Button(i) for i in range(4)]]     # A list of buttons is created

    window = sg.Window('Generated Layouts', layout)

    event, values = window.Read()

    print(event, values)
    window.Close()

"""
    Construct #1 - List comprehension to generate rows of Buttons

    More list super-power, this time used to build a series of buttons doing DOWN the window instead of across

"""

def layout1():
    layout = [[sg.Button(i)] for i in range(4)]    # a List of lists of buttons.  Notice the ] after Button

    window = sg.Window('Generated Layouts', layout)

    event, values = window.Read()

    print(event, values)
    window.Close()


"""
    Construct #2 - List comprehension to generate a row of Buttons and concatenation of more lines of elements

    Comprehensions are super-powers of Python.  In this example we're using a comprehension to create 4 buttons that
    are all on the same row, just like the previous example.
    However, here, we want to not just have a row of buttons, we want have an OK button at the bottom.
    To do this, you "add" the rest of the GUI layout onto the end of the generated part.
    
    Note - you can't end the layout line after the +. If you wanted to put the OK button on the next line, you need
    to add a \ at the end of the first line.
    See next Construct on how to not use a \ that also results in a VISUALLY similar to a norma layout
"""

def layout2():
    layout = [[sg.Button(i) for i in range(4)]] + [[sg.OK()]]  # if want to split, can't add newline after + to do it

    window = sg.Window('Generated Layouts', layout)

    event, values = window.Read()

    print(event, values)
    window.Close()


"""
    Construct # 3 - Adding together what appears to be 2 layouts
    
    Same as layout2, except that the OK button is put on another line without using a \ so that the layout appears to
    look like a normal, multiline layout without a \ at the end
    
    Also shown is the OLD tried and true way, using layout.append.  You will see the append technique in many of the
    Demo programs and probably elsewhere.  Hoping to remove these and instead use this more explicit method of +=.
    
    Using the + operator, as you've already seen, can be used in the middle of the layout.  A call to append you cannot
    use this way because it modifies the layout list directly.
"""

def layout3():
    # in terms of formatting, the layout to the RIGHT of the = sign looks like a 2-line GUI (ignore the layout +=
    layout =  [[sg.Button(i) for i in range(4)]]
    layout += [[sg.OK()]]               # this row is better than, but is the same as
    layout.append([sg.Cancel()])        # .. this row in that they both add a new ROW with a button on it

    window = sg.Window('Generated Layouts', layout)

    event, values = window.Read()

    print(event, values)
    window.Close()


"""
    Construct 4 - Using + to place Elements on the same row
    
    If you want to put elements on the same row, you can simply add them together.  All that is happening is that the
    items in one list are added to the items in another.  That's true for all these contructs using +
"""

def layout4():
    layout =  [[sg.Text('Enter some info')] + [sg.Input()] + [sg.Exit()]]

    window = sg.Window('Generated Layouts', layout)

    event, values = window.Read()

    print(event, values)
    window.Close()


"""
    Construct #5 - Simple "concatenation" of layouts
    Layouts are lists of lists.  Some of the examples and demo programs use a .append method to add rows to layouts.
    These will soono be replaced with this new technique.  It's so simple that I don't know why it took so long to
    find it.
    This layout uses list comprehensions heavily, and even uses 2 of them. So, if you find them confusing, skip down
    to the next Construct and you'll see the same layout built except for loops are used rather than comprehensions
    
    The next 3 examples all use this same window that is layed out like this:
        Each row is:
    Text1, Text2, Radio1, Radio2, Radio3, Radio4, Radio5
    Text1, Text2, Radio1, Radio2, Radio3, Radio4, Radio5
    ...
    
    It shows, in particular, this handy bit of layout building, a += to add on additional rows.
    layout =  [[stuff on row 1], [stuff on row 2]]
    layout += [[stuff on row 3]]
    
    Works as long as the things you are adding together look like this [[ ]]  (the famous double bracket layouts of PSG)
"""

def layout5():
    questions = ('Managing your day-to-day life', 'Coping with problems in your life?', 'Concentrating?',
                 'Get along with people in your family?', 'Get along with people outside your family?',
                 'Get along well in social situations?', 'Feel close to another person',
                 'Feel like you had someone to turn to if you needed help?', 'Felt confident in yourself?')

    layout = [[sg.T(qnum + 1, size=(2, 2)), sg.T(q, size=(30, 2))] + [sg.Radio('', group_id=qnum, size=(7, 2), key=(qnum, col)) for col in range(5)] for qnum, q in enumerate(questions)]
    layout += [[sg.OK()]]

    window = sg.Window('Computed Layout Questionnaire', layout)
    event, values = window.Read()

    print(event, values)
    window.Close()


"""
    Construct #6 - Computed layout without using list comprehensions
    This layout is identical to Contruct #5.  The difference is that rather than use list comprehensions, this code
    uses for loops.  Perhaps if you're a beginner this version makes more sense?

    In this example we start with a "blank layout" [[ ]] and add onto it.

    Works as long as the things you are adding together look like this [[ ]]  (the famous double bracket layouts of PSG)
"""


def layout6():
    questions = ('Managing your day-to-day life', 'Coping with problems in your life?', 'Concentrating?',
                 'Get along with people in your family?', 'Get along with people outside your family?',
                 'Get along well in social situations?', 'Feel close to another person',
                 'Feel like you had someone to turn to if you needed help?', 'Felt confident in yourself?')

    layout = [[]]
    for qnum, question in enumerate(questions):     # loop through questions
        row_layout = [sg.T(qnum + 1, size=(2, 2)), sg.T(question, size=(30, 2))]    # rows start with # and question
        for radio_num in range(5):                  # loop through 5 radio buttons and add to row
            row_layout += [sg.Radio('', group_id=qnum, size=(7, 2), key=(qnum, radio_num))]
        layout += [row_layout]                      # after row is completed layout, tack it onto the end of final layout

    layout += [[sg.OK()]]                           # and finally, add a row to the bottom that has an OK button

    window = sg.Window('Computed Layout Questionnaire', layout)
    event, values = window.Read()

    print(event, values)
    window.Close()



"""
    Construct #7 - * operator and list comprehensions 
        Using the * operator from inside the layout
        List comprehension inside the layout
        Addition of rows to layouts
        All in a single variable assignment
        
    NOTE - this particular code, using the * operator, will not work on Python 2 and think it was added in Python 3.5
    
    This code shows a bunch of questions with Radio Button choices
    
    There is a double-loop comprehension used.  One that loops through the questions (rows) and the other loops through
    the Radio Button choices.
    Thus each row is:
    Text1, Text2, Radio1, Radio2, Radio3, Radio4, Radio5
    Text1, Text2, Radio1, Radio2, Radio3, Radio4, Radio5
    Text1, Text2, Radio1, Radio2, Radio3, Radio4, Radio5
    
    What the * operator is doing in these cases is expanding the list they are in front of into a SERIES of items
    from the list... one after another, as if they are separated with comma.  It's a way of "unpacking" from within
    a statement.
    
    The result is a beautifully compact way to make a layout, still using a layout variable, that consists of a
    variable number of rows and a variable number of columns in each row.
"""

def layout7():
    questions = ('Managing your day-to-day life', 'Coping with problems in your life?', 'Concentrating?',
                 'Get along with people in your family?', 'Get along with people outside your family?',
                 'Get along well in social situations?', 'Feel close to another person',
                 'Feel like you had someone to turn to if you needed help?', 'Felt confident in yourself?')

    layout = [[*[sg.T(qnum + 1, size=(2, 2)), sg.T(q, size=(30, 2))], # These are the question # and the question text
               *[sg.Radio('', group_id=qnum, size=(7, 2), key=(qnum, col)) for col in range(5)]] for qnum, q in enumerate(questions)] + [[sg.OK()]]     # finally add an OK button at the very bottom by using the '+' operator

    window = sg.Window('Questionnaire', layout)

    event, values = window.Read()

    print(event, values)
    window.Close()


# ------------------------- Call each of the Constructs -------------------------

layout0()
layout1()
layout2()
layout3()
layout4()
layout5()
layout6()
layout7()