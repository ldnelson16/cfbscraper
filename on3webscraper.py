import requests
import json
import pandas
import datetime
#!pip install selenium
import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless=new')
options.add_argument('--disable-gpu')

def fillList(lst,deslength):
    if(len(lst)!=deslength):
        lst.insert(0,"-")
        fillList(lst,deslength)
    else:
        return lst


#define Player class
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


def webscrape(results,nameandcities,dates):
    #bring in webscraper, to get today's data
    dates+=[datetime.date.today()]
    printres=[]
    for y in range (1,21):
        url = 'https://www.on3.com/db/rankings/industry-comparison/football/2024/?page='+str(y)
        browser = webdriver.Chrome(options=options)
        browser.get(url)
        for x in range (0,50):
            try:
                xpath_name = '/html/body/div[1]/div[1]/section/main/section/section/ul/li[' + str(1+x) + ']/div[1]/div[1]/div/a'
                xpath_on3 = "/html/body/div[1]/div[1]/section/main/section/section/ul/li[" + str(1+x) + "]/div[2]/div[1]/a/div[1]/div[2]/div/span[2]/span"
                xpath_247 = "/html/body/div[1]/div[1]/section/main/section/section/ul/li[" + str(1+x) + "]/div[2]/div[2]/a/div[1]/div[2]/div/span[2]/span"
                xpath_espn = "/html/body/div[1]/div[1]/section/main/section/section/ul/li[" + str(1+x) + "]/div[2]/div[3]/a/div[1]/div[2]/div/span[2]/span"
                xpath_rivals = "/html/body/div[1]/div[1]/section/main/section/section/ul/li[" + str(1+x) + "]/div[2]/div[4]/a/div[1]/div[2]/div/span[2]/span"
                xpath_pos = "/html/body/div[1]/div[1]/section/main/section/section/ul/li["+ str(1+x) +"]/div[1]/div[1]/p[1]/span[1]"
                xpath_city = "/html/body/div[1]/div[1]/section/main/section/section/ul/li["+ str(1+x) +"]/div[1]/div[1]/p[2]/span[2]"
                xpath_state = "/html/body/div[1]/div[1]/section/main/section/section/ul/li["+ str(1+x) +"]/div[1]/div[1]/p[2]/span[2]"
                xpath_committed = "/html/body/div[1]/div[1]/section/main/section/section/ul/li[" + str(1+x) + "]/div[3]/div/a"
                name = browser.find_element("xpath", xpath_name).text
                try:
                    ron3 = browser.find_element("xpath", xpath_on3).text
                except:
                    try:
                        xpath_on3 = "/html/body/div/div[1]/section/main/section/section/ul/li[" + str(1+x) + "]/div[2]/div[1]/a/div[1]/div[2]/div/span[2]/span"
                        ron3 = browser.find_element("xpath", xpath_on3).text
                    except:
                        try:
                            xpath_on3 = "/html/body/div[1]/div[1]/section/main/section/section/ul/li[" + str(1+x) + "]/div[2]/div[1]/a/div[3]/h6[1]"
                            ron3 = browser.find_element("xpath", xpath_on3).text
                        except:
                            try:
                                xpath_on3 = "/html/body/div[1]/div[1]/section/main/section/section/ul/li[" + str(1+x) + "]/div[2]/div[1]/div/div[3]/h6[1]"
                                ron3 = browser.find_element("xpath", xpath_on3).text
                            except: 
                                ron3 = "-"
                if ron3 != "-":
                    ron3 = int(ron3)
                try:
                    r247 = browser.find_element("xpath", xpath_247).text
                except:
                    try:
                        xpath_247 = "/html/body/div/div[1]/section/main/section/section/ul/li[" + str(1+x) + "]/div[2]/div[2]/a/div[1]/div[2]/div/span[2]/span"
                        r247 = browser.find_element("xpath", xpath_247).text
                    except:
                        try:
                            xpath_247 = "/html/body/div[1]/div[1]/section/main/section/section/ul/li[" + str(1+x) + "]/div[2]/div[2]/a/div[3]/h6[1]"
                            r247 = browser.find_element("xpath", xpath_247).text
                        except:
                            try:
                                xpath_247 = "/html/body/div[1]/div[1]/section/main/section/section/ul/li[" + str(1+x) + "]/div[2]/div[2]/div/div[3]/h6[1]"
                                r247 = browser.find_element("xpath", xpath_247).text
                            except: 
                                r247 = "-"
                if r247 != "-":
                    r247 = int(r247)
                try:
                    respn = browser.find_element("xpath", xpath_espn).text
                except:
                    try:
                        xpath_espn = "/html/body/div/div[1]/section/main/section/section/ul/li[" + str(1+x) + "]/div[2]/div[3]/div/div[1]/div[2]/div/span[2]/span"
                        respn = browser.find_element("xpath", xpath_espn).text                     
                    except:
                        try:
                            xpath_espn = "/html/body/div/div[1]/section/main/section/section/ul/li[" + str(1+x) + "]/div[2]/div[3]/a/div[3]/h6[1]"
                            respn = browser.find_element("xpath", xpath_espn).text 
                        except:
                            try:
                                xpath_espn = "/html/body/div[1]/div[1]/section/main/section/section/ul/li[" + str(1+x) + "]/div[2]/div[3]/div/div[3]/h6[1]"
                                respn = browser.find_element("xpath",xpath_espn).text
                            except: 
                                respn = "-"
                if respn != "-":
                    respn = int(respn)
                try:
                    rrivals = browser.find_element("xpath", xpath_rivals).text
                except:
                    try:
                        xpath_rivals = "/html/body/div/div[1]/section/main/section/section/ul/li[" + str(1+x) + "]/div[2]/div[4]/a/div[1]/div[2]/div/span[2]/span"
                        rrivals = browser.find_element("xpath", xpath_rivals).text
                    except:
                        try:
                            xpath_rivals = "/html/body/div[1]/div[1]/section/main/section/section/ul/li[" + str(1+x) + "]/div[2]/div[4]/a/div[3]/h6[1]"
                            rrivals = browser.find_element("xpath", xpath_rivals).text
                        except:
                            try:
                                xpath_rivals = "/html/body/div[1]/div[1]/section/main/section/section/ul/li[" + str(1+x) + "]/div[2]/div[4]/div/div[3]/h6[1]"
                                rrivals = browser.find_element("xpath", xpath_rivals).text
                            except: 
                                rrivals = "-"
                if rrivals != "-":
                    rrivals = float(rrivals)
                pos = browser.find_element("xpath", xpath_pos).text
                city_state = browser.find_element("xpath", xpath_city).text
                try:
                    committed = browser.find_element("xpath",xpath_committed).text
                    if committed[:11] == "HARD COMMIT":
                        committed = True
                        team = browser.find_element("xpath",xpath_committed).get_attribute('href')
                        team = " ".join(str(team).split("/")[4].split("-")).title()
                    else:
                        committed = False
                        team = False
                except:
                    committed = False
                    team = False
                addPlayer(name,ron3,r247,respn,rrivals,pos,city_state[:-4],city_state[-2:],committed,team,results,nameandcities)
                p1 = Player(name,ron3,r247,respn,rrivals,pos,city_state[:-4],city_state[-2:],committed,team)
                printres+=[p1]
                file = open(dtFormat(datetime.date.today())+"_RecruitData_Cl24.txt","w")
                file.write("Name\tOn3 Rating\t247 Rating\tESPN Rating\tRivals Rating\tPosition\tCity\tState\tCommit Status\tCommit Team\n")
                for printr in printres:
                    file.write(printr.name+"\t"+str(printr.ron3)+"\t"+str(printr.r247)+"\t"+str(printr.respn)+"\t"+str(printr.rrivals)+"\t"+printr.position+"\t"+printr.city+"\t"+printr.state+"\t"+str(printr.committed)+"\t"+str(printr.team)+"\t"+"\n")
            except:
                print("Nothing at player #",x+y*50-49)
                pass
        browser.close()
        #outwrite this webscraper data into a new file

