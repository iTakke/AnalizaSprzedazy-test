Select SubCategory, round(sum(profit),2) as Zysk_Calkowity
from sales_data as sd
GROUP  by sd.SubCategory 
ORDER By Zysk_Calkowity desc
LIMIT 5;
