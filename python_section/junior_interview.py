#########1
from collections import UserString

# def reverse_str(s):
#     s = str(s)
#     re_st = s[::-1]
#     return re_st
#
#
# print(reverse_str(int(300001)))


############2

# def int_binary(n):
#     bin_code = bin(n)[2:]
#     revers_bin = bin_code[::-1]
#     int_code = int(revers_bin, 2)
#     print(int_code)
#     return int_code
#
# print(int_binary(13))


###############SQL 1
# SELECT *
# FROM USERS
# WHERE AGE>18
#
#
# #################SQL 2
# SELECT P.ID, P.NAME AS PRODUCT_NAME, PR_NAME AS COMPANY_NAME
# FROM PRODUCTS P
# INNER JOIN PRODUCTS PR ON P.PRODUCER_ID = PR.ID
#
# #############SQL 3
# SELECT P.ID, P.NAME AS PRODUCT_NAME, PR_NAME AS COMPANY_NAME
# FROM PRODUCTS P
# LEFT JOIN PRODUCTS PR ON P.PRODUCER_ID = PR.ID


#################SQL 4
# DELETE FROM PRODUCTS
# USING PRODUCTS P
# LEFT JOIN PRODUCERS PR ON P.PRODUCER_ID = PR.ID
# WHERE PR.ID IS NULL


print("".join(reversed("12344567")))