def dtFormat(date):
    stri=str(date.year)+"-"+str(date.month)+"-"+str(date.day)
    return stri 

def addPlayer(name,ron3,r247,respn,rrivals,pos,city,state,committed,team,results,nameandcities):
    if ron3!="-": ron3 = int(ron3)
    if r247!="-": r247 = int(r247)
    if respn!="-": respn = int(respn)
    if rrivals!="-": rrivals = float(rrivals)
    player = Player(name,ron3,r247,respn,rrivals,pos,city,state,committed,team)
    if (name,city) in nameandcities:
        results[nameandcities.index((name,city))].ron3+=[ron3]
        results[nameandcities.index((name,city))].r247+=[r247]
        results[nameandcities.index((name,city))].respn+=[respn]
        results[nameandcities.index((name,city))].rrivals+=[rrivals]
    else:
        nameandcities+=[(name,city)]
        results+=[player]

#first, bring in all previous results

results = []
nameandcities = []
startdate = datetime.date(2023,6,7)
dates=[]
x=0
while (startdate+datetime.timedelta(days=x)<datetime.date.today()):
    filename = dtFormat(startdate+datetime.timedelta(days=x))+"_RecruitData_Cl24.txt"
    try: 
        file = open(filename,"r")
        dates+=[startdate+datetime.timedelta(days=x)]
        for line in file.readlines()[1:]:
            data=line.split("\t")
            addPlayer(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],results,nameandcities)
    except: 
        print("No data from "+dtFormat(startdate+datetime.timedelta(days=x)))
    x+=1
webscrape(results,nameandcities,dates)

#resort results and nameandcities alphabetically
results.sort(key=lambda result: result.name)
nameandcities.sort(key=lambda nc: nc[0])

#go through and find duplicates
for x in range(len(results)):
    if len(results[x].ron3)!=len(dates):
        print(results[x],"Might be an error")

#go through, and if any not correct length, append hyphen to them to fill spots
for result in results:
    #print(len(result.ron3),len(result.r247),len(result.respn),len(result.rrivals),len(dates)) 
    if len(result.ron3)<=len(dates):
        #print("FILLING on3")
        fillList(result.ron3,len(dates))
    if len(result.r247)<=len(dates):
        #print("FILLING 247")
        fillList(result.r247,len(dates))
    if len(result.respn)<=len(dates):
        #print("FILLING espn")
        fillList(result.respn,len(dates))
    if len(result.rrivals)<=len(dates):
        #print("FILLING rivals")
        fillList(result.rrivals,len(dates))


#for result in results:
    #print(result)
#for namecity in nameandcities:
    #print(namecity)