import os

visitedDirectories = []
directoryStructure = {}

def walk(directory):
    for root, dirs, files in os.walk(directory):
        directoryStructure[root] = {}
        directoryStructure[root]["dirs"] = dirs
        directoryStructure[root]["files"] = files

def buildDirectory(directory):
    listing = directoryStructure[directory]
    print(directory)
    dirStr = startSection(directory)
    outputHeading(dirStr)
    outputFile.write('<div id="in' + dirStr + '" class="accordion-body collapse">')
    outputFile.write('<div class="accordion-inner">')
    outputFile.write("<ul>")
    for d in listing["dirs"]:
        buildDirectory(os.path.join(directory, d))
    outputFiles(listing["files"])
    outputFile.write("</ul></div></div>")
    outputFile.write("</div></div>")

def startSection(root):
    rootStr = root.replace(os.sep, "_").replace(".", "_")
    outputFile.write("<div class='accordion' id='out" + rootStr + "'><div class='accordion-group'>")

    return rootStr

def outputHeading(root):
    outputFile.write("<div class='accordion-heading'>")
    outputFile.write("<a class='accordion-toggle' data-toggle='collapse' data-parent='#out" + root + "' href='#in" + root + "'>")
    outputFile.write(root)
    outputFile.write("</a>")
    outputFile.write("</div>")

def outputFiles(files):
    for name in files:
        outputFile.write("<li>" + name + "</li>")

directory = "/Users/aswift/Downloads/PGMCalc"

outputFile = open("directory.html", "w")
outputFile.truncate()

outputFile.write("<html>")
outputFile.write("<head>")
outputFile.write('<script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>')
outputFile.write('<script src="http://netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/js/bootstrap.min.js"></script>')
outputFile.write('<link href="http://netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/css/bootstrap-combined.min.css" rel="stylesheet">')
outputFile.write("</head>")
outputFile.write("<body>")

walk(directory)
buildDirectory(directory)

outputFile.write("</body></html>")