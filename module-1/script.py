# ----------------------------------------------------
# 1 - Variables and Memory
# ----------------------------------------------------
# price = 1000
# print(price)



# ----------------------------------------------------
# 2 - Primitive Data Structures
# ----------------------------------------------------
# (2.1) Lists
# - Mutable
# - Index-Based

# List Methods
# https://www.w3schools.com/python/python_ref_list.asp
# .append()
# .insert()
# .pop()
# .remove()


## ------- Example 1 -------
# prices = [
#     100,            # 0
#     200,            # 1
#     450,            # 2
#     650             # 3
# ]


## ------- Example 2 -------
# products = [
#     ["Apple","iPhone 13",500],
#     ["Apple","iPhone 12",400],
#     ["Samsung","S20",450]
# ]

# products[2][2]




# (2.2) Tuples
# - Immutable
# - Index Based

## ------- Example 1 -------
# days_of_week = ("Mon","Tue","Wed","Thu","Fri","Sat","Sun")
# days_of_week[6]

## ------- Example 2 -------
# airports2 = (
#     ["dxb", "jfk", "yyz"],
#     ["Dubai International", "John F Kennedy", "Toronto Pearson International Airport"]
# )




# (2.3). Sets
# - Mutable
# - Keyless
# - Unique

## ------- Example 2 -------
# brands = { "Apple","Samsung","Nokia" }


# 4. Dictionaries
# - Mutable
# - Keys must be defined


## ------- Example 1 -------
# airports = {
#     "dxb": "Dubai International",
#     "jfk": "John F Kennedy",
#     "yyz": "Toronto Pearson International Airport"
# }

## ------- Example 2 -------
# airports3 = {
#     "Dubai": "Dubai International",
#     "New York": "John F Kennedy",
#     "Toronto": "Toronto Pearson International Airport"
# }


# airports["yyz"]           # Bracket syntax


# airports3["New York"]     # Dot syntax


# ----------------------------------------------------
# 3 - Functions
# ----------------------------------------------------
# def some_func():
#     price = 100
#     print(price)
#     numA = 10
#     numB = 20
#     the_sum = numA + numB
    
# def add_numbers(numA, numB):
#     result = numA + numB
#     return result

# add_numbers(500, 2000)



# ----------------------------------------------------
# 4 - Classes
# ----------------------------------------------------
# class Car:
    
#     # Properties (variables in a class)
#     speed = None
#     color = None
#     brand = None
    
    
#     # Methods (functions in a class)
#     def __init__(self, brand_param, color_param, price_param):
#         self.color = color_param
#         self.brand = brand_param
#         return
     
#     def accelerate(self, speed):
#         # ----
#         # ----
#         # ----
#         return
        
#     def brake(self):
#         self.accelerate(0)
#         # ----
#         # ----
#         return
        
#     def reverse(self):
#         # ----
#         # ----
#         # ----
#         return
    
  
  
  
# Instantiating classes
# model_s = Car("Tesla", "black", 300000)
# model_s.accelerate()

# civic = Car("Honda", "red", 60000)


# model_s = {
#     "accelerate": #----,
#     "brake": #-----,
#     "price": 300000,
#     "color": "black"
# }

# model_s["accelerate"]

# model_s.accelerate()



# ----------------------------------------------------
# 5 - Binary Trees
# ----------------------------------------------------
# (5.1) Binary Tree with Dictionary
# binary_tree = {
#         "node": 1,
#         "left_child": {
#                 "node": 2,
#                 "left_child": {
#                         "node": 5,
#                         "left_child": "None",
#                         "right_child": "None",
#                     },
#                 "right_child": {
#                         "node": 6,
#                         "left_child": "None",
#                         "right_child": "None",
#                     }
#             },
#         "right_child": {
#                 "node": 3,
#                 "left_child": "None",
#                 "right_child": "None"
#             },
# }

# print(binary_tree["left_child"]["right_child"]["node"])