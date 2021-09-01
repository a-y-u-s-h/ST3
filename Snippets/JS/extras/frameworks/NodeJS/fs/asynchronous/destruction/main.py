import os
import shutil
import glob

def main():
  commands = [
    "mkdir",
    "touch"
  ]

  for command in commands:
    # `edit` : {command}.sublime-snippet
    with open(f"{command}.sublime-snippet", "w") as file:
      file.write(f"""<snippet>
  <content><![CDATA[
$0
]]></content>
  <tabTrigger>{command}</tabTrigger>  
  <scope>source.js</scope>
</snippet>""")
    


if __name__ == '__main__':
  main()