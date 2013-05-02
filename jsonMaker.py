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


bioCon[0]['children'].append({'name':'BINF 6205 Computational Molecular Evolution', 'size':100, 'details':'Test'})
bioCon[0]['children'].append({'name':'BINF 6350 Biotechnology and Genomics Laboratory', 'size':100, 'details':'Test'})
bioCon[0]['children'].append({'name':'BINF 6310 Advanced Statistics for Genomics', 'size':100, 'details':'Test'})
bioCon[0]['children'].append({'name':'BINF 6318 Computational Proteomics and Metabolomics', 'size':100, 'details':'Test'})


bioCon[1]['children'].append({'name':'BINF 6202 Computational Structural Biology', 'size':100, 'details':'Test'})
bioCon[1]['children'].append({'name':'BINF 6204 Mathematical Systems Biology', 'size':100, 'details':'Test'})
bioCon[1]['children'].append({'name':'BINF 6210 Numerical Methods and Machine Learning in Bioinformatics', 'size':100, 'details':'Test'})
bioCon[1]['children'].append({'name':'BINF 6311 Biophysical Modeling', 'size':100, 'details':'Test'})


bioCon[2]['children'].append({'name':'BINF 6210 Numerical Methods and Machine Learning in Bioinformatics', 'size':100, 'details':'Test'})
bioCon[2]['children'].append({'name':'BINF 6310 Advanced Statistics for Genomics', 'size':100, 'details':'Test'})
bioCon[2]['children'].append({'name':'BINF 6380 Advanced Bioinformatics Programming', 'size':100, 'details':'Test'})
bioCon[2]['children'].append({'name':'BINF 6382 Accelerated Bioinformatics Programming', 'size':100, 'details':'Test'})

csCon = [
{'children':[] ,'name':'Data Management', 'size':100},
{'children':[] ,'name':'Networking and Distributed Computing', 'size':100},
{'children':[] ,'name':'Visualization and Computer Graphics', 'size':100},
{'children':[] ,'name':'Intelligent & Interactive Systems', 'size':100},
{'children':[] ,'name':'Applications', 'size':100}
]

csCon[0]['children'].append({'name':'ITCS 6155 Knowledge Based Systems', 'size':100, 'details':'Knowledge systems; knowledge discovery; association rules; query languages and operational semantics; decision systems; cooperative and collaborative systems; tree structured information systems; tree structured query languages; flexible query answering; chase algorithm based on rules; local and global ontologies; action rules; optimization problems for query answering systems', 'prereq':'ITCS 6162, consent of the department', 'offered':'Spring Evenings'})
csCon[0]['children'].append({'name':'ITCS 6157 Visual Databases', 'size':100, 'details':'Representation of visual content, querying visual databases, content-based interactive browsing and navigation, system architecture, similarity models, indexing visual databases, data models and knowledge structures, image retrieval by similarity, and video retrieval by content', 'prereq':'ITCS 6160 or Equivalent', 'offered':'Even Years, Fall Evenings'})
csCon[0]['children'].append({'name':'ITCS 6160 Database Systems', 'size':100, 'details':'Introduction to principles of database design, and survey of alternative database organizations and structures  Logical database organization; schemas; subschemas; data description languages; hierarchical, network, and relational databases; database management systems; normal forms', 'prereq':'ITCS 6114, consent of the department', 'offered':'Fall, Spring Evenings'})
csCon[0]['children'].append({'name':'ITCS 6161 Advanced Topics in Database Systems', 'size':100, 'details':'Continuation of ITCS 6160  Topics include deductive databases; semantic query processing; intelligent and cooperative query languages; distributed databases; active databases; heterogeneous databases, multimedia databases; data and knowledge interchange; multidatabase systems; very large databases', 'prereq':'ITCS 6160 or Equivalent', 'offered':'Odd Years, Fall Evenings'})
csCon[0]['children'].append({'name':'ITCS 6162 Knowledge Discovery in Databases', 'size':100, 'details':'he entire knowledge discovery process is covered in this course  Topics include: setting up a problem, data preprocessing and warehousing, data mining in search for knowledge, knowledge evaluation, visualization and application in decision making  A broad range of systems, such as OLAP, LERS, DatalogicR+, C4 5, AQ15, Forty-Niner, CN2, QRAS, and discretization algorithms are covered', 'prereq':'ITCS 6160, Consent of the dept.', 'offered':'Fall Evenings'})
csCon[0]['children'].append({'name':'ITCS 6163 Data Warehousing', 'size':100, 'details':'use of data in discovery of knowledge and decision making; the limitations of relational databases and SQL queries; the warehouse data models: multidimensional, star, snowflake; architecture of data warehouse and the process of warehouse construction; data consolidation from various sources; optimization; techniques for data transformation and knowledge extraction; relations with enterprise modeling', 'prereq':'ITCS 6160 or Equivalent', 'offered':'Spring Evenings'})


