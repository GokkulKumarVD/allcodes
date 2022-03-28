# arrar

# 1. Let us say your expense for every month are listed below,
# 	1. January -  2200
#  	2. February - 2350
#     3. March - 2600
#     4. April - 2130
#     5. May - 2190
#
# Create a list to store these monthly expenses and using that find out,
#
# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

# exp = [2200,2350,2600,2130,2190]

# solution1
# exp = [2200,2350,2600,2130,2190]
# print(exp[1]-exp[0])

# solution2
# print(exp[1]+exp[2]+exp[3])

# solution3
# print(2000 in exp)

# solution4
# exp.append(1980)
# print(exp[5])

# solution5
# exp[3]  = exp[3]-200
# print(exp[3])


# --------------------------------------------------

# You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']
# Using this find out,
#
# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

# solution1
# print(len(heros))

# solution2
# heros.append("black panther")
# print(heros)

# solution3
# heros[1:3]=['doctor strange']
# print(heros)

# solution4
# heros.sort()
# print(heros)


# exp = [2340,2500,2100,3100,2980]
# total = 0
# for i in range(len(exp)):
#     print("month: ", (i+1) , "expense: " , exp[i])
#     total = total + i

# ------------------------------functons in python--------------------

# def calculate_area(base,height):
#     area = (1 / 2) * base * height
#     return area
#
# area_calc = calculate_area(10,20)
# print(area_calc)

# exercise 2
# def calculate_area(d1,d2,shape="triangle):
#     if shape == "triangle":
#         area = (1 / 2) * d1 * d2
#         print("triangle")
#     else:
#         area = d1 * d2
#         print("rectangle")
#     return area
#
# area_ = calculate_area(10,20,"rectangle")
# print(area_)


# exercise 3
#
# def pattern(n=5):
#     for i in range(n):
#         s = ''
#         for j in range(i+1):
#             s = s + "*"
#         print(s)
#
#
#
#
# star = pattern(4)


# -----------------------------------dictionary and tuple


# exercise1
#
# survey = {"China":143,"India":136,"USA":32,"Pakistan":21}
#
# question = input("What action would you like to perform: ")
#
# if question.lower() == "print":
#     for country,pop in survey.items():
#         print(f"{country} ==> {pop}")
#
# if question.lower() == "add":
#     country_ = input("Enter county name: ")
#     if country_ in survey:
#
#         print('Country already in database')
#
#     else:
#         add_pop = input("Enter population count: ")
#         survey[country_] = add_pop
#
# print(survey)


# exercise 3

stk = {"info":[600,630,620],"ril":[1430,1490,1567],"mtl":[234,180,160]}


def print_():
    for i in stk:
        print(f"{stk} ==> ")


def main():
    option = input("Would you like to add or print ")
    if option == "print":
        print_()
    elif option == "add":
        add_()


if __name__ == '__main__':
    main()














