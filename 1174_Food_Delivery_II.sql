# Write your MySQL query statement below

select round(sum(if (min_ord=min_cust_pref,1,0)*100)/count(min_ord),2) as immediate_percentage from 
(
select  delivery_id , customer_id , min(order_date) as min_ord , min(customer_pref_delivery_date) as min_cust_pref 
from Delivery 
group by customer_id

) as new_table
