import os
import shutil
import glob

def main():
  types = [
    "bool",
    "char",
    "string",
    "int",
    "long",
    "decimal",
    "float",
    "double",
  ]

  for t in types:
    pwd = os.getcwd()

    # `take` : {t}
    if not os.path.exists(f"{t}"):
      os.makedirs(f"{t}")
    os.chdir(f"{t}")
    
    # `edit` : {t}.sublime-snippet
    with open(f"{t}.sublime-snippet", "w") as file:
      file.write(f"""<snippet>
  <content><![CDATA[
{t}
]]></content>
  <tabTrigger>{t}</tabTrigger>
  <scope>source.cs</scope>
  <description>{t}</description>
</snippet>""")

    # `edit` : {t}.max.sublime-snippet
    with open(f"{t}.max.sublime-snippet", "w") as file:
      file.write(f"""<snippet>
  <content><![CDATA[
{t}.MaxValue
]]></content>
  <tabTrigger>{t}max</tabTrigger>
  <scope>source.cs</scope>
  <description>{t}max</description>
</snippet>""")

    # `edit` : to.{t}.sublime-snippet
    with open(f"to.{t}.sublime-snippet", "w") as file:
      file.write(f"""<snippet>
  <content><![CDATA[
({t}) $0
]]></content>
  <tabTrigger>to{t}</tabTrigger>
  <scope>source.cs</scope>
  <description>to{t}</description>
</snippet>""")
    

    # `cd` into : {pwd}
    if os.path.exists(f"{pwd}"):
      os.chdir(f"{pwd}")
    
    


if __name__ == '__main__':
  main()