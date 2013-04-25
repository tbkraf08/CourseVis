#!/usr/bin/env python
import json

school = {}
school['name'] = 'UNCC'

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
{'children':[] ,'name':'Data Management', 'size':100},
{'children':[] ,'name':'Networking and Distributed Computing', 'size':100},
{'children':[] ,'name':'Visualization and Computer Graphics', 'size':100},
{'children':[] ,'name':'Intelligent & Interactive Systems', 'size':100},
{'children':[] ,'name':'Applications', 'size':100}
]

csCon[0]['children'].append({'name':'ITCS 6155 Knowledge Based Systems', 'size':100})
csCon[0]['children'].append({'name':'ITCS 6157 Visual Databases', 'size':100})
csCon[0]['children'].append({'name':'ITCS 6160 Database Systems', 'size':100})
csCon[0]['children'].append({'name':'ITCS 6161 Advanced Topics in Database Systems', 'size':100})
csCon[0]['children'].append({'name':'ITCS 6162 Knowledge Discovery in Databases', 'size':100})
csCon[0]['children'].append({'name':'ITCS 6163 Data Warehousing', 'size':100})


csCon[1]['children'].append({'name':'ITCS 5145 Parallel Computing','size':100})
csCon[1]['children'].append({'name':'ITCS 5146 Grid Computing','size':100})
csCon[1]['children'].append({'name':'ITCS 6132 Modeling & Analysis of Communication Networks','size':100})
csCon[1]['children'].append({'name':'ITCS 6166 Computer Networks','size':100})
csCon[1]['children'].append({'name':'ITCS 6167 Advanced Networking Protocols','size':100})
csCon[1]['children'].append({'name':'ITCS 6168 Wireless Communications','size':100})



csCon[2]['children'].append({'name':'ITCS 5121 Information Visualization','size':100})
csCon[2]['children'].append({'name':'ITCS 5122 Visual Analytics','size':100})
csCon[2]['children'].append({'name':'ITCS 5123 Visualization and Visual Communication','size':100})
csCon[2]['children'].append({'name':'ITCS 6120 Computer Graphics','size':100})
csCon[2]['children'].append({'name':'ITCS 6124 Illustrative Visualization','size':100})
csCon[2]['children'].append({'name':'ITCS 6126 Large Scale Information Visualization','size':100})
csCon[2]['children'].append({'name':'ITCS 6127 Real-time Rendering Engines','size':100})
csCon[2]['children'].append({'name':'ITCS 6128 3D Display and Advanced Interfaces','size':100})
csCon[2]['children'].append({'name':'ITCS 6140 Data Visualization','size':100})



csCon[3]['children'].append({'name':'ITCS 5152 Computer Vision','size':100})
csCon[3]['children'].append({'name':'ITCS 6050 Topics in Intelligent Systems','size':100})
csCon[3]['children'].append({'name':'ITCS 6111 Evolutionary Computation','size':100})
csCon[3]['children'].append({'name':'ITCS 6125 Virtual Environments','size':100})
csCon[3]['children'].append({'name':'ITCS 6134 Digital Image Processing','size':100})
csCon[3]['children'].append({'name':'ITCS 6150 Intelligent Systems','size':100})
csCon[3]['children'].append({'name':'ITCS 6151 Intelligent Robotics','size':100})
csCon[3]['children'].append({'name':'ITCS 6156 Machine Learning','size':100})
csCon[3]['children'].append({'name':'ITCS 6158 Natural Language Processing','size':100})
csCon[3]['children'].append({'name':'ITCS 6267 Intelligent Information Retrieval','size':100})
csCon[3]['children'].append({'name':'ITCS 6500 Complex Adaptive Systems','size':100})


csCon[4]['children'].append({'name':'ITCS 5133 Numerical Computation Methods and Analysis','size':100})
csCon[4]['children'].append({'name':'ITCS 5180 Mobile Application Development','size':100})
csCon[4]['children'].append({'name':'ITCS 5230 Introduction to Game Design and development','size':100})
csCon[4]['children'].append({'name':'ITCS 5231 Advanced Game Design and Development','size':100})
csCon[4]['children'].append({'name':'ITCS 5232 Game Design and Development Studio','size':100})
csCon[4]['children'].append({'name':'ITCS 5235 Game Engine Construction','size':100})
csCon[4]['children'].append({'name':'ITCS 5236 Artificial Intelligence for Computer Games','size':100})
csCon[4]['children'].append({'name':'ITCS 5237 Audio Processing for Entertainment Computing','size':100})
csCon[4]['children'].append({'name':'ITCS 6153 Neural Networks','size':100})
csCon[4]['children'].append({'name':'ITCS 6159 Intelligent Tutoring Systems','size':100})
csCon[4]['children'].append({'name':'ITCS 6165 Coding and Information Theory','size':100})
csCon[4]['children'].append({'name':'ITCS 6222 Biomedical Signal Processing','size':100})
csCon[4]['children'].append({'name':'ITCS 6224 Biomedical Image Processing','size':100})
csCon[4]['children'].append({'name':'ITCS 6226 Bioinformatics ','size':100})
csCon[4]['children'].append({'name':'ITCS 6228 Medical Informatics','size':100})


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

with open('readme.json', 'wb') as outfile:
	json.dump(college, outfile)