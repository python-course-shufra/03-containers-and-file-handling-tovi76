classroom = [
    {
        'name': 'Alice',
        'email': 'alice@example.com',
        'grades': [
            ('math', 91),
            ('english', 78),
            ('math', 90),
            ('history', 34),
            ('math', 95),
        ],
    },
    {
        'name': 'Bob',
        'email': 'bob@example.com',
        'grades': [
            ('math', 85),
            ('english', 92),
            ('history', 75),
        ],
    },
    {
        'name': 'Charlie',
        'email': 'charlie@example.com',
        'grades': [
            ('physics', 78),
            ('english', 81),
            ('english', 89),
            ('history', 68),
            ('english', 82),
            ('physics', 91),
        ],
    },
]
def return_student(myname):
    for i, student in enumerate(classroom):
        if student['name']==myname:
            return i
    return -1





def add_student(name, email=None):
    if not email:
        email = f"{name.lower()}@example.com"
    new_student = {
        'name': name,
        'email': email,
        'grades': []
    }
    classroom.append(new_student)



def delete_student(name):
    index=return_student(name)
    del classroom[index]

# delete_student('Bob')
# print(classroom)

    


def set_email(name, email):
    index=return_student(name)
    classroom[index]['email']=email

# set_email('Bob', 'le.com')
# print(classroom)


def add_grade(name, profession, grade):
        index=return_student(name)
        new_grade=classroom[index]['grades'].append((profession, grade))
        

# add_grade('Alice','mbmbm',90)
# print(classroom)

def avg_grade(name, profession):
    count=0
    sum=0
    index=return_student(name)
    for i in classroom[index]['grades']:
        if i[0]==profession:
            count+=1
            sum+=i[1]
    return sum/count
            
            

# print(avg_grade('Alice','math'))



def get_professions(name):
    index=return_student(name)
    s=set()
    for i in classroom[index]['grades']:
        s.add(i[0])
    return s

# print(get_professions('Alice'))
    
