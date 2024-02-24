{{
    config(
        materialized='view'
    )
}}

with tripdata as 
(
    select *
    from {{ source('staging','fhv_tripdata') }}
    where EXTRACT(YEAR FROM (TIMESTAMP(CAST(pickup_datetime AS STRING)))) = 2019
)
select
   -- identifiers
   {{ dbt_utils.generate_surrogate_key(['dispatching_base_num', 'pickup_datetime']) }} as tripid,
   {{ dbt.safe_cast("dispatching_base_num", api.Column.translate_type("string")) }} as dispatching_base_num,
   {{ dbt.safe_cast("affiliated_base_number", api.Column.translate_type("string")) }} as affliated_base_num,
   {{ dbt.safe_cast("pu_location_id", api.Column.translate_type("integer")) }} as pickup_location_id,
   {{ dbt.safe_cast("do_location_id", api.Column.translate_type("integer")) }} as dropoff_location_id, 

    -- timestamps
    cast(pickup_datetime as timestamp) as pickup_datetime,
    cast(dropoff_datetime as timestamp) as dropoff_datetime,

    -- trip info
    sr_flag
from tripdata

-- dbt build --select <model.sql> --vars '{'is_test_run: false}'
{% if var('is_test_run', default=true) %}

  limit 100

{% endif %}
