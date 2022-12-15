#visualization

--------------------------------------------------------
tables needed: 
1) count liked songs by year: 
insert into song_count ("year", song_ct)
select 
distinct(right(date_added, 4)) as "year"
,count(track_list) as song_ct
from song_details
group by "year" order by 1 desc;

select * from song_count
2) fav songs by year:

3) top fav artists by year:

4) avg scores by year:

5) Fav genre by year:



q = "SELECT * FROM df_target LIMIT 3"
sqldf(q, globals())





from pandas_profiling import ProfileReport
prof = ProfileReport(df)
prof.to_file(output_file='report.html')




https://towardsdatascience.com/complete-guide-to-data-visualization-with-python-2dd74df12b5e
df.describe() 
df.info()
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
df.plot(x="artists_list", y="track_list", kind="bar")
#################################################
#################################################
#################################################
#################################################

df_merged.to_csv('C:/projects/Data Engineering/py/apicalls/spotify/data/song_details.csv', encoding='utf-8')
