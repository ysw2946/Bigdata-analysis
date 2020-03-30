libname sql "C:\Users\ysw29\Downloads\SQL실습데이터";
proc sql;
title 'population of large countries grouped by continent';
select continent, sum(population) as totpop format=comma 15.
from sql.countries
where population gt 1000000
group by continent
order by totpop;
quit;

PROC SQL;
select *
from sql.countries
where population gt 5000000;
quit;
