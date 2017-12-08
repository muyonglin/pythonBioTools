class geneBankParser(object):
	"""docstring for geneBankParser
		@input: filepath, 
				strings of tags (like 'LOCUS,source/country')
	"""
	def __init__(self, inFilePath, inString,multipleSeq=True ):
		super(geneBankParser, self).__init__()
		self.iS = inString
		self.iFP = inFilePath
		self.iFS = self.getFormattedTags()
		self.ss = open(inFilePath).read()
		self.gL = self.readSeq()
		self.sd = self.constructDict()
		#print(self.sd)
		self.rt = self.extractInfo()
		self.writeOut()

	#formatted List ['LOCUS',[source,country]]	
	def getFormattedTags(self):
		inSList = self.iS.split(",")		
		fList = []
		for item in inSList:
			if "/" in item:
				fList.append(item.split("/"))
			else:
				fList.append(item)
		return(fList)			
 

	def readSeq(self):
		import re
		sse = re.sub("\n *?[0-9]+ ","",self.ss)
		sse = re.sub("\n {18}","",sse)
		sse = re.sub("\n {12}","",sse)
		gbList = sse.split("//\n")
		return(gbList)
	def constructDict(self):
		import re
		dictList = []
		for item in list(filter(None,self.gL)):
			spList = item.split("\n")
			spDict = {}
			for item1 in spList:
				if "   /" in item1:
					smallDict = {}
					#print(item1)	
					#split by 4 space (only the first tage will be split out)
					#misc_feature needs right four space to split out									
					bpList = list(filter(None,item1.split("    "))) 
					#print(bpList)
					if bpList[0] == "FEATURES":
						spDict[bpList[0]] = ["_".join(bpList[1:])]
					#will discard item without '=' after the second element
					for item2 in bpList:
						if "   /" in item2 and item2 != ' Location/Qualifiers':
							bpList2 =  item2.split("   /")
							#print(bpList2)
							for item3 in bpList2:
								if "=" in item3:
									smallDict[item3.split("=")[0]] = [item3.split("=")[1]]
					#print(bpList)
					spDict[bpList[0].replace(" ","")] = [bpList[1].split("   /")[0].replace(" ",""),smallDict]
				else:
					bpList = list(filter(None,item1.split(" ")))
					#print(bpList)
					if bpList == []:
						continue
					if bpList[0] == "ORIGIN":
						spDict[bpList[0]] = ["".join(bpList[1:])]
					else:
						spDict[bpList[0]] = ["_".join(bpList[1:])]
			#print(spDict)
			dictList.append(spDict)
		return(dictList)  
	def extractInfo(self):
		#LOCUS source: country, collection_date
		resultList = []	   
		for item in self.sd:
			#print(item.keys())			
			outList = []
			for item1 in self.iFS:
				#print(item1)
				#print(type(item1))
				if type(item1) == str:
					if item1 in item.keys():
						outList.append(item[item1][0])
					elif item1 not in item.keys():
						outList.append("no" + str(item1).replace('\n',"")+"Tag")
				elif type(item1) == list:
					#print(item[item1[0]][1].keys())
					if item1[0] in item.keys() and item1[1] in item[item1[0]][1].keys():
						#outList.append(item1[1] + item[item1[0]][1][item1[1]][0])
						outList.append(item[item1[0]][1][item1[1]][0][1:-1])
					elif item1[0] in item.keys() and item1[1] not in item[item1[0]][1].keys():	
						outList.append("no" + str(item1[1]).replace('\n',"") +"Tag")
					elif item1[0] in item.keys():
						outList.append("no" + str(item1[0]).replace('\n',"") +"Tag")
			#print(outList,item1)				  
			if "ORIGIN" in item.keys():
				resultList.append(("/".join(outList),item["ORIGIN"][0]))
			elif "ORIGIN" not in item.keys():
				resultList.append(("/".join(outList),"noSeq"))
			#print(outList,"_".join(outList)) 

		return(resultList)	
	def writeOut(self):
		outHandle = open(self.iFP + "_extract.fasta",'w')
		for item in self.rt:
			outHandle.write(">%s\n%s\n" % (item[0],item[1]))
		outHandle.close()		
		print("done!")	


###########################################################################################
#tkinter
###########################################################################################
#coding=utf-8
#import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
class MainWindow:
	def __init__(self):
		self.root = Tk()
		#self.root.geometry("400x100+350+240")
		self.root.title("extract information from geneBank")

		self.keyName = Label(self.root,text="Tag",font="Times 15 bold",width=8)
		self.filePath = Button(self.root, text="File",width=10,font="Times 15 bold"
			, command=self.getFilePath)

		self.keyName_text = Entry(self.root,width=40,font="Times 15")
		self.keyName_text.insert(10,'ACCESSION,source/country,source/collection_date')
		self.filePath_text = Label(self.root,width=40)

		self.run_Button = Button(self.root, text="Run",width=10,font="Times 15 bold"
			,command=self.runExtractInfo)

		self.keyName.grid(row = 0,column = 0,columnspan = 1)
		self.filePath.grid(row = 2,column = 1,columnspan = 2,padx=5)

		self.keyName_text.grid(row = 0,column = 1, columnspan = 7,pady=5)
		self.filePath_text.grid(row = 1,column = 1, columnspan = 7,pady=5)
		self.run_Button.grid(row=2, column=4,columnspan=2,padx=5 )

		self.root.mainloop()
	def getFilePath(self):
		from tkinter import filedialog
		self.filename = filedialog.askopenfilename()
		self.filePath_text.config(text=self.filename)

	def runExtractInfo(self):
		try:
			self.filename
		except NameError:
			self.filePath_text.config(text='No File Selected')
		else:
			self.extractTags = self.keyName_text.get()
			if self.extractTags == '':
				self.filePath_text.config(text='No Tags Selected')
				return(0)
			else:
				geneBankParser(self.filename,self.extractTags)
				self.filePath_text.config(text='Extraction done!')
MainWindow()