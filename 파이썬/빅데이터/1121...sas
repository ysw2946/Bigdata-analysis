data one ;
input x y ;
cards ;
294   30
247   32
267   37
358   44
423   47
311   49
450   56
534   62
438   68
697   78
688   80
630   84
709   88
627   97
615   100
999   109
1022   114
1015   117
700   106
850   128
980   130
1025   160
1021   97
1200   180
1250   112
1500   210
1650   135
run ;

proc gplot ;
plot y*x ;
run ;

proc reg ;
model y=x ;
run ;

proc transreg ;
model boxcox(y/lambda=-2 to 2 by 1 )=identity(x) ;
run ;
/*box-cox result lambda 값이 0에서 1사이가 최적 즉 lambda 를 통한 transforamtion이 필요 x */

/* Y 만 transformation */
data two ;
set one ;
logy=log(y) ;
run ;

proc gplot ;
plot logy*x ;
run ;

proc reg ;
model logy=x ;
run ;

/* X Y 둘다 transformation*/ 
data three ;
set two ;
logx=log(x) ;
run ;

proc gplot ;
plot logy*logx ;
run ;

proc reg ;
model logy=logx ;
run ;

data three;
b0=14.448;
b1=0.1054;
a0=3.515;
a1=0.0012;
yhat()=(b0+b1);
yhat1()=(a0+a1);
run;
proc print;
var x1 yhat yhat1 ;
run;
