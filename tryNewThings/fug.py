import pandas as pd
from fugue_sql import fsql



input_df = pd.DataFrame(
    {
        "price": [1, 2, 3, 4],
        "fruit": (['Apple', 'Lemon', 'Orange', 'Quava'])

    }) 

query = '''
        SELECT price, fruit FROM input_df
        WHERE price > 1
        PRINT
        '''
fsql(query).run()
