"""
Questions:
MistaKE ON TEST FOR aLICE?
"""

numbers = [1, 2, 3]
t = (5, 10, 15, 20)
value = 15
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

student_grades = {'Alice': 85, 'Bob': 90, 'Charlie': 78}


def add_to_list(numbers):
    """
    Task:
    - Add the number 6 to the given list `numbers`.
    
    Return:
    - The modified list.
    """
    numbers += [6]
    print(numbers)
    return numbers



def remove_from_list(numbers):
    """
    Task:
    - Remove the number 3 from the given list `numbers`.
    
    Return:
    - The modified list.
    """
    numbers.pop(2)
    print(numbers)
    return numbers
    


def insert_at_beginning(numbers):
    """
    Task:
    - Insert the number 0 at the beginning of the given list `numbers`.
    
    Return:
    - The modified list.
    """
    # INSERT METHOD
    numbers.insert(0,0)
    print(numbers)
    return numbers


def reverse_list(numbers):
    """
    Task:
    - Reverse the order of elements in the list `numbers`.
    
    Return:
    - The reversed list.
    """
    # REVERSE
    numbers.reverse()
    print(numbers)
    return numbers


def create_new_tuple(t):
    """
    Task:
    - Create a new tuple that contains the first two elements of the tuple `t`.
    
    Return:
    - The new tuple with the first two elements.
    """
    
    new_tup = t[0], t[1]

    # ONLY TUPLE METHODS = COUNT AND INDEX
    print(new_tup)
    return new_tup



def check_if_value_exists(t, value):
    """
    Task:
    - Check if the value 15 exists in the tuple `t`.
    
    Return:
    - True if the value exists, otherwise False.
    """
    for tup in t:
        if tup == value:
            return True
        else:
            False


def find_intersection(set1, set2):
    """
    Task:
    - Find the intersection of sets `set1` and `set2`.
    
    Return:
    - The intersection of the two sets.
    """
    # COORELATION BETWEEN SET OPERATIONS AND ENGLISH MEANINFG
    # USE INTERSECTION BUILT IN FUNCTION
    a = set1 & set2
    # a = set1.intersection(set2)
    print(a)
    return a


def find_union(set1, set2):
    """
    Task:
    - Find the union of sets `set1` and `set2`.
    
    Return:
    - The union of the two sets.
    """
    union = set1 & set2
    print(union)
    return union


def find_difference(set1, set2):
    """
    Task:
    - Find the difference between set1 and set2 (i.e., set1 - set2).
    
    Return:
    - The difference between the two sets.
    """
    difference = set1 - set2
    print(difference)
    return difference


def add_student(student_grades):
    """
    Task:
    - Add a new student 'David' with a grade of 92 to the dictionary `student_grades`.
    
    Return:
    - The updated dictionary with the new student.
    """
    student_grades['David'] = 92
    print(student_grades)
    return student_grades


def change_bob_grade(student_grades):
    """
    Task:
    - Change Bob’s grade to 95 in the dictionary `student_grades`.
    
    Return:
    - The updated dictionary with Bob’s grade changed.
    """
    student_grades['Bob'] = 95
    print(student_grades)
    return student_grades


def delete_charlie(student_grades):
    """
    Task:
    - Delete 'Charlie' from the dictionary `student_grades`.
    
    Return:
    - The updated dictionary with Charlie removed.
    """
    del(student_grades['Charlie'])
    print(student_grades)
    return student_grades


def retrieve_alice_grade(student_grades):
    """
    Task:
    - Retrieve the grade of Alice from the dictionary `student_grades`.
    
    Return:
    - Alice's grade.
    """
    
    print(student_grades['Alice'])
    return student_grades['Alice']
    


    
# add_to_list(numbers)
# remove_from_list(numbers)
# insert_at_beginning(numbers)
# reverse_list(numbers)
# create_new_tuple(t)
# check_if_value_exists(t,value)
find_intersection(set1,set2)
# find_union(set1,set2)
# find_difference(set1, set2)
# add_student(student_grades)
# change_bob_grade(student_grades)
# delete_charlie(student_grades)
# retrieve_alice_grade(student_grades)