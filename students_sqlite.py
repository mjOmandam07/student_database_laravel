import sqlite3


conn = sqlite3.connect('students_test.db')
cursor = conn.cursor()



college_table = """CREATE TABLE college(
					code VARCHAR(20),
					name VARCHAR(255),
					PRIMARY KEY(code))
					)"""



colleges = [
	('COET', 'College of Engineering & Technology'),
	('CSM', 'College of Science & Mathematics'),
	('CCS', 'College of Computer Studies'),
	('CED', 'College of Education'),
	('CASS', 'College of Arts & Social Sciences'),
	('CBAA', 'College of Business Administration & Accountancy'),
	('CON', 'College of Nursing'),
	('SGS', 'School of Graduate Studies')
]

insert_college = 'INSERT INTO college (collegeCode, name) VALUES (?,?)', colleges




department_table = """CREATE TABLE department(
						id INTEGER,
						name VARCHAR(255),
						college_code VARCHAR(255),
						PRIMARY KEY(id),
						FOREIGN KEY(college_code) REFERENCES college(code)
						ON DELETE SET NULL ON UPDATE CASCADE
						)"""

departments = [
	('Chemical Engineering & Technology', 'COET'),
	('Civil Engineering', 'COET'),
	('Electrical & Electronics Engineering & Technology', 'COET'),
	('Materials & Resources Engineering & Technology', 'COET'),
	('Mechanical Engineering & Technology', 'COET'),


	('Biology', 'CSM'),
	('Chemistry','CSM'),
	('Mathematics & Statistics', 'CSM'),
	('Physics', 'CSM'),
	('Marine Science', 'CSM'),

	('Computer Science', 'CCS'),
	('Information Technology', 'CCS'),
	('Electronics Engineering Technology', 'CCS'),

	('Science & Mathematics Education', 'CED'),
	('Professional Education', 'CED'),
	('Physical Education', 'CED'),
	('Technology Teacher Education', 'CED'),

	('Psychology', 'CASS'),
	('English', 'CASS'),
	('Filipino', 'CASS'),
	('History', 'CASS'),
	('Political Science', 'CASS'),
	('Sociology', 'CASS'),
	('Philosophy & Humanities', 'CASS'),

	('Accountancy', 'CBAA'),
	('Economics', 'CBAA'),
	('Marketing', 'CBAA'),
	('Hospitality & Tourism Management', 'CBAA'),

	('Nursing', 'CON')



]

insert_department = 'INSERT INTO department (name, college_code) VALUES (?,?)', departments

course_table = """CREATE TABLE course(
					code VARCHAR(20),
					name VARCHAR(255),
					deptNo INTEGER,
					college_code VARCHAR(20),
					PRIMARY KEY(code),
					FOREIGN KEY(deptNo) REFERENCES department(id)
					ON DELETE SET NULL ON UPDATE CASCADE,
					FOREIGN KEY(college_code) REFERENCES college(code)
					ON DELETE SET NULL ON UPDATE CASCADE
)"""


