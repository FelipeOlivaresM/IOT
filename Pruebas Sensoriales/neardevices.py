from bluetooth import *
print "Performing inquiry ..."

nearby_devices = discover_devices(lookup_names = True)

print "Found %d devices" % len(nearby_devices)

for name,addr in nearby_devices:
	print "%s - %s" % (addr,name) 