csCon[1]['children'].append({'name':'ITCS 5145 Parallel Computing','size':100, 'details':'Types of parallel computers, programming techniques for multiprocessor and multicomputer systems, parallel strategies, algorithms, and languages', 'prereq':'ITCS 1215, ITCS 3182, consent of department', 'offered':'Spring'})
csCon[1]['children'].append({'name':'ITCS 5146 Grid Computing','size':100, 'details':'Grid computing software components, standards, web services, security mechanisms, schedulers and resource brokers, workflow editors, grid portals, grid computing applications', 'prereq':'ITCS 1215, Graduate Standing', 'offered':'On Demand'})
csCon[1]['children'].append({'name':'ITCS 6132 Modeling & Analysis of Communication Networks','size':100, 'details':'The objective of this course is to develop an understanding of modeling and analysis techniques for communication systems and networks  The intent is to enable the student to understand how to comparatively analyze the cost and performance impact of network architecture and protocol design decisions  Modeling techniques for analytical analysis, simulation based analysis, and measurement based analysis will be presented  Concepts covered include validation/verification of models, workload characterization, metric selection, presentation and interpretation of results  A semester long analysis project will be undertaken', 'prereq':'A course in communication networks, consent of the department', 'offered':'Fall, Even Years'})
csCon[1]['children'].append({'name':'ITCS 6166 Computer Networks','size':100, 'details':'Introduction to the concepts of communication networks; Types of networks; wired and wireless media; communication architectures; network protocols; coding and modulation; multiplexing and multiple access; error and flow control; routing; Internet Protocols; transport protocols; Assignments include implementation and analysis of network protocols', 'prereq':'knowledge of probability theory', 'offered':'Fall, Evenings'})
csCon[1]['children'].append({'name':'ITCS 6167 Advanced Networking Protocols','size':100, 'details':'This course focuses on advanced networking concepts and protocols related to the design, implementation, integration, and management of networking and communication systems  Topics include: topology control protocols, ad hoc routing protocols, power management protocols, distributed data processing protocols for various networking systems (Internet, wireless mesh networks, ad hoc networks, sensor networks, peer-to-peer networks)', 'prereq':'ITCS 6166, ITCS 6168', 'offered':'Spring Evenings'})
csCon[1]['children'].append({'name':'ITCS 6168 Wireless Communications','size':100, 'details':'The course provides an overview of mobile systems and wireless networking technologies  Emphasis will be on resource management, routing and quality of service at the MAC and networking layers for mobile systems  Students will undertake a semester long research project to survey the research literature and identify specific challenges for cellular telecommunications, wireless LANS, ad hoc networks, mesh networks or sensor networks', 'prereq':'Graduate standing in CS SIS ECE, Optics, a prior course in networking', 'offered':'Fall, Odd Years'})



