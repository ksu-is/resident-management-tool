
import time
import pickle
import os
class home:
    def _init_(self):
        self.id=0
        self.fname=' '
        self.lastname=' '
        self.dob=''
        self.ssn=0
        self.gender=' '
        self.bgroup=' '
        self.transfusion=' '
        self.dnr=''
        self.livwill=''
        self.insname=''
        self.inseffdate=''
        self.inspolicy=''
        self.insgroup=''
        self.secinsname=''
        self.secinseffdate=''
        self.secinspolicy=''
        self.secinsgroup=''
        self.emergcontactname=''
        self.relationship=''
        self.emergcontactphone=0
        self.emergcontactemail=''
        self.doctor=''
        self.docaddress=''
        self.doccity=''
        self.docstate=''
        self.doczipcode=0
        self.docphone=0
        self.phamarcy=''
        self.pharmaddress=''
        self.pharmcity=''
        self.pharmstate=''
        self.pharmzipcode=0
        self.pharmphone=''
        self.monthlyfee=0
        self.payment=''

    def input(self):
        self.id=input("Enter Resident ID: ")
        self.fname=raw_input("Enter Resident's First Name: ")
        self.lastname=raw_input("Enter Resident's Last Name: ")
        self.dob=input("Enter Resident's DOB: ")
        self.ssn=input("Enter Resident's Last 4 of SSN: ")
        self.gender=raw_input("Enter Resident's Gender(Male/Female/Other):")
        self.bgroup=raw_input("Enter Resident's Blood Group: ")
        self.transfusion=raw_input("Does resident consent to blood transfusion? (Yes/No): ")
        self.dnr=raw_input("Does resident have a DNR order?(Yes/No): ")
        self.livwill=raw_input("Does residnet have a living will? (Yes/No):")
        self.insname=raw_input("Enter primary insurance name: ")
        self.inseffdate=raw_input("Enter primary insurance effective date: ")
        self.inspolicy=raw_input("Enter primary insurance policy number: ")
        self.insgroup=raw_input("Enter primary insurance group number: ")
        self.secinsname=raw_input("Enter secondary insurance name: ")
        self.secinseffdate=raw_input("Enter secondary insurance effective date: ")
        self.secinspolicy=raw_input("Enter secondary insurance policy number: ")
        self.secinsgroup=raw_input("Enter secondary insurance group number: ")
        self.emergcontactname=raw_input("Enter Emergency Contact Name: ")
        self.emergcontactphone=input("Enter emergency contact's phone number: ")
        self.emergcontactemail=raw_input("enter emergency contact's email address: ")
        self.relationship=raw_input("Enter emergency contact relationship to resident: ")
        self.doctor=raw_input("Enter Resident's Primary Care Physician's name: ")
        self.docaddress=raw_input("Enter PCP's address: ")
        self.doccity=raw_input("Enter PCP's city: ")
        self.docstate=raw_input("Enter PCP's state: ")
        self.doczipcode=raw_input("Enter PCP's zipcode: ")                    
        self.docphone=input("Enter PCP's phone number: ")
        self.phamarcy=raw_input("Enter resident's pharmacy name: ")
        self.pharmaddress=raw_input("Enter resident's pharmacy street name:")
        self.pharmcity=raw_input("Enter pharmacy's city: ")
        self.pharmstate=raw_input("Enter pharmacy's state: ")
        self.pharmzipcode=input("Enter pharmacy's zipcode: ")
        self.pharmphone=input("Enter pharmacy's phone number: ")
        self.monthlyfee=input("Enter resident's monthly payment: $ ")
        self.paymethod=raw_input("Enter resident's mode of payment (Check/Credit Card/Wire Transfer/Money Order/Cashier's Check): ")


    def output(self):
        print ("RESIDENT ID NUMBER: "),self.id
        print ("RESIDENT'S FIRST NAME: "),self.fname
        print ("RESIDENT'S LAST NAME: "),self.lastname
        print ("RESDIENT'S DOB: "),self.dob
        print ("RESIDENT'S LAST 4 OF SSN: "),self.ssn
        print ("RESIDENT'S GENDER: "),self.gender
        print ("RESIDENT'S BLOOD GROUP: "),self.bgroup
        print ("RESIDENT AGREES TO BLOOD TRASFUSION: "),self.transfusion
        print ("RESIDENT HAS DNR: "), self.dnr
        print ("RESIDENT HAS LIVING WILL: "),self.livwill
        print ("RESIDENT'S PRIMARY INSURANCE: "),self.insname
        print ("PRIMARY INSURANCE EFFECTIVE DATE: "),self.inseffdate
        print ("PRIMARY INSURANCE POLICY NUMBER: "),self.inspolicy
        print ("PRIMARY INSURANCE GROUP NUMBER: "),self.insgroup
        print ("RESIDENT'S SECONDARY INSURANCE: "),self.secinsname
        print ("SECONDARY INSURANCE EFFECTIVE DATE: "),self.secinseffdate
        print ("SECONDARY INSURANCE POLICY NUMBER: "),self.secinspolicy
        print ("SECONDARY INSURANCE GROUP NAME: "),self.secinsgroup
        print ("EMERGENCY CONTACT: "),self.emergcontactname
        print ("RELATIONSHIP TO RESIDENT: "),self.relationship
        print ("CONTACT NUMBER: "),self.emergcontactphone
        print ("CONTACT EMAIL: "),self.emergcontactemail
        print ("RESIDENT'S PCP: "),self.doctor
        print ("PCP'S ADDRESS: "),self.docaddress
        print ("PCP'S CITY: "),self.doccity
        print ("PCP'S STATE: "),self.docstate
        print ("PCP'S ZIPCODE: "),self.doczipcode
        print ("PCP'S PHONE NUMBER: "),self.docphone
        print ("RESIDENT'S PHARMACY: "),self.phamarcy
        print ("PHARMACY ADDRESS: "),self.pharmaddress
        print ("CITY: "),self.pharmcity
        print ("STATE: "),self.pharmstate
        print ("ZIPCODE: "),self.pharmzipcode
        print ("PHONE NUMBER: "),self.pharmphone
        print ("RESIDENT'S MONTHLY PAYMENT: "),self.monthlyfee
        print ("RESIDENTS'S MODE OF PAYMENT: "),self.paymethod

