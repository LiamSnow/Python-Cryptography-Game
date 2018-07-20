import pygame as pg

pointer = pg.cursors.compile((
  "                        ",
  "        xx              ",
  "       x..x             ",
  "       x..x             ",
  "       x..x             ",
  "       x..x             ",
  "       x..xxx           ",
  "       x..x..xxx        ",
  "       x..x..x..xx      ",
  "       x..x..x..x.x     ",
  "   xxx x..x..x..x..x    ",
  "   x..xx........x..x    ",
  "   x...x...........x    ",
  "    x..............x    ",
  "     x.............x    ",
  "     x.............x    ",
  "      x............x    ",
  "      x...........x     ",
  "       x..........x     ",
  "       x..........x     ",
  "        x........x      ",
  "        x........x      ",
  "        xxxxxxxxxx      ",
  "                        "), black='x', white='.', xor='o')

# (size_x, size_y,), (center_x, center_y)
pointer = ((24, 24), (12, 12), *pointer)

textmarker = pg.cursors.compile(pg.cursors.textmarker_strings)
textmarker = ((8, 16), (4, 8), *textmarker)