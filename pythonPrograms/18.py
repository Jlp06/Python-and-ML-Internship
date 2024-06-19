
# Check anagram
from collections import Counter

def check_anagram(s1, s2):
    if Counter(s1) == Counter(s2):
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")


str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
check_anagram(str1, str2)
