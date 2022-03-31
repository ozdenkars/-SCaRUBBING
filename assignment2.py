print("""
<-----RULES----->
1. BRUSH DOWN
2. BRUSH UP
3. VEHICLE ROTATES RIGHT
4. VEHICLE ROTATES LEFT
5. MOVE UP TO X
6. JUMP
7. REVERSE DIRECTION
8. VIEW THE MATRIX
0. EXIT 
""")
loop = 0
while loop == 0:

    command = input("Please enter the commands with a plus sign (+) between them.")
    command = command.split("+")
    command = [str(x) for x in command]

    n = int(command[0])
    command.pop(0)

    row = [" " for x in range(n)]
    mat = [row for y in range(n)]
    row.insert(0,"+")
    row.append("+")

    list1 = []

    class Car:
        def __init__(self, x, y, direction, brush, matrix):
            self.x = x
            self.y = y
            self.direction = direction
            self.brush = brush
            self.matrix = matrix


    vec =Car(0,1,"right","up",mat)

    def paint(x,y):
        mat[x] = list(mat[x])
        list1 = mat[x]
        list1[y] = "*"

    for x in range(len(command)):
        if command[x] == "1":
            vec.brush = "down"
            paint(x=vec.x,y=vec.y)
        elif command[x] == "2":
            vec.brush = "up"
        elif command[x] == "3":
            if vec.direction == "right":
                vec.direction = "down"
            elif vec.direction == "left":
                vec.direction = "up"
            elif vec.direction == "down":
                vec.direction = "left"
            elif vec.direction == "up":
                vec.direction = "right"

        elif command[x] == "4":
            if vec.direction == "right":
                vec.direction = "up"
            elif vec.direction == "left":
                vec.direction = "down"
            elif vec.direction == "down":
                vec.direction = "right"
            elif vec.direction == "up":
                vec.direction = "left"

        elif command[x][0] == "5":
            if vec.brush == "down":
                m = command[x][2:]
                m = int(m)
                if vec.direction == "right" and (vec.y + m) <= len(row) - 2:
                    for i in range(m+1):
                        paint(x=vec.x, y=(vec.y + i))
                    vec.y = (vec.y) + m
                elif vec.direction == "down" and (vec.x + m) < len(mat):
                    for i in range(m + 1):
                        paint(x=(vec.x) + i, y=vec.y)
                    vec.x = (vec.x) + m
                elif vec.direction == "up" and m <= vec.x:
                    for i in range(m + 1):
                        paint(y=vec.y, x=(vec.x - i))
                    vec.x = (vec.x) - m
                elif vec.direction == "left" and m < vec.y:
                    for i in range(m + 1):
                        paint(x=vec.x, y=(vec.y - i))
                    vec.y = (vec.y) - m
                elif (vec.y + m) > len(row) - 2 and vec.direction == "right":
                    for i in range(vec.y, n + 1):
                        paint(x=vec.x, y=i)
                    for i in range(1, ((vec.y + m) % (len(row) - 2)) + 1):
                        paint(x=vec.x, y=i)
                    vec.y = (vec.y + m) % (len(row) - 2)
                elif (vec.x + m) >= len(mat) and vec.direction == "down":
                    for i in range(vec.x, n):
                        paint(x=i, y=vec.y)
                    for i in range(0, ((vec.x + m) % len(mat)) + 1):
                        paint(x=i, y=vec.y)
                    vec.x = (vec.x + m) % len(mat)
                elif m > vec.x and vec.direction == "up":
                    for i in range(0, vec.x + 1):
                        paint(x=i, y=vec.y)
                    for i in range(n - (m - vec.x), n):
                        paint(x=i, y=vec.y)
                    vec.x = n - (m - vec.x)
                elif m >= vec.y and vec.direction == "left":
                    for i in range(1, vec.y + 1):
                        paint(x=vec.x, y=i)
                    for i in range((n - (m - vec.y)), n + 1):
                        paint(x=vec.x, y=i)
                    vec.y = n - (m - vec.y)
            elif vec.brush == "up":
                m = command[x][2:]
                m = int(m)
                if vec.direction == "right" and (vec.y + m) <= len(row) - 2:
                    vec.y = vec.y + m
                elif vec.direction == "down" and (vec.x + m) < len(mat):
                    vec.x = vec.x + m
                elif vec.direction == "up" and m <= vec.x:
                     vec.x = vec.x - m
                elif vec.direction == "left" and m < vec.y:
                    vec.y = vec.y - m
                elif (vec.y + m) > len(row) - 2 and vec.direction == "right":
                    vec.y = (vec.y + m) % (len(row) - 2)
                elif (vec.x + m) >= len(mat) and vec.direction == "down":
                    vec.x = (vec.x + m) % len(mat)
                elif m > vec.x and vec.direction == "up":
                    vec.x = n - (m - vec.x)
                elif m >= vec.y and vec.direction == "left":
                    vec.y = n - (m - vec.y)
        elif command[x] == "6":
            vec.brush = "up"
            m = 3
            if vec.direction == "right" and (vec.y + m) <= len(row) - 2:
                vec.y = (vec.y) + m
            elif vec.direction == "down" and (vec.x + m) < len(mat):
                vec.x = (vec.x) + m
            elif vec.direction == "up" and m <= vec.x:
                vec.x = (vec.x) - m
            elif vec.direction == "left" and m < vec.y:
                vec.y = (vec.y) - m
            elif (vec.y + m) > len(row) - 2 and vec.direction == "right":
                vec.y = (vec.y + m) % (len(row) - 2)
            elif (vec.x + m) >= len(mat) and vec.direction == "down":
                vec.x = (vec.x + m) % len(mat)
            elif m > vec.x and vec.direction == "up":
                vec.x = n - (m - vec.x)
            elif m >= vec.y and vec.direction == "left":
                vec.y = n - (m - vec.y)
        elif command[x] == "7":
            if vec.direction == "right":
                vec.direction = "left"
            elif vec.direction == "left":
                vec.direction = "right"
            elif vec.direction == "down":
                vec.direction = "up"
            elif vec.direction == "up":
                vec.direction = "down"
        elif command[x] == "8":
            list_plus = ["+"] * (n + 2)
            print("".join(map(str, list_plus)))
            for row in mat:
                print("".join(map(str, row)))

            print("".join(map(str, list_plus)))
        elif command[x] == "0":
            loop = 1
            break
        else:
            del mat
            print("You entered an incorrect command. Please try again!")
            loop = 0
            break