csCon[2]['children'].append({'name':'ITCS 5121 Information Visualization', 'prereq':'graduate standing', 'size':100, 'details':'Information visualization concepts, theories, design principles, popular techniques, evaluation methods, and information visualization applications', 'prereq':'graduate standing', 'offered':'Spring Evenings'})
csCon[2]['children'].append({'name':'ITCS 5122 Visual Analytics','prereq':'any of STAT 1220 1221 1222 2122, 2223, approval of the instructor','size':100, 'details':'This course introduces the new field of visual analytics, which integrates interactive analytical methods and visualization   Topics include: critical thinking, visual reasoning, perception/cognition, statistical and other analysis techniques, principles of interaction, and applications', 'prereq':'any of STAT 1220 1221 1222 2122, 2223, approval of the instructor', 'offered':'Fall Evenings'})
csCon[2]['children'].append({'name':'ITCS 5123 Visualization and Visual Communication','prereq':'none','size':100, 'details':'Understanding the relatively technical field of visualization from the point of view of visual communication, this course draws connections with photography, design, illustration, aesthetics, and art  Both technical and theoretical aspects of the various fields are covered, and the connections between them are investigated', 'prereq':'None', 'offered':'Spring Evenings'})
csCon[2]['children'].append({'name':'ITCS 6120 Computer Graphics','prereq':'full graduate standing, consent of the department','size':100, 'details':'Introduction to the design and implementation of interactive graphics systems  Raster and vector display systems, I/O devices; graphics primitives and their attributes; raster algorithms and clipping; 2D/3D geometric transformations; 3D viewing and projections; hierarchical and procedural models; surface representation; color and lighting models; rendering algorithms; global illumination and texture mapping', 'prereq':'full graduate standing, consent of the department', 'offered':'Fall Evenings'})
csCon[2]['children'].append({'name':'ITCS 6124 Illustrative Visualization','prereq':'ITCS 4120, ITCS 5120','size':100, 'details':'This course focuses on advanced concepts and techniques related to the design, implementation, integration, and management of illustrative visualization and computer graphics  Topics include various advanced visualization topics: feature extraction, non-photorealistic rendering, point-based rendering, hardware-accelerated rendering, segmentation, image generation, animation, evaluation, design, and interaction', 'prereq':'ITCS 4120, ITCS 5120', 'offered':'Spring Evenings'})
csCon[2]['children'].append({'name':'ITCS 6126 Large Scale Information Visualization','prereq':'ITCS 4121, ITCS 5121','size':100, 'details':'Concept, theory, design principles, data processing techniques, and visual metaphors and interaction techniques for massive, multi-dimensional, multi-source, time-varying information exploration', 'prereq':'ITCS 4121, ITCS 5121', 'offered':'On Demand'})
csCon[2]['children'].append({'name':'ITCS 6127 Real-time Rendering Engines','prereq':'ITCS 5120, ITCS 6120','size':100, 'details':'This course focuses on advanced concepts and techniques employed in building real-time rendering systems that support a high level of realism as well as handle large geometric models  Topics include: modern graphics hardware, programmable shaders, shadow and environment mapping, image-based modeling and rendering, large data models (simplification, level of detail), high quality interactive rendering', 'prereq':'ITCS 5120, ITCS 6120', 'offered':'On Demand'})
csCon[2]['children'].append({'name':'ITCS 6128 3D Display and Advanced Interfaces','prereq':'ITCS 4120, ITCS 6120','size':100, 'details':'The course covers the fundamentals of 3D display hardware and software technology  Topics include: human visual spatial perception of natural and synthetic 3D images, 3D display hardware, human computer interface algorithms for effective stereoscopic display, 3D display rendering techniques ', 'prereq':'ITCS 4120, ITCS 6120', 'offered':'On Demand'})
csCon[2]['children'].append({'name':'ITCS 6140 Data Visualization','prereq':'Full graduate standing, consent of the department','size':100, 'details':'Emphasis on the methodology and application of data visualization to scientific and engineering data; data types and models; visualization methods; volume visualization; scalar, vector and tensor fields; multi-variate visualization; visualization systems and models; visualization applications; visualization software and hardware; research issues and future trends', 'prereq':'Full graduate standing, consent of the department', 'offered':'On Demand'})



