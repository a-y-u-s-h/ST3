import os
import shutil
import glob

def main():
  current = os.getcwd()
  for i in os.listdir("."):
    if i != "main.py":
      name = i.capitalize()

      # `cd` into : ${i}
      if os.path.exists(os.path.join(current, i)):
        os.chdir(os.path.join(current, i))
      
      # `edit` : {i}.sublime-snippet
      with open(f"{i}.sublime-snippet", "w") as file:
        file.write(f"""<snippet>
  <content><![CDATA[
{name}
]]></content>
  <tabTrigger>{i}</tabTrigger>
  <scope>source.Kotlin</scope>
</snippet>
        """)

      # `edit` : {i}max.sublime-snippet
      with open(f"{i}max.sublime-snippet", "w") as file:
        file.write(f"""<snippet>
  <content><![CDATA[
{name}.MAX_VALUE
]]></content>
  <tabTrigger>{i}max</tabTrigger>
  <scope>source.Kotlin</scope>
</snippet>
        """)

      # `edit` : {i}min.sublime-snippet
      with open(f"{i}min.sublime-snippet", "w") as file:
        file.write(f"""<snippet>
  <content><![CDATA[
{name}.MIN_VALUE
]]></content>
  <tabTrigger>{i}min</tabTrigger>
  <scope>source.Kotlin</scope>
</snippet>
        """)

      # `cd` into : {current}
      if os.path.exists(f"{current}"):
        os.chdir(f"{current}")
      
    

if __name__ == '__main__':
  main()