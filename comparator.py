from dbhandler import *
import os
import pefile
import pyimpfuzzy
import ssdeep

test_path="D:\\SRC\\imphash\\test"

for i in os.listdir(test_path):
	fname = i
	print(i)
	fpath = test_path+"//"+i
	pe = pefile.PE(fpath)
	imph = pe.get_imphash()
	fuzimp=pyimpfuzzy.get_impfuzzy(fpath)
	fuzfhash = ssdeep.hash_from_file(fpath)
	print(fpath+'--'+imph+'--'+fuzimp+'--'+fuzfhash)
	dbsearch(fpath,fuzimp)
#   dbInsert(fname,md5,sha256,imph,fuzimp,fuzfhash)