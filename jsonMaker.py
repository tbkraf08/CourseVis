#!/usr/bin/env python
import json

# paste the results into http://jsonformatter.curiousconcept.com/ to make the output pleasant 
college = {}
college['name'] = 'College of Computing & Informatics'

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

college['children'] = d

with open('deptInfo.json', 'wb') as outfile:
	json.dump(college, outfile)