#FUNCTION

import time
import pickle
import os

def writehome():
    fout=open("home.DAT","ab")
    ob=home()
    print ("ENTER NEW RESIDENT INFORMATION: :")
    ob.input()
    pickle.dump(ob,fout)
    print ("Records Saved")

def readhome():
    fin=open("home.DAT","rb")
    ob=home()
    try:
        print ("SWEET COMFORT HOME RESIDENTS: :")
        while True:
            ob=pickle.load(fin)
            ob.output()
            print
    except EOFError:
        fin.close()

def Searchhomeid(n):           #search by resident id
    fin=open("home.DAT","rb")
    ob=home()
    flag=False
    try:
        print
        print("\nRESIDENT DETAILS:--")
        while True:
            ob=pickle.load(fin)
            if ob.id==n:
                ob.output()
                flag=True
    except EOFError:
        if not flag:
            print ("\n")
            print ("\n")
            print (" ...____________________... ")
            print ("    | NO RECORD FOUND | ")
            print ("     ~~~~~~~~~~~~~~~~~~~~~ ")
            fin.close()
    
def Searchhomessn(n):          #search by resident ssn
    fin=open("home.DAT","rb")
    ob=home()
    flag=False
    try:
        print
        print ("n\RESIDENT DETAILS:--")
        while True:
            ob=pickle.load(fin)
            if ob.ssn==n:
                 ob.output()
                 flag=True
    except EOFError:
        if not flag:
            print ("\n")
            print ("\n")
            print (" ...____________________... ")
            print ("    | NO RECORD FOUND | ")
            print ("     ~~~~~~~~~~~~~~~~~~~~~ ")
            fin.close()

