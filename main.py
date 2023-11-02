
import random

#PHASE 1

obstacles = [(9, 7), (8, 7), (7, 7), (7, 8)]

def pathway(obst):
    # this function returns the pathway of the self-driving vehicle
    # the variable obst take the a list with the locations of the obstacles

    # Movement is the list that will be returned at the end of the function
    movement = [(0, 0)]

    # abscissa is the variable that will give the abscissa of the vehicle
    abscissa = 0

    # ordinate is the variable that will give the ordinate of the vehicle
    ordinate = 0

    # number_movement is the variable that gives the number of times the vehicle moved from a loction to another
    number_movement = 0

    # removed_obstacles is a list that gives the obstacles that stop the vehicle from reaching the final point. They need to be removed.
    removed_obstacles = []

    while (9, 9) not in movement:

        # next_positions are the different movements the vehicle can do from his place
        next_positions = [(abscissa + 1, ordinate + 1), (abscissa, ordinate + 1), (abscissa + 1, ordinate),
                          (abscissa - 1, ordinate + 1), (abscissa - 1, ordinate), (abscissa + 1, ordinate - 1),
                          (abscissa, ordinate - 1)]

        # possible_positions are the the locstions that are part of next_positions but have no obstacles on them
        possible_positions = []

        for i in next_positions:
            if i not in obst:
                possible_positions.append(i)
            if i in obst:
                removed_obstacles.append(i)
        movement.append(possible_positions[0])
        if abscissa == 8:
            abscissa = 8
        else:
            abscissa = movement[-1][0]
        if ordinate == 8:
            ordinate = 8
        else:
            ordinate = movement[-1][1]
        possible_positions.clear()
        number_movement += 1

        if number_movement > 1000:
            """This is because the diagonal movement (fastest movement) have the priority in this algorithm. 
            Any vehicle that need more than 1000 movements is then certainly stuck."""

            print("Unable to reach the delivery point")
            return "The obstacle(s) to be removed is(are) {} ".format(removed_obstacles)

        removed_obstacles.clear()

    return movement


print(pathway(obstacles))

#PHASE 2

list_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_obstacles = []


def obstacle_generator():
    # This function return a list of 20 new obstacles

    for i in range(0, 2):
        new_obstacles.append((random.choice(list_numbers), random.choice(list_numbers)))
    for i in [(0, 0), (9, 9), (9, 7), (8, 7), (7, 7), (7, 8)]:

        if i in new_obstacles:
            """This condition make sure that the initial and final point and the obstacles
            already existing are not part of the 20 new obstacles"""

            new_obstacles.remove(i)

        if new_obstacles.count(i) > 1:
            # This condition makes sure there is no repetition

            new_obstacles.remove(i)

    if len(new_obstacles) != 20:
        # This condition makes sure there is still 20 new obsatcles. Otherwise we do it again.

        obstacle_generator()

    return new_obstacles


a = obstacle_generator()
for i in obstacles:
    a.append(i)
print(a)

#PHASE 3

print(pathway([(9,7), (8,7), (7,7), (7,8), (7,9)]))

"""On top of that, the pathway function gives priority to diagonal movements which are the fastest ones. 
So all the results that are given are the fastest passway possible for the set of obstacles entered."""