# 3. Remove the vowels

string = "Guvi Geeks Network Private Limited"
vowels = "AEIOUaeiou"
result=""
for char in string:
    if char not in vowels:
        result +=char
print(result)
