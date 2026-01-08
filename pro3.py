'''MENTAL ABILITY QUIZ'''
import random

class Questionarrangement:
    def __init__(self,content):
           self.content = content
            
    def format(self):
         questions = []

         blocks = self.content.split("\n\n") 
         for block in blocks:
            
            lines = block.split("\n")
            
            question_text = lines[0]
            options_text = lines[1:5]
            answer_txt = lines[5].split(":")[1].strip()

            questions.append({
                  "question" : question_text ,
                  "options" : options_text ,
                  "answer" : answer_txt
            })
         return questions
             
class Quizcontroller:
    def __init__(self,list_of_questions):
        self.questions = list_of_questions

    def quiz(self):
         
          random.shuffle(self.questions)
          Score = 0
          for question in self.questions[:10]:
                 
                 q = question.get("question")
                 o = question.get("options")
                 a = question.get("answer")
                 print(q)
                 for option in o:
                  print(option)
                 
                 print('''
                       Enter A for Answer as option a 
                       Enter B for Answer as option b 
                       Enter C for Answer as option c 
                       Enter d for Answer as option d ''')
                 n = input("Enter your answer here :").lower()
                 
                 if n == a :
                       Score = Score + 1
                       print(f"Your answer is correct! as {a}")

                 else :
                    print("wrong answer !")

                         
          return Score
                
        

print("Welcome to the Mental Ability Quiz! ")
print('''
    Insructions: The Quiz will contian 10 Random Questions 
               : For each question there will 4 alternate options 
               : Only 1 option is correct answer out of 4 options 
               : Correct answer results into +1 score
               : wrong answer results into 0 score
               : Attemptation of all questions are mandatory ''')

while True :
           print("*** Once you start the Quiz you can't exit it until it is completed *** ")
           menu = input('''
                        Menu : Press S to start the quiz :
                               Press E to exit the quiz  : ''').lower()
             
           if menu == "s":
                with open("Question.txt",'r') as f :
                       arrange = f.read()
                       data = Questionarrangement(arrange)
                       list_of_questions = data.format()

                       control = Quizcontroller(list_of_questions)   
                       result = control.quiz()

                       if result > 4 :
                        print(f"Congratulations you have passed the quiz with the Score :{result}")
                        
                       elif result <= 4 :
                         print(f"You are Failed in the quiz as your score : {result}, Better luck! next time")
           
           elif menu == "e":
                   break 

           else :
                print("Error! , Please select form S or E only :")

print("Thank you ! for using Mental Ability Quiz")
print("Comeback with more preparation :)")
print("Have a Nice Day !")                