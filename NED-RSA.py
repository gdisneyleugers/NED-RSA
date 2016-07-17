from sys import argv,exit
import primefac
import gmpy
from Crypto.PublicKey import RSA
try:
	spacer = "-" * 64
	pub_input = argv[1]
	raw_key = file(pub_input, 'r').read()
	pub_key = RSA.importKey("""{0}""".format(raw_key))
	n = long((pub_key.n))
	print spacer
	print "N: {0}".format(n)
	e = long((pub_key.e))
	print spacer
	print "E: {0}".format(e)
	print spacer
	pnq = list(primefac.primefac(n))
	p = str(pnq[0]).strip('mqz(L)')
	q = str(pnq[1]).strip('mqz(L)')
	print "P: {0}".format(p)
	print spacer
	print "Q: {0}".format(q)
	print spacer
	d = long(gmpy.invert(e,(int(p)-1)*(int(q)-1)))
	print "D: {0}".format(d)
	print spacer
	key = RSA.construct((n,e,d))
	print key.exportKey()
except IndexError:
	print "RSA NED reconstruction attack"
	print "{0} pub-key.pem".format(argv[0])
	exit()
except ValueError:
	print "Key size to large!"
	exit()
except KeyboardInterrupt:
	print "For Science!"
	exit()
