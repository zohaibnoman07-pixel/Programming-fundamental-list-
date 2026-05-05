# M01: Remove all occurrences of 2
a = [1, 2, 4, 2, 5, 2, 6]

result = []
for x in a:
    if x != 2:
        result.append(x)

print(result)


# M02: Second largest distinct value
nums = [9, 2, 11, 7, 11, 3]

largest = nums[0]
for x in nums:
    if x > largest:
        largest = x

second = None
for x in nums:
    if x != largest:
        if second is None or x > second:
            second = x

print("Second largest =", second)


# M03: Rotate left by 1
a = [10, 20, 30, 40, 50]

first = a[0]
a = a[1:]
a.append(first)

print(a)


# M04: Insert 99 at index k
a = [1, 2, 3, 4, 5]
k = int(input("Enter index: "))

new_list = []

for i in range(len(a)):
    if i == k:
        new_list.append(99)
    new_list.append(a[i])

print(new_list)


# M05: Delete element at index k
a = [5, 6, 7, 8, 9, 10]
k = int(input("Enter index: "))

new_list = []

for i in range(len(a)):
    if i != k:
        new_list.append(a[i])

print(new_list)


# M06: Longest word
sentence = input("Enter a sentence: ")

words = sentence.split()
longest = words[0]

for w in words:
    if len(w) > len(longest):
        longest = w

print("Longest word:", longest)
print("Length:", len(longest))


# M07: Join words with separator
sentence = input("Enter a sentence: ")

words = sentence.split()

result = ""
for i in range(len(words)):
    result += words[i]
    if i != len(words) - 1:
        result += " | "

print(result)


# M08: Unique elements (preserve order)
a = [3, 3, 2, 3, 1, 2, 4, 4]

unique = []

for x in a:
    if x not in unique:
        unique.append(x)

print(unique)


# M09: Frequency count (no dictionary)
a = [1, 1, 1, 2, 2, 3, 4, 4]
checked = []

for x in a:
    if x not in checked:
        count = 0
        for y in a:
            if y == x:
                count += 1
        print(x, "occurs", count, "times")
        checked.append(x)


# M10: Bubble Sort
a = [8, 3, 5, 2, 9, 1]

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] > aa[i], a[j] = a[j], a[i]

print(a)