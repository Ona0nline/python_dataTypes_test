"""
Questions:
MistaKE ON TEST FOR SUM??
"""

def int_division():
    """
    Task:
    - Perform integer division of 7 by 2.
    
    Return:
    - The result of the division (integer).
    """
    a = 7
    b = 2
    int_div = a//b
    print(int_div)
    return int_div


def float_multiplication():
    """
    Task:
    - Multiply 3.0 by 2.
    
    Return:
    - The result of the multiplication (float).
    """
    a = 3.0
    b = 2
    prod = a * b
    print(prod)
    return prod


def combine_operations():
    """
    Task:
    - Add the result of integer division and multiplication.
    
    Return:
    - The combined result (float).
    """
    sum = int_division() + float_multiplication()
    print(sum)
    return sum


def extract_word():
    """
    Task:
    - Extract the word 'awesome' from the string 'Python is awesome!'.
    
    Return:
    - The extracted word ('awesome').
    """
    string = "Python is awesome"
    split_word = string.split()
    print(split_word[2])
    return(split_word[2])


def to_lowercase():
    """
    Task:
    - Convert the string 'Python is awesome!' to lowercase.
    
    Return:
    - The lowercase version of the string.
    """

    string = "Python is awesome!"
    print(string.lower())
    return string.lower()
    


def count_o():
    """
    Task:
    - Count how many times the letter 'o' appears in the string 'Python is awesome!'.
    
    Return:
    - The count of the letter 'o'.
    """
    o_count = 0
    string = 'Python is awesome!'
    for char in string:
        if char == 'o':
            o_count += 1
    print(o_count)
    return o_count


def evaluate_boolean():
    """
    Task:
    - Evaluate the expression 'not (5 > 3) and (10 == 5 * 2)'.
    
    Return:
    - The boolean result of the expression.
    """
    expression = not (5>3) and (10 == 5 * 2)
    print(bool(expression))

if __name__ == "__main__":
    int_division()
    float_multiplication()
    combine_operations()
    extract_word()
    to_lowercase()
    count_o()
    evaluate_boolean()