courses = [
	('BSCERE', 'Bachelor of Science in Ceramics Engineering',4,'COET'),
	('BSCHE', 'Bachelor of Science in Chemical Engineering',1,'COET'),
	('BSCE', 'Bachelor of Science in Civil Engineering',2,'COET'),
	('BSCPE', 'Bachelor of Science in Computer Engineering',3,'COET'),
	('BSEE', 'Bachelor of Science in Electrical Engineering',3,'COET'),
	('BSECE', 'Bachelor of Science in Electronics & Communications Engineering',3,'COET'),
	('BSME', 'Bachelor of Science in Mechanical Engineering',5,'COET'),
	('BSMETE', 'Bachelor of Science in Metallurgical Engineering',4,'COET'),
	('BSEM', 'Bachelor of Science in Mining Engineering',4,'COET'),
	('BSIAM','Bachelor of Science in Industrial Automation & Mechatronics',3,'COET'),
	('BSEnvE', 'Bachelor of Science in Environmental Engineering',1,'COET'),
	('BSEnvET', 'Bachelor of Science in Environmental Engineering Technology',1,'COET'),
	('BET-CHET', 'Bachelor of Engineering Technology-Chemical Engineering Technology',1,'COET'),
	('BET-CET','Bachelor of Engineering Technology-Civil Engineering Technology',2,'COET'),
	('BET-ELET', 'Bachelor of Engineering Technology-Electrical Engineering Technology',3,'COET'),
	('BET-ECET', 'Bachelor of Engineering Technology-Electronics & Communications Engineering Technology',3,'COET'),
	('BET-MET', 'Bachelor of Engineering Technology-Mechanical Engineering Technology',5,'COET'),

	('BS BIO(AnBio)', 'Bachelor of Science in Biology Major in Animal Biology',6,'CSM'),
	('BS BIO(Bdv)', 'Bachelor of Science in Biology Major in Biodiversity',6,'CSM'),
	('BS BIO(MCB)', 'Bachelor of Science in Biology Major in Microbiology',6,'CSM'),
	('BS BIO(PlBio)', 'Bachelor of Science in Biology Major in Plant Biology',6,'CSM'),
	('BS MARINE BIO', 'Bachelor of Science in Marine Biology',10,'CSM'),
	('BS CHEM', 'Bachelor of Science in Chemistry',7,'CSM'),
	('BS MATH', 'Bachelor of Science in Mathematics',8,'CSM'),
	('BS PHYSICS', 'Bachelor of Science in Physics',9,'CSM'),
	('BS STAT', 'Bachelor of Science in Statistics',8,'CSM'),
	('MS PHYSICS', 'Master of Science in Physics',9,'CSM'),
	('MS MARINE BIO', 'Master of Science in Marine Biology',10,'CSM'),
	('MS MATH', 'Master of Science in Mathematics',8,'CSM'),
	('MS CHEM', 'Master of Science in Chemistry',7,'CSM'),
	('MS ENVSCI', 'Master of Science in Environmental Science',6,'CSM'),
	('MS BIO', 'Master of Science in Biology',6,'CSM'),
	('MS STAT', 'Master of Science in Statistics',8,'CSM'),
	('MPhys','Master of Physics',9,'CSM'),
	('MMath', 'Master of Mathematics',8,'CSM'),
	('MApSta', 'Master of Applied of Statistics',8,'CSM'),
	('PHD BIO', 'Doctor of Philosophy in Biology',6,'CSM'),
	('PHD CHEM', 'Doctor of Philosophy in Chemistry',7,'CSM'),
	('PHD MATH', 'Doctor of Philosophy in Mathematics',8,'CSM'),
	('PHD PHYSICS', 'Doctor of Philosophy in Physics',9,'CSM'),


	('BSCA', 'Bachelor of Science in Computer Applications',13,'CCS'),
	('BSCS', 'Bachelor of Science in Computer Science',11,'CCS'),
	('BSIS', 'Bachelor of Science in Information System',12,'CCS'),
	('BSIT', 'Bachelor of Science in Information Technology',12,'CCS'),

	('BPE', 'Bachelor of Physical Education',16,'CED'),
	('BSEd BIO', 'Bachelor of Secondary Education Major in Biology',14,'CED'),
	('BSEd CHEM', 'Bachelor of Secondary Education Major in Chemistry',14,'CED'),
	('BSEd FIL', 'Bachelor of Secondary Education Major in Filipino',14,'CED'),
	('BSEd MATH', 'Bachelor of Secondary Education Major in Mathematics',14,'CED'),
	('BSEd PHYSICS', 'Bachelor of Secondary Education Major in Physics',14,'CED'),
	('BTVTEd-DT', 'Bachelor of Technical-Vocational Teacher Education Major in Drafting Technology',17,'CED'),
	('BTLEd-HE', 'Bachelor of Technology & Livelihood Education Major in Home Economics',17,'CED'),
	('BTLEd-IA', 'Bachelor of Technology & Livelihood Education Major in Industrial Arts',17,'CED'),
	('BEEd SCI MAT', 'Bachelor of Elementary Education Major in Science & Mathematics',14,'CED'),

	('BA ELS', 'Bachelor of Arts in English Language Studies',19,'CASS'),
	('BA FIL', 'Bachelor of Arts in Filipino',20,'CASS'),
	('BA HISTORY', 'Bachelor of Arts in History',21,'CASS'),
	('BA POL SCI', 'Bachelor of Arts in Political Science',22,'CASS'),
	('BA PSYCH', 'Bachelor of Arts in Psychology',18,'CASS'),
	('BA SOCIO', 'Bachelor of Arts in Sociology',23,'CASS'),
	('BS PHIL', 'Bachelor of Science in Philosophy Major in Applied Ethics',24,'CASS'),
	('BS PSYCH', 'Bachelor of Science in Psychology',18,'CASS'),

	('BSA', 'Bachelor of Science in Accountancy',25,'CBAA'),
	('BSBA-B.ECON', 'Bachelor of Science in Business Administration Major in Business Economics',26,'CBAA'),
	('BSBA-MKT MGT', 'Bachelor of Science in Business Administration Major in Marketing Management',27,'CBAA'),
	('BS ECON', 'Bachelor of Science in Economics',26,'CBAA'),
	('BS ENTREP', 'Bachelor of Science in Entrepreneurship',27,'CBAA'),
	('BS HM', 'Bachelor of Science in Hospitality Management',28,'CBAA'),

	('BS NURSING', 'Bachelor of Science in Nursing',29,'CON'),

	('MSCE', 'Master of Science in Civil Engineering',2,'SGS'),
	('MSME', 'Master of Science in Mechanical Engineering',5,'SGS'),
	('MSEE', 'Master of Science in Electrical Engineering',3,'SGS'),
	('MSMSE', 'Master of Science in Materials Science and Engineering',4,'SGS'),
	('MEng', 'Master of Engineering',4,'SGS'),
	('Eng.D.CE', 'Doctor of Engineering in Civil Engineering',2,'SGS'),
	('Eng.D.MSE', 'Doctor of Engineering in Materials Science and Engineering',4,'SGS'),
	('Eng.D.ME', 'Doctor of Engineering in Mechanical Engineering',5,'SGS'),

	('MSCA', 'Master of Science in Computer Applications',13,'SGS'),
	('MSCS', 'Master of Science in Computer Science',11,'SGS'),
	('MSIT', 'Master of Science in Information Technology',12,'SGS'),
	

	('MSPE', 'Master of Science in Physical Education',16,'SGS'),
	('MSEd BIO', 'Master of Science Education in Biology',14,'SGS'),
	('MSEd CHEM', 'Master of Science Education in Chemistry',14,'SGS'),
	('MSEd PHYSICS', 'Master of Science Education in Physics',14,'SGS'),
	('MSEd ELEM MATH', 'Master of Science Education in Elementary Mathematics',14,'SGS'),
	('MSEd SEC MATH', 'Master of Science Education in Secondary Mathematics',14,'SGS'),
	('MSEd GEN SCI', 'Master of Science Education in General Science',14,'SGS'),
	('MA ED(Reading)', 'Master of Arts in Education Major in Reading',15,'SGS'),
	('MA ED(Guidance & Counseling)', 'Master of Arts in Education Major in Guidance & Counseling',15,'SGS'),
	('PHDSEd CHEMISTRY', 'Ph.D. in Science Education in Chemistry',14,'SGS'),

	('MA ELS', 'Master of Arts in English Language Studies',19,'SGS'),
	('MA FIL', 'Master of Arts in Filipino',20,'SGS'),
	('MA SOCIO', 'Master of Arts in Sociology',23,'SGS'),
	('MFil', 'Master of Filipino',20,'SGS'),
	('MHis', 'Master in History',21,'SGS'),
	('MELS', 'Master in English Language Studies',19,'SGS'),
	('MSocio', 'Master in Sociology',23,'SGS'),
	('PHD FIL', 'Doctor of Philosophy in Filipino',20,'SGS'),
	('PHD LS', 'Doctor of Philosophy in Language Studies',19,'SGS'),

	('MBA', 'Master in Business Administration',27,'SGS'),
	('BA.D', 'Doctor in Business Administration',27,'SGS')




]

