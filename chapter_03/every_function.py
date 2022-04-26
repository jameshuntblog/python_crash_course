# every_function.py

programming_languages = ['Python','VBA','JavaScript','CSS','SQL','C','C++','Scala','Java','R']
print(programming_languages)
print(programming_languages[1])
print(programming_languages[1].title())
print(programming_languages[1].upper())
print(programming_languages[-1].title())
print(programming_languages[-1].upper())
print(len(programming_languages))
message = f"My first programming language was {programming_languages[1].upper()}."
print(message)

programming_languages.append('Ruby')
print(programming_languages)

programming_languages.insert(0,'Ruby on Rails')
print(programming_languages)

del programming_languages[0]
print(programming_languages)

popped_programming_language = programming_languages.pop()
print(popped_programming_language)
print(programming_languages)

dont_need = 'R'
programming_languages.remove(dont_need)
print(programming_languages)

print(sorted(programming_languages))
print(sorted(programming_languages,reverse=True))

programming_languages.reverse()
print(programming_languages)
programming_languages.reverse()
print(programming_languages)

programming_languages.sort()
print(programming_languages)