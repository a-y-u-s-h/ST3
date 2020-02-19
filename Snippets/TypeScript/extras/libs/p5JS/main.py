import os
import shutil
import glob

def main():
  modules = {
    "Color": {
      "Creating and Reading" : [
        "alpha()",
        "blue()",
        "brightness()",
        "color()",
        "green()",
        "hue()",
        "lerpColor()",
        "lightness()",
        "red()",
        "saturation()"
      ],
      "Setting" : [
        "background()",
        "clear()",
        "colorMode()",
        "fill()",
        "noFill()",
        "noStroke()",
        "stroke()"
      ]
    },
    "Constants": {
      "Constants" : [
        "HALF_PI",
        "PI",
        "QUARTER_PI",
        "TAU",
        "TWO_PI",
        "DEGREES",
        "RADIANS"
      ]
    },
    "DOM": {"Classes": ["p5.Element"]},
    "Data": {
      "Dictionary" : ["createStringDict()", "createNumberDict()"],
      "Array Functions" : [
        "append()",
        "arrayCopy()",
        "concat()",
        "reverse()",
        "shorten()",
        "shuffle()",
        "sort()",
        "splice()",
        "subset()"
      ],
      "Conversion" : [
        "float()",
        "int()",
        "str()",
        "boolean()",
        "byte()",
        "char()",
        "unchar()",
        "hex()",
        "unhex()"
      ],
      "String Functions": [
        "join()",
        "match()",
        "matchAll()",
        "nf()",
        "nfc()",
        "nfp()",
        "nfs()",
        "split()",
        "splitTokens()",
        "trim()"
      ]
    },
    "Environment": {
      "Functions" : [
        "print()",
        "cursor()",
        "frameRate()",
        "noCursor()",
        "windowResized()",
        "fullscreen()",
        "pixelDensity()",
        "displayDensity()",
        "getURL()",
        "getURLPath()",
        "getURLParams()"
      ],
    "Constants" : [
        "frameCount",
        "focused",
        "displayWidth",
        "displayHeight",
        "windowWidth",
        "windowHeight",
        "width",
        "height"
      ]
    },
    "Rendering": {
      "Functions" : [
        "createCanvas()",
        "resizeCanvas()",
        "noCanvas()",
        "createGraphics()",
        "blendMode()",
        "setAttributes()"
      ],
      "Classes": [
        "p5.Graphics"
      ]
    },
    "Shape": {
      "2D Primitives" : [
        "arc()",
        "ellipse()",
        "circle()",
        "line()",
        "point()",
        "quad()",
        "rect()",
        "square()",
        "triangle()"
      ],
      "Attributes": [
        "ellipseMode()",
        "noSmooth()",
        "rectMode()",
        "smooth()",
        "strokeCap()",
        "strokeJoin()",
        "strokeWeight()"
      ],
      "Curves" : [
        "bezier()",
        "bezierDetail()",
        "bezierPoint()",
        "bezierTangent()",
        "curve()",
        "curveDetail()",
        "curveTightness()",
        "curvePoint()",
        "curveTangent()"
      ],
      "Vertex" : [
        "beginContour()",
        "beginShape()",
        "bezierVertex()",
        "curveVertex()",
        "endContour()",
        "endShape()",
        "quadraticVertex()",
        "vertex()"
      ],
      "3D Primitives": [
        "plane()",
        "box()",
        "sphere()",
        "cylinder()",
        "cone()",
        "ellipsoid()",
        "torus()"
      ],
      "3D Models" : [
        "loadModel()",
        "model()"
      ]
    },
    "Structure": {
      "Functions" : [
        "remove()",
        "noLoop()",
        "loop()",
        "push()",
        "pop()",
        "redraw()"
      ],
      "Definitions" : [
        "preload()",
        "setup()",
        "draw()",
      ]
    },
    "Transform": {
      "Functions": [
        "applyMatrix()",
        "resetMatrix()",
        "rotate()",
        "rotateX()",
        "rotateY()",
        "rotateZ()",
        "scale()",
        "shearX()",
        "shearY()",
        "translate()"
      ]
    },
    "Typography": {},
    "Events": {},
    "IO": {},
    "Image": {},
    "Lights, Camera": {},
    "Math": {}
  }

  for module, info in modules.items():
    if type(info) is dict:
      for key, value in info.items():
        if type(value) is list:
          for x in value:
            if x.endswith(f"()"):
              name = x[:-2]
              snippet = f"""<snippet>
  <content><![CDATA[
${{1:s.}}{name}($0)
]]></content>
  <tabTrigger>{name.lower().replace("_", "")}</tabTrigger>
  <scope>source.ts</scope>
  <description>{name}</description>
</snippet>"""

              if "preload" == name or "draw" == name or "setup" == name:
                snippet = f"""<snippet>
  <content><![CDATA[
let {name} = () = {{
  $0
}}
]]></content>
  <tabTrigger>{name.lower().replace("_", "")}</tabTrigger>
  <scope>source.ts</scope>
  <description>{name}</description>
</snippet>"""
              path = os.path.join(f"p5", f"{module}", f"{key}")
              if not os.path.exists(f"{path}"):
                os.makedirs(f"{path}")
              path = os.path.join(path, f"{name}.sublime-snippet")
              # `edit` : {path}
              with open(f"{path}", "w") as file:
                file.write(f"{snippet}")
              
            elif "." in x:
              pass
            else:
              name = x
              snippet = f"""<snippet>
  <content><![CDATA[
${{1:s.}}{name}
]]></content>
  <tabTrigger>{name.lower().replace("_", "")}</tabTrigger>
  <scope>source.ts</scope>
  <description>{name}</description>
</snippet>"""
              path = os.path.join(f"p5", f"{module}", f"{key}")
              if not os.path.exists(f"{path}"):
                os.makedirs(f"{path}")
              path = os.path.join(path, f"{name.lower().replace('_', '')}.sublime-snippet")
              # `edit` : {path}
              with open(f"{path}", "w") as file:
                file.write(f"{snippet}")                  


if __name__ == '__main__':
  main()