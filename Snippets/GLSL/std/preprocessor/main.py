import os
import shutil
import glob

def main():
  keywords = [
    "#define",
    "#undef",
    "#if",
    "#ifdef",
    "#ifndef",
    "#else",
    "#elif",
    "#endif",
    "#error",
    "#pragma",
    "#extension",
    "#version",
    "#line"
  ]

  for k in keywords:
    with open(f"{k}.sublime-snippet", "w") as file:
      file.write(f"""<snippet>
  <content><![CDATA[
{k} $0
]]></content>
  <tabTrigger>{k.replace("#", "").lower()}</tabTrigger>
  <scope>source.glsl</scope>
  <description>{k}</description>
</snippet>
""")
    


if __name__ == '__main__':
  main()