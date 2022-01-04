"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jacob Cabral
ID:      190689750
Email:   cabr9750@mylaurier.ca
__updated__ = "2020-03-11"
-------------------------------------------------------
"""
from Letter import Letter


def do_comparisons(file_variable, bst):
    """
    -------------------------------------------------------
    Retrieves every letter in file_variable from bst. Generates
    comparisons in bst objects. Each Letter object in bst contains
    the number of comparisons found by searching for that Letter
    object in file_variable.
    Use: do_comparisons(file_variable, bst)
    -------------------------------------------------------
    Parameters:
        file_variable - the already open file containing data to evaluate (file)
        bst - the binary search tree containing 26 Letter objects
            to retrieve data from (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    for i in file_variable:
        i.strip()
        line = i.split(" ")
        for word in line:
            for letter in word:
                if letter.isalpha():
                    bst.retrieve(Letter(letter.upper()))
    return

    
def comparison_total(bst):
    """
    -------------------------------------------------------
    Sums the comparison values of all Letter objects in bst.
    Use: total = comparison_total(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        total - the total of all comparison fields in the bst
            Letter objects (int)
    -------------------------------------------------------
    """
    a = bst.inorder()
    total = 0
    for var in a:
        total += var.comparisons
    return total


def letter_table(bst):
    """
    -------------------------------------------------------
    Prints a table of letter counts for each Letter object in bst.
    Use: letter_table(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    count = 0
    a = bst.inorder()
    for var in a:
        count += var.count
    print("Letter Count/Percent Table\n")
    print("Total Count: {:,d}\n".format(count))
    print("Letter  Count       %")
    print("---------------------")
    for var in a:
        print("{:>5}  {:,d}   {:>3.2f}%".format(var.letter, var.count, (var.count / count) * 100))
    return
                    
# def hash_table(num_slots, foods):
#     """
#     UHHHHH this does something
#     Parameters:
#     num_slots and foods
#     Use:
#     hash_table(num_slots, foods)
#     Returns:
#     None
#     """
#     # print the header
#     print('Hashes\nHash     Slot Key\n======== ==== ====================')
#     for food in foods:
#         hash_val = hash(food)
#         slot_num = hash_val % num_slots
#         # this is the Food version
#         # print('{:8d} {:4d} {:s}, {:d}'.format(hash_val, slot_num, food.name, food.origin))
#         # this is the movie version (that the testing is still using)
#         print('{:8d} {:4d} {:s}, {:d}'.format(hash_val, slot_num, food.title, food.year))
#     return

# def insert_words(fv, hash_set):
#     """
#     -------------------------------------------------------
#     Retrieves every Word in fv and inserts into
#     a Hash_Set.
#     Each Word object in hash_set contains the number of comparisons
#     required to insert that Word object from file_variable into hash_set.
#     -------------------------------------------------------
#     Parameters:
#         fv - the already open file containing data to evaluate (file)
#         hash_set - the Hash_Set to insert the words into (Hash_Set)
#     Returns:
#         None
#     -------------------------------------------------------
#     """
#     for i in fv:
#         i.strip()
#         line = i.split(" ")
#         for word in line:
#             if word.isalpha():
#                 hash_set.insert(Word(word.lower()))
# 
# 
# def comparison_total(hash_set):
#     """
#     -------------------------------------------------------
#     Sums the comparison values of all Word objects in hash_set.
#     -------------------------------------------------------
#     Parameters:
#         hash_set - a hash set of Word objects (Hash_Set)
#     Returns:
#         total - the total of all comparison fields in the Hash_Set
#             Word objects (int)
#         max_word - the word having the most comparisons (Word)
#     -------------------------------------------------------
#     """
#     total = 0
#     max_word = 0
#     for var in hash_set:
#         max_word = var
#         break
#     for var in hash_set:
#         total += var.comparisons
#         if var.comparisons > max_word.comparisons:
#             max_word = var
#     print("Using array-based list Hash_Set")
#     print("Total Comparisons: {:,}".format(total))
#     print("Word with maximum comparisons '{}': {:,}".format(max_word.word, max_word.comparisons))
#     return total, max_word
