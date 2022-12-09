
trees = []

def check_direction(my_pos_x,my_pos_y,direction): # <-0 , /\ 1, -> 2, \/ 3
    dir_score = 0
    if direction == 0:
        for i in range (my_pos_y -1 , -1, -1):
            #print (f"my tree {trees[my_pos_x][my_pos_y]} target tree {trees[my_pos_x][i]}")
            if trees[my_pos_x][i] >= trees[my_pos_x][my_pos_y]:
                if i != 0 and i != len(trees):
                    dir_score += 1
                break
            else:
                dir_score += 1
    elif direction == 1:
        for i in range (my_pos_x - 1, -1, -1):
            #print (f"my tree {trees[my_pos_x][my_pos_y]} target tree {trees[i][my_pos_y]}")
            if trees[i][my_pos_y] >= trees[my_pos_x][my_pos_y]:
                if i != 0 and i != len(trees):
                    dir_score += 1
                break
            else:
                dir_score += 1
    elif direction == 2:
        for i in range (my_pos_y + 1, len(trees[0])):
            #print (f"my tree {trees[my_pos_x][my_pos_y]} target tree {trees[my_pos_x][i]}")
            if trees[my_pos_x][i] >= trees[my_pos_x][my_pos_y]:
                if i != 0 and i != len(trees):
                    dir_score += 1
                break
            else:
                dir_score += 1
    elif direction == 3:
        for i in range (my_pos_x + 1, len(trees)):
            #print (f"my tree {trees[my_pos_x][my_pos_y]} target tree {trees[i][my_pos_y]}")
            if trees[i][my_pos_y] >= trees[my_pos_x][my_pos_y]:
                if i != 0 and i != len(trees):
                    dir_score += 1
                break
            else:
                dir_score += 1
    return dir_score
    


def check_visability (x, y):
    return check_direction(x, y, 0) * check_direction(x, y, 1) * check_direction(x, y, 2) * check_direction(x, y, 3) 


with open("data.txt", "r") as file:

    for line in file:
        tree_line = []
        for num in line.strip():
            tree_line.append(int(num))
        trees.append(tree_line)
        print(tree_line)
        
    #print(trees)
    output = 0
    for x in range(len(trees)):
        for y in range(len(trees[0])):
            print(f"{x} {y} {check_visability(x,y)}")
            if check_visability(x,y) > output:
                output = check_visability(x,y)
    print (output)