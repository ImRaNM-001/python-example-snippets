def find_min(a: int, b: int, c: int) -> None:
    if a <= b and a <= c:
        print(f'{a} is smaller')
    elif b <= c and b <= a:
        print(f'{b} is smaller')
    else:
        print(f'{c} is smaller')

      
find_min(65, 65, 231)             # find_min(65, 65, 231) <= is added instead of < only to avoid printing 231 is smaller in this case
find_min(100, 37, 231)



# optimized using "min" fn
# find_min = lambda a, b, c: min(a, b, c)
# print(find_min(3, 41, 111))
