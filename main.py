#1-misol
words = ["python", "java", "c++", "golang"]

words = [word.upper() for word in words]

print(words)


#2-misol
nested = [[1, 2], [3, 4], [5, 6]]
flat = []

for sublist in nested:
    for item in sublist:
        flat.append(item)

print(flat)


#3-misol
numbers = [100, 200, 300, 400]

numbers[0] = 999

print(numbers)


#4-misol
roy = []

for i in range(6):
    son = int(input(f"{i+1}-sonni kiriting: "))
    if son > 0:
        roy.append(son)

print("Siz kiritgan musbat sonlar:", roy)

#5-misol
words = ["apple", "banana", "kiwi", "strawberry"]

eng_uzun = max(words, key=len)

print("Eng uzun so'z:", eng_uzun)
print("Uzunligi:", len(eng_uzun))
