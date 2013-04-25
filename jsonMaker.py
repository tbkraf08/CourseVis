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
{'name':'Genomic Biology Cluster', "size":100, 'children':[]},
{'name':'Modeling and Simulation Cluster', "size":100, 'children':[]},
{'name':'Computing and Technology Cluster', "size":100, 'children':[]},
]


bioCon[0]['children'].append({'name':'BINF 6205 Computational Molecular Evolution', 'size':100})
bioCon[0]['children'].append({'name':'BINF 6350 Biotechnology and Genomics Laboratory', 'size':100})
bioCon[0]['children'].append({'name':'BINF 6310 Advanced Statistics for Genomics', 'size':100})
bioCon[0]['children'].append({'name':'BINF 6318 Computational Proteomics and Metabolomics', 'size':100})


bioCon[1]['children'].append({'name':'BINF 6202 Computational Structural Biology', 'size':100})
bioCon[1]['children'].append({'name':'BINF 6204 Mathematical Systems Biology', 'size':100})
bioCon[1]['children'].append({'name':'BINF 6210 Numerical Methods and Machine Learning in Bioinformatics', 'size':100})
bioCon[1]['children'].append({'name':'BINF 6311 Biophysical Modeling', 'size':100})


bioCon[2]['children'].append({'name':'BINF 6210 Numerical Methods and Machine Learning in Bioinformatics', 'size':100})
bioCon[2]['children'].append({'name':'BINF 6310 Advanced Statistics for Genomics', 'size':100})
bioCon[2]['children'].append({'name':'BINF 6380 Advanced Bioinformatics Programming', 'size':100})
bioCon[2]['children'].append({'name':'BINF 6382 Accelerated Bioinformatics Programming', 'size':100})

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
{'name':'Programmer & Software Engineer', 'size':100, 'children':[]},
{'name':'HIM / Exchange Specialist', 'size':100, 'children':[]},
{'name':'HI Privacy and Security Specialist', 'size':100, 'children':[]},
{'name':'Health Analyst', 'size':100, 'children':[]}
]



healthCon[0]['children'].append({'name':'Network-Based Application Development [HCIP 5166]', 'size':100})
healthCon[0]['children'].append({'name':'Current Issues in Health Informatics [HCIP 6070]', 'size':100})
healthCon[0]['children'].append({'name':'Software System Design and Implementation [HCIP 6112]', 'size':100})
healthCon[0]['children'].append({'name':'Knowledge Discovery in Databases [HCIP 6162]', 'size':100})
healthCon[0]['children'].append({'name':'Principles of Human-Computer Interaction [HCIP 6350]', 'size':100})
healthCon[0]['children'].append({'name':'Advanced Programming for HI [HCIP 6390]', 'size':100})
healthCon[0]['children'].append({'name':'Architecting HI Systems [HCIP 6391]', 'size':100})
healthCon[0]['children'].append({'name':'Enterprise Health Information Systems [HCIP 6392]', 'size':100})
healthCon[0]['children'].append({'name':'Personalization and Recommender Systems [HCIP 6410]', 'size':100})




healthCon[1]['children'].append({'name':'Current Issues in Health Informatics [HCIP 6070]', 'size':100})
healthCon[1]['children'].append({'name':'Quality and Outcomes Management in Health Care [HCIP 6134]', 'size':100})
healthCon[1]['children'].append({'name':'Information Resources Management [HCIP 6146]', 'size':100})
healthCon[1]['children'].append({'name':'Health Law and Ethics [HCIP 6150]', 'size':100})
healthCon[1]['children'].append({'name':'Principles of Computer Networks and Databases [HCIP 6199]', 'size':100})
healthCon[1]['children'].append({'name':'Medical Practice Management [HCIP 6330]', 'size':100})
healthCon[1]['children'].append({'name':'Enterprise Health Information Systems [HCIP 6392]', 'size':100})
healthCon[1]['children'].append({'name':'Advanced Health Data Integration w/Lab [HCIP 6393]', 'size':100})



