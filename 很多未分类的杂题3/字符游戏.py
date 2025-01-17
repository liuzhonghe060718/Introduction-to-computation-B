words=list(input())
yuan=["a","e","i","o","u","y"]
answer=[]
for word in words:
    word=word.lower()
    if word not in yuan:
        answer.append(f".{word}")
print(''.join(answer))