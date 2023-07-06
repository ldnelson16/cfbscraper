import {Player} from './playerclass.js';

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

let res = []
let nameandcities = []
addPlayer("J",1,1,1,1,"Q","Q","W",false,false,res,nameandcities);
console.log(res[0].print());
console.log(nameandcities);
addPlayer("J",1.1,1,1,1,"Q","Q","W",false,false,res,nameandcities);
console.log(res[0].print());
console.log(nameandcities);
