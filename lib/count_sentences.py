class MyString:
    def __init__(self, value=''):
        if isinstance(value, str):
            self._value = value
        else:
            raise ValueError("Value must be a string")

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            raise ValueError("Value must be a string")

    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(self):
        # Replace multiple punctuation marks with a single one
        cleaned_value = self._value.replace('!', '.').replace('?', '.')
        # Split the string by the period and filter out empty strings
        sentences = [s for s in cleaned_value.split('.') if s.strip()]
        return len(sentences)

string = MyString("This is a string! It has three sentences. Right?")
print(string.count_sentences())  
print(string.is_sentence())      
print(string.is_question())      
print(string.is_exclamation())   