csCon[3]['children'].append({'name':'ITCS 5152 Computer Vision','size':100, 'details':'General introduction to Computer Vision and its application  Topics include low-level vision, 2D and 3D segmentation, 2D description, 2D recognition, 3D description and model-based recognition, and interpretation', 'prereq':'ITCS 1215, MATH 2164', 'offered':'Spring, Odd Years'})
csCon[3]['children'].append({'name':'ITCS 6050 Topics in Intelligent Systems','size':100, 'details':'Topics in intelligent systems selected to supplement the regular course offerings  May be repeated for credit as topics vary', 'prereq':'Consent of the Dept.', 'offered':'On Demand'})
csCon[3]['children'].append({'name':'ITCS 6111 Evolutionary Computation','size':100, 'details':'General introduction to optimization problems  Optimization techniques: hill climbing, simulated annealing, evolution strategies, and genetic algorithms  Evolution programming techniques', 'prereq':'ITCS 6114, consent of the department', 'offered':'Even Spring Evenings'})
csCon[3]['children'].append({'name':'ITCS 6125 Virtual Environments','size':100, 'details':'This course will cover the current state of the art in the design and implementation of Virtual Environments  Topics covered will include: position tracking, design of head-traced and head-mounted displays, stereoscopic display, presence in virtual environments, 3D user interface design, and applications of VEs  Previous experience in computer graphics or 3D game design is helpful but not required', 'prereq':'Graduate Standing', 'offered':'On Demand'})
csCon[3]['children'].append({'name':'ITCS 6134 Digital Image Processing','size':100, 'details':'Image perception; image types/applications; image restoration and enhancement; edge/boundary detection; image transformation; image segmentation; statistical and syntactical pattern recognition; image information measures and compression', 'prereq':'full graduate standing, consent of the department Cross listed as ECGR 6118', 'offered':'Fall Evenings'})
csCon[3]['children'].append({'name':'ITCS 6150 Intelligent Systems','size':100, 'details':'To introduce core ideas in AI  Heuristic versus algorithmic methods; problem solving; game playing and decision making; automatic theorem proving; pattern recognition; adaptive learning; projects to illustrate theoretical concepts', 'prereq':'full graduate standing, consent of the department', 'offered':'Fall Evenings'})
csCon[3]['children'].append({'name':'ITCS 6151 Intelligent Robotics','size':100, 'details':'General introduction to spatial descriptions and transformations, and manipulator position and motion  More study on robot planning, programming, sensing, vision, and CAD/CAM', 'prereq':'ITCS 1215, MATH 2164', 'offered':'Odd, Spring Evenings'})
csCon[3]['children'].append({'name':'ITCS 6156 Machine Learning','size':100, 'details':'Machine learning methods and techniques including: acquisition of declarative knowledge; organization of knowledge into new, more effective representations; development of new skills through instruction and practice; and discovery of new facts and theories through observation and experimentation', 'prereq':'ITCS 6150, consent of the department', 'offered':'Odd Years, Fall '})
csCon[3]['children'].append({'name':'ITCS 6158 Natural Language Processing','size':100, 'details':'Principles, methodologies, and programming methods of natural language processing including foundations of natural language understanding, namely: lexical, syntactic, and semantic analysis, discourse integration, and pragmatic and morphological analysis', 'prereq':'ITCS 6150', 'offered':'On Demand'})
csCon[3]['children'].append({'name':'ITCS 6267 Intelligent Information Retrieval','size':100, 'details':'Topics include: definition of the information retrieval problem, modeling the information retrieval problem, evaluation of information retrieval, query languages and operations, text processing, indexing and searching, parallel and distributed information retrieval, user interface and visualization, multimedia information retrieval, and information retrieval applications', 'prereq':'ITCS 6114', 'offered':'On Demand'})
csCon[3]['children'].append({'name':'ITCS 6500 Complex Adaptive Systems','size':100, 'details':'Cross listed as ITIS 6500/8500  Prerequisite: Permission of instructor  Complex adaptive systems (CAS) are networked (agents/part interact with their neighbors and, occasionally, distant agents), nonlinear (the whole is greater than the sum of its parts), adaptive (the system learns to change with its environment), open (new resources are being introduced into the environment), dynamic (the change is a norm), emergent (new, unplanned features of the system get introduced through the interaction of its parts/agents), and self-organizing (the parts organize themselves into a hierarchy of subsystems of various complexity)  Ant colonies, networks of neurons, the immune system, the Internet, social institutions, organizations of cities, and the global economy are a few examples where the behavior of the whole is much more complex than the behavior of the parts  This course will cover those and similar topics in an interactive manner  Examples of our current research effort will be provided  Topics include: Self-organization; emergent properties; learning; agents; localization affect; adaptive systems; nonlinear behavior; chaos; complexity', 'prereq':'consent of the department', 'offered':'On Demand'})