healthCon[2]['children'].append({'name':'Vulnerability Assessment and System Assurance [HCIP 5220]', 'size':100})
healthCon[2]['children'].append({'name':'Computer Forensics [HCIP 5250]', 'size':100})
healthCon[2]['children'].append({'name':'Current Issues in Health Informatics [HCIP 6070]', 'size':100})
healthCon[2]['children'].append({'name':'Quality & Outcomes Management in Health Care [HCIP 6134]', 'size':100})
healthCon[2]['children'].append({'name':'Network Security [HCIP 6167]', 'size':100})
healthCon[2]['children'].append({'name':'Principles of Information Security and Privacy [HCIP 6200]', 'size':100})
healthCon[2]['children'].append({'name':'Access Control & Security Architecture [HCIP 6210]', 'size':100})
healthCon[2]['children'].append({'name':'Information Infrastructure Protection [HCIP 6230]', 'size':100})
healthCon[2]['children'].append({'name':'Applied Cryptography [HCIP 6240]', 'size':100})




healthCon[3]['children'].append({'name':'Current Issues in Health Informatics [HCIP 6070]', 'size':100})
healthCon[3]['children'].append({'name':'Health and Disease [HCIP 6104]', 'size':100})
healthCon[3]['children'].append({'name':'Quality & Outcomes Management in Health Care  [HCIP 6134]', 'size':100})
healthCon[3]['children'].append({'name':'Information Resources Management [HCIP 6146]', 'size':100})
healthCon[3]['children'].append({'name':'Health Law and Ethics [HCIP 6150]', 'size':100})
healthCon[3]['children'].append({'name':'Knowledge Discovery in Databases [HCIP 6162]', 'size':100})
healthCon[3]['children'].append({'name':'Data Warehousing [HCIP 6163]', 'size':100})
healthCon[3]['children'].append({'name':'Analytic Epidemiology [HCIP 6260]', 'size':100})
healthCon[3]['children'].append({'name':'Medical Practice Management [HCIP 6330]', 'size':100})
healthCon[3]['children'].append({'name':'Advanced Health Data Integration w/Lab [HCIP 6393]', 'size':100})


infoCon = [
{'name':'Human-Computer Interaction Concentration', 'size':100, 'children':[]},
{'name':'Information Security and Privacy concentration', 'size':100, 'children':[]},
{'name':'Advanced Data and Knowledge Discovery Concentration', 'size':100, 'children':[]},
{'name':'Information Technology Management Concentration', 'size':100, 'children':[]},
{'name':'Software Systems Design and Engineering Concentration', 'size':100, 'children':[]},
{'name':'Design Concentration', 'size':100, 'children':[]}
]


infoCon[0]['children'].append({'name':'ITIS 6400 Principles of Human-Computer Interaction', 'size':100})
infoCon[0]['children'].append({'name':'ITIS 6410 Personalization and Recommender Systems', 'size':100})
infoCon[0]['children'].append({'name':'ITIS 6420 Usable Security and Privacy', 'size':100})
infoCon[0]['children'].append({'name':'ITCS 5121 Information Visualization', 'size':100})
infoCon[0]['children'].append({'name':'ITCS 5122 Visual Analytics', 'size':100})
infoCon[0]['children'].append({'name':'ITCS 6140 Data Visualization', 'size':100})
infoCon[0]['children'].append({'name':'ITCS 6216 Introduction to Cognitive Science', 'size':100})
infoCon[0]['children'].append({'name':'ITCS 6128 Display and Advanced Interfaces', 'size':100})



infoCon[1]['children'].append({'name':'ITIS 5220 Vulnerability Assessment and System Assurance', 'size':100})
infoCon[1]['children'].append({'name':'ITIS 5221 Secure Programming and Penetration Testing', 'size':100})
infoCon[1]['children'].append({'name':'ITIS 5250 Computer Forensics', 'size':100})
infoCon[1]['children'].append({'name':'ITIS 6150 Software Assurance', 'size':100})
infoCon[1]['children'].append({'name':'ITIS 6167 Network Security', 'size':100})
infoCon[1]['children'].append({'name':'ITIS 6210 Access Control and Security Architecture', 'size':100})
infoCon[1]['children'].append({'name':'ITIS 6220 Data Privacy', 'size':100})
infoCon[1]['children'].append({'name':'ITIS 6230 Information Infrastructure Protection', 'size':100})
infoCon[1]['children'].append({'name':'ITIS 6240 Applied Cryptography', 'size':100})
infoCon[1]['children'].append({'name':'ITIS 6362 Information Technology: Ethics, Policy, and Security', 'size':100})
infoCon[1]['children'].append({'name':'ITIS 6420 Usable Security and Privacy', 'size':100})


