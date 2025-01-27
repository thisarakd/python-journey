# backslash
# file_path = "file\python\test.py"  #error
file_path = "path = file\\python\\test.py"  #no error
print(file_path)

# single cotation
sentence1 = "1 - I'm Thisara"
sentence2 = '2 - I\'m Thisara'
print(sentence1)
print(sentence2)

# double cotation
sentence3 = '3 - He said "I want to call you"'
sentence4 = "4 - He said \"I want to call you\""
print(sentence3)
print(sentence4)

# new line
sentence5 = "5 - Hello\nWorld"
print(sentence5)

# tab space
sentence6 = "6 - Hello\tWorld"
print(sentence6)

# carriage return
sentence7 = "7 - Hello \rWorld"
print(sentence7)

# backspace
sentence8 = "8 - Hello\b World"
print(sentence8)

# raw strings
print(r"raw string - Hello\n World")

# multiline strings with triple quotes
print("""triple quotes - Hello!
My name is Thisara.
Nice to meet you!""")