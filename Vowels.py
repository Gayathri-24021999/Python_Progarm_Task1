# 1. Vowels
string = "Guvi Geeks Network Private Limited"
vowels = "AEIOUaeiou"
# total_count = sum(string.count(vowels) for vowels in vowels)
# print(total_count)
vowels_count = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0, 'A':0, 'E':0, 'I':0, 'O':0, 'U':0}
for char in string:
    if char in vowels:
        vowels_count[char] +=1
total_vowels = sum(vowels_count.values())
print("total_vowels", total_vowels)
for vowels, count in vowels_count.items():
    print(f"count of '{vowels}':", count)
