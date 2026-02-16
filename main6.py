def move_right():
    turn_right()
    move()
    
while not at_goal():
    if wall_in_front():
        if right_is_clear():
            move_right()
        elif wall_on_right():
            turn_left()
            if wall_in_front():
                turn_left()
                move()
            else:
                move()
    elif front_is_clear():
        if right_is_clear():
            move_right()
        elif wall_on_right():
            move()





while not at_goal():
    if wall_on_right():
        move()
    elif wall_in_front() and not wall_on_right():
        turn_right()
        move()
    elif wall_in_front() and wall_on_right():
        turn_left()
