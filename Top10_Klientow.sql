select customername, round(sum(Sales),2) as Sprzedaz, round(sum(Profit),2) as Zysk, count(OrderID) as Ilosc_Zamowien
from sales_data as sd
Group by customername 
order by Zysk DESC 
limit 10;