infoCon[2]['children'].append({'name':'ITIS 5510 Web Mining', 'size':100})
infoCon[2]['children'].append({'name':'ITIS 6520 Network Sciences', 'size':100})
infoCon[2]['children'].append({'name':'ITIS 6162 Knowledge Discovery in Databases', 'size':100})
infoCon[2]['children'].append({'name':'ITCS 6155 Knowledge-Based Systems', 'size':100})
infoCon[2]['children'].append({'name':'ITIS 6163 Data Warehousing', 'size':100})


infoCon[3]['children'].append({'name':'ITIS 6362 Information Technology Ethics, Policy, and Security', 'size':100})
infoCon[3]['children'].append({'name':'ITIS 6130 Software Requirements Engineering for Information Systems.', 'size':100})
infoCon[3]['children'].append({'name':'ITIS 6164 Online Info Systems', 'size':100})
infoCon[3]['children'].append({'name':'ITIS 6230 Information Infrastructure Protection', 'size':100})
infoCon[3]['children'].append({'name':'GEOG 6615 Advanced Seminar in Spatial Decision Support Systems', 'size':100})
infoCon[3]['children'].append({'name':'MBAD 6121 Business Information Systems', 'size':100})
infoCon[3]['children'].append({'name':'MBAD 6122 Decision Modeling and Analysis via Spreadsheets', 'size':100})
infoCon[3]['children'].append({'name':'MBAD 6202 Business Information Systems Development', 'size':100})



infoCon[4]['children'].append({'name':'ITIS 5221 Secure Programming and Penetration Testing', 'size':100})
infoCon[4]['children'].append({'name':'ITIS 5180 Mobile Application Development', 'size':100})
infoCon[4]['children'].append({'name':'ITIS 6130 Software Requirements Engineering for Information Systems.', 'size':100})
infoCon[4]['children'].append({'name':'ITIS 6140 Software Testing and Quality Assurance', 'size':100})
infoCon[4]['children'].append({'name':'ITIS 6148 Advanced OO Design and Implementation', 'size':100})
infoCon[4]['children'].append({'name':'ITIS 6164 Online Info Systems', 'size':100})
infoCon[4]['children'].append({'name':'ITIS 6210 Access Control and Security Architecture', 'size':100})
infoCon[4]['children'].append({'name':'ITIS 6362 Information Technology Ethics, Policy, and Security', 'size':100})
infoCon[4]['children'].append({'name':'ITIS 6400 Principles of Human-Computer Interaction', 'size':100})
infoCon[4]['children'].append({'name':'GEOG 6615 Advanced Seminar in Spatial Decision Support Systems', 'size':100})
infoCon[4]['children'].append({'name':'MBAD 6202 Business Information Systems Development', 'size':100})



infoCon[5]['children'].append({'name':'ITIS 5180 Mobile Application Development', 'size':100})
infoCon[5]['children'].append({'name':'ITIS 6400 Principles of Human Computer Interaction', 'size':100})
infoCon[5]['children'].append({'name':'ITIS 6500 Complex Adaptive Systems', 'size':100})
infoCon[5]['children'].append({'name':'ITIS 6880 Design-focused Independent Study', 'size':100})
infoCon[5]['children'].append({'name':'ITCS 5122 Visual Analytics', 'size':100})
infoCon[5]['children'].append({'name':'ITCS 5230 Introduction to Game Design and Development', 'size':100})
infoCon[5]['children'].append({'name':'ARCH 7201/ ITCS7201/ITIS7201 Studio Lab I', 'size':100})
infoCon[5]['children'].append({'name':'ARCH 7202/ ITCS7202/ITISS7202 Studio Lab II', 'size':100})



d[0]['children'] = bioCon
d[1]['children'] = csCon
d[2]['children'] = healthCon
d[3]['children'] = infoCon

college['children'] = d

with open('readme.json', 'wb') as outfile:
	json.dump(college, outfile)