# stripping_whitespace.py

favorite_language = 'python '
print(favorite_language)
print(len(favorite_language))
print(favorite_language.rstrip())
print(len(favorite_language.rstrip()))
print(favorite_language)
print(len(favorite_language))


favorite_language = ' python '
print(favorite_language)
print(len(favorite_language))
favorite_language = favorite_language.rstrip()
print(favorite_language)
print(len(favorite_language))

favorite_language = ' python '
print(favorite_language)
print(len(favorite_language))
favorite_language = favorite_language.lstrip()
print(favorite_language)
print(len(favorite_language))

favorite_language = ' python '
favorite_language = favorite_language.strip()
print(favorite_language)
print(len(favorite_language))