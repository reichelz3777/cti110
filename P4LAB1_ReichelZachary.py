user_text = input()
count_text = 0

for x in user_text:
    if not (x in " .,!"):
        count_text += 1
        
print(count_text)
