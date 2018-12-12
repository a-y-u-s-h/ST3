import re
from shell import *
from pprint import pprint

# <============================>

class Snippet(object):
  """
  Description:
  
    Instance of this class contains
    information about a snippet.

    => TAB trigger.
    => Snippet content.
    => What language and hierarchy
       it belongs to.
    
  """
  def __init__(self, language, text):
    super(Snippet, self).__init__()
    self.language = language
    self.text = text

  @property
  def tabtrigger(self):
    return re.search(r'(?<=<tabTrigger>)([^ ]+)(?=<\/tabTrigger>)', self.text, flags = (re.I | re.S)).group(0)

  @property
  def content(self):
    return re.search(r'(?<=<content><!\[CDATA\[)([^⁃]+)(?=\]\]><\/content>)', self.text, flags = (re.I | re.S)).group(0)


# <============================>

class README(object):
  """
  Description:
  
    Instance of this class contains
    information about README.md that's
    to be generated.
    
  """
  def __init__(self):
    super(README, self).__init__()
    self.config = readyaml("config.yaml")["documentation"]
    self.root     = "../"
    self.location = "../README.md"
    self.snippets = []

  def setup(self):
    """  
    -------------------------------------
  
      Reads in all the snippets, 
      creates an array of `Snippet`
      objects out of them.
  
    -------------------------------------
  
      args => None
      kwargs => None
      
    -------------------------------------  
    """
    pprint(self.config)

# <============================>

def main():
  readme = README()
  readme.setup()

if __name__ == '__main__':
  main()