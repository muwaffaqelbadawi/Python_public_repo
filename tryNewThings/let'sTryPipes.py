from pipe import select, where

nums = [1, 2, 3, 4, 5, 6]

Squared = list(
    filter(lambda x: x % 2 == 0,
           map(lambda x: x**2, nums)
           )
)

print(Squared)

pipsSqusred = list(
    nums
    | select(lambda x: x**2)
    | where(lambda x: x % 2 == 0)
)

print(pipsSqusred)
