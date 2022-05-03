# def print_args( *args, **kwargs):
#         weekIds = args[0] if len(args)> 0 else range(1,13)
#         nprojects = kwargs.get('nprojects', 8)
#         print(f'{nprojects} projects in {len(weekIds)} weeks', end=': ')
#         print(f"slary about {kwargs['salary']} {kwargs['unit']}")
# print_args(nprojects=10, speed=7, salary='5x', unit=' that of peers')  
# memo = {0:0, 1:1}
# def fun(n):
#     if not n in memo:
#          memo[n] = fun(n-1) +fun(n-1)
#     return memo[n]
# r = fun(10)
# print(len(memo))

def integer_generator(limit):
    n=0
    while n < limit:
        n +=1
        yield n
res= integer_generator(8)
print(list(res), type(res))