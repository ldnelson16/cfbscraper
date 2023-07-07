import {Player} from './playerclass.js';
import { Builder, By } from 'selenium-webdriver';
import 'selenium-webdriver';
import chrome from 'selenium-webdriver/chrome.js';


function fillList(lst,deslength) {
  if(lst.length<deslength){
    lst.unshift("-");
    fillList(lst,deslength);
  }
  else {
    return lst;
  }
}
function searchAofAs(arr,arrfind,wantindex=false){
  for(let i=0;i<arr.length;++i){
    if(arr[i].includes(arrfind[0])&&arr[i].includes(arrfind[1])){
      if (wantindex) {return i;}
      return true;
    }
  }
  return false;
}
function addPlayer(name,ron3,r247,respn,rrivals,pos,city,state,committed,team,results,nameandcities) {
  let player=new Player(name,ron3,r247,respn,rrivals,pos,city,state,committed,team);
  if (searchAofAs(nameandcities,[name,city])){
    results[searchAofAs(nameandcities,[name,city],true)].ron3.push(ron3);
    results[searchAofAs(nameandcities,[name,city],true)].r247.push(r247);
    results[searchAofAs(nameandcities,[name,city],true)].respn.push(respn);
    results[searchAofAs(nameandcities,[name,city],true)].rrivals.push(rrivals);
  }
  else{
    nameandcities.push([name,city]);
    results.push(player);
  }
}
async function webScrape(results,nameandcities,dates,url){
  const driver = await new Builder().forBrowser('chrome').build()/*.setChromeOptions(new chrome.Options().headless())*/;
  await driver.get(url);
  var elm = driver.findElement(By.xpath('/html/body/div[1]/div[1]/section/main/section/section/ul/li[2]/div[1]/div[1]/div/a'));
  for(let i=0;i<50;++i){
    //take all data
  }
  elm.getText().then(function(txt) {
    console.log("txt: " + txt);
  });
  /*driver.findElement(By.xpath('/html/body/div[1]/div[1]/section/main/section/section/ul/li[2]/div[1]/div[1]/div/a').then(function(element){
    element.getText().then(function(text){
        console.log(text);
    });
  }));*/
}

let res = []
let nameandcities = []
addPlayer("J",1,1,1,1,"Q","Q","W",false,false,res,nameandcities);
console.log(res[0].print());
console.log(nameandcities);
addPlayer("J",1.1,1,1,1,"Q","Q","W",false,false,res,nameandcities);
console.log(res[0].print());
console.log(nameandcities);

webScrape(res,nameandcities,res,"https://www.on3.com/db/rankings/industry-comparison/football/2024/?page=1");
