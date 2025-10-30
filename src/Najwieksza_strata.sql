select Subcategory, round(sum(Profit),2) as Strata_Calkowita
from sales_data as sd 
Group BY sd.SubCategory 
HAVING sum(Profit) < 0
ORDER BY Strata_Calkowita asc
LIMIT 5;
