class Programmers:
    name = ""
    language = ""
    projectAssigned = ""
    def __init__(self,name,language,projectAssigned):
        self.name = name
        self.language = language
        self.projectAssigned = projectAssigned

    def greet(self):
        print(self.name)
        print(self.language)
        print(self.projectAssigned)

archie = Programmers("Archie","C#","Healthcare Management")
tejas = Programmers("Tejas","Python","Healthcare Management")

archie.greet()
tejas.greet()
