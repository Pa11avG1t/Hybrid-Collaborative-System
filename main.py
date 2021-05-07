########################################## Recommendation System #####################################################

print("Are you new user")
new = input("Type y for yes , n for no: ")
print("Hi User ,Please type your name:\n")
name = input()
fru = open('user', 'r')
if new == 'y':
    for u in fru.readlines():
        if name == u[:-1]:
            print("Username Already Taken")
            name = input("Please type new username: ")
            break

fru.close()
fu = open("user", "a")
fu.write(name+'\n')
fu.close()
print(name)
f = open(name, "a")


print("Welcome to our mart ,What you want to buy from the choices below\n")

database = {0: 'Sofa', 1: 'Chair', 2: 'TV', 3: 'Fridge', 4: 'Table', 5: 'Oven', 6: 'Induction Cooker', 7: 'RO',
            8: 'Mirror', 9: 'Bread' , 10: 'Cricket Bat', 11: 'Tennis Bar' , 12: 'Hockey' , 13: 'Football' , 14: 'Basketball',
            15: 'Stool', 16: 'CFL', 17: 'LED Light', 18: 'Allout', 19: 'Electric Tandoor', 20: 'Smartphone', 21: 'Speaker',
            22: 'Ceiling Fan', 23: 'Toy Gun', 24: 'Baby Soap', 25: 'Soap', 26: 'Shampoo', 27: 'Loofah', 28: 'Electric Cell',
            29: 'Trimmer', 30: 'Shaving Cream', 31: 'Razor', 32: 'Shoes', 33: 'Wrist Watch', 34: 'Mattress', 35: 'Pillow',
            36: 'Bedsheet', 37: 'Cricket ball', 38: 'Cricket Pad', 39: 'Gloves', 40: 'Tennis Ball', 41: 'Hair Oil',
            42: 'Face Cream', 43: 'Body Lotion', 44: 'Pen', 45: 'Notebook', 46: 'Printer', 47: 'A4 Pages', 48:'Printer Ink',
            49: 'Computer'}

print(database)
print("Type your choice\n")
choices = list(map(int, input().split(',')))

for i in choices:
    f.write(database[i]+'\n')

f.close()

price = [100000, 5000, 50000, 50000, 40000, 20000, 2000, 25000, 1500, 30, 1000, 1000, 1100, 550, 600, 510, 350, 600, 150, 10000,
        20000, 8000, 5000, 1000, 100, 80, 300, 200, 40, 1000, 100, 250, 6000, 6000, 20000, 10000, 2000, 60, 700, 500, 100,
        100, 200, 300, 10, 50, 5000, 100, 500, 50000]


print("Your item costs :\n")

for i in choices:
    print(price[i])

print("Items recently bought by you :\n")
f = open(name, "r")
a = set(f.readlines())

count=0
for i in a:
    print(i[:-1])
    count +=1
    if count == 5:
        break

mat = []

pur = [0 for i in range(len(database.keys()))]

for i in choices:
    pur[i] = 1

mat.append(pur)

m = open('matrix', 'r')

if m:
    a = m.readlines()
    for i in a:
        if len(i) > 1:
            mat.append(list(map(int, i.split(','))))
m.close()

m = open('matrix', 'w')
for i in mat:
    m.write(','.join([str(elem) for elem in i]))
    m.write('\n')
m.close()

reco = {}
Vec_A = {}
Vec_B = {}

for i in range(len(price)):
    a = []
    for j in mat:
        a.append(j[i])
    if i in choices:
        Vec_A.update({i: a})
    else:
        Vec_B.update({i: a})

for vec_a in Vec_A.values():

    for j, vec_b in Vec_B.items():

        dot = sum(a * b for a, b in zip(vec_a, vec_b))
        norm_a = sum(a * a for a in vec_a) ** 0.5
        norm_b = sum(b * b for b in vec_b) ** 0.5

        # Cosine similarity
        if norm_a == 0 or norm_b == 0:
            cos_sim = 0
        else:
            cos_sim = dot / (norm_a * norm_b)

        if j in reco.keys():
            reco[j] += cos_sim
        else:
            reco.update({j: cos_sim})

#print(mat)
#print(reco)
print('\nRecommendations:')
count=0
for i in sorted(reco.items(), key=lambda kv: (kv[1], kv[0]))[::-1]:
    if i[1] > 0:
        print(database[i[0]])
    count+=1
    if count==5:
        break