csCon[4]['children'].append({'name':'ITCS 5133 Numerical Computation Methods and Analysis','size':100, 'details':'Introduction to principles and techniques behind numerical methods and algorithms that underlie modern scientific and engineering applications  Roots of equations; linear systems (direct methods, LU/QR factorization, iterative methods); Eigen values and vectors; Interpolation, Approximation; Numerical Differentiation/Integration, ODEs and PDEs', 'prereq':'ITCS 2214, either MATH 1120 or MATH 1241', 'offered':'On Demand'})
csCon[4]['children'].append({'name':'ITCS 5180 Mobile Application Development','size':100, 'details':'Mobile platforms are at the center of attention of users and organizations nowadays  Most organizations and businesses are rapidly migrating toward the cloud and need to provide a fast and easy mechanism for users to stay connected to their services  Mobile applications are the top trend nowadays given the high variety of new mobile devices and platforms such as Apple\u2019s iOS and Google\u2019s Android  In this course, students will be introduced to the foundations of mobile development and its unique requirements and constraints  Students will design and build a variety of mobile applications with a hands-on and project-based approach', 'prereq':'Full graduate standing, permission of the department', 'offered':'On Demand'})
csCon[4]['children'].append({'name':'ITCS 5230 Introduction to Game Design and development','size':100, 'details':'Basic concepts and techniques for electronic game design and development  Topics include: game history and genres, game design teams and processes, what makes a game fun, level and model design, game scripting and programming including computer graphics and animation, artificial intelligence, industry issues, and gender and games', 'prereq':'none', 'offered':'Fall'})
csCon[4]['children'].append({'name':'ITCS 5231 Advanced Game Design and Development','size':100, 'details':'Advanced concepts and techniques for electronic game design and development  This course is a project-centered course where students explore complex gameplay and interactivity  The course explores topics from the introductory course in more depth, such as: applying software engineering techniques to developing games, advanced game programming and scripting, networking, graphics, physics, audio, game data structures and algorithms, and artificial intelligence', 'prereq':'ITCS 5230', 'offered':'Spring'})
csCon[4]['children'].append({'name':'ITCS 5232 Game Design and Development Studio','size':100, 'details':'Application of advanced concepts and techniques for electronic game design and development  Teams will use engineering techniques to incorporate game programming and scripting, networking, graphics, physics, audio, game data structures and algorithms, and artificial intelligence into an electronic game  Individuals will develop a complete portfolio of prior work and the class project', 'prereq':'ITCS 5120 ITCS 5231', 'offered':'Spring Evenings'})
csCon[4]['children'].append({'name':'ITCS 5235 Game Engine Construction','size':100, 'details':'Introduction to principles and techniques behind modern computer and console game engines  Graphics Rendering Pipeline (transformations, lighting ,shading); 2D/3D Texture Mapping; Image Based Rendering; Spatial Data Structures and Acceleration Algorithms; Level of Detail; Collision Detection, Culling and Intersection Methods; Vertex/Pixel Shaders; Pipeline Optimization; Rendering Hardware', 'prereq':'ITCS 5120, Permission of Department', 'offered':'On Demand, Evenings'})
csCon[4]['children'].append({'name':'ITCS 5236 Artificial Intelligence for Computer Games','size':100, 'details':'No Desc. Available.', 'prereq':'ITCS 6150', 'offered':'No Info. Available.'})
csCon[4]['children'].append({'name':'ITCS 5237 Audio Processing for Entertainment Computing','size':100, 'details':'Introduction to the principles and applications of audio (digital signal) processing focusing on entertainment domains  Topics include: analysis of signals, transforms, digital filter design techniques, audio engine development, file encoding/decoding, spatial sound rendering, optimization, and advanced audio techniques', 'prereq':'MATH 1242 MATH 2164, ITCS 6114, equivalents', 'offered':'On Demand.'})
csCon[4]['children'].append({'name':'ITCS 6153 Neural Networks','size':100, 'details':'Topics include: Basic notions and models of artificial neural nets; single layer neural classifiers; multilayer one-way neural nets; single layer feedback networks; neural models of associative memory; self organizing neural nets; translation between neural networks and knowledge bases; applications of neural networks', 'prereq':'ITCS 6114', 'offered':'On Demand'})
csCon[4]['children'].append({'name':'ITCS 6159 Intelligent Tutoring Systems','size':100, 'details':'This course introduces the issues relevant to creating adaptive learning systems using artificial intelligence and includes a project to build a small Intelligent Tutoring System (ITS)  Topics include: representation of knowledge and cognition, ITS design, adaptive user interfaces, design and evaluation of feedback, experimental methods, educational data mining, history of intelligent tutoring, tutor authoring, and issues for implementation', 'prereq':'Graduate standing, permission of the instructor', 'offered':'On Demand'})
csCon[4]['children'].append({'name':'ITCS 6165 Coding and Information Theory','size':100, 'details':'Information theory; coding theory; Shannon theorem; Markov process; channel capacity; data transmission codes; error correcting codes; data compression; data encryption', 'prereq':'knowledge of probability theory', 'offered':'On Demand'})
csCon[4]['children'].append({'name':'ITCS 6222 Biomedical Signal Processing','size':100, 'details':'Topics include: Fundamental techniques in processing, analysis, feature extraction, and classification of complex signals; origin and processing techniques for biomedical signals, including ECG, ENG, EEG, MEG, ERG, EMG, respiratory signals, blood sound, and pressure signals', 'prereq':'Graduate standing', 'offered':'On Demand'})
csCon[4]['children'].append({'name':'ITCS 6224 Biomedical Image Processing','size':100, 'details':'Topics include: Review of image processing and pattern recognition (2-D Fourier transforms, 2-D Wavelet transform, denoising of medical images); origin and processing of X-ray images; CT images; MRI images; ultrasonic images; PET images; thermal images; electrical impedance images; cross-registration between images of different source; stereotactic neurosurgery; stereotactic radiosurgery/radiotherapy; robot-assisted surgery', 'prereq':'Graduate standing, Math 2164, its equivalent', 'offered':'On Demand'})
csCon[4]['children'].append({'name':'ITCS 6226 Bioinformatics ','size':100, 'details':'Brief Review of molecular biology, proteins and their classifications, DNA, RNA, and using microarrays and gene chips for sequencing; review of computational techniques for bioinformatics, expectation maximization, Bayesian classifiers, dynamic programming, information theory and entropy analysis, Markov chain models, and neural networks; computational techniques for local and multiple sequence alignment; application of Markov chains in finding genes; using information theory to estimate binding sites, start Codon prediction; RNA secondary structure prediction; computational techniques for protein function prediction; Advanced signal processing techniques in feature extraction from protein sequences', 'prereq':'Graduate standing', 'offered':'On Demand'})
csCon[4]['children'].append({'name':'ITCS 6228 Medical Informatics','size':100, 'details':'This course focuses on methods and techniques used in storage, communication, processing, analysis, integration, management, and distribution of medical information  The course emphasizes the applications of telemedicine and intelligent computer-aided decision making systems in different medical and surgical systems  The course also discusses the computational methods to accept or reject a new drug or a new treatment for a given disease', 'prereq':'Graduate standing', 'offered':'On Demand, Evenings'})


