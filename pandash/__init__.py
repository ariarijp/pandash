import pandas as pd
from redash_dynamic_query import RedashDynamicQuery


def query_to_df(redash: RedashDynamicQuery, query_id: int, bind: dict = None) -> pd.DataFrame:
    result = redash.query(query_id, bind)
    data = result['query_result']['data']
    columns = [column['name'] for column in data['columns']]
    return pd.DataFrame(data['rows'], columns=columns)
