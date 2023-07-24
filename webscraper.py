import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

options = Options()
#options.add_argument('--headless=new')
options.add_argument('--disable-gpu')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

def remove_ascii_characters(text):
    ascii_free_text = ""
    for char in text:
        if ord(char) < 128:  # Check if the character is within the ASCII range
            ascii_free_text += char
    return ascii_free_text

def fillList(lst,deslength):
    if(len(lst)!=deslength):
        lst.insert(0,"-")
        fillList(lst,deslength)
    else:
        return lst

def webscrape(data,nameandcities,dates):
    #bring in webscraper, to get today's data
    dates+=[dtFormat(datetime.date.today())]
    data["dates"]=dates
    print(dates)
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
                xpath_committed = "/html/body/div[1]/div[1]/section/main/section/section/ul/li[" + str(1+x) + "]/div[3]/div/a"
                name = browser.find_element("xpath", xpath_name).text
                name=remove_ascii_characters(name)
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
                addPlayer(name,ron3,r247,respn,rrivals,pos,city_state[:-4],city_state[-2:],team,data,nameandcities,dates)
            except:
                print("Nothing at player #",x+y*50-49)
                pass
        browser.close()
        #outwrite this webscraper data into a new file

def dtFormat(date):
    stri=str(date.year)+"-"+str(date.month)+"-"+str(date.day)
    return stri 

def addPlayer(name,ron3,r247,respn,rrivals,pos,city,state,team,data,nameandcities,dates):
    if (name,city) in nameandcities:
        data["players"][nameandcities.index((name,city))]["ON3 Rating"]+=[ron3]
        data["players"][nameandcities.index((name,city))]["247 Rating"]+=[r247]
        data["players"][nameandcities.index((name,city))]["ESPN Rating"]+=[respn]
        data["players"][nameandcities.index((name,city))]["Rivals Rating"]+=[rrivals]
    else:
        nameandcities+=[(name,city)]
        ron3=fillList([ron3],len(dates))
        r247=fillList([r247],len(dates))
        respn=fillList([respn],len(dates))
        rrivals=fillList([rrivals],len(dates))
        data["players"]+=[{"name":name,"ON3 Rating":ron3,"247 Rating":r247,"ESPN Rating":respn,"Rivals Rating":rrivals,"Pos":pos,"City":city,"State":state,"Commit Status":team}]

file = open("data.json")
data=json.load(file)
#load results
nameandcities=[]
try:
    dates=data["dates"]
except: 
    print("NO DATES, file should be empty")
    dates=[]
for player in data["players"]:
    nameandcities+=[(player["name"],player["City"])]
file.close()
print("Beginning Webscraping")
webscrape(data,nameandcities,dates)

#alphabetize results
data["players"]=sorted(data["players"],key=lambda p: p["name"])

#test print statements
#print(data)
#print(nameandcities)

#write out new file
json_dt=json.dumps(data)
with open("data.json","w") as f:
    f.write(json_dt)