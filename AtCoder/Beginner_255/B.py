N, K = input().split(' ')
A = input().split(' ')

def get_distance(x, y, a_x, a_y):
    return ((x-a_x)**2 + (y-a_y)**2)**(1/2)

coords = [ (0,0) for _ in range(int(N)) ]

for index in range(int(N)):
    x, y = input().split(' ')
    coords[index] = (int(x), int(y))

max_r = 0
for a in A:
    a_coords = coords[int(a)-1]
    for coord in coords:
        max_r = max(max_r, get_distance(coord[0], coord[1], a_coords[0], a_coords[1]))

print(max_r)

