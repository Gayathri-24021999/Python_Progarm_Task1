# 7. Freq char

test = "Guvi Geeks Network Private Limited"
char_freq = {}
for char in test:
    if char in char_freq:
        char_freq[char] +=1
    else:
        char_freq[char] =1
most_frequent_char = max(char_freq, key=char_freq.get)
print(most_frequent_char)
