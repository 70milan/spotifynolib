/* count liked songs by year */

insert into song_count ("year", song_ct)
select 
distinct(right(date_added, 4)) as "year"
,count(track_list) as song_ct
from song_details
group by "year" order by 1 desc;


/* tracks by year */

select min("2018") as "2018",min("2019") as "2019",min("2020") as "2020",min("2021")as "2021", min("2022") as "2022" from(
select
YEAR_ADDED,
row_number() over(partition by year_added order by track_list) as rn,
case when	YEAR_ADDED = '2018' then track_list else null end as "2018",
case when	YEAR_ADDED = '2019' then track_list else null end as "2019",
case when	YEAR_ADDED = '2020' then track_list else null end as "2020",
case when	YEAR_ADDED = '2021' then track_list else null end as "2021",
case when	YEAR_ADDED = '2022' then track_list else null end as "2022"
from dataeng.year_added group by year_added, track_list) as temp
group by rn order by rn

/* artists by year */

select min("2018") as "2018",min("2019") as "2019",min("2020") as "2020",min("2021")as "2021", min("2022") as "2022" from(
select
YEAR_ADDED,
row_number() over(partition by year_added order by artists_list) as rn,
case when	YEAR_ADDED = '2018' then artists_list else null end as "2018",
case when	YEAR_ADDED = '2019' then artists_list else null end as "2019",
case when	YEAR_ADDED = '2020' then artists_list else null end as "2020",
case when	YEAR_ADDED = '2021' then artists_list else null end as "2021",
case when	YEAR_ADDED = '2022' then artists_list else null end as "2022"
from dataeng.year_added group by year_added, artists_list) as temp
group by rn order by rn

/* artists by year */