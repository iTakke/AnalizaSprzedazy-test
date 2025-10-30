select sd.State, round(sum(sales),2) as Sprzedaz, round(sum(profit),2) as Zysk,
round((sum(profit)*100/sum(sales)),2) as Zysk_Marzy_Procent
from sales_data sd 
Group by sd.State
order by Zysk_Marzy_Procent desc;