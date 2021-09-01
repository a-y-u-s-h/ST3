import os
import shutil
import glob

def main():
  keywords = [
    "gl_FrontColor",
    "gl_BackColor",
    "gl_FrontSecondaryColor",
    "gl_BackSecondaryColor",
    "gl_TexCoord",
    "gl_FogFragCoord",
    "gl_Color",
    "gl_SecondaryColor",
    "gl_TexCoord",
    "gl_FogFragCoord",
    "gl_PointCoord"
  ]

  for k in keywords:
    # `edit` : {k}.sublime-snippet
    with open(f"{k}.sublime-snippet", "w") as file:
      file.write(f"""<snippet>
  <content><![CDATA[
{k}
]]></content>
  <tabTrigger>{k.replace("_", "").lower()}</tabTrigger>
  <scope>source.glsl</scope>
  <description>{k}</description>
</snippet>
""")
    


if __name__ == '__main__':
  main()