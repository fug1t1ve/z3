from z3 import *
v1=BitVec('v1',32)
v2=BitVec('v2',32)
v3=BitVec('v3',32)
v4=BitVec('v4',32)
v5=BitVec('v5',32)
v6=BitVec('v6',32)
v7=BitVec('v7',32)
v8=BitVec('v8',32)
v9=BitVec('v9',32)
v10=BitVec('v10',32)
v11=BitVec('v11',32)
v12=BitVec('v12',32)
v13=BitVec('v13',32)
v14=BitVec('v14',32)
v15=BitVec('v15',32)
v16=BitVec('v16',32)
v17=BitVec('v17',32)
v18=BitVec('v18',32)
v19=BitVec('v19',32)
v20=BitVec('v20',32)
v21=BitVec('v21',32)
v22=BitVec('v22',32)
v23=BitVec('v23',32)
v24=BitVec('v24',32)
v25=BitVec('v25',32)
st=BitVec('st',32)
s=Solver()
s.add(st*2*(v1^st)-v1==10858)
s.add(st>85,st<=95,v1>96,v1<=111)
s.add(v1%v2==7,v2>90)
s.add(v2/v3+(v3^v2)==21,v2<=99,v3<=119)
s.add(v3%v4+v3==137,v3>115,v4<=99,v4==95)
s.add((v5+v4)^v5==225,v4>90,v5<=89,v5>85)
s.add(v6>110,v7>115,(v6+v7)^(v5+v6)==44,(v6+v7)%v5+v6==161)
s.add(v7>=v8,v8>=v9,v7<=119,v8>90,v9<=89,(v7+v9)^(v8+v9)==122,(v7+v9)%v8+v9==101)
s.add(v9<=v10,v10<=v11,v11<=114,(v9+v10)/v11*v10==97,(v11^(v9-v10))*v10==-10088)
s.add(v11==v12,v12>=v13,v13<=99,v13+v11*(v13-v12)-v11==-1443)
s.add(v13>=v14,v14>=v15,v14*(v13+v15+1)-v15==15514,v14>90,v14<=99)
s.add(v15<=v16,v15>=v17,v16>100,v16<=104,v15+(v16^(v16-v17))-v17==70,(v16+v17)/v15+v15==68)
s.add(v17>=v18,v18>=v19,v18<=59,v19<=44,v17+(v18^(v19+v18))-v19==111,(v18^(v18-v19))+v18==101)
s.add(v19<v20,v20<v21,v19>40,v20>90,v21<109,v21+(v20^(v21+v19))-v19==269,(v21^(v20-v19))+v20==185)
s.add(v21>=v23,v22>=v23,v22<=99,v23>90,v21+(v22^(v22+v21))-v23==185)
s.add(v24>=v25,v23<=v24,v25>95,v24<=109,(((v24-v23)*v24)^v25)-v23==1214,(((v25-v24)*v25)^v23)+v24==-1034)
print(s.check())
print(s.model())
