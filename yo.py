import random;
import time;
import datetime;
import re;
list_of_stations=['del','hyd','amr','ban','mum','goa','che','kol','shi','sri']
class ToStation:
    to=""
    def details(self):
        print(" stations with their code:\n 1.Delhi - del\n 2.Hyderabad - hyd\n 3.Amaravathi - amr\n 4.Bangalore - ban\n 5.Mumbai - mum\n 6.Goa - goa\n 7.Chennai - che\n 8.Kolkata - kol\n 9.Shimla - shi\n 10.Srinagar - sri\n")
        ToStation.to=input("enter your to station code:")
        while(ToStation.to not in list_of_stations):
            ToStation.to=input("Incorrect entry. enter your to station again:")
            break
        
class FromStation:
    fro=""
    def details(self):
        print(" stations with their code:\n 1.Delhi - del\n 2.Hyderabad - hyd\n 3.Amaravathi - amr\n 4.Bangalore - ban\n 5.Mumbai - mum\n 6.Goa - goa\n 7.Chennai - che\n 8.Kolkata - kol\n 9.Shimla - shi\n 10.Srinagar - sri\n")
        FromStation.fro=input("enter your from station:")
        while(FromStation.fro not in list_of_stations):
            FromStation.fro=input("Incorrect entry. enter your to station again:")
            break
    
class DateOfJourney:
    day="";date="";month="";year="";timing=""
    def getDetails(self):
        print("enter date of journey (format [dont miss commas and must be in lowercases]:fri,18,apr,2004):")
        list_of_days=['mon','tue','wed','thu','fri','sat','sun']
        list_of_dates=[str(i) for i in list(range(1,32))]
        list_of_months=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
        list_of_years=[str(datetime.datetime.now().year),str(datetime.datetime.now().year+1)]
        list_of_timings=['00:00','2:00','4:00','6:00','9:00','12:00','14:00','16:30','18:00','21:00','22:00']
        DateOfJourney.day,DateOfJourney.date,DateOfJourney.month,DateOfJourney.year=input().split(',')
        while( DateOfJourney.year not in list_of_years or DateOfJourney.month not in list_of_months or DateOfJourney.year not in list_of_years):
            DateOfJourney.day,DateOfJourney.date,DateOfJourney.month,DateOfJourney.year=input("invalid entry,enter again as per instructions:").split(',')
        print("enter timings [as it is]:\n",list_of_timings)
        DateOfJourney.timing=input()
        while(DateOfJourney.timing not in list_of_timings):
                DateOfJourney.timing=input("invalid entry enter again as per instructions:")
class PassengerDetails:
    name=""
    age=""
    sex=""
    children=0
    adults=0
    def get(self):
        PassengerDetails.name=input("enter your name:")
        PassengerDetails.age=int(input("enter age:"))
        PassengerDetails.sex=input("enter your sexualitiy(f/m/o):")
        while((PassengerDetails.sex)!='f' and (PassengerDetails.sex)!='m' and (PassengerDetails.sex)!='o'):
            PassengerDetails.sex=input("enter again (f/m/o):")

class Train(FromStation,ToStation,DateOfJourney,PassengerDetails):
    amount=0.00
    def reserve(self):
        FromStation.details(self)
        ToStation.details(self)
        DateOfJourney.getDetails(self)

    def bookTickets(self):
        PassengerDetails.adults=int(input("enter no.of adults(maximum no.of seats are 60):"))
        while(PassengerDetails.adults>60):
            PassengerDetails.adults=int(input("please enter no.of adults again(maximum no.of seats are 60):"))
        PassengerDetails.childern=int(input("enter no.of childern(maximum no.of seats are 60):"))
        while(PassengerDetails.childern>60):
            PassengerDetails.childern=int(input("please enter no.of childern again(maximum no.of seats are 60):"))
        dic={'del':3,'hyd':8,'amr':9,'ban':7,'mum':5,'goa':6,'che':10,'kol':4,'shi':2,'sri':1}
        m = list_of_stations
        n = list_of_stations
        if(FromStation.fro == ToStation.to):
            print("Dear customer you have choosen same station as from and to address.Try again")
            FromStation.details(self)
            ToStation.details(self)
            
        else:
            for i in range(0,9):
                for j in range(0,9):
                    if(m[i]==FromStation.fro):
                        if(n[j]==ToStation.to):
                            c=dic[m[i]]
                            d=dic[n[j]]
                            l=abs(c-d)
                            Train.amount=((100*(l)+0.5*(l)+0.1*(l))*PassengerDetails.adults)+((100*(l)+0.5*(l)+0.1*(l))*PassengerDetails.childern)/2
                        else:
                            continue
            print("Tickets have been booked!!!reservation confirmed")
            
    def deleteTickets(self):
        print("Tickets have been deleted.....")
        Train.amount=0.00
        FromStation.fro=''
        ToStation.to=''
        DateOfJourney.day=""
        DateOfJourney.date=""
        DateOfJourney.month=""
        DateOfJourney.year=""
        DateOfJourney.timing=""
        
    def login(self):
        PassengerDetails.get(self)
            
    def ticket(self):
        dic={ }
        print('-*-'*20)
        print("date of ticket generation: ",time.ctime(),"\nPassenger details:\n","name:",PassengerDetails.name,"\t age:",PassengerDetails.age,"\t gender:",PassengerDetails.sex,
              "\n Date of journey: ",DateOfJourney.day,DateOfJourney.date,DateOfJourney.month,DateOfJourney.year,"\t timings: ",DateOfJourney.timing,
              "\n From:",FromStation.fro,"\t To:",ToStation.to,"\n number of childern:",PassengerDetails.childern,"\n number of adults:",PassengerDetails.adults, "Total Amount:",self.amount)
        print("Thank you for your time and money !!! have a safe journey")
        print('-*-'*20)
        
print("*"*7+"Welcome to prayanam railways!!!"+"*"*7+"\t ~ yatriyo kripaya dyandhe....")
obj = Train()
obj.reserve()
print("enter\n 0: login\n 1: to book tickets\n 2: to print ticket\n 3: to delete tickets\n 777:to exit\n")
sus=int(input())
while(sus!=777):
    if(sus==0):
        obj.login()
    if(sus==1):
        obj.bookTickets()
    if(sus==2):
        obj.ticket()
    if(sus==3):
        obj.deleteTickets()
        print("Do visit us again")
    sus=int(input("enter 0: login\n 1: to book tickets\n 2: to print ticket\n 3: to delete tickets\n 777:to exit\n"))
if(sus==777):
    print("Thank you for your attention.Do visit us again")
    pass
