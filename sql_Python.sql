select * from dataset_1
select weather,temperature from dataset_1
select * from dataset_1 limit 10
select distinct passanger from dataset_1 
select weather from dataset_1 where destination='Home'
select * from dataset_1 order by coupon 
select destination as Destination from dataset_1
select occupation from dataset_1 group by occupation
select weather,avg(temperature) as avg_temp from dataset_1 group by weather 
select weather,count('temperature') as count_temp from dataset_1 group by weather
select weather , count(distinct temperature) as 'count_distinct_temp' from dataset_1 group by weather
select weather , sum(temperature) as 'sum_temp' from dataset_1 group by weather 
select weather , min(temperature) as 'min_temp' from dataset_1 group by weather
select weather,max(temperature) as 'max_temp' from dataset_1 group by weather
select occupation from dataset_1 group by occupation having occupation = "Student"
select * from dataset_1 union select * from table_to_union
select distinct destination from (select * from dataset_1 union select * from table_to_union)
select destination passanger from(select * from dataset_1 where passanger ='alone')
select * from dataset_1 where weather like 'sun%'
select distinct temperature from dataset_1 where temperature between 29 and 75
select occupation from dataset_1 where occupation in ('Sales & Related ', 'Man agement')