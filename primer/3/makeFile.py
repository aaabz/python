import os

filename=raw_input("filename:")
if os.path.exists(filename):
    print "file exist"
else:
    exit()


fd=open(filename,'w')
fd.writelines("test")
fd.close()

print "done"

