import re

def add_blanks(word, sentence, blank = "__"):
  return re.sub(word, blank, sentence, flags=re.IGNORECASE)