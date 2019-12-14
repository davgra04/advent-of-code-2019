import sys,os
import curses
from pprint import pprint
from computer import Computer
import time


class game:

    def __init__(self):

        # read program from file
        ########################################
        input_file = "input.txt"

        with open(input_file, "r") as ifh:
            lines = [l.rstrip() for l in ifh.readlines()]

        ops = [int(x) for x in lines[0].rstrip().split(",")]

        self.screen = []

        for i in range(25):
            self.screen.append(["." for j in range(50)])

        self.last_ball_pos_x = -1
        self.last_ball_pos_y = -1
        self.ball_pos_x = -1
        self.ball_pos_y = -1
        self.paddle_pos = -1
        self.ball_motion_x = 1
        self.ball_motion_y = 1
        self.paddle_status = "init"
        self.score = 0


        # set up computer and run
        ########################################

        self.comp = Computer(pause_on_output=True)
        self.comp.load_program(ops)

        # set free play
        self.comp.memory[0] = 2


    def set_input(self):
        


        # last_ball_pos_x = ball_pos_x

        # # find horizontal position of ball and paddle
        # for row_idx, row in enumerate(self.screen):
        #     for pos, tile in enumerate(row):
        #         if tile == "o":



        # print("ball_pos_x:", self.ball_pos_x)
        # print("paddle_pos:", self.paddle_pos)


        # ball_going_left = True
        # if last_ball_pos_x > ball_pos_x:
        #     ball_going_left = False


        if self.ball_motion_x == 1:
            target = self.ball_pos_x #+ 1
        else:
            target = self.ball_pos_x #- 1


        if self.paddle_pos < target:
            self.comp.inputs = [1, 1, 1]
            self.paddle_status = "moving right"
        elif self.paddle_pos > target:
            self.comp.inputs = [-1, -1, -1]
            self.paddle_status = "moving left"
        else:
            self.comp.inputs = [0, 0, 0]
            self.paddle_status = "doing nothing"











    # def draw_screen(self):
    #     # for row in self.screen:
    #     #     print("".join(row))