def Modihome(b,a): #to modify resident information
    fin=open("home.DAT","rb")
    fout= open("TEMP.DAT","ab")
    ob=home()
    flag = False
    try:
        while True:
            ob=pickle.load(fin)
            if ob.id==b:
                flag=True
                if n==1:
                    a=input("ENTER NEW RESIDENT DOB:")
                    ob.dob=a
                    pickle.dump(ob,fout)
                elif n==2:
                    a=input("ENTER NEW LAST 4 OF RESIDENT'S SSN:")
                    ob.ssn=a
                    pickle.dumb(ob,fout)
                elif n==3:
                    a=input("DOES RESIDENT AGREE TO A BLOOD TRANSFUSION? (YES/NO):")
                    ob.transfusion=a
                    pickle.dump(ob,fout)
                elif n==4:
                    a=input("DOES RESIDENT HAVE A DNR? (YES/NO):")
                    ob.dnr=a
                    pickle.dumb(ob,fout)
                elif n==5:
                    a=input("DOES THE RESIDENT HAVE A LIVING WILL? (YES?NO):")
                    ob.livwill=a
                    pickle.dumb(ob,fout)
                elif n==6:
                    a=input("ENTER RESIDENT'S NEW PRIMARY INSURANCE PROVIDER:")
                    ob.insname=a
                    pickle.dumb(ob,fout)
                elif n==7:
                    a=input("ENTER NEW POLICY EFFECTIVE DATE:")
                    ob.inseffdate=a
                    pickle.dumb(ob,fout)
                elif n==8:
                    a=input("ENTER NEW POLICY NUMBER:")
                    pickle.dumb(ob.fout)
                elif n==9:
                    print ("*****UPATE RESIDENT'S ACCOUNT****")
                    ob.input()
                    pickle.dump(ob,fout)
                else:
                    pickle.dumb(ob,fout)
     
    except EOFError:
        if not flag:
            print("\n")
            print("\n")
            print (" ...____________________... ")
            print ("    | NO RECORD FOUND | ")
            print ("    ~~~~~~~~~~~~~~~~~~~~~ ")
        fin.close()

    fout.close()
    os.remove("home.DAT")
    os.rename("TEMP.DAT","home.DAT")

def Delhome(n):
    fin=open("home.DAT","rb")
    fout=open("TEMP.DAT","wb")
    ob=home()
    flag=False
    try:
        while True:
              ob=pickle.load(fin)
              if ob.id==n:
                 flag=True
                 print("RECORD DELETED")
              else:
                 pickle.dump(ob,fout)
    except EOFError:
              if not flag:
                  print("RECORD DOES NOT EXIST")
              fin.close()
              fout.close()
              os.remove("home.DAT")
              os.rename("TEMP.DAT","home.DAT")


#MAIN PROGRAM
while True:
    print("\n")
    print("SWEET COMFORT RESIDENT MANAGEMENT SYSTEM \n")
    print("1. ENTER NEW RESIDENT INFORMATION \n2. SHOW ALL RESIDENTS")
    print("3. SEARCH BY RESIDENT ID# \n4. SEARCH BY LAST 4 SSN")
    print("5. MODIFY RECORD \n6. DELETE RECORD \n7. CLOSE")

    select=input("\nPLEASE MAKE A SELECTION: ")
    if select==1:
       writehome()
    elif select==2:
       readhome()
    elif select==3:
        Searchhomeid(n)
    elif select==4:
        Searchhomessn(n)
    elif select==5:
        m=input("ENTER RESIDENT'S ID# TO MODIFY: ")
        print("\n")
        print("_____________________")
        print("|..RESIDENT FOUND...|")
        print("______________________")
        print("\n")
        print("WHAT INFORMATION WOULD YOU LIKE TO MODIFY:")
        print
        print("1.RESIDENT'S DOB")
        print("2.RESIDENT'S SSN")
        print("3.RESIDENT'S BLOOD TRANFUSION CONSENT")
        print("4.RESIDENT'S DNR CONSENT")
        print("5.RESIDENT HAS LIVING WILL")
        print("6.RESIDENT'S PRIMARY INSURANCE PROVIDER")
        print("7.NEW PRIMARY INSURANCE EFFECTIVE DATE")
        print("8.NEW PRIMARY INSURANCE POLICY NUMBER")
        print("9.MODIFY ALL")
        n=input("::--")
        Modihome(m,n)
    elif select==6:
        n=input("ENTER RESIDENT ID# TO DELETE:")
        Delhome(n)
    elif select==7:
        print("\n")
        print("CLOSING WINDOW"),
        time.sleep(.8)
        print(".")
        time.sleep(.8)
        print(".")
        time.sleep(.8)
        print(".")
        time.sleep(.8)
        print(".")
        break
    else:
        print("SEARCHING......")
        time.sleep(.6)
        print(".")
        time.sleep(.6)
        print(".")
        time.sleep(.6)
        print(".")
        time.sleep(.6)
        print(".")
        print("\n\n\n.........PLEASE RE-ENTER YOUR SELECTION........\n\n\n")
   
    

              
                    
                        
                    
                    
                
