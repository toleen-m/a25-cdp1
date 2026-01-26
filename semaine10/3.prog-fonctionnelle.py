from functools import reduce

# reduce permet de réduire une séquence otérable en une valeur unique 
print("---------------- REDUCE ")
panier = [
    {
        "name": "Oignon",
        "price": 5, 
        "quantity": 1
    }, 
    {
        "name": "Pomme",
        "price": 1.48, 
        "quantity": 10     
    }, 
    {
        "name": "Poulet",
        "price": 19, 
        "quantity": 2     
    }, 
    {
        "name": "Celeri",
        "price": 3, 
        "quantity": 2     
    }
]

# def fn(treduce, item): 
#     return treduce + item["price"] * item["quantity"]

# total = reduce(fn, panier, 0)

# print(total)

# 5 
# 19.8
# 57.8
# 63.8 

# total = 0 
# for item in panier: 
#     total += + item["price"] * item["quantity"]

# print(total)

def fn(acc, item):
    acc["total_price"] += item["price"] * item["quantity"]
    acc["total_quantity"] += item["quantity"]
    return acc


total = reduce(fn, panier, {"total_price": 0, "total_quantity": 0})
print(total)

# ------ fonctions lambda
# lambda param1, param2... : expression 
print("---------------- LAMBDA ")

a = [1, 2, 3]
b = map(lambda x: x*2, a)
print(list(b))


total = reduce(lambda treduce, item: treduce + item["price"] * item["quantity"], panier, 0)

# ------ exercice 
# Trouvez les nombres paires d'une liste, en écrivant qu'une seule ligne. 

la_liste = [1, 25, 45, 74, 8, 102, 56]
print(list(filter(lambda x: x%2==0, la_liste)))

# def multiply_by(factor):
#     def multiply(item):
#         return item * factor
#     return multiply

def multiply_by(factor):
    return lambda item: factor*item

double = multiply_by(2)
print(double(124))