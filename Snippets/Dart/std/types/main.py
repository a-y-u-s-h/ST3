import os
import shutil
import glob

def main():
  types = [
    "int",
    "double",
    "String",
    "bool",
    "num",
    "Function"
  ]

  for t in types:
    # `edit` : {t.lower()}.sublime-snippet
    with open(f"{t.lower()}.sublime-snippet", "w") as file:
      file.write(f"""<snippet>
  <content><![CDATA[
{t}
]]></content>
  <tabTrigger>{t.lower()}</tabTrigger>
  <scope>source.dart</scope>
</snippet>
""")
    


if __name__ == '__main__':
  main()