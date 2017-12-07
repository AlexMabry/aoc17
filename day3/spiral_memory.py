import math
input = 289326

sqrt = int(math.ceil(math.sqrt(input)))
outer_layer = sqrt + 1 if sqrt % 2 == 0 else sqrt
inner_layer = outer_layer - 2
outer_distance_remaining = int(input - math.pow(inner_layer, 2))
manhattan_distance = outer_distance_remaining % (outer_layer - 1) # - (outer_layer-1)//2 + (outer_layer-1)//2

print(manhattan_distance)



