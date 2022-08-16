def main(a,b,c):
    """
    Find how many positive numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of positive numbers in the given numbers
    """
    m=0
    if a>0:
        m+=1
    if b>0:
        m+=1
    if c>0:
        m+=1
    return m









#     if a > 0:
#         if b > 0:
#             if c > 0:
#                 x = 3
#             else: #c < 0
#                 x = 2
#         if b < 0:
#             if c > 0:
#                 x = 2
#             else: #c < 0
#                 x = 1
#     elif a < 0:
#         if b > 0:
#             if c > 0:
#                 x = 2
#             else: # c < 0
#                 x = 1
#         if b < 0:
#             if c > 0:
#                 x = 1
#             else: #c<0
#                 x=0
#     return x
# y = main(12, 56, -9)
# print(y)