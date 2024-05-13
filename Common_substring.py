# 6. Common substring
str1 = "GuviGeeksNetwork"
str2 = "Guviprivatelimited"
max_length =0
start_index=0
for i in range(len(str1)):
    for j in range(len(str2)):
        length=0
        while i + length<len(str1) and j+length<len(str2) and str1[i+length]== str2[j + length]:
            length +=1
            if length > max_length:
                max_length = length
                start_index = i
longest_substring = str1[start_index:start_index + max_length]
print(longest_substring)
