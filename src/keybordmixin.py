class KeybordMixin:
    def __init__(self):
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    def language_change(self):
        if self.__language == 'EN':
            self.__language = "RU"
        else:
            self.__language = 'EN'
        return self
