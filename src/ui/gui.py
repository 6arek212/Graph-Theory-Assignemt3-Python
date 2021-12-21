import pygame
import os
from src.impl.GraphAlgo import GraphAlgo
from src.ui.Range import Range, WorldGraph, Range2D, Range2Range
from pygame.constants import RESIZABLE
from pygame import Color, display, gfxdraw
from types import SimpleNamespace


class UI:

    def __init__(self, graph: GraphAlgo):
        pygame.init()
        self.graph = graph
        self.worldGraph = WorldGraph()
        self.world2Frame = None
        self.WIDTH, self.HEIGHT = 900, 700
        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT), depth=32, flags=RESIZABLE)
        self.RED = (255, 0, 0)
        self.WHITE = (255, 255, 255)
        self.FONT = pygame.font.SysFont('Arial', 10, bold=True)
        self.FPS = 60


    def updateFrame(self):
        rx = Range(70, self.WIN.get_width() - 70)
        ry = Range(self.WIN.get_height() - 100, 150)
        frame = Range2D(rx, ry)
        self.world2Frame = self.worldGraph.w2f(self.graph.get_graph(), frame)

    def draw_Edge(self, src, dest):
        s = self.graph.get_graph().Nodes[src].pos
        d = self.graph.get_graph().Nodes[dest].pos
        s0 = self.world2Frame.worldToframe(s)
        d0 = self.world2Frame.worldToframe(d)

        pygame.draw.line(self.WIN, (0,0,255),
                         (s0[0], s0[1]), (d0[0], d0[1]))

    def draw_Node(self, node, r):
        pos = node.pos
        fp = self.world2Frame.worldToframe(pos)
        gfxdraw.filled_circle(self.WIN, int(fp[0]), int(fp[1]),
                              r, Color(64, 80, 174))
        gfxdraw.aacircle(self.WIN, int(fp[0]), int(fp[1]),
                         r, Color(255, 255, 255))

        id_srf = self.FONT.render(str(node.key), True, Color(255, 255, 255))
        rect = id_srf.get_rect(center=(fp[0], fp[1]))
        self.WIN.blit(id_srf, rect)

    def draw_graph(self):
        self.updateFrame()

        for e in self.graph.get_graph().Edges:
            self.draw_Edge(e[0], e[1])

        for n in self.graph.get_graph().get_all_v().values():
            self.draw_Node(n, 10)

        pygame.display.update()

    def draw_text(self , text ,font , color , surface , x ,y):
        txtobj = font.render(text , 1 , color)
        txtrect = txtobj.get_rect()
        txtrect.topleft= (x,y)
        surface.blit(txtobj , txtrect)

    def runGUI(self):
        run = True
        clock = pygame.time.Clock()
        # self.draw_text('main menu' , self.FONT, self.WHITE , self.WIN , 20,20)
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.draw_text('main menu', self.FONT, self.WHITE, self.WIN, 20, 20)
            self.draw_graph()
        clock.tick(self.FPS)
        pygame.quit()

# if __name__ == "__main__":
#     main()
