import pandas as pd
size = pd.Categorical(['M', 'S', 'M', 'L'],
                      ordered=True,
                      categories=['S', 'M', 'L']
                      )

print(size)
print(size.min())
