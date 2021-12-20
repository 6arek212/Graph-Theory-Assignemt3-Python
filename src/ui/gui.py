import pygame
from pygame import time, display, Color, QUIT
from src.impl.graoh_algo import GraphAlgo

pygame.init()
clock = time.Clock()

WIDTH, HEIGHT = 900, 600
REFRESH_RATE = 60
RADIUS = 20
PADDING = 50

screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=pygame.constants.RESIZABLE)
pygame.display.set_caption('Graph Theory')
FONT = pygame.font.SysFont('Ariel', 30, bold=False)

graph_algo = GraphAlgo()
graph_algo.load_from_json('../../data/A0.json')

min_x = min(graph_algo.get_graph().get_all_v().values(), key=lambda n: n.pos[0]).pos[0]
min_y = min(graph_algo.get_graph().get_all_v().values(), key=lambda n: n.pos[1]).pos[1]
max_x = max(graph_algo.get_graph().get_all_v().values(), key=lambda n: n.pos[0]).pos[0]
max_y = max(graph_algo.get_graph().get_all_v().values(), key=lambda n: n.pos[1]).pos[1]


def scale(data, min_screen, max_screen, min_data, max_data):
    """
    get the scaled data with proportions min_data, max_data
    relative to min and max screen dimensions
    """
    return ((data - min_data) / (max_data - min_data)) * (max_screen - min_screen) + min_screen


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit(0)

    screen.fill(Color(0, 0, 0))
    for node in graph_algo.get_graph().get_all_v().values():
        x = scale(node.pos[0], PADDING, screen.get_width() - PADDING, min_x, max_x)
        y = scale(node.pos[1], PADDING, screen.get_height() - PADDING, min_y, max_y)

        for edge in node.edges_out.keys():
            x2 = scale(graph_algo.get_graph().get_all_v()[edge].pos[0], PADDING, screen.get_width() - PADDING, min_x,
                       max_x)
            y2 = scale(graph_algo.get_graph().get_all_v()[edge].pos[1], PADDING, screen.get_height() - PADDING, min_y,
                       max_y)
            pygame.draw.line(screen, (22, 222, 22), (x, y), (x2, y2))

        pygame.draw.circle(screen, pygame.Color(255, 255, 255), (x, y), RADIUS)
        id_srf = FONT.render(str(node.key), True, (255, 0, 0))
        rect = id_srf.get_rect(center=(x, y))
        screen.blit(id_srf, rect)

    display.update()
    clock.tick(REFRESH_RATE)
