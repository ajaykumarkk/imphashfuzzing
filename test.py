import pyimpfuzzy

import sys

#hash1 = pyimpfuzzy.get_impfuzzy("D:\\SRC\\imphash\\samples\\Git-2.20.1-64-bit.exe")
#hash2 = pyimpfuzzy.get_impfuzzy("D:\\SRC\\imphash\\samples\\vlc-3.0.6-win64.exe")
hash1="48:o4/c+4QjuC5Q4FNO0MeAXGo4E/gjF5J/RscXr9ubudS19WOG/iB:oc94A5TNO0MHYXrMeS1oXiB"
hash2="48:I2/dKEE8QyoOttGarYau/LsquqQEHA9vPel1bEX/KA/6UyJra8ESvS55w+0o4Rn2:ImdKNstGoYa6ZGxfOBA"
print("ImpFuzzy1: %s" % hash1)
print ("ImpFuzzy2: %s" % hash2)

print ("Compare: %i" % pyimpfuzzy.hash_compare(hash1, hash2))