print("\n\n\n")
print("---------------------------------------++ WELCOME TO XYZ BLOOD DONATION BLOOD SERVICES ++-----------------------------------------")
print("\n                                                 This Is A Login Portal\n\n")
print("Please follow the given instructions in order to log in")
print("\nFOR ADMIN LOGIN: PRESS 1")
print("FOR USER LOGIN : PRESS 2")
q=int(input())

class donor:
  x=0 #for counting no. of donors
  def _init_(self,name,age,sex,blood_group,platelets_count,wbc_count,rbc_count):
    self.name=name
    self.age=age
    self.sex=sex
    self.blood_group=blood_group
    self.platelets_count=platelets_count
    self.wbc_count=wbc_count
    self.rbc_count=rbc_count
    donor.x+=1

donor_1=donor('JAY',20,'MALE','A+',200234,34768,54678)
donor_2=donor('GAURAV',44,'MALE','AB-',203456,36758,56780)
donor_3=donor('ANSHI',34,'FEMALE','O+',345670,45678,36987)
donor_4=donor('ASHIMA',29,'FEMALE','B-',354678,67547,45691)
donor_5=donor('ALEX',31,'MALE','A+',321432,56543,56764)
donor_6=donor('SUMAN',33,'FEMALE','A-',265439,45654,65478)
donor_7=donor('RAHUL',48,'MALE','A+',234188,45678,65785)
donor_8=donor('KAMLESH',24,'MALE','A+',267554,45694,56543)
donor_9=donor('LAXMAN',25,'MALE','AB+',265354,46614,52743)
donor_10=donor('PRAKHAR',52,'MALE','A+',267462,45204,56783)


def blood_banks():
  print("\n\nFollowing blood banks are avalable near you: ")
  print("\n\n1. Jeevan Jyoti Blood Bank")
  print("\n2. Indra Diagonostic Centre & Blood Bank")
  print("\n3. AMA Blood Bank")
  print("\n4. ML Nehru Blood Bank")
  print("\n5. Indra Blood Bank")
  print("\n6. City Hospital and Blood Bank")


def rare_blood_groups():
  print("\nDonors with rare blood groups and their details are listed below: ")
  print("\nNAME       AGE         SEX           BLOOD_GROUP\n")
  print("MADHAV      44         MALE           AB-\n")
  print("RASHMIKA    34         FEMALE         O+\n")
  print("SURBHI      29         FEMALE         B-\n")
  print("ABHIMANYU   25         MALE           AB+\n")

if q==1:
  print("\n\n-------------------- Welcome Admin ---------------------\n")
  w=input("Please enter your username: ")
  w.lower()
  if w=='harsh':
    b=input("\nUsername found!\n\n Please enter your password: ")
    b.lower()
    if b=='123':
      print("\nSigned In successfully!")
      print("\n\n-------------Hello Admin Welcome back-----------------")
      print("\n\nTell me what you want to know")
      print("\n1. Details of the Donors")       #Only admins can know the details of the donors
      print("\n2. Details of the Blood Banks")
      print("\n3. Details of the donors with rare blood groups")
      a=int(input("\n\nEnter a choice from the above: "))
      if a==1:
        l1=[donor_1,donor_2,donor_3,donor_4,donor_5,donor_6,donor_7,donor_8,donor_9,donor_10]
        for f in l1:
          print("\n")
          print(f._dict_)
      elif a==2:
        blood_banks()
      elif a==3:
        rare_blood_groups()
      else:
        print("\nInvalid Choice!")
    else:
      print("\nPassword doesn't match!")

  else:
    print("\nAdmin not found. Please enter the correct Username")

elif q==2:
  print("\n\n-------------------- Welcome User ---------------------\n")
  w=input("Please enter your username: ")
  w.lower()
  if w=='amruth' or 'siddhant' or 'vani' or 'madhav' or 'gaurav':
    b=input("\nUsername found!\n\n Please enter your password: ")
    b.lower()
    c=1
    if b=='password':

      print("\nSigned In successfully!")
      while c==1:
          print("\n\n-------------Hello User Welcome back-----------------")
          print("\n\nTell me what you want to know")
          print("\n1. Number of the Donors available")  #Users can only know the number of donors available and not their details
          print("\n2. Details of the Blood Banks")
          print("\n3. Details of the donors with rare blood groups")
          print("\n4. To EXIT")
          a=int(input("\n\nEnter a choice from the above: "))
          if a==1:
            print("\nTotal number of Donors avalable is: ",donor.x) #donor.x for counting the number of donors
          elif a==2:
            blood_banks()
          elif a==3:
            rare_blood_groups()
          elif a==4:
            c=0
            print("Thank You ,Hope to see you soon!!")
          else:
            print("Invalid choice ! Please Enter a valid one")
    else:
      print("\nPassword doesn't match!")

  else:
    print("\nUser not found. Please enter the correct Username")

else:
  print("\nWrong Choice! Please enter from the above choice only")