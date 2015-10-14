import requests
import json
import sys

error = """\nERROR: %s \nCorrect usuage is python url2id.py -f <filename> or python url2id.py <id>\n"""

SOUNDCLOUD_ID = '4e13081ee9020b565401209b115c43d0'
RESOLVE_URL = 'http://api.soundcloud.com/resolve?url=%s&client_id=' + SOUNDCLOUD_ID
OUTPUT_FILENAME_EXTENSION = "_out.txt"

ids = []
msg = ""
lines = []
filemode = False

if len(sys.argv) == 2:
	lines.append(sys.argv[1])
elif len(sys.argv) == 3:
	if(sys.argv[1] != "-f"):
		msg = "INCORRECT INPUT FORMAT."
	else: 
		filemode = True
		with open(sys.argv[2], 'r') as f:
			lines = f.readlines()
else:
	msg = "NOT ENOUGH INPUTS"

if(msg):
	print error % msg
	sys.exit(1)

print "Resolving url(s) now...\n"
for l in lines:
	cur_id = json.loads(requests.get(RESOLVE_URL % l).text)['id']
	print cur_id
	ids.append(cur_id)

print ""

if(filemode):
	print "Writing output to file..."
	out_filname = sys.argv[2].split('.')[0] + OUTPUT_FILENAME_EXTENSION
	with open(out_filname, 'w') as out:
		for i in ids:
			out.write(str(i) + "\n")

	print "Output written to %s" % out_filname 