healthCon = [
{'name':'Programmer & Software Engineer', 'size':100, 'children':[]},
{'name':'HIM / Exchange Specialist', 'size':100, 'children':[]},
{'name':'HI Privacy and Security Specialist', 'size':100, 'children':[]},
{'name':'Health Analyst', 'size':100, 'children':[]}
]



healthCon[0]['children'].append({'name':'Network-Based Application Development [HCIP 5166]', 'size':100, 'details':'Test'})
healthCon[0]['children'].append({'name':'Current Issues in Health Informatics [HCIP 6070]', 'size':100, 'details':'Test'})
healthCon[0]['children'].append({'name':'Software System Design and Implementation [HCIP 6112]', 'size':100, 'details':'Test'})
healthCon[0]['children'].append({'name':'Knowledge Discovery in Databases [HCIP 6162]', 'size':100, 'details':'Test'})
healthCon[0]['children'].append({'name':'Principles of Human-Computer Interaction [HCIP 6350]', 'size':100, 'details':'Test'})
healthCon[0]['children'].append({'name':'Advanced Programming for HI [HCIP 6390]', 'size':100, 'details':'Test'})
healthCon[0]['children'].append({'name':'Architecting HI Systems [HCIP 6391]', 'size':100, 'details':'Test'})
healthCon[0]['children'].append({'name':'Enterprise Health Information Systems [HCIP 6392]', 'size':100, 'details':'Test'})
healthCon[0]['children'].append({'name':'Personalization and Recommender Systems [HCIP 6410]', 'size':100, 'details':'Test'})




healthCon[1]['children'].append({'name':'Current Issues in Health Informatics [HCIP 6070]', 'size':100, 'details':'Test'})
healthCon[1]['children'].append({'name':'Quality and Outcomes Management in Health Care [HCIP 6134]', 'size':100, 'details':'Test'})
healthCon[1]['children'].append({'name':'Information Resources Management [HCIP 6146]', 'size':100, 'details':'Test'})
healthCon[1]['children'].append({'name':'Health Law and Ethics [HCIP 6150]', 'size':100, 'details':'Test'})
healthCon[1]['children'].append({'name':'Principles of Computer Networks and Databases [HCIP 6199]', 'size':100, 'details':'Test'})
healthCon[1]['children'].append({'name':'Medical Practice Management [HCIP 6330]', 'size':100, 'details':'Test'})
healthCon[1]['children'].append({'name':'Enterprise Health Information Systems [HCIP 6392]', 'size':100, 'details':'Test'})
healthCon[1]['children'].append({'name':'Advanced Health Data Integration w/Lab [HCIP 6393]', 'size':100, 'details':'Test'})



healthCon[2]['children'].append({'name':'Vulnerability Assessment and System Assurance [HCIP 5220]', 'size':100, 'details':'Test'})
healthCon[2]['children'].append({'name':'Computer Forensics [HCIP 5250]', 'size':100, 'details':'Test'})
healthCon[2]['children'].append({'name':'Current Issues in Health Informatics [HCIP 6070]', 'size':100, 'details':'Test'})
healthCon[2]['children'].append({'name':'Quality & Outcomes Management in Health Care [HCIP 6134]', 'size':100, 'details':'Test'})
healthCon[2]['children'].append({'name':'Network Security [HCIP 6167]', 'size':100, 'details':'Test'})
healthCon[2]['children'].append({'name':'Principles of Information Security and Privacy [HCIP 6200]', 'size':100, 'details':'Test'})
healthCon[2]['children'].append({'name':'Access Control & Security Architecture [HCIP 6210]', 'size':100, 'details':'Test'})
healthCon[2]['children'].append({'name':'Information Infrastructure Protection [HCIP 6230]', 'size':100, 'details':'Test'})
healthCon[2]['children'].append({'name':'Applied Cryptography [HCIP 6240]', 'size':100, 'details':'Test'})




