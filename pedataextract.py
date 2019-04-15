from dbhandler import *
import os
import pefile
import pyimpfuzzy
import ssdeep


mal_path = "D:\\SRC\\imphash\\samples"
dbCreate()
print("--")
for i in os.listdir(mal_path):
	fname = i
	print(i)
	fpath = mal_path+"//"+i
	print(fpath)
	md5 = md5Checksum(fpath)
	sha256 = sha256checksum(fpath)
	pe = pefile.PE(fpath)
	imph = pe.get_imphash()
	fuzimp=pyimpfuzzy.get_impfuzzy(fpath)
	fuzfhash = ssdeep.hash_from_file(fpath)
	print(fpath+'--'+md5+'--'+sha256+'--'+imph+'--'+fuzimp+'--'+fuzfhash)
	#dbInsert(fname,md5,sha256,imph,fuzimp,fuzfhash)