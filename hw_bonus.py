"""
💎 Exercise-1 (Longest Consecutive Sequence):
Write a function "longest_consecutive(my_list: list[int]) -> int" that takes a 
list of integers and returns the length of the longest consecutive elements 
sequence in the list. The list might be unsorted.

Example:

longest_consecutive([100, 4, 200, 1, 3, 2]) -> 4
"""

def longest_consecutive(my_list: list[int]) -> int:
    if not my_list:
        return 0
    num_set = set(my_list)
    max_length = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_length = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            max_length = max(max_length, current_length)

    return max_length



print(longest_consecutive([100, 4, 200, 1, 3, 2]))

"""
💎 Exercise-2 (Find missing number):
Write a function "find_missing(my_list: list[int]) -> int" that takes a 
list of integers from 1 to n. The list can be unsorted and have one 
number missing. The function should return the missing number.

Example:

find_missing([1, 2, 4]) -> 3
"""

def find_missing(my_list: list[int]) -> int:
    if len(my_list) <= 1:
        return None
    n = len(my_list) + 1
    total_sum = n * (n + 1) // 2
    actual_sum = sum(my_list)
    return total_sum - actual_sum



print(find_missing([1, 2, 4]))


"""
💎 Exercise-3 (Find duplicate number):
Write a function "find_duplicate(my_list: list[int]) -> int" that takes a list 
of integers where each integer is in the range of 1 to n (n is the size of the list). 
The list can have one number appearing twice and the function should return this number.

Example:

find_duplicate([1, 3, 4, 2, 2]) -> 2
"""

def find_duplicate(my_list: list[int]) -> int:
    slow, fast = my_list[0], my_list[0]


    while True:
        slow = my_list[slow]
        fast = my_list[my_list[fast]]
        if slow == fast:
            break


    slow = my_list[0]
    while slow != fast:
        slow = my_list[slow]
        fast = my_list[fast]

    return slow


print(find_duplicate([1, 3, 4, 2, 2]))


"""
💎 Exercise-4 (Group Anagrams):
Write a function "group_anagrams(words: list[str]) -> list[list[str]]" that 
takes a list of strings (all lowercase letters), groups the anagrams together, 
and returns a list of lists of grouped anagrams.

An Anagram is a word or phrase formed by rearranging the letters of 
a different word or phrase, typically using all the original letters exactly once.

group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) 
-> [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
"""

def group_anagrams(words: list[str]) -> list[list[str]]:
    from collections import defaultdict
    anagram_groups = defaultdict(list)

    for word in words:
        sorted_word = ''.join(sorted(word))
        anagram_groups[sorted_word].append(word)

    return list(anagram_groups.values())



print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

