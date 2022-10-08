"""Hops flask middleware example"""
from flask import Flask
import ghhops_server as hs
import rhino3dm


# register hops app as middleware
app = Flask(__name__)
hops: hs.HopsFlask = hs.Hops(app)


# flask app can be used for other stuff drectly
@app.route("/help")
def help():
    return "Welcome to Grashopper Hops for CPython!"


@hops.component(
    "/binmult",
    inputs=[hs.HopsNumber("A"), hs.HopsNumber("B")],
    outputs=[hs.HopsNumber("Multiply")],
)
def BinaryMultiply(a: float, b: float):
    return a * b

"""
@hops.component(
    "/add",
    name="Add",
    nickname="Add",
    description="Add numbers with CPython",
    inputs=[
        hs.HopsNumber("A", "A", "First number"),
        hs.HopsNumber("B", "B", "Second number"),
    ],
    outputs=[hs.HopsNumber("Sum", "S", "A + B")]
)
def add(a: float, b: float):
    return a + b


@hops.component(
    "/pointat",
    name="PointAt",
    nickname="PtAt",
    description="Get point along curve",
    icon="pointat.png",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsNumber("t", "t", "Parameter on Curve to evaluate")
    ],
    outputs=[hs.HopsPoint("P", "P", "Point on curve at t")]
)
def pointat(curve: rhino3dm.Curve, t=0.0):
    return curve.PointAt(t)


@hops.component(
    "/srf4pt",
    name="4Point Surface",
    nickname="Srf4Pt",
    description="Create ruled surface from four points",
    inputs=[
        hs.HopsPoint("Corner A", "A", "First corner"),
        hs.HopsPoint("Corner B", "B", "Second corner"),
        hs.HopsPoint("Corner C", "C", "Third corner"),
        hs.HopsPoint("Corner D", "D", "Fourth corner")
    ],
    outputs=[hs.HopsSurface("Surface", "S", "Resulting surface")]
)
def ruled_surface(a: rhino3dm.Point3d,
                  b: rhino3dm.Point3d,
                  c: rhino3dm.Point3d,
                  d: rhino3dm.Point3d):
    edge1 = rhino3dm.LineCurve(a, b)
    edge2 = rhino3dm.LineCurve(c, d)
    return rhino3dm.NurbsSurface.CreateRuledSurface(edge1, edge2)
"""

"""
Search for text in a file or across multiple files
Create, update, move, and rename files and folders
Search the Web and download online content
Update and format data in Excel spreadsheets of any size
Split, merge, watermark, and encrypt PDFs
Send reminder emails and text notifications
Fill out online forms
"""

""" 
██╗███╗   ██╗████████╗██████╗  ██████╗ ██████╗ ██╗   ██╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗
██║████╗  ██║╚══██╔══╝██╔══██╗██╔═══██╗██╔══██╗██║   ██║██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║
██║██╔██╗ ██║   ██║   ██████╔╝██║   ██║██║  ██║██║   ██║██║        ██║   ██║██║   ██║██╔██╗ ██║
██║██║╚██╗██║   ██║   ██╔══██╗██║   ██║██║  ██║██║   ██║██║        ██║   ██║██║   ██║██║╚██╗██║
██║██║ ╚████║   ██║   ██║  ██║╚██████╔╝██████╔╝╚██████╔╝╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║
╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝  ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
"""

# hello
@hops.component(
    "/hello",
    name="Hello",
    nickname="Hello",
    description="Say hello to the someone",
    inputs=[
        hs.HopsString("Name", "N", "Name of the person to say hello to")
    ],
    outputs=[hs.HopsString("Greeting", "G", "Greeting to the person")]
)
def hello(name: str):
    print (name)
    return f"Hello {name}"



if __name__ == "__main__":
    app.run(debug=True)
