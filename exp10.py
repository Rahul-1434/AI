print("Chatbot that provides information of college")
print("*" * 40)
print("You may ask any one of these questions")
print("What is your college name?")
print("How many departments are there?")
print("Which department you belong to?")
print("Is faculty teaching well?")
print("Where does your college located?")
print("How much is the fee for CSE?")
print("Is the college good for placements?")
print("Is any function celebrated in your college?")
print("Quit")

while True:
    question = input("Enter one question from above list: ")
    
    if question in ["What is your college name?"]:
        print("Mother Theresa Institute of Engineering and Technology")
    elif question in ["How many departments are there?"]:
        print("Nearly 7 batch")
    elif question in ["Which department you belong to?"]:
        print("I belong to CSE department")
    elif question in ["Is faculty teaching well?"]:
        print("Yes")
    elif question in ["Where does your college located?"]:
        print("In Palamaner")
    elif question in ["How much is the fee for CSE?"]:
        print("Nearly one lakh")
    elif question in ["Is the college good for placements?"]:
        print("Yeah, it's good")
    elif question in ["Is any function celebrated in your college?"]:
        print("Yes")
    elif question in ["Quit"]:
        break
    else:
        print("I don't understand what you said")
