def capTofront(word):
    words,words1 = '' , ''
    for i in word:
        if i.isupper():
            words += i
        else:
            words1 += i
    return words + words1

print(capTofront('hApPy'))
print(capTofront('moveMENT'))
print(capTofront('shOrtCAKE'))