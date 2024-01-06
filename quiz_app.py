import itertools
import sys
import random

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
            return 1
      return 0


answer=''
def main():

    sys.argv
    subject=sys.argv[1]
    num_questions=int(sys.argv[2])
    
    with open(rf'questions\{subject}.txt', mode='r') as file:
        print(num_questions)
        
        NumCorrectAnswer=0
        for line in itertools.islice(file, num_questions):
            correct_index=(view_question(f'{line}'))
            answer=int(input())
            if(answer==correct_index):
                 NumCorrectAnswer=NumCorrectAnswer+1
            # print(IsCorrect(answer,correct_index))
            # if(IsCorrect(answer,correct_index)):
                 
            print (NumCorrectAnswer)
        
        print(f'you answerd {NumCorrectAnswer}/{num_questions} correct answers')
            

            




if __name__ == '__main__':
    main()
