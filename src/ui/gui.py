import pygame
from pygame import time, display, Color, QUIT

from src.impl.di_graph import DiGraph
from src.impl.graph_algo import GraphAlgo
import pygame_menu
from tkinter import *
from tkinter import simpledialog
from src.ui.Range import Range, WorldGraph, Range2D
from src.ui.controller import UIController, ShortestPathEvent, CenterEvent
import tkinter.messagebox

pygame.init()
clock = time.Clock()

WIDTH, HEIGHT = 900, 600
REFRESH_RATE = 60
RADIUS = 20
PADDING = 50

screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=pygame.constants.RESIZABLE)
pygame.display.set_caption('Graph Theory')
FONT = pygame.font.SysFont('Ariel', 30, bold=False)


def callback(event):
    window = Tk()
    window.wm_withdraw()
    window.geometry("1x1+200+200")
    tkinter.messagebox.showinfo(title="Greetings", message=event)


controller = UIController(GraphAlgo(), callback)

menu = pygame_menu.Menu('Welcome', 400, 300,
                        theme=pygame_menu.themes.THEME_BLUE)
menu_algo = pygame_menu.Menu('Algorithms', 400, 300,
                             theme=pygame_menu.themes.THEME_BLUE)
menu_graph = pygame_menu.Menu('Graph Operations', 400, 300,
                              theme=pygame_menu.themes.THEME_BLUE)


def on_change_filename(name):
    global filename
    filename = name


def get_frame():
    rx = Range(PADDING, screen.get_width() - PADDING)
    ry = Range(PADDING, screen.get_height() - PADDING)
    return Range2D(rx, ry)


world_graph = WorldGraph()
wf = world_graph.w2f(controller.graph_algo.get_graph(), get_frame())


def update_world():
    wf.world = world_graph.GraphRange(controller.graph_algo.get_graph(), wf.frame)


def update_frame():
    wf.frame = get_frame()


def get_node_by_coordinate(x, y):
    pass


def show_graph():
    while True:
        update_frame()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    menu.mainloop(screen)
                if event.key == pygame.K_a:
                    menu_algo.mainloop(screen)
                if event.key == pygame.K_g:
                    menu_graph.mainloop(screen)

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                controller.graph_algo.get_graph().add_node(controller.graph_algo.get_graph().v_size(),
                                                           (wf.frameToWorld((pos[0], pos[1], 0))))

        screen.fill(Color(0, 0, 0))
        for node in controller.graph_algo.get_graph().get_all_v().values():
            x, y, z = wf.worldToframe(node.pos)
            for edge in node.edges_out.keys():
                x2, y2, z2 = wf.worldToframe(controller.graph_algo.get_graph().get_all_v()[edge].pos)
                pygame.draw.line(screen, (22, 222, 22), (x, y), (x2, y2))

        for node in controller.graph_algo.get_graph().get_all_v().values():
            x, y, z = wf.worldToframe(node.pos)
            pygame.draw.circle(screen, pygame.Color(255, 255, 255), (x, y), RADIUS)
            id_srf = FONT.render(str(node.key), True, (255, 0, 0))
            rect = id_srf.get_rect(center=(x, y))
            screen.blit(id_srf, rect)

        display.update()
        clock.tick(REFRESH_RATE)


def show(new_graph: bool = False):
    if not new_graph:
        if not controller.graph_algo.load_from_json(f'../../data/{filename}.json'):
            callback('Error file was not found')
            return
    else:
        controller.graph_algo.graph = DiGraph()
    update_world()
    show_graph()


def get_input(event):
    if event == 'shortest-path':
        try:
            Tk().wm_withdraw()
            input = simpledialog.askstring(title="Q",
                                           prompt='enter key1 & key2 seperated by ,')
            str = input.split(',')
            controller.on_trigger_event(ShortestPathEvent(int(str[0]), int(str[1])))
        except Exception as e:
            print('error', e)

    if event == 'center':
        controller.on_trigger_event(CenterEvent())

    if event == 'delete-node':
        Tk().wm_withdraw()
        input = simpledialog.askstring(title="Q",
                                       prompt='enter node key')
        controller.graph_algo.get_graph().remove_node(int(input.strip()))

    if event == 'add-edge':
        try:
            Tk().wm_withdraw()
            input = simpledialog.askstring(title="Q",
                                           prompt='enter key1 & key2 & w seperated by ,')
            str = input.split(',')
            controller.graph_algo.get_graph().add_edge(int(str[0]), int(str[1]), int(str[2]))
        except Exception as e:
            print('error', e)

    if event == 'remove-edge':
        try:
            Tk().wm_withdraw()
            input = simpledialog.askstring(title="Q",
                                           prompt='enter key1 & key2  seperated by ,')
            str = input.split(',')
            controller.graph_algo.get_graph().remove_edge(int(str[0]), int(str[1]))
        except Exception as e:
            print('error', e)


    if event == 'save':
        controller.graph_algo.save_to_json('../../out.json')


    show_graph()


menu_algo.add.button('Shortest Path', lambda: get_input('shortest-path'))
menu_algo.add.button('Center', lambda: get_input('center'))
menu_algo.add.button('TSP', lambda: get_input('tsp'))
menu_algo.add.button('Cancel', lambda: get_input(''))


menu_graph.add.button('Save Graph', lambda: get_input('save'))
menu_graph.add.button('Remove Node', lambda: get_input('delete-node'))
menu_graph.add.button('Add Edge', lambda: get_input('add-edge'))
menu_graph.add.button('Remove Edge', lambda: get_input('remove-edge'))
menu_graph.add.button('Cancel', lambda: get_input(''))


filename = 'A0'
menu.add.text_input('Enter graph filename :', default='A0', onchange=on_change_filename)
menu.add.button('New Graph', lambda: {show(True)})
menu.add.button('Load Graph', lambda: {show(False)})
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(screen)
