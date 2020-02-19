import os
import shutil
import glob

def main():
  functions = [
    "mix",
    "adjust-hue",
    "lighten",
    "darken",
    "saturate",
    "desaturate",
    "rgba",
    "opacify",
    "transparentize",
    "adjust-color",
    "scale-color",
    "scale-color",
    "change-color"
  ]

  for f in functions:
    snippet = f"""<snippet>
  <content><![CDATA[
{f}($0)
]]></content>
  <tabTrigger>{f}</tabTrigger>
  <scope>source.css meta.property-list.css - meta.property-value.css, source.less - meta.property-value.css, source.scss - meta.property-list - support.function.name.sass.library - variable.other.root</scope>
  <description>{f}</description>
</snippet>
    """
    # `edit` : {f}.sublime-snippet
    with open(f"{f}.sublime-snippet", "w") as file:
      file.write(f"{snippet}")
    


if __name__ == '__main__':
  main()