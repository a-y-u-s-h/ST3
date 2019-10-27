import os
import shutil
import glob

def main():
  booleans = ["true", "false", "nil"]

  for b in booleans:
    # `edit` : {b}.sublime-snippet
    with open(f"{b}.sublime-snippet", "w") as file:
      file.write(f"""<snippet>
  <content><![CDATA[
{b}
]]></content>
  <tabTrigger>{b}</tabTrigger>
  <scope>source.ruby</scope>
  <description>{b}</description>
</snippet>
""")
    


if __name__ == '__main__':
  main()