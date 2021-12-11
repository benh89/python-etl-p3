import sql
from pgsql import query_create
from pgsql import query_insert
from google.cloud import bigquery;


if __name__ == '__main__':
    query_create(sql.create_schema)

    client = bigquery.Client()
    query = client.query(
        """
    #StandardSQL
    with loc_info as(
    select t1.geo_id,t2.sub_region_1 as state,t2.sub_region_2 as county,
           avg(t2.retail_and_recreation_percent_change_from_baseline) as sales_vector 
    from `bigquery-public-data.census_bureau_acs.county_2017_1yr` t1
      join `bigquery-public-data.covid19_google_mobility.mobility_report` t2 on t1.geo_id||'.0' = t2.census_fips_code
    where t1.median_rent < 2000 and t1.median_age < 30
    group by t1.geo_id,t2.sub_region_1,t2.sub_region_2
    having sales_vector > -15)
    select geo_id,state,county,sales_vector 
    from loc_info             
    order by sales_vector desc 

        """
    )
    for row in query.result():
        query_insert(sql.insert_county,row)
        #print(row)
