import os
import shutil
import glob

def main():
  snippets = {
    "i1" : "Int8",
    "i2" : "Int16",
    "i3" : "Int32",
    "i4" : "Int64", 
    "ui1" : "UInt8",
    "ui2" : "UInt16",
    "f1" : "Float32",
    "f2" : "Float64",
    "bint" : "BigInt",
    "bfloat" : "BigFloat",
    "char": "Char"
  }

  for snip, actual in snippets.items():
    snippet = f"""
<snippet>
  <content><![CDATA[
{actual}
]]></content>
  <tabTrigger>{snip}</tabTrigger>
  <scope>source.julia</scope>
  <description>{actual}</description>
</snippet>
"""
    # `edit` : {actual}.sublime-snippet
    with open(f"{actual}.sublime-snippet", "w") as file:
      file.write(snippet)
    

if __name__ == '__main__':
  main()