import sqlite3
from sqlite3 import Error
import hashlib
import pyimpfuzzy

def dbConnect():
	conn = sqlite3.connect('Malware_Data.db')
	return conn
	print("Connected Successfully")

def dbCreate():
	conn=dbConnect()
	conn.execute(''' CREATE TABLE if not exists  MalwareDump(id INTEGER PRIMARY KEY AUTOINCREMENT ,name STRING,md5 STRING,sha256 STRING,imphash STRING,fuzImp STRING,fuzfhash STRING,family STRING);''')

	#print("Table Created Successfully")

def dbInsert(nm,m,s,imp,fimp,ffh):
	conn=dbConnect()
	c=conn.cursor()
	c.execute('INSERT INTO MalwareDump(id,name,md5,sha256,imphash,fuzImp,fuzfhash) values(NULL,"{}","{}","{}","{}","{}","{}");'.format(nm,m,s,imp,fimp,ffh))
	conn.commit()
	conn.close()
	print("Inserted TO DB : "+nm)

def unprocessedhandling(h):
	conn=dbConnect()
	c=conn.cursor()
	for hash in h:
		c.execute('UPDATE VT set notinvt = {} WHERE md5="{}";'.format(1,hash))
		conn.commit()
	conn.close()
	return

def md5Checksum(filePath):
	with open(filePath, 'rb') as fh:
		m = hashlib.md5()
		while True:
			data = fh.read(8192)
			if not data:
				break
			m.update(data)
		return m.hexdigest()


def sha256checksum(path):
	sha256_hash = hashlib.sha256()
	with open(path,"rb") as f:
		for byte_block in iter(lambda: f.read(4096),b""):
			sha256_hash.update(byte_block)
		return sha256_hash.hexdigest()

def dbsearch(path,finp):
	conn = dbConnect()
	c = conn.cursor()
	cout = c.execute('select fuzImp from MalwareDump;')
	rows = cout.fetchall()
	for i in rows:
		print(path+"--"+str(pyimpfuzzy.hash_compare(finp, i)))
