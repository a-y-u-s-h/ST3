import os
import shutil
import glob

def main():
  for i in os.listdir():
    if os.path.isdir(f"{i}"):
      pwd = os.getcwd()
      if os.path.exists(f"{i}"):
        os.chdir(f"{i}")
        with open(f"{i}.max.sublime-snippet", "w") as file:
          file.write(f"""<snippet>
  <content><![CDATA[
{i}.max
]]></content>
  <tabTrigger>{i}max</tabTrigger>
  <scope>source.d</scope>
  <description>{i}.max</description>
</snippet>
""")
                    
        with open(f"{i}.min.sublime-snippet", "w") as file:
          file.write(f"""<snippet>
  <content><![CDATA[
{i}.min
]]></content>
  <tabTrigger>{i}min</tabTrigger>
  <scope>source.d</scope>
  <description>{i}.min</description>
</snippet>
""")
        # `cd` into : {pwd}
        if os.path.exists(f"{pwd}"):
          os.chdir(f"{pwd}")
        
if __name__ == '__main__':
  main()