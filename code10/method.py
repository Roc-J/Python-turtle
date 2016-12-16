ss = "Hello World"
print ss.upper()

tt = ss.lower()
print tt

ss = "     Hello,World    "
els = ss.count("l")
print els

print "***" + ss.strip() + "***"
print "***" + ss.lstrip() + "***"
print "***" + ss.rstrip() + "***"

news = ss.replace("o","***")
print news