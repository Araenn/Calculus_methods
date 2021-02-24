key = int(input("Choose the enrcyption key :"))
message = input("What's your secret message ? :")


maping = {}

for i in range(26):
    i_caesar = (i + cle) % 26
    c_caesar = chr(i_caesar + ord('a'))
    c = chr(i + ord('a'))
    maping[c] = c_caesar
result = ""

for c in message:
    result = result + maping[c]
print(result)
