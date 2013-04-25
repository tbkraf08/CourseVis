#!/usr/bin/env python

import json
import traceback # traceback.print_exc(file=sys.stdout)
import time
import sys

d = [
{'name':'Bioinformatics'},
{'name':'Computer Science'},
{'name':'Health Informatics'},
{'name':'Information Technology'}
]

bioCon = [
{'name':'Big Data in Bioinformatics', "size":100},
{'name':'Computational Biophysics', "size":100},
{'name':'Computational Mass Spectrometry', "size":100},
{'name':'Genome-Wide Association Analysis', "size":100},
{'name':'High-Throughput Studies', "size":100},
{'name':'Metagenomics', "size":100},
{'name':'Plant Genomics', "size":100},
{'name':'Structural Bioinformatics', "size":100},
{'name':'Systems Biology', "size":100}
]

csCon = [
{'name':'Data Management', 'size':100},
{'name':'Networking and Distributed Computing', 'size':100},
{'name':'Visualization and Computer Graphics', 'size':100},
{'name':'Intelligent & Interactive Systems', 'size':100},
{'name':'Applications', 'size':100}
]

healthCon = [
{'name':'Programmer & Software Engineer', 'size':100},
{'name':'HIM / Exchange Specialist', 'size':100},
{'name':'HI Privacy and Security Specialist', 'size':100},
{'name':'Health Analyst', 'size':100}
]

infoCon = [
{'name':'Human-Computer Interaction Concentration', 'size':100},
{'name':'Information Security and Privacy concentration', 'size':100},
{'name':'Advanced Data and Knowledge Discovery Concentration', 'size':100},
{'name':'Information Technology Management Concentration', 'size':100},
{'name':'Software Systems Design and Engineering Concentration', 'size':100}
]

d[0]['children'] = bioCon
d[1]['children'] = csCon
d[2]['children'] = healthCon
d[3]['children'] = infoCon


def main(args):
	with open('deptInfo.json', 'wb') as outfile:
		json.dump(d, outfile)

if __name__ == '__main__':
	print '\n\nUsage:\npython jsonFileCreator.py'

	argv = sys.argv[1:]
	args = {}
	if argv:
		args = {}

		# there should be an specifier for each parameter
		# so there should always be an even number of args
		# set the first item to be the specifier of the dict
		# and the second is the value 
		if len(argv) % 2 == 0:
			for i in range(len(argv)-1):
				args[argv[i]] = argv[i+1]

	t0 = time.time()
	main(args)
	t1 = time.time()
	
	mins = int((t1-t0)/60)
	secs = t1-t0 - (mins*60)
	print 'elapsed time:', mins,'minutes', secs,'seconds'