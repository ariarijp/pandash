# pandash

Convert Redash Query Result as Pandas DataFrame

## Installation

```bash
$ pip install git+https://github.com/ariarijp/pandash
```

## Usage

```python
from redash_dynamic_query import RedashDynamicQuery

from pandash import query_to_df

redash = RedashDynamicQuery(endpoint='https://redash.example.com',
                            apikey='REDASH_API_KEY',
                            data_source_id=1,
                            max_wait=60)

df = query_to_df(redash, 1)
```

## License

MIT

## Author

[ariarijp](https://github.com/ariarijp)