healthCon[3]['children'].append({'name':'Current Issues in Health Informatics [HCIP 6070]', 'size':100, 'details':'Test'})
healthCon[3]['children'].append({'name':'Health and Disease [HCIP 6104]', 'size':100, 'details':'Test'})
healthCon[3]['children'].append({'name':'Quality & Outcomes Management in Health Care  [HCIP 6134]', 'size':100, 'details':'Test'})
healthCon[3]['children'].append({'name':'Information Resources Management [HCIP 6146]', 'size':100, 'details':'Test'})
healthCon[3]['children'].append({'name':'Health Law and Ethics [HCIP 6150]', 'size':100, 'details':'Test'})
healthCon[3]['children'].append({'name':'Knowledge Discovery in Databases [HCIP 6162]', 'size':100, 'details':'Test'})
healthCon[3]['children'].append({'name':'Data Warehousing [HCIP 6163]', 'size':100, 'details':'Test'})
healthCon[3]['children'].append({'name':'Analytic Epidemiology [HCIP 6260]', 'size':100, 'details':'Test'})
healthCon[3]['children'].append({'name':'Medical Practice Management [HCIP 6330]', 'size':100, 'details':'Test'})
healthCon[3]['children'].append({'name':'Advanced Health Data Integration w/Lab [HCIP 6393]', 'size':100, 'details':'Test'})


infoCon = [
{'name':'Human-Computer Interaction Concentration', 'size':100, 'children':[]},
{'name':'Information Security and Privacy concentration', 'size':100, 'children':[]},
{'name':'Advanced Data and Knowledge Discovery Concentration', 'size':100, 'children':[]},
{'name':'Information Technology Management Concentration', 'size':100, 'children':[]},
{'name':'Software Systems Design and Engineering Concentration', 'size':100, 'children':[]},
{'name':'Design Concentration', 'size':100, 'children':[]}
]


infoCon[0]['children'].append({'name':'ITIS 6400 Principles of Human-Computer Interaction', 'size':100, 'details':'Test'})
infoCon[0]['children'].append({'name':'ITIS 6410 Personalization and Recommender Systems', 'size':100, 'details':'Test'})
infoCon[0]['children'].append({'name':'ITIS 6420 Usable Security and Privacy', 'size':100, 'details':'Test'})
infoCon[0]['children'].append({'name':'ITCS 5121 Information Visualization', 'size':100, 'details':'Test'})
infoCon[0]['children'].append({'name':'ITCS 5122 Visual Analytics', 'size':100, 'details':'Test'})
infoCon[0]['children'].append({'name':'ITCS 6140 Data Visualization', 'size':100, 'details':'Test'})
infoCon[0]['children'].append({'name':'ITCS 6216 Introduction to Cognitive Science', 'size':100, 'details':'Test'})
infoCon[0]['children'].append({'name':'ITCS 6128 Display and Advanced Interfaces', 'size':100, 'details':'Test'})



infoCon[1]['children'].append({'name':'ITIS 5220 Vulnerability Assessment and System Assurance', 'size':100, 'details':'Test'})
infoCon[1]['children'].append({'name':'ITIS 5221 Secure Programming and Penetration Testing', 'size':100, 'details':'Test'})
infoCon[1]['children'].append({'name':'ITIS 5250 Computer Forensics', 'size':100, 'details':'Test'})
infoCon[1]['children'].append({'name':'ITIS 6150 Software Assurance', 'size':100, 'details':'Test'})
infoCon[1]['children'].append({'name':'ITIS 6167 Network Security', 'size':100, 'details':'Test'})
infoCon[1]['children'].append({'name':'ITIS 6210 Access Control and Security Architecture', 'size':100, 'details':'Test'})
infoCon[1]['children'].append({'name':'ITIS 6220 Data Privacy', 'size':100, 'details':'Test'})
infoCon[1]['children'].append({'name':'ITIS 6230 Information Infrastructure Protection', 'size':100, 'details':'Test'})
infoCon[1]['children'].append({'name':'ITIS 6240 Applied Cryptography', 'size':100, 'details':'Test'})
infoCon[1]['children'].append({'name':'ITIS 6362 Information Technology: Ethics, Policy, and Security', 'size':100, 'details':'Test'})
infoCon[1]['children'].append({'name':'ITIS 6420 Usable Security and Privacy', 'size':100, 'details':'Test'})


