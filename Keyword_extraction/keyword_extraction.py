#This program extracts keywords from a given PDF document using Rapid Automatic Keyword Extraction algorithm and lists the keywords
# in a .csv file in the order of their scores/weightages

import PyPDF2
import rake
import csv

filename = "text_list.txt"
fh = open(filename, "a")
stoppath = "SmartStoplist.txt"

#This line extract keywords having words of atleast 5 characters, phrases having atmost 3 words
# and keywords appearing atleast 4 times in the text
rake_object = rake.Rake(stoppath, 5, 3, 4)		#You can change these parameters as per your need
#Open text file for keywords extraction
pdfFileObj = open('JavaBasics-notes.pdf', 'rb')

#pdfReader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#Convert the content from pdf file to txt file
for i in range(pdfReader.numPages):
	pageObj = pdfReader.getPage(i)
	text = pageObj.extractText()
	#text_list.append(text)
	fh.writelines(text)
fh.close()

pdfFileObj.close()
text_file = open("text_list.txt", 'r')
text_pdf = text_file.read()

#Run the rake tool to get keywords
keywords = rake_object.run(text_pdf)
f = open("keywords.csv", "w")
columnTitleRow = "Keyword, Weight\n"
f.write(columnTitleRow)
for i in range(len(keywords)):
		keyword = keywords[i][0]
		weight = str(keywords[i][1])
		row = keyword + "," + weight + "\n"
		f.write(row)
f.close()
