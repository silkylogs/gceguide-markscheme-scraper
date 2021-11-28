'''
https://papers.gceguide.com/A%20Levels/Physics%20(9702)/2017/9702_w17_ms_22.pdf
The whole link consists of
1. the protocol + website
2. the qualification (o or a level)
3. the subject + subject code
4. the year
5. the filename

The filename consists of
(subject code)_(summer or winter)(year)_(markscheme or question paper)_(paper number).pdf

So, the data input for an A level markscheme scraper (though the qualification can change in a later time) are:
1. subject (subject codes can be hardcoded in)
2. the full year (eg: 2017)
3. season (wether it was held during the summer (typically may-june) or winter (typically oct-nov))
4. paper number

https://papers.gceguide.com/A%20Levels/Physics%20(9702)/2017/9702_w17_ms_21.pdf
https://papers.gceguide.com/A%20Levels/Biology%20(9700)/2009/9700_w09_ms_33.pdf
https://papers.gceguide.com/A%20Levels/Mathematics%20(9709)/2016/9709_m16_ms_12.pdf
https://papers.gceguide.com/A%20Levels/Mathematics%20(9709)/2018/9709_m18_ms_62.pdf
This data tells us that the stucture remains consistent across different subjects
Though for mathematics the filename has to be dealt with seperately due to the paper number and the subject name being different

If for some reason your pdf viewer cannot open the file, chances are that page does not exist
'''

import os

class SubjectCodes:
	def __init__(self) -> None:
		self.physics = str("9702")
		self.biology = str("9700")
		self.chemistry = str("9701")
		self.mathematics = str("9709")

	def SubjectToCode(self, subject:str) -> str:
		if(subject == "mathematics" or subject == "Mathematics"):
			return self.mathematics
		elif(subject == "chemistry" or subject == "Chemistry"):
			return self.chemistry
		elif(subject == "biology" or subject == "Biology"):
			return self.biology
		elif(subject == "physics" or subject == "Physics"):
			return self.physics
		else:
			print("SubjectCodes.SubjectToCode(): Warning: unknown subject")
			return str("0000")

	def CodeToSubject(self, code:str) -> str:
		if(code == self.physics):
			return "Physics"
		elif(code == self.chemistry):
			return "Chemistry"
		elif(code == self.biology):
			return "Biology"
		elif(code == self.mathematics):
			return "Mathematics"
		else:
			print("SubjectCodes.CodeToSubject(): Warning: unknown code")
			return "Error"


class LinkClass:
	def __init__(self) -> None:
		self.website = str('https://papers.gceguide.com/')
		self.qualificaton = str("A%20" + "Levels")
		self.subject = str("Physics")
		self.year = str("2017")
		self.filename = str(".pdf")
		self.season = str("s") #s for summer, w for winter
		self.paperNumber = str("11")

def ConstructFilename(linkClass:LinkClass, subjectCodes:SubjectCodes) -> str:
	
	#code to prepend filename with
	code = subjectCodes.SubjectToCode(linkClass.subject)
	year = str(linkClass.year[-2] + linkClass.year[-1])

	if(not(linkClass.season == "s" or linkClass.season == "w")):
		print("ConstructFilename(): Warning: expected value of linkClass.season to be 's' or 'w', found " + linkClass.season)

	return str(code + "_" + linkClass.season + year + "_ms_" + linkClass.paperNumber + ".pdf")


def AssembleLink(linkClass:LinkClass, subjectCodes:SubjectCodes) -> str:
	code = subjectCodes.SubjectToCode(linkClass.subject)
	filename = ConstructFilename(linkClass, subjectCodes)

	return str("https://papers.gceguide.com/" + linkClass.qualificaton + "/" + linkClass.subject + "%20(" + code + ")/" + linkClass.year + "/" + filename)


def DataInput(linkClass:LinkClass) -> None:
	print("Enter subject(eg: Physics), full year(eg: 2017), season(eg: s or w), and 2 digit paper number(eg: 11)")
	linkClass.subject = str(input("Enter subject: "))
	linkClass.year = str(input("Enter year: "))
	linkClass.season = str(input("Enter season: "))
	linkClass.paperNumber = str(input("Enter paper number: "))



linkClass = LinkClass()
subjectCodes = SubjectCodes()

DataInput(linkClass)
link = AssembleLink(linkClass, subjectCodes)
filename = ConstructFilename(linkClass, subjectCodes)
print("Generated link: " + link)
os.system("curl --output " + filename + " " + link)