insert_courses = 'INSERT INTO course (courseCode, name, departmentNo, college_code) VALUES (?,?,?,?)', courses



student_table = """CREATE TABLE student(
					id VARCHAR(9) NOT NULL,
					firstName VARCHAR(50) NOT NULL,
					lastName VARCHAR(50) NOT NULL,
					yearLevel SMALLINT NOT NULL,
					gender CHAR NOT NULL,
					course VARCHAR(255),
					PRIMARY KEY(id),
					FOREIGN KEY(course) REFERENCES course(code)
					ON DELETE SET NULL ON UPDATE CASCADE
					)"""
				
## NAME COURSE YEAR DEPARTMENT COLLEGE ####
#cursor.executemany()
'''
cursor.execute("SELECT * FROM college")
display = cursor.fetchall()
for i in display:
	print('(',i[0],') ', i[1])'''
#conn.commit()
'''
cursor.execute("""SELECT courseCode, c.name, d.name as deptName, clg.name as collegeName 
					FROM course as c, department as d, college as clg
					WHERE c.college_code = 'COET' AND c.departmentNo = departmentID AND clg.collegeCode = c.college_code """)
'''

'''
cursor.execute(""" SELECT c.courseCode, c.name, d.name, clg.name 
				FROM ((course as c JOIN department as d ON c.departmentNo = d.departmentID)
				 JOIN college as clg ON  c.college_code = clg.collegeCode) WHERE c.college_code = 'COET' """)	


display = cursor.fetchall()
for i in display:
	print('(',i[0],') ', i[1],' | Department of',i[2],' | ',i[3],'\n')'''


