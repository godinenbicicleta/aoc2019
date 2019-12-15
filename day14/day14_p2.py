import math



from math import ceil

def parse_quantities(quant):
    num, name = quant.split(" ")
    return int(num), name

def parse_ingredients(ingredients):
    ingList = [parse_quantities(i.strip()) for i in ingredients.split(",")]
    return ingList

def process_data(text):
    data = text.strip().split("\n")
    data = [[parse_ingredients(d.split(" => ")[0]),
            parse_quantities(d.split(" => ")[1])] for d in data]
    return data

def is_primitive(LABEL):
    for ingredients, result in data:
        quantity, res = result
        if res == LABEL and len(ingredients) == 1 and ingredients[0][1] == "ORE":
            return ingredients[0][0]
    return False




with open("input.txt", "r") as f:
    data = process_data(f.read())

data = process_data("""
15 RNMTG => 6 QSXV
21 MKJN => 9 KDFZ
1 KVFL, 4 NZWL => 3 FHDT
1 FZJXD, 2 SWZK, 1 QRLRS => 6 ZRNK
8 KVFL => 6 SBZKF
11 DXFB, 1 CPBXJ, 8 TXFCS, 1 ZPMHL, 1 BCHTD, 2 FZJXD, 2 WKZMQ, 1 NZWL => 8 MPLJ
5 KDFZ, 1 QSXV => 9 TXFCS
1 PMLGM, 21 CKVN => 3 KVFL
1 XFRLH, 3 QRLRS => 4 CKVN
5 KBJS, 15 XFRLH, 6 WZPZX, 15 KVFL, 4 DXFB, 4 ZPMHL, 11 JCKCK, 26 KFGPB => 9 BWVS
10 KNRDW, 2 XCML => 9 BCNL
26 LBLH => 9 KBJS
5 DTFBQ, 4 PJTD => 6 FHKSW
6 HTRFP, 1 FVXV, 4 JKLNF, 1 TXFCS, 2 PXBP => 4 JRBFT
21 DTFBQ => 9 JGQJ
2 KBJS => 3 FZJXD
24 LBLH => 6 QFMTZ
1 CBNJT => 7 LSCW
5 KVFL => 2 NZWL
12 DNHL, 4 BCNL => 4 LBLH
15 RHVG => 1 PJCWT
4 KDFZ, 1 KVFL => 3 BCHTD
2 XFDW, 7 BCHTD => 7 WKZMQ
2 SBZKF, 1 PLTX => 3 DXFB
1 PLTX, 11 HTRFP, 6 PMLGM => 1 JCKCK
1 TQCX, 10 DNHL => 8 DTFBQ
2 TQCX, 2 KTBFB => 5 RHVG
8 MVFW => 3 CPBXJ
148 ORE => 4 CBNJT
9 CPBXJ, 5 DTFBQ => 6 PMLGM
11 ZXCF, 15 PJCWT, 4 FZJXD => 7 PJTD
1 JGQJ => 6 DCBNV
4 LSCW, 16 BCNL => 7 MVFW
1 RHVG => 4 XFDW
8 MPLJ, 16 JRBFT, 43 KBJS, 11 NZWL, 4 BWVS, 22 ZPMHL => 1 FUEL
1 QFMTZ, 3 CKVN => 5 PLTX
5 CKVN, 10 SWZK => 7 HTRFP
2 PXBP, 1 QRLRS, 7 KTBFB => 7 NDZGV
1 QRLRS, 9 KBJS, 2 TQCX => 2 SWZK
9 TZKZ, 3 ZRNK, 4 PXBP => 4 FVXV
1 PMLGM, 1 SWZK, 6 FZJXD => 7 MKJN
16 MVFW, 2 KBJS => 7 ZXCF
1 MVFW => 6 HVGF
1 LSCW, 1 HVGF => 8 RNMTG
5 ZRNK, 1 TQCX => 3 PXBP
130 ORE => 5 KNRDW
1 RHVG, 2 KFGPB, 1 LSCW => 7 QRLRS
6 XFRLH => 8 TZKZ
24 HVGF, 8 KTBFB => 1 XFRLH
2 KNRDW, 2 CBNJT => 6 DNHL
1 FHDT => 4 JKLNF
1 QSXV, 10 XFGZX, 2 DCBNV => 8 ZPMHL
1 FHDT, 7 NDZGV => 4 WZPZX
11 FHKSW => 5 XFGZX
10 LSCW => 8 KTBFB
133 ORE => 1 XCML
8 XCML => 4 TQCX
6 CPBXJ, 8 CBNJT => 6 KFGPB
""")

#data = process_data(
#"""
#171 ORE => 8 CNZTR
#7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL
#114 ORE => 4 BHXH
#14 VRPVC => 6 BMBT
#6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL
#6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT
#15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW
#13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW
#5 BMBT => 4 WPTQ
#189 ORE => 9 KTJDG
#1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP
#12 VRPVC, 27 CNZTR => 2 XDBXC
#15 KTJDG, 12 BHXH => 5 XCVML
#3 BHXH, 2 VRPVC => 7 MZWV
#121 ORE => 7 VRPVC
#7 XCVML => 6 RJRHP
#5 BHXH, 4 VRPVC => 5 LTCX
#"""        )


