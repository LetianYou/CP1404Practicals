from programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

languages_list = [python, ruby, visual_basic]

print("Languages with Dynamic Typing:")
for language in languages_list:
    if language.is_dynamic():
        print(language.name)

print(F"{python}\n{ruby}\n{visual_basic}")
