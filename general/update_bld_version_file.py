import sys

FILELOC = sys.argv[1]
BUILDSITE = sys.argv[2]
BUILDNUM = sys.argv[3]

ver = open(FILELOC +"/"+BUILDSITE.upper()).readline()

if ver is not None:

    file = open(FILELOC +"/"+BUILDSITE.upper(), 'w')
    file.write(BUILDNUM)
    file.close()

else:
    print("No Version Number.")