def reduce_iter(to_it):
    new_list = [list(to_it.pop())]
    while to_it:
        num, label = to_it.pop()
        if label in [l for _,l in new_list]:
            for elem in new_list:
                if elem[1] == label:
                    elem[0] += num
        else:
            new_list = [[num, label]]+new_list

    return [tuple(k) for k in new_list]

print("data = ")
print(data)
print("================================")

"""
[(8, 'MPLJ'), (16, 'JRBFT'), (43, 'KBJS'), (11, 'NZWL'), (4, 'BWVS'), (22,'ZPMHL')]
(1, 'FUEL')

148 ORE => CBNJT
"""
def get_dependencies(label):
    if is_primitive(label):
        return set()
    for ingredients, result in data.copy():
        quantity, res = result
        if res == label:
            return set([x[1] for x in ingredients])
    return set()

def get_all_dependencies(label):
    dependencies = get_dependencies(label)
    to_check = dependencies.copy()
    while to_check:
        to_add = to_check.pop()
        for dep in get_dependencies(to_add):
            dependencies.add(dep)
            to_check.add(dep)
    return dependencies


def sort_required(lista):
    new_list = []
    for num, label in lista[:]:
        new_list.append((num, label, get_all_dependencies(label)))

    new_list2 = []
    for num, label, dependencies in new_list[:]:
        num_shared = 0
        for num_, label2, dependencies_ in new_list[:]:
            if label != label2 and label2 in dependencies:
                num_shared += 1
        if is_primitive(label):
            num_shared  = 0
        new_list2.append((num, label, num_shared))
    new_list2.sort(key = lambda x: x[2])
    return [(a,b) for a,b,c in new_list2]


sobrantes = {}
def get_required_for(num, LABEL):
    for ingredients, result in data.copy():
        quantity, res = result
        if res == LABEL:
            initial_quantities =  ingredients
            break
    ing = initial_quantities.copy()
    # [(1, "ABC), (2, "CDE"), ...]
    multiple = int(ceil(num/quantity))
    required = [(multiple * val, label) for (val, label) in ing]
    return sort_required(required)





primitives = {x[1]:{"needed":is_primitive(x[1]), "produced":x[0]} for k,x in data if is_primitive(x[1])}


def get_all_required(num, LABEL):
    primitive_sum = {prim:0 for prim in primitives}
    to_iterate = get_required_for(num, LABEL)
    # [[16, 'MPLJ'], [32, 'JRBFT'], [86, 'KBJS'], [22, 'NZWL'], [8, 'BWVS']]
    while len(to_iterate)>0:
        new_num,next_to_get = to_iterate.pop()
        if next_to_get in primitive_sum:
            primitive_sum[next_to_get] += new_num
            continue
        to_iterate = sort_required(get_required_for(new_num, next_to_get) + to_iterate.copy())
        to_iterate = sort_required(reduce_iter(to_iterate.copy()))

    return primitive_sum
{'CBNJT': {'needed': 148, 'produced': 4}, 'KNRDW': {'needed': 130, 'produced': 5}}
('CBNJT', 4484), ('KNRDW', 12756), ('XCML', 4074)


def get_ore(primitive_items):
    ORE = 0
    for label, needed in primitive_items:
        q, l = get_required_for(needed, label)[0]
        print("label: ", label, "q: ", q,"needed: ",  needed)
        ORE += q

    return ORE

def get_ore_prim(primitive_items):
    ORE = 0
    excess = 0
    for label, num_needed in primitive_items:
        techo = int(math.ceil(num_needed/primitives[label]["produced"])*primitives[label]["needed"])
        actual = int(num_needed/primitives[label]["produced"]*primitives[label]["needed"])
        ORE += techo
        excess += techo-actual

    return ORE, excess


print(get_required_for(1,"FUEL"))
print(primitives)

print("ex1 sol")
ps = get_all_required(1,"FUEL")
print(ps)
print(get_ore(ps.items()))
print(get_ore_prim(ps.items()))
f = 1
while True:
    ps = get_all_required(f,"FUEL")
    ore, excess = get_ore_prim(ps.items())
    if excess == 0:
        print(f)
        break
    else:
        f += 1

print("ex1 sol")
ps = get_all_required(16,"FUEL")
print(ps)
print(get_ore(ps.items()))
print(get_ore_prim(ps.items()))

"""
start with   1000000000000/required_for_16*16
then brute force
"""

print("ex1 sol")
i=0
while True:
    f = 1572309+i
    ps = get_all_required(f,"FUEL")
    print(ps)
    ore = get_ore(ps.items())
    print("fuel: ",f,"ore: ",ore)
    i+=1
    if ore>1000000000000:
        break
