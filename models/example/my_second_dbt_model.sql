-- Use the `ref` function to select from other models

select
    *,
    null as column_3
from {{ ref('my_first_dbt_model') }}
where id = 1