'''
cursor.execute("""INSERT INTO student(studentID, firstName, lastName, yearLevel, gender, course) 
				VALUES ('2018-1607', 'Mark Joshua', 'Omandam', '3', 'Male', 'Bachelor of Science in Computer Science')""")		

conn.commit()'''

#####################################################3
''' FINAL ANSWER ########################################
###################################################
cursor.execute("""SELECT s.firstName, s.lastName, c.courseCode, c.name, s.yearLevel, d.name, clg.collegeCode, clg.name FROM
					(((student AS s LEFT JOIN course AS c ON s.course = c.courseCode)
					LEFT JOIN department as d ON c.departmentNo = d.departmentID)
					LEFT JOIN college AS clg ON d.college_code = clg.collegeCode )""")

display = cursor.fetchall()
print(display)
#for i in display:
#	print(i[0],i[1],'|(',i[2],')',i[3],'|','Year:',i[4],'| Department of',i[5],'|(',i[6],')',i[7])'''
#############################################################################


###### DEPARTMENT WITHOUT SGS #####################

cursor.execute("""SELECT d.name, c.courseCode,c.name FROM 
				((department AS d JOIN course as c ON d.departmentID = c.departmentNo AND d.name = 'Electrical & Electronics Engineering & Technology')
				JOIN college as clg ON c.college_code = clg.collegeCode AND clg.collegeCode != 'SGS')""")

display = cursor.fetchall()
for i in display:
	print(i)	

######################################################


########################################33
###### ADD STUDENT #####################
'''
ID = input('id: ')
fname = input('fname: ')
lname = input('lname: ')
gender = input('gender: ')
yrLvl = int(input('yrLvl: '))
course = input('Course: ')

#Bachelor of Engineering Technology-Electronics & Communications Engineering Technology

cursor.execute(""" SELECT courseCode FROM course WHERE name = '{}'""".format(course))
display = cursor.fetchall()
for i in display:
	course_in = i[0]
print(course_in)

cursor.execute("""INSERT INTO student(studentID, firstName, lastName, yearLevel, gender, course)
				 VALUES('%s','%s','%s',%d,'%s','%s')""" % (ID,fname,lname,yrLvl,gender,course_in))

conn.commit()'''
#####################################################

#################SEARCH Student#######################################################
'''cursor.execute("""SELECT s.firstName, s.lastName, c.courseCode,s.yearLevel, d.name, clg.collegeCode, clg.name FROM
					(((student AS s LEFT JOIN course AS c ON s.course = c.courseCode)
					LEFT JOIN department as d ON c.departmentNo = d.departmentID)
					LEFT JOIN college AS clg ON d.college_code = clg.collegeCode )
					WHERE s.studentID = '2018-1608'""")

display = cursor.fetchall()
for i in display:
	print(i[0],i[1],'|',i[2],'|','Year:',i[3],'| Department of',i[4],'|(',i[5],')',i[6])'''

####################################################################################################



