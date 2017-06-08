import markdown
from sys import argv, exit

if len(argv) <= 1:
    print "ERROR: Must provide source file."
    exit()

fin = open(argv[1], 'r')
outFile = argv[1].split(".")[0] + ".html"
fout = open(outFile, 'w')

html = markdown.markdown(fin.read())
print html
fout.write(html)

fin.close()
fout.close()
