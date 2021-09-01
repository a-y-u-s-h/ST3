import os
import shutil
import glob

def main():
  keywords = [
    "sampler1D",
    "sampler2D",
    "sampler3D",
    "samplerCube",
    "sampler2DRect",
    "sampler1DShadow",
    "sampler2DShadow",
    "sampler2DRectShadow",
    "sampler1DArray",
    "sampler2DArray",
    "sampler1DArrayShadow",
    "sampler2DArrayShadow",
    "samplerBuffer "
  ]

  for k in keywords:
    # `edit` : {k}.sublime-snippet
    with open(f"to.{k}.sublime-snippet", "w") as file:
      file.write(f"""<snippet>
  <content><![CDATA[
{k}($0)
]]></content>
  <tabTrigger>to{k}</tabTrigger>
  <scope>source.glsl</scope>
  <description>to{k}</description>
</snippet>
""")
    


if __name__ == '__main__':
  main()