import os,shutil

hzid =[
{'idb':373123,'zyh':'825958'},
{'idb':375924,'zyh':'828139'},
{'idb':376915,'zyh':'715920'},
{'idb':381487,'zyh':'832512'},
{'idb':387784,'zyh':'749352'},
{'idb':393772,'zyh':'834434'},
{'idb':395625,'zyh':'843435'},
{'idb':396421,'zyh':'837791'},
{'idb':398178,'zyh':'807585'},
{'idb':410034,'zyh':'854680'},
{'idb':415870,'zyh':'859118'},
{'idb':423230,'zyh':'864751'},
{'idb':425004,'zyh':'866159'},
{'idb':425859,'zyh':'866777'},
{'idb':427747,'zyh':'674736'},
{'idb':431936,'zyh':'860731'},
{'idb':433265,'zyh':'872174'},
{'idb':433715,'zyh':'872535'},
{'idb':441043,'zyh':'878048'},
{'idb':447444,'zyh':'882935'},
{'idb':451490,'zyh':'825556'},
{'idb':455153,'zyh':'867149'},
{'idb':455512,'zyh':'861406'},
{'idb':466683,'zyh':'897387'},
{'idb':462435,'zyh':'894232'},
{'idb':476615,'zyh':'905108'},
{'idb':477263,'zyh':'905592'},
{'idb':473201,'zyh':'781778'},
{'idb':476952,'zyh':'873350'},
{'idb':130760,'zyh':'651463'},
{'idb':384233,'zyh':'834717'},
{'idb':388120,'zyh':'837760'},
{'idb':386058,'zyh':'836100'},
{'idb':393616,'zyh':'841878'},
{'idb':393629,'zyh':'841928'},
{'idb':394081,'zyh':'798521'},
{'idb':392710,'zyh':'841222'},
{'idb':395239,'zyh':'843147'},
{'idb':397357,'zyh':'844808'},
{'idb':411084,'zyh':'855491'},
{'idb':409650,'zyh':'835287'},
{'idb':410017,'zyh':'819223'},
{'idb':417992,'zyh':'834585'},
{'idb':427013,'zyh':'841605'},
{'idb':432167,'zyh':'871321'},
{'idb':433892,'zyh':'872677'},
{'idb':434326,'zyh':'873005'},
{'idb':437925,'zyh':'875637'},
{'idb':439870,'zyh':'877188'},
{'idb':443019,'zyh':'879497'},
{'idb':444567,'zyh':'880701'},
{'idb':447479,'zyh':'836907'},
{'idb':451206,'zyh':'885770'},
{'idb':459802,'zyh':'892282'},
{'idb':467021,'zyh':'897665'},
{'idb':468835,'zyh':'899024'},
{'idb':461046,'zyh':'893172'},
{'idb':460601,'zyh':'825835'},
{'idb':474121,'zyh':'903122'},
{'idb':473311,'zyh':'902494'},
{'idb':458886,'zyh':'891586'},
{'idb':475419,'zyh':'808424'},
{'idb':370886,'zyh':'742761'},
{'idb':372448,'zyh':'825472'},
{'idb':387638,'zyh':'837384'},
{'idb':392132,'zyh':'840817'},
{'idb':390086,'zyh':'839252'},
{'idb':398179,'zyh':'841754'},
{'idb':402613,'zyh':'848909'},
{'idb':411107,'zyh':'855508'},
{'idb':415529,'zyh':'858856'},
{'idb':419902,'zyh':'862163'},
{'idb':425000,'zyh':'866114'},
{'idb':426345,'zyh':'867149'},
{'idb':432943,'zyh':'871898'},
{'idb':435558,'zyh':'873939'},
{'idb':436378,'zyh':'841886'},
{'idb':446434,'zyh':'882147'},
{'idb':446999,'zyh':'874899'},
{'idb':448687,'zyh':'883866'},
{'idb':452516,'zyh':'885770'},
{'idb':457514,'zyh':'890533'},
{'idb':467612,'zyh':'816973'},
{'idb':470053,'zyh':'899954'},
{'idb':477846,'zyh':'906071'},
{'idb':473864,'zyh':'880447'},
{'idb':464157,'zyh':'879908'},
{'idb':475182,'zyh':'903978'},
{'idb':173781,'zyh':'663170'},
{'idb':125222,'zyh':'650955'},
{'idb':368603,'zyh':'822439'},
{'idb':370347,'zyh':'823837'},
{'idb':363675,'zyh':'807287'},
{'idb':373406,'zyh':'826176'},
{'idb':380592,'zyh':'831811'},
{'idb':384234,'zyh':'811019'},
{'idb':386197,'zyh':'836237'},
{'idb':387000,'zyh':'836127'},
{'idb':388462,'zyh':'701709'},
{'idb':389432,'zyh':'838748'},
{'idb':395343,'zyh':'835301'},
{'idb':406373,'zyh':'836274'},
{'idb':415306,'zyh':'840149'},
{'idb':417303,'zyh':'860209'},
{'idb':434458,'zyh':'873107'},
{'idb':435738,'zyh':'874078'},
{'idb':435018,'zyh':'873524'},
{'idb':441918,'zyh':'878675'},
{'idb':445406,'zyh':'715233'},
{'idb':452546,'zyh':'886765'},
{'idb':453744,'zyh':'887654'},
{'idb':455627,'zyh':'876895'},
{'idb':470061,'zyh':'899960'},
{'idb':478808,'zyh':'880629'},
{'idb':469457,'zyh':'751913'},
{'idb':461810,'zyh':'860058'},
{'idb':468283,'zyh':'898629'},
{'idb':468145,'zyh':'887622'},
{'idb':470066,'zyh':'675928'},
{'idb':472253,'zyh':'901671'},
{'idb':475191,'zyh':'903969'},
{'idb':370573,'zyh':'824023'},
{'idb':369831,'zyh':'790059'},
{'idb':372468,'zyh':'825479'},
{'idb':371647,'zyh':'824843'},
{'idb':372174,'zyh':'825252'},
{'idb':375918,'zyh':'828133'},
{'idb':378817,'zyh':'830366'},
{'idb':387303,'zyh':'835829'},
{'idb':386306,'zyh':'836328'},
{'idb':390922,'zyh':'819223'},
{'idb':389876,'zyh':'837677'},
{'idb':387991,'zyh':'804262'},
{'idb':393608,'zyh':'820561'},
{'idb':404715,'zyh':'732110'},
{'idb':405521,'zyh':'851182'},
{'idb':408262,'zyh':'853242'},
{'idb':412615,'zyh':'856661'},
{'idb':415515,'zyh':'858840'},
{'idb':415888,'zyh':'832230'},
{'idb':418088,'zyh':'843091'},
{'idb':422372,'zyh':'864088'},
{'idb':424053,'zyh':'864723'},
{'idb':432340,'zyh':'871445'},
{'idb':433739,'zyh':'872551'},
{'idb':433672,'zyh':'872518'},
{'idb':435690,'zyh':'874048'},
{'idb':442566,'zyh':'878048'},
{'idb':445720,'zyh':'881328'},
{'idb':454447,'zyh':'888179'},
{'idb':453397,'zyh':'887400'},
{'idb':470190,'zyh':'900060'},
{'idb':476960,'zyh':'898629'},
{'idb':472587,'zyh':'857372'},
{'idb':468126,'zyh':'898507'},
{'idb':469156,'zyh':'889154'},
{'idb':475333,'zyh':'644647'},
{'idb':168741,'zyh':'658330'},
{'idb':368644,'zyh':'822508'},
{'idb':372306,'zyh':'813611'},
{'idb':380508,'zyh':'831729'},
{'idb':382636,'zyh':'833443'},
{'idb':383848,'zyh':'834407'},
{'idb':386290,'zyh':'836281'},
{'idb':388129,'zyh':'837766'},
{'idb':390267,'zyh':'839363'},
{'idb':390343,'zyh':'836929'},
{'idb':392702,'zyh':'841249'},
{'idb':391696,'zyh':'840475'},
{'idb':393592,'zyh':'841876'},
{'idb':397531,'zyh':'844941'},
{'idb':417134,'zyh':'860076'},
{'idb':418944,'zyh':'861406'},
{'idb':424137,'zyh':'865477'},
{'idb':427120,'zyh':'867664'},
{'idb':433319,'zyh':'872224'},
{'idb':431685,'zyh':'870961'},
{'idb':435615,'zyh':'732110'},
{'idb':443481,'zyh':'879835'},
{'idb':443003,'zyh':'879417'},
{'idb':443976,'zyh':'880239'},
{'idb':450131,'zyh':'884961'},
{'idb':450665,'zyh':'885371'},
{'idb':451252,'zyh':'885822'},
{'idb':450565,'zyh':'885271'},
{'idb':471888,'zyh':'901383'},
{'idb':460621,'zyh':'892892'},
{'idb':468285,'zyh':'898635'},
{'idb':467155,'zyh':'867095'},
{'idb':469472,'zyh':'899517'},
{'idb':470316,'zyh':'900164'},
{'idb':469810,'zyh':'899782'},
{'idb':478866,'zyh':'906909'},
{'idb':476599,'zyh':'839389'},
{'idb':478609,'zyh':'845474'},
{'idb':463556,'zyh':'895097'},
{'idb':462777,'zyh':'894523'},
{'idb':471838,'zyh':'901335'},
{'idb':472588,'zyh':'901943'},
{'idb':168563,'zyh':'658152'},
{'idb':270235,'zyh':'747660'},
{'idb':369178,'zyh':'822909'},
{'idb':369545,'zyh':'823202'},
{'idb':372511,'zyh':'813630'},
{'idb':387183,'zyh':'837043'},
{'idb':393483,'zyh':'841800'},
{'idb':392392,'zyh':'841013'},
{'idb':397674,'zyh':'845050'},
{'idb':399321,'zyh':'846361'},
{'idb':404519,'zyh':'835287'},
{'idb':405847,'zyh':'851437'},
{'idb':410166,'zyh':'854782'},
{'idb':416959,'zyh':'859950'},
{'idb':415320,'zyh':'838581'},
{'idb':427276,'zyh':'867869'},
{'idb':432981,'zyh':'871941'},
{'idb':433714,'zyh':'867567'},
{'idb':436795,'zyh':'766850'},
{'idb':435006,'zyh':'873517'},
{'idb':437253,'zyh':'875160'},
{'idb':436471,'zyh':'872224'},
{'idb':445263,'zyh':'880771'},
{'idb':442207,'zyh':'650794'},
{'idb':447251,'zyh':'882778'},
{'idb':447712,'zyh':'800218'},
{'idb':451362,'zyh':'885857'},
{'idb':455887,'zyh':'889264'},
{'idb':454698,'zyh':'888366'},
{'idb':457049,'zyh':'890172'},
{'idb':457170,'zyh':'714766'},
{'idb':466836,'zyh':'897529'},
{'idb':466783,'zyh':'897463'},
{'idb':460585,'zyh':'892866'},
{'idb':461409,'zyh':'791427'},
{'idb':462444,'zyh':'894269'},
{'idb':475882,'zyh':'904516'},
{'idb':476180,'zyh':'892484'},
{'idb':475952,'zyh':'904567'},
{'idb':168948,'zyh':'658527'},
{'idb':370949,'zyh':'824324'},
{'idb':374360,'zyh':'826940'},
{'idb':379813,'zyh':'831150'},
{'idb':383828,'zyh':'834380'},
{'idb':382444,'zyh':'832512'},
{'idb':384660,'zyh':'702581'},
{'idb':384047,'zyh':'834571'},
{'idb':387969,'zyh':'837626'},
{'idb':387318,'zyh':'836929'},
{'idb':390251,'zyh':'839364'},
{'idb':395268,'zyh':'803543'},
{'idb':397470,'zyh':'844878'},
{'idb':406689,'zyh':'852083'},
{'idb':411499,'zyh':'855817'},
{'idb':410956,'zyh':'855402'},
{'idb':411782,'zyh':'856017'},
{'idb':417887,'zyh':'860617'},
{'idb':420649,'zyh':'804683'},
{'idb':431806,'zyh':'871050'},
{'idb':434370,'zyh':'873041'},
{'idb':436671,'zyh':'859038'},
{'idb':441680,'zyh':'876213'},
{'idb':440372,'zyh':'877559'},
{'idb':444089,'zyh':'873724'},
{'idb':451250,'zyh':'824796'},
{'idb':455060,'zyh':'879719'},
{'idb':458591,'zyh':'891365'},
{'idb':469561,'zyh':'899578'},
{'idb':478028,'zyh':'906221'},
{'idb':473998,'zyh':'903025'},
{'idb':474104,'zyh':'903111'},
{'idb':471864,'zyh':'901365'},
{'idb':459183,'zyh':'891810'}]

def main():
  for item in hzid:
    filepath =  'D:\\savedoc\\'+item['zyh'][-3:] +'\\'+item['zyh']+'\\'+str(item['idb'])
    if os.path.exists(filepath):
      shutil.copytree(filepath, 'E:\\'+item['zyh']+'\\'+str(item['idb']))
      print(filepath+'copy dir finished!')

if __name__ == '__main__':
  print('开始执行....')
  main()
  print('结束....')