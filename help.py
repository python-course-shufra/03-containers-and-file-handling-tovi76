import random
import sys


def view_question(text):
        text=text.strip()
        text=text.split(';')
        question=text[0]
        correct_answer=text[1]
        options=(f'{text[2]},{text[1]}')
        options=options.split(',')
        random.shuffle(options)
        
        print(question)

        correct_index=None
        for i, item in enumerate(options):
            print (f'{i+1}. {item}')
            if(item==correct_answer):
                  correct_index=i+1
        return (correct_index)
      

def IsCorrect(answer, correct_index):
      if(answer==correct_index):
            NumOfCorrectAnswer=1

            
        
            
        
view_question('What is the result of 7 + 4? ; 11 ; 9, 14, 18')
