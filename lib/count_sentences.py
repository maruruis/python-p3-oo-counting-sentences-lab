#!/usr/bin/env python3

class MyString:
  pass
  def __init__(self, value=""):
    self._value = value

  @property
  def value(self):
    return self._value

  @value.setter
  def value(self, string_val):
    if not isinstance(string_val, str):
      print("The value must be a string.")
      self._value = string_val

  def is_sentence(self):
    return self._value.endswith(".")

  def is_question(self):
    return self._value.endswith("?")

  def is_exclamation(self):
    return self._value.endswith("!")

  def count_sentences(self):
    cleaned_value = self._value.replace('!', '.').replace('?', '.')
    sentences = [s for s in cleaned_value.split('.') if s]
    return len(sentences)