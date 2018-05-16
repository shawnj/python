#update the number in a version file
import sys

FILELOC = sys.argv[1]

ver = open(FILELOC+"/VERSION").readline()

if ver is not None:
    line = list(ver.rstrip())
    new_patch_num = int(line[len(line)-1])+1
    line[len(line)-1] = str(new_patch_num)
    ver = ''.join(line)

    file = open(FILELOC+"/VERSION", 'w')
    file.write(ver)
    file.close()
    print(ver)
    
else:
    print("No Version Number.")