infoCon[2]['children'].append({'name':'ITIS 5510 Web Mining', 'size':100, 'details':'Test'})
infoCon[2]['children'].append({'name':'ITIS 6520 Network Sciences', 'size':100, 'details':'Test'})
infoCon[2]['children'].append({'name':'ITIS 6162 Knowledge Discovery in Databases', 'size':100, 'details':'Test'})
infoCon[2]['children'].append({'name':'ITCS 6155 Knowledge-Based Systems', 'size':100, 'details':'Test'})
infoCon[2]['children'].append({'name':'ITIS 6163 Data Warehousing', 'size':100, 'details':'Test'})


infoCon[3]['children'].append({'name':'ITIS 6362 Information Technology Ethics, Policy, and Security', 'size':100, 'details':'Test'})
infoCon[3]['children'].append({'name':'ITIS 6130 Software Requirements Engineering for Information Systems.', 'size':100, 'details':'Test'})
infoCon[3]['children'].append({'name':'ITIS 6164 Online Info Systems', 'size':100, 'details':'Test'})
infoCon[3]['children'].append({'name':'ITIS 6230 Information Infrastructure Protection', 'size':100, 'details':'Test'})
infoCon[3]['children'].append({'name':'GEOG 6615 Advanced Seminar in Spatial Decision Support Systems', 'size':100, 'details':'Test'})
infoCon[3]['children'].append({'name':'MBAD 6121 Business Information Systems', 'size':100, 'details':'Test'})
infoCon[3]['children'].append({'name':'MBAD 6122 Decision Modeling and Analysis via Spreadsheets', 'size':100, 'details':'Test'})
infoCon[3]['children'].append({'name':'MBAD 6202 Business Information Systems Development', 'size':100, 'details':'Test'})



infoCon[4]['children'].append({'name':'ITIS 5221 Secure Programming and Penetration Testing', 'size':100, 'details':'Test'})
infoCon[4]['children'].append({'name':'ITIS 5180 Mobile Application Development', 'size':100, 'details':'Test'})
infoCon[4]['children'].append({'name':'ITIS 6130 Software Requirements Engineering for Information Systems.', 'size':100, 'details':'Test'})
infoCon[4]['children'].append({'name':'ITIS 6140 Software Testing and Quality Assurance', 'size':100, 'details':'Test'})
infoCon[4]['children'].append({'name':'ITIS 6148 Advanced OO Design and Implementation', 'size':100, 'details':'Test'})
infoCon[4]['children'].append({'name':'ITIS 6164 Online Info Systems', 'size':100, 'details':'Test'})
infoCon[4]['children'].append({'name':'ITIS 6210 Access Control and Security Architecture', 'size':100, 'details':'Test'})
infoCon[4]['children'].append({'name':'ITIS 6362 Information Technology Ethics, Policy, and Security', 'size':100, 'details':'Test'})
infoCon[4]['children'].append({'name':'ITIS 6400 Principles of Human-Computer Interaction', 'size':100, 'details':'Test'})
infoCon[4]['children'].append({'name':'GEOG 6615 Advanced Seminar in Spatial Decision Support Systems', 'size':100, 'details':'Test'})
infoCon[4]['children'].append({'name':'MBAD 6202 Business Information Systems Development', 'size':100, 'details':'Test'})



infoCon[5]['children'].append({'name':'ITIS 5180 Mobile Application Development', 'size':100, 'details':'Test'})
infoCon[5]['children'].append({'name':'ITIS 6400 Principles of Human Computer Interaction', 'size':100, 'details':'Test'})
infoCon[5]['children'].append({'name':'ITIS 6500 Complex Adaptive Systems', 'size':100, 'details':'Test'})
infoCon[5]['children'].append({'name':'ITIS 6880 Design-focused Independent Study', 'size':100, 'details':'Test'})
infoCon[5]['children'].append({'name':'ITCS 5122 Visual Analytics', 'size':100, 'details':'Test'})
infoCon[5]['children'].append({'name':'ITCS 5230 Introduction to Game Design and Development', 'size':100, 'details':'Test'})
infoCon[5]['children'].append({'name':'ARCH 7201/ ITCS7201/ITIS7201 Studio Lab I', 'size':100, 'details':'Test'})
infoCon[5]['children'].append({'name':'ARCH 7202/ ITCS7202/ITISS7202 Studio Lab II', 'size':100, 'details':'Test'})



d[0]['children'] = bioCon
d[1]['children'] = csCon
d[2]['children'] = healthCon
d[3]['children'] = infoCon

college['children'] = d

with open('readme.json', 'wb') as outfile:
	json.dump(college, outfile)