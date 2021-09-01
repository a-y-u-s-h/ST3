import os
import shutil
import glob

def main():
  F = [
    "product",
    "sum",
    "min",
    "max",
    "sorted",
    "zipWithIndex"
  ]
  
  for f in F:
    # `edit` : {i}.sublime-snippet
    with open(f"{f}.sublime-snippet", "w") as file:
      file.write(f"""
<snippet>
  <content><![CDATA[
$0.{f}
]]></content>
  <tabTrigger>{f}</tabTrigger>
  <scope>source.scala</scope>
  <description>{f}</description>
</snippet>

""")
    


if __name__ == '__main__':
  main()