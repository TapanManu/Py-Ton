import os
import sys
from time import sleep

def main():
	menu()


def menu():
	os.system('clear')
    	print("")
    	print("")
    	print("")
    	print("")
    	print("")

    	choice = raw_input("""
                      			A: Enter Student details
                      			B: Enter Attendance
                      			C: Generate Report
                      			Q: Quit

                      			Please enter your choice: """)

    	if choice == "A" or choice == "a" :
        	students()
    	elif choice == "B" or choice == "b":
         	attn()
   	elif choice == "C" or choice == "c":
         	reports()
    	elif choice=="Q" or choice == "q":
		os.system('clear')
         	sys.exit
    	else:
        	print("You must only select either A,B,C, or Q.")
        	print("Please try again")
        	main()

def students():
	os.system('clear')	
	file1=open("students.txt","a")
	tcontinue = "y"
	while tcontinue == "y" :
		tname = raw_input("Enter Name :")
		trollno = input("Enter Roll No:")
		file1.write(tname+","+str(trollno)+'\n')	
		print('\n')
		tcontinue = raw_input("Continue [y/n]")
		print('\n')
		if tcontinue == 'n' :
			break
	file1.close
	file1 = ""
	main()

def attn():
	os.system('clear')

	file_in = open('students.txt','r')
	file_out = open('attn.txt',"a")

	line = file_in.readline()
	while line:
	
		tname = line.split(",")
		
		trollno = ""
		trollno = tname[1].splitlines()[0]
		print tname[0] + " - " + trollno
		tattn=""
		tattn=raw_input("Absent Hrs Seperated By Commas / <Enter> for Next Student \t")
	
		if len(tattn) == 0:
			tattn = "xxxxxx"
			
		else :
			tabsent = tattn.split(",")
			abslen = len(tabsent)
			tattn = "xxxxxx"
			
			i = 0
			while i < abslen :
		
				if tabsent[i] == "1":
					tattn = "a"+ tattn[1:6]
				if tabsent[i]== "2" :
					tattn = tattn[0]+"a"+tattn[2:6] 
				if tabsent[i]== "3" :
					tattn = tattn[0:2]+"a"+tattn[3:6]
				if tabsent[i]== "4" :
					tattn = tattn[0:3]+"a"+tattn[4:6]
				if tabsent[i]== "5" : 
					tattn = tattn[0:4]+"a"+tattn[5]
				if tabsent[i]== "6" :
					tattn = tattn[0:5]+"a"
			
				i+=1
				
		outstring = ""	
		outstring = tname[0]+","+trollno+","+tattn+"\n"
		file_out.write(outstring)
		print tattn
		line=file_in.readline()

	file_in.close
	file_out.close
	file_out = ""
	tcontinue = raw_input("Press <Enter> Key to Continue....")
	main()


def reports():
	import os
	file_master = open('students.txt','r')
	line_master = file_master.readline()

	os.system('clear')
	totwdays = input("\n\n\n\n\n\n\t\t\t\t\tNo. Of Working Days \t")

	os.system('clear')

	cnt = 0

	tname = line_master.split(",")
	print "Attendance Report"
	print "--------------------------------------------------------------------------------------------------------"
	print "Total Absent Hrs."
	print  "\t" +"1 Hr" + "\t" + " 2 Hr" + "\t" + "3 Hr" + "\t" + "4 Hr" + "\t" + "5 Hr"+ "\t" + "6 Hr" + "\t\t"  	+"TotAbsHrs"+"\t"+"Tot WHrs"+ "\t" + "Att %"
	print "--------------------------------------------------------------------------------------------------------"
	while line_master :
		totabshrs = 0
		hr1ctr = 0
		hr2ctr = 0
		hr3ctr = 0
		hr4ctr = 0
		hr5ctr = 0
		hr6ctr = 0
		
		file_in = open('attn.txt','r')
		line = file_in.readline()
		tattn = line.split(",")
	
		while line:
		
			if tname[0] == tattn[0] :   # name check			
			
				tattnstring = ""
				tattnstring = tattn[2]
			
				if tattnstring[0] == "a" :
					hr1ctr = hr1ctr + 1
					totabshrs+= 1
				if tattnstring[1] == "a" :
					hr2ctr = hr2ctr + 1
					totabshrs+= 1
				if tattnstring[2] == "a" :
					hr3ctr = hr3ctr + 1
					totabshrs+= 1
				if tattnstring[3] == "a" :
					hr4ctr = hr4ctr + 1
					totabshrs+= 1
				if tattnstring[4] == "a" :
					hr5ctr = hr5ctr + 1
					totabshrs+= 1
				if tattnstring[5] == "a" :
					hr6ctr = hr6ctr + 1
					totabshrs+= 1			
				
				line = file_in.readline()
				tattn = line.split(",")
			else :
				line = file_in.readline()
				tattn = line.split(",")		
	
		file_in.close

	
		totwhrs = float(totwdays * 6)	
		tatpercentage = (100-float(totabshrs/totwhrs) * 100)
	
		print "Name " + "\t" + tname[0]
		print "Roll#" + "\t" + tname[1]
		print "--------------------------------------------------------------------------------------------------------"
		print  "\t"+ str(hr1ctr) + "\t" + str(hr2ctr) + "\t" + str(hr3ctr)+"\t" + str(hr4ctr) + "\t" + str(hr5ctr) + "\t" + str(hr6ctr) + "\t\t" +str(totabshrs)+"\t\t"+str(totwhrs)+"\t\t"+ str(round(tatpercentage,2))
		print "--------------------------------------------------------------------------------------------------------"
		line_master = file_master.readline()
		tname = line_master.split(",")

	file_in.close
	file_master.close
	tcontinue = raw_input("Press <Enter> Key to Continue....")
	main()
		
main()