def draw_menu(stdscr):






    frame = 0


    g = game()




    left_collision = False
    right_collision = False


    max_drawn_x = 0
    max_drawn_y = 0


    k = 0
    cursor_x = 0
    cursor_y = 0

    # Clear and refresh the self.screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Loop where k is the last character pressed
    while (k != ord('q')):

        # Initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        # if k == curses.KEY_RIGHT:
        #     cursor_x = cursor_x + 1
        # elif k == curses.KEY_LEFT:
        #     cursor_x = cursor_x - 1



        stdscr.addstr(height-3, 0, "frame: {}".format(frame))


        # stdscr.addstr(height-17, 0, "left_collision: {}".format(left_collision))
        # stdscr.addstr(height-16, 0, "right_collision: {}".format(right_collision))

        stdscr.addstr(height-14, 0, "last_ball_pos_y: {}".format(g.last_ball_pos_y))
        stdscr.addstr(height-13, 0, "ball_pos_y: {}".format(g.ball_pos_y))
        # stdscr.addstr(height-12, 0, "ball_motion_y: {}".format(g.ball_motion_y))

        stdscr.addstr(height-10, 0, "last_ball_pos_x: {}".format(g.last_ball_pos_x))
        stdscr.addstr(height-9, 0, "ball_pos_x: {}".format(g.ball_pos_x))
        # stdscr.addstr(height-8, 0, "ball_motion_x: {}".format(g.ball_motion_x))

        stdscr.addstr(height-6, 0, "paddle_pos: {}".format(g.paddle_pos))
        stdscr.addstr(height-5, 0, "paddle_status: {}".format(g.paddle_status))





        # run intcode program

        # resume program twice to obtain 3 outputs
        g.set_input()
        g.comp.resume_program()
        # draw_screen()
        g.set_input()
        g.comp.resume_program()
        # draw_screen()
        g.set_input()
        g.comp.resume_program()
        outputs = g.comp.get_outputs()
        # print("outputs:", outputs)

        # for row_idx, row in enumerate(g.screen):
        #     stdscr.addstr(row_idx, 0, "".join(row))





        # i = ""

        # while i != "":
        #     i = input("give input:")
        #     print("input:", i)
        #     if i == "a":
        #         comp.inputs = [-1]
        #     elif i == "s":
        #         comp.inputs = [0]
        #     elif i == "d":
        #         comp.inputs = [1]


        if g.comp.halted:
            break

        # draw
        x = outputs[0]
        y = outputs[1]
        tile = outputs[2]

        # if x > max_drawn_x:
        #     max_drawn_x = x
        # if y > max_drawn_y:
        #     max_drawn_y = y

        if x == -1 and y == 0:
            # input()
            # continue
            g.score = tile
        stdscr.addstr(height-1, 0, "score: {}".format(g.score))

        if tile == 0:
            g.screen[y][x] = "."
            # pass
        elif tile == 1:
            g.screen[y][x] = "W"
        elif tile == 2:
            g.screen[y][x] = "B"
        elif tile == 3:
            g.screen[y][x] = "="
            g.paddle_pos = x
        elif tile == 4:
            g.screen[y][x] = "o"

            g.last_ball_pos_x = g.ball_pos_x
            g.ball_pos_x = x

            g.last_ball_pos_y = g.ball_pos_y
            g.ball_pos_y = y

            # g.ball_pos_x = pos

            # left_collision = g.screen[y][x-1] == "B" or (g.screen[y-g.ball_motion_y][x-1] == "B" and g.screen[y-g.ball_motion_y][x] != "B")
            # right_collision = g.screen[y][x+1] == "B" or (g.screen[y-g.ball_motion_y][x+1] == "B" and g.screen[y-g.ball_motion_y][x] != "B")

            # left_collision = g.screen[row_idx][pos-1] == "B" or g.screen[row_idx + 1][pos-1] or g.screen[row_idx - 1][pos-1]
            # right_collision = g.screen[row_idx][pos+1] == "B" or g.screen[row_idx + 1][pos+1] == "B" or g.screen[row_idx - 1][pos+1] == "B"

            # adjust ball motion


            # if g.ball_pos_y > g.last_ball_pos_y:
            #     g.ball_motion_y = -1
            # elif g.ball_pos_y < g.last_ball_pos_y:
            #     g.ball_motion_y = 1



            # if g.ball_pos_x > g.last_ball_pos_x or left_collision:
            #     g.ball_motion_x = 1
            # elif g.ball_pos_x < g.last_ball_pos_x or right_collision:
            #     g.ball_motion_x = -1

            # if g.ball_pos_x == 1:
            #     g.ball_motion_x = 1
            # elif g.ball_pos_x == 41:
            #     g.ball_motion_x = -1


            # else:
            #     g.ball_motion_x = 0


            for row_idx, row in enumerate(g.screen):
                stdscr.addstr(row_idx, 0, "".join(row))
            stdscr.refresh()





        # draw_screen()
        # print()



        # draw screen

        # for row_idx, row in enumerate(self.screen):
        #     stdscr.addstr(row_idx, 0, "".join(row))




        # # Declaration of strings
        # title = "Curses example"[:width-1]
        # subtitle = "Written by Clay McLeod"[:width-1]
        # keystr = "Last key pressed: {}".format(k)[:width-1]
        # statusbarstr = "Press 'q' to exit | STATUS BAR | Pos: {}, {}".format(cursor_x, cursor_y)
        # if k == 0:
        #     keystr = "No key press detected..."[:width-1]

        # # Centering calculations
        # start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
        # start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
        # start_x_keystr = int((width // 2) - (len(keystr) // 2) - len(keystr) % 2)
        # start_y = int((height // 2) - 2)

        # # Rendering some text
        # whstr = "Width: {}, Height: {}".format(width, height)
        # stdscr.addstr(0, 0, whstr, curses.color_pair(1))

        # # Render status bar
        # stdscr.attron(curses.color_pair(3))
        # stdscr.addstr(height-1, 0, statusbarstr)
        # stdscr.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
        # stdscr.attroff(curses.color_pair(3))

        # # Turning on attributes for title
        # stdscr.attron(curses.color_pair(2))
        # stdscr.attron(curses.A_BOLD)

        # # Rendering title
        # stdscr.addstr(start_y, start_x_title, title)

        # # Turning off attributes for title
        # stdscr.attroff(curses.color_pair(2))
        # stdscr.attroff(curses.A_BOLD)

        # # Print rest of text
        # stdscr.addstr(start_y + 1, start_x_subtitle, subtitle)
        # stdscr.addstr(start_y + 3, (width // 2) - 2, '-' * 4)
        # stdscr.addstr(start_y + 5, start_x_keystr, keystr)
        # stdscr.move(cursor_y, cursor_x)

        # Refresh the screen
        # stdscr.refresh()

        # Wait for next input

        frame += 1

        # time.sleep(1)

        if frame < 1000000:
            continue


        

        k = stdscr.getch()

    print("score:", g.score)
    input()


def main():
    curses.wrapper(draw_menu)

if __name__ == "__main__":
    main()