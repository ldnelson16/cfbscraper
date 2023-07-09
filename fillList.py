#from on3webscraper import Player
import datetime
class Player:
    def __init__(self,name,ratingon3,rating247,ratingespn,ratingrivals,position,city,state,committed,team = False):
        try: ratingon3=int(ratingon3)
        except: pass
        try: rating247=int(rating247)
        except: pass
        try: ratingespn=int(ratingespn)
        except: pass
        try: ratingrivals=float(ratingrivals)
        except: pass
        self.name = name
        self.ron3 = [ratingon3]
        self.r247 = [rating247]
        self.respn = [ratingespn]
        self.rrivals = [ratingrivals]
        self.position = position
        self.city = city
        self.state = state
        self.committed = committed
        self.team = team
    def __str__(self):
        if self.committed == True:
            ret_format = "{}: Ratings - On3:{}, 247:{}, ESPN:{}, Rivals:{}\nPos: {}, City: {}, State: {}\n{} commit"
            return ret_format.format(self.name,self.ron3,self.r247,self.respn,self.rrivals,self.position,self.city,self.state,self.team)
        else:
            ret_format = "{}: Ratings - On3:{}, 247:{}, ESPN:{}, Rivals:{}\nPos: {}, City: {}, State: {}"
            return ret_format.format(self.name,self.ron3,self.r247,self.respn,self.rrivals,self.position,self.city,self.state)
        

def fillList(lst,deslength):
    if(len(lst)!=deslength):
        lst.insert(0,"-")
        fillList(lst,deslength)
    else:
        return lst
    

print(datetime.date.today())
p1 = Player("James Doe",15,25,25,5.4,"QB","Manhattan","NY",False)
print(p1.ron3)
print(p1)
deslen=10
if len(p1.ron3) <= deslen:
    fillList(p1.ron3,deslen)
print(p1.ron3)
print(p1)


startdate = datetime.date(2023,6,8)
def dtFormat(date):
    stri=str(date.year)+"-"+str(date.month)+"-"+str(date.day)
    return stri 
for x in range ((datetime.date.today()-startdate).days):
    filename = dtFormat(startdate+datetime.timedelta(days=x))+"_RecruitData_Cl24.txt"
    try: file = open(filename,"r")
    except: print("PASSED")
    print(filename)

line="Ju�Juan Johnson"
line=line.replace(r'[^\x00-\x7F]', ' ')
print(line)