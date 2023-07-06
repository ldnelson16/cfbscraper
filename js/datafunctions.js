function fillList(lst,deslength) {
  if(lst.length<deslength){
    lst.unshift("-");
    fillList(lst,deslength);
  }
  else {
    return lst;
  }
}
function addPlayer(name,ron3,r247,respn,rrivals,pos,city,state,committed,team,results,nameandcities) {
  let player=new Player(name,ron3,r247,respn,rrivals,pos,city,state,committed,team);
  if ((name,city) in nameandcities){
    results[nameandcities.index((name,city))].ron3+=[ron3]
    results[nameandcities.index((name,city))].r247+=[r247]
    results[nameandcities.index((name,city))].respn+=[respn]
    results[nameandcities.index((name,city))].rrivals+=[rrivals]
  }
  else{
    nameandcities+=[(name,city)]
    results+=[player]
  }
}