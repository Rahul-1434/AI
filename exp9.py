print('simple question and Answer')
print('============================')
print('you may ask any one of these questions')
print("Hi")
print("How Are You?")
print('What is your name?')
print('What did you do yestarday?')
print('Quit')
while True:
    question=input('enter one question form above list:')
    question=question.lower()
    if question in ['hi']:
        print('Hello')
    elif question in ['how are you?','how do you do?']:
        print('i am fine')
    elif question in ['what is your name?']:
        name=input('enter your name')
        print('my name is ',name)
    elif question in ['are you working?','are you doing any job?']:
        print('YES, I am working in RBI')
    elif question in ['what did you do yestarday?']:
        print('I saw bahubali 5 Times')
    elif question in ['quit','exit']:
        break
    else:
        print("i don't understand")
