""" Data Types in Python"""
a = (1,2,3)
b = "Python Full Stack"
print(type(a))

  
 
print(type(b))
c = {'a':12,'b':23,'c':23}
"""Print marks greater than or equal to 30"""
marks = [20,34,39,40,22]
for i in range(0,len(marks)):
 if (marks[i] >= 30) :
  print(marks[i])

"""Built in functions"""
print("Max", max(marks))
print("Min",min(marks))
avg = sum(marks)/len(marks)
print("Avg",avg)
max = 0
"""Without using built in functions"""
for i in range(0 ,len(marks)): 
 if (marks[i] > max ):
  max = marks[i]
print(max)

for i in range(0,len(marks)):
 if (marks[i] < marks[i-1]):
  max = marks[i]
 else : 
  max = marks[i-1]
print(max)

"""Class in pyton"""

class Employee:
 code : int
 name : str
 dept : str
 desg : str
 sal  : int
 aadhar : int
 def  __init__(self,code,name,dept,desg,sal,aadhar=None):
  self.code = 1 
  self.name = name
  self.dept = dept
  self.desg = desg
  self.sal  =  sal
  self.aadhar = aadhar 
 """
 def infromation(self):
   return f"code : {self.code} name : {self.name} dept : {self.dept}"
 """
 def __str__ (self):
   return f"code : {self.code} name : {self.name} dept : {self.dept} aadhar : {self.aadhar}" 
emp1 = Employee(1,'b','v','a',2)
#print(emp1.infromation())
print(emp1)

emp2 = Employee(331,'bar','vas','ad',2,13434)
#print(emp1.infromation())
print(emp2)


"""Write a function to calculate electricity bill payment as per details 

units consumed <=100 rate is 1Rs/unit
units consumed >100 <=200 is 2Rs/unit
units consumed >200 rate is 4Rs/unit
Sample Calculation :

100 --100 *1 = 100Rs
150 --100*1 + 50*2 = 200Rs
300 -- 100*1+ 100*2 + 100*4 = 700Rs
"""

def electbills(units):
 billamount = 0
 if(units <= 100):
  billamount = units*100
 if(units >100 & units <=200):
  billamount = 100*1+((units-100)*2)
 if(units>200):
  billamount = 100*1+100*2+((units-200)*4)
 return billamount
 

print(electbills(130))
print(electbills(500))
print(electbills(700))

"""Write  a function to display maximum points for a team
 
"""
class Team:
 team: str
 season: int
 matches : int
 points : int
 def  __init__(self,team,season,matches,points):
  self.team = team
  self.season = season
  self.matches = matches
  self.points = points
 def __str__ (self):
   return f"Team : {self.team} Season : {self.season} matches : {self.matches} points : {self.points}" 

GT = Team('GT',2023,5,3)
CSK = Team('CSK',2023,5,5)
RR = Team('RR',2023,5,3)

print(GT)
print(CSK)
print(RR)
index = 0
arr = [GT,CSK,RR]
Max=0
for i in range(0,(len(arr))):
 if (arr[i].points > Max):
  Max = arr[i].points
  index = i 

print(Max)
print(arr[index].team)
