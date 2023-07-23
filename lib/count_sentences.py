#!/usr/bin/env python3

class MyString:
  def __init__(self, value = ""):
    self._value = value
  
  def get_value(self):
    return self._value
  
  def set_value(self, the_value):
    if type(the_value) == str:
      self._value = the_value
    else:
      print("The value must be a string.")
  
  value = property(get_value, set_value)

  def is_sentence(self):
    return self._value.endswith(".")
  
  def is_question(self):
    return self._value.endswith("?")
  
  def is_exclamation(self):
    return self._value.endswith("!")
  
  def count_sentences(self):
    value = self.value
    for mark in ["!", "?"]:
      value = value.replace(mark, ".")
    
    value_splited = value.split(".")
    sentences = [not_empty_str for not_empty_str in value_splited if not_empty_str]
    return len(sentences)
