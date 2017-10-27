import pandas as pd
from redash_dynamic_query import RedashDynamicQuery


def query_as_df(redash: RedashDynamicQuery, query_id: int, bind: dict = None) -> pd.DataFrame:
    result = redash.query(query_id, bind)
    data = result['query_result']['data']
    columns = [column['name'] for column in data['columns']]
    df = pd.DataFrame(data['rows'])
    return df[columns]
