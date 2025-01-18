#!/usr/bin/env python3

class MyString:
  # lib/mystring.py   
    def __init__(self, value=''):  
        self.value = value  

    @property  
    def value(self):  
        return self._value  

    @value.setter  
    def value(self, val):  
        if not isinstance(val, str):  
            raise ValueError("Value must be a string.")  
        self._value = val  

    def is_sentence(self):  
        """Check if the value ends with a period."""  
        return self.value.endswith('.')  
    
    def is_question(self):  
        """Check if the value ends with a question mark."""  
        return self.value.endswith('?')  
    
    def is_exclamation(self):  
        """Check if the value ends with an exclamation mark."""  
        return self.value.endswith('!')  

    def count_sentences(self):  
        """Count the number of sentences in the value."""  
        # Replacing multiple punctuation followed by whitespaces with a single period  
        cleaned_value = self.value.replace('!', '.').replace('?', '.').strip()  
        # Split by periods and filter out empty strings to count valid sentences  
        sentences = [sentence for sentence in cleaned_value.split('.') if sentence]  
        return len(sentences)
    
my_string = MyString("Hello! How are you doing? I hope you are well.")  
print(my_string.is_sentence())        
print(my_string.is_question())        
print(my_string.is_exclamation())     
print(my_string.count_sentences())    
