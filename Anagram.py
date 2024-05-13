# 8. Anagram

string1 = "angel"
string2 = "glean"

string1 = string1.replace(" ", "").lower()
string2 = string2.replace(" ", "").lower()
if sorted(string1) == sorted(string2):
    print("True")
else:
    print("False")
