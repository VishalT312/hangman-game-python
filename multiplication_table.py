
# write a program that print multiplication table between 11 to 20 

# def multiplication_table(num1,num2):
#     for i in range(num1,num2+1):
#         for j in range(1,11):
#             print(f"{i} X {j} = {i*j}")


# # num1,num2 = int(input("Enter two numbers between which you want the multiplication table: "))
# num1, num2 = map(int, input("Enter two numbers (start end): ").split())


# multiplication_table(num1,num2)


def multiplication_table(num1,num2):
    if num2 > num1:
        for i in range(num1,num2+1):
            for j in range(1,11):
                print(f"{i} X {j} = {i*j}")
    else:
        print("Invalid Numbers!! Try Again!!")
            


num1 = int(input("Enter start number for multplication table: "))
num2 = int(input("Enter end number for multplication table: "))

multiplication_table(num1,num2)


# 5 Rows and 5 Columns align with space

# def multiplication_table(num1, num2):
#     # Step through tables in chunks of 5 (5 columns per row of tables)
#     for start in range(num1, num2 + 1, 5):
#         end = min(start + 4, num2)  # make sure we don’t go past num2

#         # Print 10 rows for each set of 5 tables
#         for row in range(1, 11):
#             line = ""
#             for i in range(start, end + 1):  # print side by side
#                 line += f"{i} X {row} = {i*row:<6}".ljust(18)  # fixed width
#             print(line)
#         print()  # blank line after each 5-column block


# num1 = int(input("Enter start number for multiplication table: "))
# num2 = int(input("Enter end number for multiplication table: "))

# multiplication_table(num1, num2)
