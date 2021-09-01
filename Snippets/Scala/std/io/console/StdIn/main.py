import os
import shutil
import glob

def main():
  read = [
    "readFloat",
    "readDouble",
    "readBoolean",
    "readByte",
    "readChar",
    "readFloat",
    "readInt",
    "readLine",
    "readLong",
    "readShort",
    "readf",
    "readf1",
    "readf2",
    "readf3"
  ]

  # `take` : read
  if not os.path.exists(f"read"):
    os.makedirs(f"read")
  os.chdir(f"read")
  
  for i in read:
    # `edit` : {i}.sublime-snippet
    with open(f"{i}.sublime-snippet", "w") as file:
      file.write(f"""
<snippet>
  <content><![CDATA[
{i}
]]></content>
  <tabTrigger>{i}</tabTrigger>
  <scope>source.scala</scope>
  <description>{i}</description>
</snippet>

""")
    


if __name__ == '__main__':
  main()