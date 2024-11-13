students = [('Alice', 85), ('Bob', 90), ('Charlie', 78), ('David', 92)]
nested = {'a': [1, 2, 3], 'b': (4, 5), 'c': {'x': 10, 'y': 20}}

def create_squares_of_evens():
    """
    Task:
    - Create a list of squares for all even numbers from 1 to 20 using list comprehension.
    
    Return:
    - The list of squares of even numbers.
    """
    square_list = []
    for index in range(1,11):
        if index % 2 == 0:
            index ** 2
          
            square_list.append(index**2)
    print(square_list)
    return square_list


def convert_to_dict(students):
    """
    Task:
    - Convert the list of student tuples into a dictionary where the name is the key and the grade is the value.
    
    Return:
    - The dictionary created from the list of students.
    """
    diction = dict(students)
    print(diction)
    return diction

def access_value_x(nested):
    """
    Task:
    - Access the value of 'x' from the nested dictionary `nested = {'a': [1, 2, 3], 'b': (4, 5), 'c': {'x': 10, 'y': 20}}`.
    
    Return:
    - The value of 'x' (which is 10).
    """
    print(nested['c']['x'])
    return nested['c']['x']


def append_to_list_in_dict(nested):
    """
    Task:
    - Append the value 6 to the list under key 'a' in the nested dictionary `nested = {'a': [1, 2, 3], 'b': (4, 5), 'c': {'x': 10, 'y': 20}}`.
    
    Return:
    - The updated dictionary.
    """
    nested['a'] = nested['a'] + [6]
    print(nested)
    return nested
    

def convert_tuple_to_list_and_append(nested):
    """
    Task:
    - Convert the tuple under key 'b' in the nested dictionary into a list and add the value 6 at the end.
    
    Return:
    - The updated dictionary.
    """
    nested['b'] = list(nested['b']) + [6]
    print(nested)
    return nested
    
    

create_squares_of_evens()
convert_to_dict(students)
access_value_x(nested)
append_to_list_in_dict(nested)
convert_tuple_to_list_and_append(nested)
