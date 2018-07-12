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

pointer = ((24, 24), (12, 12), *pointer)
