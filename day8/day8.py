with open("input.txt", "r") as f:
    datos = [int(i) for i in f.read().strip()]

#25 pixels wide and 6 pixels tall
width = 25
height = 6
num_layers = int(len(datos)/width/height)

layer_size = width*height
layers = {}

for ix,(start, end) in enumerate(zip(
        [i*layer_size for i in range(num_layers)],
        [(i+1)*layer_size for i in range(num_layers)],
        )):
    layers[ix] = datos[start:end]

num_zeros = [(key,value.count(0)) for key,value in layers.items()]

min_layer = layers[sorted(num_zeros, key = lambda x: x[1])[0][0]]

print(min_layer.count(1)*min_layer.count(2))


print(layers)
final_layer = [2 for _ in range(layer_size)]
for layer, nums in layers.items():
    for ix,num in enumerate(nums):
        if final_layer[ix] == 2:
            final_layer[ix] = num


for ix,num in enumerate(final_layer):
    if ix > 0 and ix%25 == 0:
        print("")
    if num  == 0:
        print(" ", end = '')
    else:
        print("X", end = '')
print("")
