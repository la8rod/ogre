import pygame, random, time, sys
from pygame.locals import *
from random import *
import string
from itertools import count
pygame.init()



#Constants
WINDOWW = 600
WINDOWH = 600
COLUMNS = 6
ROWS = 6
THICK = 10
GRID_WIDTH = WINDOWW/COLUMNS
GRID_HEIGHT = WINDOWH/ROWS
FPS = 3
FPSCLOCK = pygame.time.Clock()

#directions
SOUTH = {'south':0}
EAST = {'east':90}
WEST = {'west':270}
NORTH = {'north':180}
DIRECTIONS = (SOUTH, EAST, NORTH, WEST)
#colors
#           R    G    B    T    element
BLACK    =(  0,   0,   0)       #gridlines, obstacles
GRAY     =(100, 100, 100)       #null
DGRAY    =( 50,  50,  50)
NAVYBLUE =( 60, 60,  100)  #
WHITE    =(255, 255, 255)       #infinity
DWHITE   =(150, 150, 150)       #obstacle white
RED      =(255,   0,   0)       #fire, grid lines
DRED     =(128,   0,   0)       #obstacle red
GREEN    =(  0, 255,   0)       #earth
DGREEN   =(  0, 128,   0)       #obstacle green
BLUE     =(  0,   0, 255)       #water
DBLUE    =(  0,   0, 128)       #obstacle BLUE
YELLOW   =(255, 255,   0)       #Move display
GOLD     =(128, 128,   0)
ORANGE   =(255, 128,   0)       #action display
DORANGE  =(128,  64,   0)       #
PURPLE   =(255,   0, 255)       #void
DPURPLE  =(128,   0, 128)       #obstacle purple
CYAN     =(  0, 255, 255)       #sky
DCYAN    =(  0, 128, 128)       #obstacle cyan

LIST_ELEMENT_TYPE = {1:"void", 2:"infinity", 3:"fire", 4:"earth", 5:"water", 6:"sky", 7:"null"}
LIST_ELEMENT_COLOR = {1:PURPLE, 2:WHITE, 3:RED, 4:GREEN, 5:BLUE, 6:CYAN, 7:GRAY}
DLIST_ELEMENT_COLOR = {1:DPURPLE, 2:DWHITE, 3:DRED, 4:DGREEN, 5:DBLUE, 6:DCYAN, 7:DGRAY}
F_SPEED_DICT = {'b': .5 , 'n':1,
                'i': 1, 'r':.6,
                'g': .8, 'b':.5,
                'v': .5, 'c':.8,
                'N':.5, 'I':.5,
                'R':.3, 'G':.4,
                'B':.25, 'V':.25,
                'C':.3}

ELEMENT_COLOR = {"void":PURPLE, "infinity":WHITE, "fire":RED, "earth":GREEN, "water":BLUE, "sky":CYAN, "null":GRAY}
TERRAIN_TYPE = {1:["swamp"], 2:["plains"], 3:["mountain"], 4:["forests"], 5:["river", "lake", "sea"], 6:["precipitation"], 7:["road","town", ]}
ACTIVE_FIELD_GRIDS = []
mousex = 0
mousey = 0
squads = {}
squad_rects = {}
squad_names = []
places = {}
towns = {}
mouseClicked = False
windowSurface = pygame.display.set_mode((WINDOWW, WINDOWH))
MENUW = 600
MENUH = 600
MENU_G_L = 100
menuSurface = pygame.display.set_mode((MENUW, MENUH))
menuSurface.fill(WHITE)
STATUSW = 600
STATUSH = 600
statusSurface = pygame.display.set_mode((STATUSW, STATUSH))
statusSurface.fill(WHITE)
#field map section
FIELDW = 600
FIELDH = 600
MENU_RECT_WIDTH = 100
MENU_RECT_HEIGHT = 25
fieldSurface = pygame.display.set_mode((FIELDW, FIELDH))
fieldSurface.fill(BLACK)
font = pygame.font.SysFont('Arial', 10)
#world map section
WORLDW = 600
WORLDH = 600

#world mape images
world_map = pygame.image.load('C:\Python27\python test folder and drafts\graphic files\ogre fantasy\world_map_edit.png')
stage_site = pygame.image.load('C:\Python27\python test folder and drafts\graphic files\ogre fantasy\stage_site.bmp')
worldSurface = pygame.display.set_mode((WORLDW, WORLDH))
WORLDE = {0:(450,400), 1:(450,300)}
WORLDEN = {0:'Headquarters', 1:'Hamen'}

#field tiles images
field_forest_tiles = ['C:\Python27\python test folder and drafts\graphic files\ogre fantasy\map field tiles\mforest1.bmp',
                         'C:\Python27\python test folder and drafts\graphic files\ogre fantasy\map field tiles\mforest2.bmp',
                         'C:\Python27\python test folder and drafts\graphic files\ogre fantasy\map field tiles\mforest3.bmp',
                         'C:\Python27\python test folder and drafts\graphic files\ogre fantasy\map field tiles\mforest4.bmp']
field_mountain_tiles = ['C:\Python27\python test folder and drafts\graphic files\ogre fantasy\map field tiles\mountain1.bmp',
                         'C:\Python27\python test folder and drafts\graphic files\ogre fantasy\map field tiles\mountain2.bmp',
                         'C:\Python27\python test folder and drafts\graphic files\ogre fantasy\map field tiles\mountain3.bmp',
                         'C:\Python27\python test folder and drafts\graphic files\ogre fantasy\map field tiles\mountain4.bmp']
field_plain_tiles = ['C:\Python27\python test folder and drafts\graphic files\ogre fantasy\map field tiles\plain1.bmp',
                         'C:\Python27\python test folder and drafts\graphic files\ogre fantasy\map field tiles\plain2.bmp',
                         'C:\Python27\python test folder and drafts\graphic files\ogre fantasy\map field tiles\plain3.bmp',
                         'C:\Python27\python test folder and drafts\graphic files\ogre fantasy\map field tiles\plain4.bmp']
field_snow_tiles = ['C:\Python27\python test folder and drafts\graphic files\ogre fantasy\map field tiles\snow1.bmp',
                         'C:\Python27\python test folder and drafts\graphic files\ogre fantasy\map field tiles\snow2.bmp',
                         'C:\Python27\python test folder and drafts\graphic files\ogre fantasy\map field tiles\snow3.bmp',
                         'C:\Python27\python test folder and drafts\graphic files\ogre fantasy\map field tiles\snow4.bmp']
field_swamp_tiles = ['C:\Python27\python test folder and drafts\graphic files\ogre fantasy\map field tiles\swamp1.bmp',
                         'C:\Python27\python test folder and drafts\graphic files\ogre fantasy\map field tiles\swamp2.bmp',
                         'C:\Python27\python test folder and drafts\graphic files\ogre fantasy\map field tiles\swamp3.bmp',
                         'C:\Python27\python test folder and drafts\graphic files\ogre fantasy\map field tiles\swamp4.bmp']
field_water_tiles = ['C:\Python27\python test folder and drafts\graphic files\ogre fantasy\map field tiles\water1.bmp',
                         'C:\Python27\python test folder and drafts\graphic files\ogre fantasy\map field tiles\water2.bmp',
                         'C:\Python27\python test folder and drafts\graphic files\ogre fantasy\map field tiles\water3.bmp',
                         'C:\Python27\python test folder and drafts\graphic files\ogre fantasy\map field tiles\water4.bmp']
field_neutral_tiles = ['C:\Python27\python test folder and drafts\graphic files\ogre fantasy\map field tiles\mneutral1.bmp',
                         'C:\Python27\python test folder and drafts\graphic files\ogre fantasy\map field tiles\mneutral2.bmp',
                         'C:\Python27\python test folder and drafts\graphic files\ogre fantasy\map field tiles\mneutral3.bmp',
                         'C:\Python27\python test folder and drafts\graphic files\ogre fantasy\map field tiles\mneutral4.bmp',
                       'C:\Python27\python test folder and drafts\graphic files\ogre fantasy\map field tiles\mneutral5.bmp',
                         'C:\Python27\python test folder and drafts\graphic files\ogre fantasy\map field tiles\mneutral6.bmp',
                         'C:\Python27\python test folder and drafts\graphic files\ogre fantasy\map field tiles\mneutral7.bmp',
                         'C:\Python27\python test folder and drafts\graphic files\ogre fantasy\map field tiles\mneutral8.bmp']

FIELD_OBSTACLE_TILES = {1: 'C:\Python27\python test folder and drafts\graphic files\ogre fantasy\map field tiles\swamp5.bmp',
                        2: 'C:\Python27\python test folder and drafts\graphic files\ogre fantasy\map field tiles\plain5.bmp',
                        3: 'C:\Python27\python test folder and drafts\graphic files\ogre fantasy\map field tiles\mountain5.bmp',
                        4: 'C:\Python27\python test folder and drafts\graphic files\ogre fantasy\map field tiles\mforest5.bmp',
                        5: 'C:\Python27\python test folder and drafts\graphic files\ogre fantasy\map field tiles\water5.bmp',
                        6: 'C:\Python27\python test folder and drafts\graphic files\ogre fantasy\map field tiles\snow5.bmp',
                        7: 'C:\Python27\python test folder and drafts\graphic files\ogre fantasy\map field tiles\neutral9.bmp'}

headings = {'n':'C:\Python27\python test folder and drafts\ogre Fantasy\headings\morth.bmp',
            's':'C:\Python27\python test folder and drafts\ogre Fantasy\headings\south.bmp',
            'e':'C:\Python27\python test folder and drafts\ogre Fantasy\headings\east.bmp',
            'w':'C:\Python27\python test folder and drafts\ogre Fantasy\headings\west.bmp',
            'ne':'C:\Python27\python test folder and drafts\ogre Fantasy\headings\mortheast.bmp',
            'nw':'C:\Python27\python test folder and drafts\ogre Fantasy\headings\morthwest.bmp',
            'se':'C:\Python27\python test folder and drafts\ogre Fantasy\headings\southeast.bmp',
            'sw':'C:\Python27\python test folder and drafts\ogre Fantasy\headings\southwest.bmp',
            'o':'C:\Python27\python test folder and drafts\ogre Fantasy\headings\omni.bmp'}

north = pygame.image.load(headings['n'])
south = pygame.image.load(headings['s'])
east = pygame.image.load(headings['e'])
west = pygame.image.load(headings['w'])
northeast = pygame.image.load(headings['ne'])
northwest = pygame.image.load(headings['nw'])
southeast = pygame.image.load(headings['se'])
southwest = pygame.image.load(headings['sw'])
omni = pygame.image.load(headings['o'])
h_images = {'n':north,'s':south, 'w':west, 'e':east,
            'ne':northeast, 'se':southeast,
            'nw':northwest, 'sw':southwest,
            'o':omni}

FIELD_TILES = {1:field_swamp_tiles, 2:field_plain_tiles, 3:field_mountain_tiles,
               4:field_forest_tiles, 5:field_water_tiles, 6:field_snow_tiles,
               7:field_neutral_tiles}

e_Inventory = []
te_Inventory = {'all':[], 'item':[], 'weapon':[], 'off_Hand':[], 'helmet':[], 'armor':[],
                'accessory':[]}
p_Inventory = []
tp_Inventory = {'all':[],'item':[], 'weapon':[],
                'off_Hand':[], 'helmet':[], 'armor':[],
                'accessory':[]}

efunds = 1000
pfunds = 1000

##thrust =  actions('thrust', 1, 5, {7:"null"}, 'physical', None, 'stagger', 0, 2, None, 0, 'line', 75, 2, True, '-')
##backstab = actions('backstab', 1, int(user.hit_Points_Max * 0.10),{7:"null"}, 'status', None, 'KO',  0, 1, None, 0, None, 35, 0, False, '-')
##riposte = actions('riposte', 1, 1, {7:"null"}, 'status', None, 'riposte', 0, 0, None, 0, None, 100, 1.2, None, '+')
##split = actions('split', 1, int(user.hit_Points_Max * 0.15), {7:"null"}, 'physical', None, 'stagger', 0, 1, None, 0, None, 65, 2, True, '-')
##cyclone =  actions('cyclone', 1, int(user.hit_Points_Max * 0.05), {7:"null"}, 'physical', None, 'stagger', 0, 3, 'square area', 0, 'square', 80, 0.75, True, '-')
##kadabra = actions('kadabra', 1, 10, {7:"null"}, 'physical', None, None, 0, 3, None, 1, None, 75, 1, False, '-')
##charge = actions('charge', 1, int(user.hit_Points_Max * 0.05), {7:"null"}, 'physical', None, None, 20, 6, None, 0,None, 100, 1.3, False, '-')
##guard = actions('guard', 1, 1, {7:"null"}, 'status', None, 'guard', 0, 0, None, 0, None, 100, 1, None, '+')
##retreat = actions('retreat', 1, 1, {7:"null"}, 'move', None, 'retreat', (user.speed * 5), 0, None, 0, None, 100, 1, None, ' ')

def menu_map_mode():
    pygame.mouse.set_visible(True)
    pygame.display.set_caption('menu mode')
    menuSurface
    menuSurface.fill(WHITE)
    pygame.display.update()
    return menuSurface
    
def world_map_mode(player, stage_objects):
    pygame.mouse.set_visible(True)
    pygame.display.set_caption('world_map')
    w = worldSurface
    a_stages = active_stage_objects(player.stage_count, stage_objects)
    w.blit(world_map, (0,0))
    world_stage_setup(w, player.stage_count, a_stages)
    pygame.display.update()
    choice = None
    menu_select = -1
    wm_mode = True
    copy = worldSurface.copy()
    select = None
    stage = None
    
    while wm_mode == True:
        w.blit(copy, (0,0))
        while choice == None:
            point = get_input()
           #print point
            if point == None:
                break
            
            select, stage = rect_checker(point, a_stages)
            #print stage
            if select == True:
                #x = stage.keys()
                #x = x[0]
                #a = a_stages[stage.name]
                confirm = yes_or_no(w, stage.name + ' : Would you like to start this stage?')
                if confirm == True:
                   #print stage.stage
                    #print stage.stage.field_Rects_List, 'field rects list'
                    #print stage.stage.field_Rects_Dict, 'field rects dict'
                    #not_a_value = raw_input('any clues as to why its messing up?')
                    field_map_mode(player, stage.stage)
                    w.blit(copy, (0,0))
                elif confirm != True:
                    w.blit(copy, (0,0))
                    
            elif select != True:
                pass
            
            if menu_select in point:
##                if event.type == KEYDOWN:
##                print 'button pressed'
##                print event.key
##                if event.key == K_m:
               #print 'm is pressed'
                menu_option, menu_rect = menu_bar(w)
               #print 'what happened?'
               #print menu_option
                if menu_option == 'roster':
                    selection, selection_rect = roster_menu()
                   #print selection
                    if selection == 'edit character':
                        y = pygame.display.get_surface()
                        select = False
                       #print select
                        while select != None:
                           #print select
                            select = edit_character_menu(player.roster, y, player.inventory)
                    
                    if selection == None:
                        break
                if menu_option == 'army inventory':
                   #print menu_option
                   #print menu_rect
                    item = scroll_menu(w, 200, 300,
                                       50, 100, player.inventory, 'all', None, 15)
                    if item == None:
                        break
                elif menu_option == None:
                    break

                #menu_select, menu_rect = menu_bar(w)
                #if menu_select
            w.blit(copy, (0,0))
            pygame.display.update()


##def world_map_mode():
##    pygame.mouse.set_visible(True)
##    pygame.display.set_caption('world_map')
##    worldSurface
##    worldSurface.blit(world_map, (0,0))
##    pygame.display.update()
##    return worldSurface

def world_stage_setup(surf, player_stage_count, stage_objects):
    p = player_stage_count
    for stage in stage_objects:
        s = stage_objects[stage]
        surf.blit(s.image, s.rect.topleft)
        pygame.draw.rect(surf, BLACK, s.rect, 1)
    #pygame.display.update()

def active_stage_objects(player_stage_count, stage_objects):
    active_stages = {}
    p = player_stage_count
    for stage in stage_objects:
        s = stage_objects[stage]
        if s.count <= p:
            active_stages[s.name] = s
        elif s.count > p:
            pass
    return active_stages


def field_map_mode(player, stage): #enemy roster and towns should be part of the stage class
    #l = len(stage)
##    if l == 1:
##        stage = stage.values()
##        stage = stage[0].stage
##    elif l > 1:
##        k = stage.keys()
##        select, rect = menu_bar(worldSurface, k)
##        stage = stage[select]
##        stage = stage.stage
    #squads = {}
    #squad_rects = {}
    #squad_names = []
    pygame.mouse.set_visible(True)
    pygame.display.set_caption('field map')
    fieldSurface
    #stage = field_Map_Level(fieldSurface, 10, 'C:\Python27\python test folder and drafts\mield_level2.txt', towns, 1000, 'loyalist', {}, 10)
    efunds = stage.funds
    pfunds = player.funds
    rebel_Army = player.roster #create_Roster(10, 'rebel')
    loyalist_Forces = stage.enemy_Forces #create_Roster(10, 'loyalist')
    sfd = stage.field_Rects_Dict
    able_roster = list(rebel_Army)
    able_enemy_roster = list(loyalist_Forces)
    squad_nums = 0
    rebel_Base, enemy_Base = base_Check(stage.towns)
    towns = stage.towns
    f_count = 0

    for town in stage.towns:
        t = stage.towns[town]
        fieldSurface.blit(t.image, t.topleft)

    field_Mode = True
    mouse_Click = None
    squad_Command = []
    first_Click = True
    first_Point = None
    second_Click = False
    second_Point = None
    squad_dest = ()
    pygame.display.update()
    #copy = fieldSurface.copy()

    #should have mouse click first, to fix the issue of clicking and the rect isn't there
    #as much as i hate to do it now, i should modulize all these things into functions
    
    while field_Mode is True:
        f_count += 1
        
        squads_length = len(squads)
        fieldSurface.fill(BLACK)
        color = 0
        a_squads = {}
        rect_changes = []
        #active squad update
        for squad in squads:
            a = squads[squad]
            if a.status.has_key('decimated') == True:
                pass
            elif a.status.has_key('decimated') != True:
                a_squads[a.name] = a
        #draw in field_rects
                
        for rect in stage.field_Rects_List:
            #LIST_ELEMENT_TYPE = {1:"void", 2:"infinity",  5:"water", 
            change_list = [1,2,5]
            change = randrange(0, 11)
            if rect.element_Type in change_list and rect.obstacle != True and change == 10:
                #if f_count % 3 == 0:
                rect.image_change()
                    #rect_changes.append(rect)
                    #fieldSurface.blit(rect.image, rect.rect.topleft)
                #elif f_count % 3 != 0:
                 #   pass
            else:
                pass
            
            fieldSurface.blit(rect.image, rect.rect.topleft)
            color = color + 1

        for town in stage.towns:
            t = stage.towns[town]
            fieldSurface.blit(t.image, t.topleft)
            

        copy = fieldSurface.copy()

        #copy = fieldSurface.copy()

        #checks for squad collision and initiates bttlemode
        if squads_length > 1:
            flag1 = None
            flag2 = None
            flag3 = None
            flag4 = None
            
            for squadx in a_squads:
        
                x = a_squads[squadx]
                
                for squady in a_squads:
                    y = a_squads[squady]
        
                    if doRectsOverlap(x.rect, y.rect) == True and x.allegiance != y.allegiance:
                       #print x.effect_Rect.topleft,x.effect_Rect.bottomright, y.rect.topleft, y.effect_Rect.bottomright
                        a, b = x.effect_Rect.topleft
                        if x.status.has_key('in transit') == False and y.status.has_key('in transit') == True:
                            b_field = x.effect_Rect
                            flag1 = True
                        elif x.status.has_key('in transit') == True and y.status.has_key('in transit') == False:
                            b_field = y.effect_Rect
                            flag2 = True
                        if flag1 == None and flag2 == None:
                            c = x.effect_Rect
                            d = y.effect_Rect
                            ct = c.topleft
                            dt = d.topleft
                            if ct[0] <= dt[0]:
                                e = ct[0]
                            elif ct[0] > dt[0]:
                                e = dt[0]
                            if ct[1] <= dt[1]:
                                f = ct[1]
                            elif ct[1] > dt[1]:
                                f = dt[1]
                            b_field = pygame.rect.Rect(e,f, 60, 60)
                        flags = {'flag1':flag1, 'flag2':flag2, 'flag3':flag3}
                        #print flags
                        belligerents = {x.allegiance : {x.name: x},
                                        y.allegiance: {y.name: y}}
                        start_points = {x.name : x.rect.center,
                                        y.name : y.rect.center}
                        for squadz in a_squads:
                            z = a_squads[squadz]
                            if z == (x or y):
                                pass
                            elif z != (x or y):
                                if x.effect_Rect.collidepoint(z.rect.center) == 1:
                                    start_points[z.name] = z.rect.center
                                    if belligerents.has_key(z.allegiance) == True:
                                        belligerents[z.allegiance][z.name] = z

                                    elif belligerents.has_key(z.allegiance) == False:
                                        belligerents[z.allegiance]= {z.name:z}

                                elif x.effect_Rect.collidepoint(z.rect.center) != 1:
                                    pass
                        oa = a
                        rect_list = []
                        #gathers the field rects and converts them to map_grids... need to change the 6 there a variable to represent the width of the field
                        for b in range(b, b + (6 * stage.grid_Side), stage.grid_Side):
                           #print b, 'b'
                            modb = (b/stage.grid_Side) * stage.grid_Side
                            for oa in range(oa, oa + (6 * stage.grid_Side), stage.grid_Side):

                                moda = (oa/stage.grid_Side) * stage.grid_Side
                                rect_list.append(stage.field_Rects_Dict[(moda,modb)])
                                
                            oa = a
                        l = len(belligerents)
                        if flag4 != True:
                            belligerents, flow, loser = time_flow(belligerents, start_points, rect_list, b_field, stage.towns)
                        flag4 = True
                       #print loser, 'loser'
                        #updates the effect of the battle to the squads
                        for squad in squads:
                            s = squads[squad]
                            if s.allegiance in belligerents:

                                valid = belligerents[s.allegiance].has_key(s.name)
                                if valid == True:
                                    squ = belligerents[s.allegiance].pop(s.name)
                                    if squ.allegiance == loser:
                                        squ.rect.center = squ.lost_battle(stage.towns)
                                elif valid != True:
                                    pass
                        del belligerents
        #pygame.display.update()
                        
        #check what places are occupied
        
        for location in stage.towns:
            s = stage.towns
            sl = stage.towns[location]
            sl.occupied(squads)
            sll = len(sl.roster)
            if sl.allegiance == 'loyalist' and sl.base == True and sll > 0:
                sl.roster, new_squad = sl.auto_squad(stage)
            
        #checks to see if conditions for victory have been met
        #print 'checking for victory'
        victory = victory_check(towns)
        st = type('str')
        it = type(1)
        v = type(victory)
        #print victory
        if v == st:
            if victory == 'victory' or victory == 'defeat':
                field_Mode = False
                break
        #elif v == it,: need to figure out how to address the amount of points
        #ncessary for integer counts, based on condition completion as a
        #a means to victory
        elif victory == None:    
            pass
        #checks inputs
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 3:
                    break
                mx, my = event.pos
                point = (mx, my)
               #print point
                #should make thisa dictionary with a list of places and what has been clicked. 
                #m_Click_Base = rebel_base.rect.collidepoint(point)
                #m_Click_Enemy = enemy_base.rect.collidepoint(point)
                #m_Click_f_town1 = f_town1.rect.collidepoint(point)
                for town in stage.towns:
                    t = stage.towns[town]
                    if t.rect.collidepoint(point) == True:
                        t.menu_rects = t.menu()
                        selection = t.menu_select()
                        
                        if selection == 'services':
                            t.menu_rects = t.menu(selection)
                            selection = t.menu_select()
                            
                            if selection == 'create squad':
                                if t.base == True:
                                    if t.allegiance == 'rebel':
                                        able_roster = create_Squad(able_roster, t.rect.center)
                                    elif t.allegiance == 'loyalist':
                                        able_enemy_roster = create_Squad(able_enemy_roster, t.rect.center, rebel_Base)
                                squad_nums = squad_nums + 1
                                
                            elif selection == 'merchant':
                                pfunds = t.general_store(p_Inventory, tp_Inventory, pfunds)
                                
                            elif selection == 'enlistment':
                                rebel_Army, able_roster, pfunds = t.recruit(rebel_Army, able_roster, pfunds)
                    
                #if squads_length > 1:
                    
                for squad in squads:
                    
                    if squad_rects[squad].collidepoint(point) == True:
                        mouse_Click = True
                        squad_Command.append(squad)
                        squad_dest = squads[squad]
                        
                        if squads[squad].status.has_key('camping') == True:
                            selection = squads[squad].camp_options(squads)
                            if selection != None:    

                                if selection == 'move':
                                    squads[squad].camp_Abilities[selection](copy)
                                else:
                                    squads[squad].camp_Abilities[selection]()
                            else:
                                pass
                        elif squads[squad].status.has_key('camping') == False:
                            squads[squad].menu()
                            selection = squads[squad].menu_select(squads[squad], squads)
                            if selection != None:
                                if selection == 'move':
                                    squads[squad].field_Abilities[selection](copy)
                                else:
                                    squads[squad].field_Abilities[selection]()
                            else:
                                pass
                        else:
                            break

##                elif len(squad_rects) == 1:
##                    print 'in ==1 loop'
##                    
##                    if squad_rects[squad_names[0]].collidepoint(point) == True:
##                        mouse_Click = True
##                        squad_Command.append(squads[squad_names[0]])
##                        squad_dest = squads[squad_names[0]]
##                        
##                        if squads[squad].status.has_key('camping') == True:
##                            print 'camping in status'
##                            selection = squads[squad].camp_options(squads)
##                            
##                            if selection != None:
##                                if selection == 'move':
##                                    squads[squad].camp_Abilities[selection](copy)
##                                else:
##                                    squads[squad].camp_Abilities[selection]()
##                            else:
##                                pass
##                            
##                        elif squads[squad].status.has_key('camping') == False:
##                            squads[squad].menu()
##                            selection = squads[squad].menu_select(squads[squad], squads)
##                            if selection != None:
##                                if selection == 'move':
##                                    squads[squad].field_Abilities[selection](copy)
##                                else:
##                                    squads[squad].field_Abilities[selection]()
##                            else:
##                                pass
##
##                        else:
##                            break
##
##                elif len(squad_rects) == 1:
##                    print 'in ==1 loop'
##                    
##                    if squad_rects[squad_names[0]].collidepoint(point) == True:
##                        mouse_Click = True
##                        squad_Command.append(squads[squad_names[0]])
##                        squad_dest = squads[squad_names[0]]
##                        
##                        if squads[squad].status.has_key('camping') == True:
##                            print 'camping in status'
##                            selection = squads[squad].camp_options(squads)
##                            
##                            if selection != None:
##                                if selection == 'move':
##                                    squads[squad].camp_Abilities[selection](copy)
##                                else:
##                                    squads[squad].camp_Abilities[selection]()
##                            else:
##                                pass
##                            
##                        elif squads[squad].status.has_key('camping') == False:
##                            squads[squad].menu()
##                            selection = squads[squad].menu_select(squads[squad], squads)
##                            if selection != None:
##                                if selection == 'move':
##                                    squads[squad].field_Abilities[selection](copy)
##                                else:
##                                    squads[squad].field_Abilities[selection]()
##                            else:
##                                pass
##
##                        else:
##                            break

                    #need to change it so that only rebel pledge towns have access to services... unless player is in control of someone with loyalist allegiance
##                    if selection == 'services':
##                        towns['enemy_Base'].menu_rects = towns['enemy_Base'].menu(selection)
##                        selection = towns['enemy_Base'].menu_select()
##                        
##                        if selection == 'create squad':
##                            towns['enemy_Base'].roster = create_Squad(towns['enemy_Base'].roster)
##                            squad_nums = squad_nums + 1
##                            
##                        elif selection == 'merchant':
##                            efunds = towns['enemy_Base'].general_store(e_Inventory, te_Inventory, efunds)
                    
                   #print squads
                    m_Click_Enemy = False

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
               #print 'button pressed'
               #print event.key
                if event.key == K_m:
                   #print 'm is pressed'
                    menu_options, menu_rect = menu_bar(fieldSurface)
                   #print 'what happened?'
                   #print menu_options
                    if menu_options == 'roster':
                        selection, selection_rect = roster_menu()
                       #print selection
                        if selection == 'edit character':
                            y = pygame.display.get_surface()
                            select = False
                           #print select
                            while select != None:
                               #print select
                                select = edit_character_menu(rebel_Army, y, tp_Inventory)
                        
                        if selection == None:
                            break
                    if menu_options == 'army inventory':
                       #print menu_options
                       #print menu_rect
                        item = scroll_menu(fieldSurface, 200, 300,
                                           50, 100, tp_Inventory, 'all', None, 15)
                        if item == None:
                            break
                    elif menu_options == None:
                        break


           #print squad_dest

        for squad in squads:
            s = squads[squad]
            s.status_check(sfd)
            if s.allegiance != player.allegiance:
                #print 'in behavior check loop'
                s.status, s.route = s.behavior(squads, towns)
            s.terrain_Modifier_Dict(stage)
        #draw in squads, can unify this, since dictionaries can accept an item of 1 lenght
        #if squads_length > 1:
        for squad in squads:
            s = squads[squad]
            pygame.draw.rect(fieldSurface, s.color, s.rect, 0)
            pygame.draw.rect(fieldSurface, s.color, s.effect_Rect, 1)
            fieldSurface.blit(s.image,
                             (s.rect.topleft[0] + int((s.rect.center[0] - s.rect.topleft[0])/2),
                              s.rect.topleft[1] + int((s.rect.center[1] - s.rect.topleft[1])/2)))
            #rect_changes.append(s.rect)
##        elif squads_length == 1:
##        
##            pygame.draw.rect(fieldSurface, squads[squad_names[0]].color, squads[squad_names[0]].rect, 0)
##            pygame.draw.rect(fieldSurface, squads[squad_names[0]].color, squads[squad_names[0]].effect_Rect, 1)
##            fieldSurface.blit(squads[squad_names[0]].image,
##                             (squads[squad_names[0]].rect.topleft[0] + int((squads[squad_names[0]].rect.center[0] - squads[squad_names[0]].rect.topleft[0])/2),
##                              squads[squad_names[0]].rect.topleft[1] + int((squads[squad_names[0]].rect.center[1] - squads[squad_names[0]].rect.topleft[1])/2)))


        if mouse_Click == True:
            first_Click = False
            second_Click = True
        elif mouse_Click == False:
            first_Click = True
            second_Click = False

        pygame.display.update()
        FPSCLOCK.tick(FPS)
        
   #print 'field_Mode is done'


##def field_map_mode():
##    world_m = world_map_mode()
##    world_stage_blit(world_m)
##    x = raw_input('world map?')
##    pygame.mouse.set_visible(True)
##    pygame.display.set_caption('field map')
##    fieldSurface
##    mx, my = 500, 500
##    efunds = 1000
##    pfunds = 1000
##    rebel_Army = create_Roster(10, 'rebel')
##    loyalist_Forces = create_Roster(10, 'loyalist')
##    able_roster = list(rebel_Army)
##    able_enemy_roster = list(loyalist_Forces)
##    squad_nums = 0
##    print rebel_Army
##    items = {'wood sword':wood_sword, 'wood helmet':wood_helmet,
##             'wood armor':wood_armor, 'potion':potion, 'poison':poison,
##             'grenade':grenade, 'phoenix_Down':phoenix_Down}
##    items_cost = {'wood sword':50, 'wood helmet':50,
##                  'wood armor':50,'potion':20, 'poison':100,
##                  'grenade':200, 'phoenix_Down':300}    
##    tattoine = place('tattoine', 'town', 10, 'rebel',
##                       ['enlistment', 'create squad', 'merchant'],
##                       (550, 550), items, items_cost, True)
##    deathStar = place('deathstar', 'castle', 10, 'loyalist',
##                       ['enlistment', 'create squad', 'merchant'],
##                       (75, 30), items, items_cost, True)
##    cloudCity = place('cloud city', 'town', 10, 'rebel',
##                    ['enlistment', 'merchant'],
##                    (450, 125), None, None, False)
##    towns[tattoine.name] = tattoine
##    towns[deathStar.name] = deathStar
##    towns[cloudCity.name] = cloudCity
##    stage = field_Map_Level(fieldSurface, 10, 'C:\Python27\python test folder and drafts\mield_level2.txt')
##    fieldSurface.blit(rebel_base.image, rebel_base.rect.topleft)
##    fieldSurface.blit(enemy_base.image, enemy_base.rect.topleft)
##    fieldSurface.blit(f_town1.image, f_town1.rect.topleft)
##    field_Mode = True
##    mouse_Click = None
##    squad_Command = []
##    first_Click = True
##    first_Point = None
##    second_Click = False
##    second_Point = None
##    squad_dest = ()
##    items = {'wood sword':wood_sword, 'wood helmet':wood_helmet,
##             'wood armor':wood_armor, 'potion':potion, 'poison':poison,
##             'grenade':grenade, 'phoenix_Down':phoenix_Down}
##    items_cost = {'wood sword':50, 'wood helmet':50,
##                  'wood armor':50,'potion':20, 'poison':100,
##                  'grenade':200, 'phoenix_Down':300}
##
##    
##    while field_Mode is True:
##        squads_length = len(squads)
##        fieldSurface.fill(BLACK)
##        color = 0
##        a_squads = {}
##        for squad in squads:
##            a = squads[squad]
##            if a.status.has_key('decimated') == True:
##                pass
##            elif a.status.has_key('decimated') != True:
##                a_squads[a.name] = a
##        
##        for rect in stage.field_Rects_List:
##            fieldSurface.blit(rect.image, rect.rect.topleft)
##            color = color + 1
##        fieldSurface.blit(rebel_base.image, rebel_base.rect.topleft)
##        fieldSurface.blit(enemy_base.image, enemy_base.rect.topleft)
##        fieldSurface.blit(f_town1.image, f_town1.rect.topleft)
##        for squad in squad_rects:
##        
##            squads[squad].status_check()
##            squads[squad].terrain_Modifier_Dict(stage)
##        
##        if squads_length > 1:
##            for squad in squads:
##        
##                pygame.draw.rect(fieldSurface, squads[squad].color, squads[squad].rect, 0)
##                pygame.draw.rect(fieldSurface, squads[squad].color, squads[squad].effect_Rect, 1)
##                fieldSurface.blit(squads[squad].image,
##                                 (squads[squad].rect.topleft[0] + int((squads[squad].rect.center[0] - squads[squad].rect.topleft[0])/2),
##                                  squads[squad].rect.topleft[1] + int((squads[squad].rect.center[1] - squads[squad].rect.topleft[1])/2)))
##        elif squads_length == 1:
##        
##            pygame.draw.rect(fieldSurface, squads[squad_names[0]].color, squads[squad_names[0]].rect, 0)
##            pygame.draw.rect(fieldSurface, squads[squad_names[0]].color, squads[squad_names[0]].effect_Rect, 1)
##            fieldSurface.blit(squads[squad_names[0]].image,
##                             (squads[squad_names[0]].rect.topleft[0] + int((squads[squad_names[0]].rect.center[0] - squads[squad_names[0]].rect.topleft[0])/2),
##                              squads[squad_names[0]].rect.topleft[1] + int((squads[squad_names[0]].rect.center[1] - squads[squad_names[0]].rect.topleft[1])/2)))
##        
##        copy = fieldSurface.copy()
##
##        #checks for squad collision and initiates bttlemode
##        if squads_length > 1:
##        
##            for squadx in a_squads:
##        
##                x = a_squads[squadx]
##                for squady in a_squads:
##                    y = a_squads[squady]
##        
##                    if doRectsOverlap(x.rect, y.rect) == True and x.allegiance != y.allegiance:
##                        print x.effect_Rect.topleft,x.effect_Rect.bottomright, y.rect.topleft, y.effect_Rect.bottomright
##                        a, b = x.effect_Rect.topleft
##                        if x.status.has_key('in transit') == False and y.status.has_key('in transit') == True:
##                            bfield = x.effect_Rect
##                        elif x.status.has_key('in transit') == True and y.status.has_key('in transit') == False:
##                            b_field = y.effect_Rect
##                        #b_field = x.effect_Rect
##                        belligerents = {x.allegiance : {x.name: x},
##                                        y.allegiance: {y.name: y}}
##                        start_points = {x.name : x.rect.center,
##                                        y.name : y.rect.center}
##                        for squadz in a_squads:
##                            z = a_squads[squadz]
##                            if z == (x or y):
##                                pass
##                            elif z != (x or y):
##                                if x.effect_Rect.collidepoint(z.rect.center) == 1:
##                                    start_points[z.name] = z.rect.center
##                                    if belligerents.has_key(z.allegiance) == True:
##                                        belligerents[z.allegiance][z.name] = z
##
##                                    elif belligerents.has_key(z.allegiance) == False:
##                                        belligerents[z.allegiance]= {z.name:z}
##
##                                elif x.effect_Rect.collidepoint(z.rect.center) != 1:
##                                    pass
##                        oa = a
##                        rect_list = []
##
##                        for b in range(b, b + (6 * stage.grid_Side), stage.grid_Side):
##                            print b, 'b'
##                            modb = (b/stage.grid_Side) * stage.grid_Side
##                            for oa in range(oa, oa + (6 * stage.grid_Side), stage.grid_Side):
##
##                                moda = (oa/stage.grid_Side) * stage.grid_Side
##                                rect_list.append(stage.field_Rects_Dict[(moda,modb)])
##                                
##                            oa = a
##                        l = len(belligerents)
##                        belligerents, flow, loser = time_flow(belligerents, start_points, rect_list, b_field)
##                        print loser, 'loser'
##                        
##                        for squad in squads:
##                            s = squads[squad]
##                            if s.allegiance in belligerents:
##
##                                valid = belligerents[s.allegiance].has_key(s.name)
##                                if valid == True:
##                                    squ = belligerents[s.allegiance].pop(s.name)
##                                    if squ.allegiance == loser:
##                                        squ.rect.center = squ.lost_battle()
##                                elif valid != True:
##                                    pass
##                        del belligerents
##        pygame.display.update()
##
##        #check what places are occupied
##        for location in towns:
##            towns[location].occupied(squads)
##
##        victory = victory_check(towns)
##        st = type('str')
##        it = type(1)
##        v = type(victory)
##        print victory
##        if v == st:
##            if victory == 'victory' or victory == 'defeat':
##                field_Mode = False
##                break
##        #elif v == it,: need to figure out how to address the amount of points
##        #ncessary for integer counts, based on condition completion as a
##        #a means to victory
##        elif victory == None:    
##            pass
##        
##        for event in pygame.event.get():
##            if event.type == MOUSEBUTTONDOWN:
##                if event.button == 3:
##                    break
##                mx, my = event.pos
##                point = (mx, my)
##                print point
##                m_Click_Base = rebel_base.rect.collidepoint(point)
##                m_Click_Enemy = enemy_base.rect.collidepoint(point)
##                m_Click_f_town1 = f_town1.rect.collidepoint(point)
##                    
##                if squads_length > 1:
##                    
##                    for squad in squads:
##                        
##                        if squad_rects[squad].collidepoint(point) == True:
##                            mouse_Click = True
##                            squad_Command.append(squad)
##                            squad_dest = squads[squad]
##                            
##                            if squads[squad].status.has_key('camping') == True:
##                                selection = squads[squad].camp_options(squads)
##                                if selection != None:    
##
##                                    if selection == 'move':
##                                        squads[squad].camp_Abilities[selection](copy)
##                                    else:
##                                        squads[squad].camp_Abilities[selection]()
##                                else:
##                                    pass
##                            elif squads[squad].status.has_key('camping') == False:
##                                squads[squad].menu()
##                                selection = squads[squad].menu_select(squads[squad], squads)
##                                if selection != None:
##                                    if selection == 'move':
##                                        squads[squad].field_Abilities[selection](copy)
##                                    else:
##                                        squads[squad].field_Abilities[selection]()
##                                else:
##                                    pass
##                            else:
##                                break
##                elif len(squad_rects) == 1:
##                    print 'in ==1 loop'
##                    
##                    if squad_rects[squad_names[0]].collidepoint(point) == True:
##                        mouse_Click = True
##                        squad_Command.append(squads[squad_names[0]])
##                        squad_dest = squads[squad_names[0]]
##                        
##                        if squads[squad].status.has_key('camping') == True:
##                            print 'camping in status'
##                            selection = squads[squad].camp_options(squads)
##                            
##                            if selection != None:
##                                if selection == 'move':
##                                    squads[squad].camp_Abilities[selection](copy)
##                                else:
##                                    squads[squad].camp_Abilities[selection]()
##                            else:
##                                pass
##                            
##                        elif squads[squad].status.has_key('camping') == False:
##                            squads[squad].menu()
##                            selection = squads[squad].menu_select(squads[squad], squads)
##                            if selection != None:
##                                if selection == 'move':
##                                    squads[squad].field_Abilities[selection](copy)
##                                else:
##                                    squads[squad].field_Abilities[selection]()
##                            else:
##                                pass
##
##                        else:
##                            break
##
##                if m_Click_Base == True:
##                    towns['rebel_Base'].menu_rects = towns['rebel_Base'].menu()
##                    selection = towns['rebel_Base'].menu_select()
##                    if selection == None:
##                        break
##                    
##                    if selection == 'services':
##                        towns['rebel_Base'].menu_rects = towns['rebel_Base'].menu(selection)
##                        selection = towns['rebel_Base'].menu_select()
##                        
##                        if selection == 'create squad':
##                            able_roster = create_Squad(able_roster)
##                            squad_nums = squad_nums + 1
##                            
##                        elif selection == 'merchant':
##                            pfunds = towns['rebel_Base'].general_store(p_Inventory, tp_Inventory, pfunds)
##                            
##                        elif selection == 'enlistment':
##                            rebel_Army, able_roster, pfunds = towns['rebel_Base'].recruit(rebel_Army, able_roster, pfunds)
##                            
##                    m_Click_Base = False
##
##                if m_Click_f_town1 == True:
##                    
##                    towns['f_town1'].menu_rects = towns['f_town1'].menu()
##                    selection = towns['f_town1'].menu_select()
##                    
##                    if selection == None:
##                        break
##                    
##                    if selection == 'services':
##                        towns['f_town1'].menu_rects = towns['f_town1'].menu(selection)
##                        selection = towns['f_town1'].menu_select()
##                        
##                        if selection == 'create squad':
##                            able_roster = create_Squad(able_roster)
##                            squad_nums = squad_nums + 1
##                            
##                        elif selection == 'merchant':
##                            pfunds = towns['f_town1'].general_store(p_Inventory, tp_Inventory, pfunds)
##                            
##                        elif selection == 'enlistment':
##                            rebel_Army, able_roster, pfunds = towns['f_town1'].recruit(rebel_Army, able_roster, pfunds)
##
##                    print squads
##                    m_click_f_town1 = False
##                    
##                if m_Click_Enemy == True:
##                    towns['enemy_Base'].menu_rects = towns['enemy_Base'].menu()
##                    selection = towns['enemy_Base'].menu_select()
##                    
##                    if selection == None:
##                        break
##                    
##                    if selection == 'services':
##                        towns['enemy_Base'].menu_rects = towns['enemy_Base'].menu(selection)
##                        selection = towns['enemy_Base'].menu_select()
##                        
##                        if selection == 'create squad':
##                            towns['enemy_Base'].roster = create_Squad(towns['enemy_Base'].roster)
##                            squad_nums = squad_nums + 1
##                            
##                        elif selection == 'merchant':
##                            efunds = towns['enemy_Base'].general_store(e_Inventory, te_Inventory, efunds)
##                    
##                    print squads
##                    m_Click_Enemy = False
##
##            if event.type == QUIT:
##                pygame.quit()
##                sys.exit()
##
##            if event.type == KEYDOWN:
##                print 'button pressed'
##                print event.key
##                if event.key == K_m:
##                    print 'm is pressed'
##                    menu_options, menu_rect = menu_bar(fieldSurface)
##                    print 'what happened?'
##                    print menu_options
##                    if menu_options == 'roster':
##                        selection, selection_rect = roster_menu()
##                        print selection
##                        if selection == 'edit character':
##                            y = pygame.display.get_surface()
##                            select = False
##                            print select
##                            while select != None:
##                                print select
##                                select = edit_character_menu(rebel_Army, y, tp_Inventory)
##                        
##                        if selection == None:
##                            break
##                    if menu_options == 'army inventory':
##                        print menu_options
##                        print menu_rect
##                        item = scroll_menu(fieldSurface, 200, 300,
##                                           50, 100, tp_Inventory, 'all', None, 15)
##                        if item == None:
##                            break
##                    elif menu_options == None:
##                        break
##
##
##            print squad_dest
##
##            if mouse_Click == True:
##                first_Click = False
##                second_Click = True
##            elif mouse_Click == False:
##                first_Click = True
##                second_Click = False
##
##        pygame.display.update()
##        FPSCLOCK.tick(FPS)
##        
##    print 'field_Mode is done'

def victory_check(towns, squads = None, cs = None, roster = None, cp = None,
                  inventory = None, ci = None, ca = None, co = None):
#leave victory check alone for now 8/7/2015
    #check1 = check_personnel(cp)
    #check2 = check_squads(cs)
    #check3 = check_places(ca)
    #check4 = check_inventory(ci)
    #check5 = check_places(ct)
    count = 0
    v_count = 0
    ebo = None
    rbo = None
    #print 'in victory check'
    #print towns, 'towns'
    #if no conditions are set for victory, capture of the enemy base should
    #be the case for victory by the player. loss of the players own base signals
    #defeat 
    if cs == None and cp == None and ci == None and ca == None and co == None:
        #print ' in default loop check'
        for town in towns:
            t = towns[town]
            #print t.name
            #print 'did it print name'
            if t.base == True:
                #print t.base
                #print t.allegiance
                #print t.occupant
                if t.allegiance == 'loyalist':
                    ebo = t.occupant
                    #print 'ebo name and allegiance', ebo.name, ebo.allegiance
                elif t.allegiance == 'rebel':
                    rbo = t.occupant
                    #print 'rbo name and allegiance', rbo.name, rbo.allegiance
            elif t.base != True:
                pass

        if  ebo != None and ebo.allegiance == 'rebel':
           #print 'rebels won'
            return 'victory'
        if  rbo != None and rbo.allegiance == 'loyalist':
           #print 'loyalists won'
            return 'defeat'
        #if (rbo == None and ebo == None)
        else:
            return None
    elif cs != None or cp != None or ci != None or ca != None or co != None:
        pass
    #checks to see if a targeted squad conversion is necessary.
    #maybe be necessary to alter for capturing a unit,
    #or perhaps the neutralization of a unit
    if cs != None:
        v_count = v_count + len(cs)
    #cs should be a dictionary , made of {squad.name:squad instance} 
        for squad in cs:
            if squads[squad].allegiance == cs[squad]:
                count = count + 1
            elif squads[squad].allegiance != cs[squad]:
                pass
    #check for the acquisition of a certain character to the rebel side
    #might be necessary to alter this for capture, or neutralization
    #actually, by having objective as a variable, it can be whatever status
    #needednfor that character... so the variable cp should be a dictionary
    #with the character.name as the key, and the status as the value

    if cp != None:
        v_count = v_count + len(cp)
        for person in roster:
            for objective in cp:
                if person.status.has_key(cp[objective]) == True:
                    count = count + 1
                elif person.status.has_key(cp[objective]) != True:
                    pass

    #checks for items in the inventory, necesarry to complete a mission
    #will need to figure out how to check for number of items
    #ci should be a list of items
    if ci != None:
        l = len(ci)
        v_count = v_count + l
        if l == 1:
            if ci[0] in inventory:
                count = count + 1
            elif ci[0] not in inventory:
                pass
        if l > 1:
            for inv in ci:
                if inv in inventory:
                    count = count + 1
                elif inv not in inventory:
                    pass

    #check to see if a town has been swayed to the rebel cause
    #ca should be a dictionary made up of {place.name :necessary allegiance}
    if ca != None:
        v_count = v_count + len(ca)
        for locale in towns:
            for loc in ca:
                if towns[locale] == towns[loc]:
                    if towns[locale].allegiance == ca[loc]:
                        count = count + 1
                    elif towns[locale].allegiance == ca[loc]:
                        pass

    #checks to see if a town is occupied by the rebels, which is necessary for
    #mission completion
    #should be a dictionary of place.name:desired occupant.allegiance
    if co != None:
        v_count = v_count + len(co)
        for locale in towns:
            for loc in co:
                if towns[locale] == towns[loc]:
                    if towns[locale].occupant.allegiance == co[loc]:
                        count = count + 1
                    elif towns[locale].occupant.allegiance == co[loc]:
                        pass
                    
    if count >= v_count:
        return 'victory'
    elif count < v_count:
        return None

#defines user player class

def base_Check(towns):
    y = {}
    for town in towns:
        t = towns[town]
        if t.base == True:
            if t.allegiance == 'loyalist':
                enemy_base = t
            elif t.allegiance == 'rebel':
                rebel_base = t
        elif t.base != True:
            pass
   #print enemy_base.name, rebel_base.name, 'bases'
    return enemy_base, rebel_base
    
class p_Char:
    def __init__(self, name, rosterx, funds = 1000, allegiance = 'rebel', stage_count = 0):
        name = str(name)
        self.name = name
        if type(funds) != type(2):
            funds = 1000
        elif type(funds) == type(2):
            pass
        self.funds = funds
        a = ['loyalist', 'rebel', 'neutral']
        if allegiance not in a:
            allegiance = 'rebel'
        elif allegiance in a:
            pass
        self.allegiance = allegiance
        self.inventory = tp_Inventory
        self.roster = create_Roster(rosterx, allegiance)
        self.stage_count = stage_count

class stage_object:

    def __init__(self, name, fm_level, topleft, stage_count):
        self.name = name
        self.stage = fm_level
        self.image = stage_site
        self.rect = self.image.get_rect()
        self.rect.topleft = topleft
        self.count = stage_count
        
class field_Map_Level:

    def __init__(self, surface, grid_Side, level = None,  towns = {},
                 enemy_Funds = 0, enemy_Allegiance = 'loyalist',
                 enemy_Forces = {}, force_Number = 10):
        #terrain list
        #8/6/2015 , may need to add towns mission objectives here...
        x = 0
        y = 0
        ef = enemy_Funds
        ea = enemy_Allegiance
        self.field_Rects_List = []
        self.field_Rects_Dict = {}
        self.macro_Grids = self.create_Macro()
        self.colors = []
        self.obstacles = []
        self.grid_Side = grid_Side
        self.towns = towns
        self.funds = enemy_Funds
        if enemy_Forces == {}:
            self.enemy_Forces = create_Roster(force_Number, ea)
        elif enemy_Forces != {}:
            self.enemy_Forces = enemy_Forces
        self.towns = towns
        grid_position = {}
        self.e_dict = {'0': [7, BLACK, True], 'n':[7, GRAY, False],
                  'i': [2, WHITE, False], 'r':[3, RED, False],
                  'g': [4, GREEN, False], 'b':[5, BLUE, False],
                  'v': [1, PURPLE, False], 'c':[6, CYAN, False],
                  'N':[7, DGRAY, True ], 'I':[2, DWHITE, True],
                  'R':[3, DRED, True], 'G':[4, DGREEN, True],
                  'B':[5, DBLUE, True], 'V':[1, DPURPLE, True],
                  'C':[6, DCYAN, True]}

##        self.speed_dict = {'b': .5 , 'n':1,
##                  'i': 1, 'r':.6,
##                  'g': .8, 'b':.5,
##                  'v': .5, 'c':.6,
##                  'N':.5, 'I':.5,
##                  'R':.3, 'G':.4,
##                  'B':.25, 'V':.25,
##                  'C':.3}
##        

        k = self.e_dict.keys()
        
        if level != None:
            with open(level, 'r') as l:
                grid_data = l.read()
                #print grid_data

            for element in grid_data:
                if element in k:
                    grid_position[x,y] = self.e_dict[element]
                    rkey = grid_position[x,y][0]
                    color = grid_position[x,y][1]
                    obstacle = grid_position[x,y][2]
                    self.colors.append(color)
                    self.obstacles.append(obstacle)
                    field_Rect = field_Grid(x,y, grid_Side, rkey, element, obstacle)
                    #field_Rect.speed = self.speed_dict[element]
                    pygame.draw.rect(surface, field_Rect.color, field_Rect, 0)
                    self.field_Rects_List.append(field_Rect)
                    self.field_Rects_Dict[(x,y)] = field_Rect
                    x = x + grid_Side
                    if x >= FIELDW and y < FIELDH:
                        x = 0
                        y = y + grid_Side
                    if y >= FIELDH:
                        x = 610
        elif level == None:            
            while y < FIELDH:
                while x < FIELDW:
                    rkey = randrange(1,8)
                    
                    q = randrange(0,2)
                    if q == 1:
                        obstacle = True
                        color = DLIST_ELEMENT_COLOR[rkey]
                    else:
                        obstacle = False
                        color = LIST_ELEMENT_COLOR[rkey]
                    field_Rect = field_Grid(x,y, grid_Side, rkey, obstacle)
                    self.colors.append(color)
                    pygame.draw.rect(surface, field_Rect.color, field_Rect, 0)
                    self.field_Rects_List.append(field_Rect)
                    self.field_Rects_Dict[(x,y)] = field_Rect
                
                    x = x + grid_Side
                    if x >= FIELDW and y < FIELDH:
                        x = 0
                        y = y + grid_Side
                    if y >= FIELDH:
                        x = 610
        pygame.display.update()

    def create_Macro(self):
        macro_Rects = {}
        i = 0
        j = 0
        fw = FIELDW
        fh = FIELDH
        #s = 100
        s = 50
        for j in range(0, fw, s):
            for i in range(0, fh, s):
                macro_Rects[(i, j)] = pygame.rect.Rect(i, j, s, s)
                #print i, 'i'
                #print i, j , 'macro rects created'
                i = i + s
                
            i = 0
            j = j + s
        return macro_Rects
    
class field_Grid:
    
    def __init__(self, x, y, grid_Side, color_Code, field_code, obstacle = False):
        self.x_Coord = x/grid_Side
        self.y_Coord = y/grid_Side
        self.rect = pygame.rect.Rect(x, y, grid_Side, grid_Side)
        self.obstacle = obstacle
        self.speed = F_SPEED_DICT[field_code]
        if self.obstacle == True:
            self.color = DLIST_ELEMENT_COLOR[color_Code]
        elif self.obstacle != True:
            self.color = LIST_ELEMENT_COLOR[color_Code]

        self.element_Type = color_Code 
        self.terrain_Type = TERRAIN_TYPE[color_Code]
        if color_Code < 7:
            randnumber = randrange(0,4)
            
            if self.obstacle == True:
                image = pygame.image.load(FIELD_OBSTACLE_TILES[color_Code])
            elif self.obstacle != True:
                image = pygame.image.load(FIELD_TILES[color_Code][randnumber])
            self.image = image
            
        elif color_Code == 7:
            randnumber = randrange(0,8)
            if self.obstacle == True:
                image = pygame.image.load(FIELD_OBSTACLE_TILES[color_Code])
            elif self.obstacle == False:
                image = pygame.image.load(FIELD_TILES[color_Code][randnumber])
            self.image = image
        self.color_Code = color_Code
        self.occupant = []
        self.occupied = False
        self.grid_Side = grid_Side

    def pscore(self, poccupant, map_grids):
        x1, y1 = self.rect.center
        x2, y2 = poccupant.route[0]
        distance = -(abs(x1 - x2)+ abs(y1 - y2))
        ad = abs(distance)
        score = 0
        obs = 0
        ele = 0
        occ = 0
        spd = int((self.speed * ad) * .10)
        pen = -1 * self.adj_obstacle_check(map_grids)
        if self.obstacle == True:
            obs = (distance * 10)#int(-.10 * abs(distance))
        elif self.obstacle == False:
            obs = int(ad * .20)#int(.10 * abs(distance))
        if self.element_Type == poccupant.element_Type:
            ele = int(ad * .35) #int(0.05 * abs(distance))
        elif self.element_Type == poccupant.element_Type + 1:
            ele = int(distance * 2) #int(-0.05 * abs(distance))
        if poccupant in self.occupant:
            occ = -50
        #print self.element_Type, poccupant.element_Type, 'element types, grid and squad'
        #print distance, obs, ele, spd, 'score attributes'
        score = distance + obs + ele + spd + pen + occ #(-(distance * distance)) + obs + ele + spd
        #print 'pscore ok'
        
        return score

    def adj_obstacle_check(self, map_grids):
        s = self.grid_Side
        cx = self.rect.topleft[0]
        cy = self.rect.topleft[1]
        lx = cx - s
        gx = cx + s
        ly = cy - s
        gy = cy + s
        xc = [lx, cx, gx]
        xy = [ly, cy, gy]
        penalty = 1
        score = 0
        for x in xc:
            for y in xy:
                if map_grids.has_key((x, y)) == True:
                    mg = map_grids[(x, y)]
                    if mg.obstacle == True:
                        score = score + penalty
                    elif mg.obstacle == False:
                        pass
                elif map_grids.has_key((x, y)) == False:
                     pass
        #print 'adj obstacle check ok'

        return score
        

    def image_change(self):
        surf = pygame.display.get_surface()
        rn = randrange(0,4)
        cc = self.element_Type
        self.image = pygame.image.load(FIELD_TILES[cc][rn])
        #surf.blit(self.image, self.rect.topleft)


class squad:

    def __init__(self, members, topleft, rebel_base = None):
        self.name = members[0].name
        self.leader = members[0]
        self.max_num_of_characters = self.leader.leadership
        self.leader.leader = True
        self.element = self.leader.element
        self.element_Type = self.leader.element_type
        self.allegiance = self.leader.allegiance
        self.color = ELEMENT_COLOR[self.element]
        self.terrain_Modifier = 1
        l = len(members)
        i = 0
        x = 0
        y = 0
        q = 0
        h_cap = 0
        for i in range(l):
            x = x + members[i].speed
            if y == members[i].att_Range:
                q = q + 1
            elif y < members[i].att_Range:
                y = members[i].att_Range
                
        if l > 3:
            h_cap = 1
        elif l > 5:
            h_cap = 2
        elif l > 6:
            h_cap = 3
        elif l > 7:
            h_cap = int(l/2) + 1
        # h_cap
        self.move_Speed = 2 * (int(x/l) - h_cap)
        self.effect_Range = int(y/l) * 10
        self.roster = members
        self.status = {}
        self.field_Abilities = {'camp':self.camp, 'move':self.set_tracker, 'status':self.status_display }
        self.camp_Abilities = {'change leader':self.change_leader, 'edit character':self.edit_character,
                               'camp talk': self.camp_talk, 'hunt and gather': self.hunt, 'move':self.set_tracker}
        self.squad_Position = []
        #this will need to take coordinates once I get around to making that...
        t = topleft
        #if self.allegiance == 'rebel':
        self.rect = pygame.rect.Rect(t[0], t[1], 5*l, 5*l)
        #elif self.allegiance == 'loyalist':
        #    self.rect = pygame.rect.Rect(50, 50, 5*l, 5*l)
        self.effect_Rect = pygame.rect.Rect(self.rect.left - y, self.rect.top - y, 15 * y , 15 * y  )
        self.effect_Rect.center = self.rect.center
        if self.allegiance == 'loyalist':
            self.goal = rebel_base.rect.center
        elif self.allegiance == 'rebel':
            self.goal = self.rect.center
        self.start = self.rect.center
        self.heading = 'o'
        self.image = h_images[self.heading]
        self.image_rect = self.image.get_rect()
        self.operation_Step = 0
        self.length = l
        self.route = []
        self.previous_Path = []
        self.g_Count = 0
        self.af_grid = None
        pygame.draw.rect(fieldSurface, self.color, self.rect, 0)
        pygame.draw.rect(fieldSurface, self.color, self.effect_Rect, 1)
        pygame.display.update()
        for member in members:
            if member.weapon.equipment_type == 'bow':
                self.field_Abilities['volley'] = self.volley
                break

    def terrain_Modifier_Dict(self, field_Map_Level):
        posx = self.rect.center[0]
        posy = self.rect.center[1]
        grid_S = field_Map_Level.field_Rects_List[0].grid_Side
        x = (posx/grid_S) * grid_S
        y = (posy/grid_S) * grid_S
        weak = False
        f = field_Map_Level.field_Rects_Dict[(x,y)]
        
        if f.element_Type == self.element_Type:
            self.terrain_Modifier = 2.0
            if f.obstacle == True:
                self.terrain_Modifier = 1.5
        elif f.element_Type == self.element_Type + 1:
            self.terrain_Modifier = 0.5
            if f.obstacle == True:
                self.terrain_Modifier == 0.25
            weak = True
        elif f.element_Type != self.element_Type and weak == False:
            #print 'weak is equal to false'
        #if weak == False:
            self.terrain_Modifier = 1
            if f.obstacle == True:
                self.terrain_Modifier = 0.5

        self.terrain_Modifier = self.terrain_Modifier * f.speed
        
        #self.terrain_Modifier = int(self.terrain_Modifier * f.speed)

    def ppath_find(self, map_grids):
        cx, cy = self.rect.center
        side = map_grids[(0,0)].grid_Side
        cx = (cx / side) * side
        cy = (cy / side) * side
        cfg = map_grids[(cx, cy)]
        if self.af_grid == None:
            self.af_grid = cfg
        if cfg == self.af_grid:
            self.g_Count = self.g_Count + 1
            if self.g_Count >= 3:
                self.previous_Path.append(self.af_grid.rect.topleft)
        elif cfg != self.af_grid:
            self.previous_Path.append(self.af_grid.rect.topleft)
            self.af_grid = cfg
        #self.af_grid = cfg
        s = cfg.grid_Side
        fw = FIELDW
        fh = FIELDH
        i1 = cx - s
        i2 = cx - 2*s
        j1 = cy - s
        j2 = cy - 2*s
        y1 = cx + s
        y2 = cx + 2*s
        z1 = cy + s
        z2 = cy + 2*s
        xc = [ i2, i1, cx, y1, y2]
        yc = [ j2, j1, cy, z1, z2]
        ppath = {}
        pscores = {}
        for x in xc:
            for y in yc:
                if map_grids.has_key((x, y)) == True:
                    ppath[(x, y)] = map_grids[(x, y)]

                elif map_grids.has_key((x, y)) != True:
                    pass
        #print ppath
        #x = input('number, ppath')
        return ppath

    def ppath_assess(self, p_grids, map_grids):
        sx, sy = self.rect.center
        s = -999999
        r_path = {}
        good = False
        #d1 = 9999
        #d2 = 9999
        #d3 = 9999
        d_scores = {}
        gcx, gcy = self.route[0]
        #print self.route
        #d = abs(sx - gcx) + abs(sy - gcy)
        d = ((sx- gcx)*(sx-gcx) + (sy - gcy)*(sy-gcy))
##        e = self.element_Type
##        r_path = {}
##        d1 = f
##        d2 = f
##        d3 = f
        #print p_grids
        pscores = {}
        #while good == False:
        #print 'assessing...'
        s =-999999
        #d = abs(sx - gcx) + abs(sy - gcy)
        pd = 99999
        d1 = 999999
        pgkeys = p_grids.keys()
        #print sx, sy, gcx, gcy, 'sx sy gcx gcy'
        for grid in p_grids:
            g = p_grids[grid]
            score = g.pscore(self, map_grids)
            pgx, pgy = g.rect.center
            r_path[score] = g
            #maybe the error is tied to using the scores of the grid and the distance as the key, maybe i should i try using coordinates to keep other values from being 
            #pgx, pgy = g.rect.center
            #pd = abs(pgx - gcx) + abs(pgy - gcy)
            pd = ((pgx- gcx)*(pgx-gcx) + (pgy - gcy)*(pgy-gcy))
            d_scores[pd] = g
            pscores[score] = g.rect.topleft
            #print g.rect.topleft
            #print pd, d, 'is pd < than d?'
            if pd <= d:
                if pd < d1:
                    d1 = pd
                if score > s:
                    s = score
                elif score <= s:
                    pass

            
                
        #print s, d1, 's and d1'
        #print sx, sy, 'current position'
        #print pscores, 'grids scores'
        #print r_path[s].rect.topleft, 'selected grid'
        #print r_path, 'rpath'
        dlist = d_scores.keys(),
        #print dlist, 'distance scores', d, 'd'
        #print 'ppath assess good'
        md = min(d_scores)

        if s == -999999 and d1 == 999999 and d < md:
            return None
            #print p_grids, s, score, 'pgrids s and score'
            #x = raw_input('d = -9999 ...')
##            elif s != -999999:
            #good = True

                
                #print score, ' > ', d
            #elif score < d:
                #print score, ' < ', d
            #print score
            #print g.rect.topleft

        if r_path[s] == d_scores[d1]:
            #print 'optimum grid', r_path[s].rect.topleft, self.element
            return r_path[s]
        elif r_path[s] != d_scores[d1]:
            if d_scores[d1].obstacle == False:
             #   print 'not optimum grid 1', d_scores[d1].rect.topleft, self.element
                return d_scores[d1]
            elif d_scores[d1].obstacle == True:
                if r_path[s].obstacle == True:
                #if r_path[s].obstacle == False:
                    #print 'not optimum grid 2', r_path[s].rect.topleft, self.element
              #      print 'not optimum grid 2', d_scores[d1].rect.topleft, self.element
                    #return r_path[s]
                    return d_scores[d1]
                elif r_path[s].obstacle == False:
                    drx, dry = r_path[s].rect.center
                    #dr = abs(drx - gcx) + abs(dry - gcy)
                    dr = ((drx- gcx)*(drx-gcx) + (dry - gcy)*(dry-gcy))
               #     print dr, d, 'dr and d'
                    if dr < d:
                #        print 'not optimum grid 3', r_path[s].rect.topleft, self.element
                        return r_path[s]

        #print sx, sy, 'current position'
        #print pscores, 'grids scores'
        #print r_path[s].rect.topleft, 'selected grid'
        #print r_path, 'rpath'
        #print d_scores, 'distance scores'
        #print 'ppath assess good'
        #x = raw_input('what''s going on in ppath_assess')
        return r_path[s] 

    def path_planner(self, stage):
       #print 'in planner'
        cx, cy = self.rect.center
        gx, gy = self.route[0]
        #dx = abs(cx - gx)
        #dy = abs(cy - gy)
        path = []
        scores = {}
        distances = {}
        d = 0
        score = 0
        c_score = 0
        map_grids = stage.field_Rects_Dict
        macro_grids = stage.macro_Grids
        #k = 0
        for topleft in macro_grids:
        #    k = k + 1
        #    print k
            g_score = 0
            mgr = macro_grids[topleft]
            mx, my = mgr.center
            dx = abs(mx - gx)
            dy = abs(my - gy)
            d = dx + dy
            distances[topleft] = d
            for f_rect in map_grids:
            #    k = k + 1
            #    print k
                fg = map_grids[f_rect]
                fgr = fg.rect.center
                if mgr.collidepoint(fgr) == 1:
                    g_score = g_score + fg.pscore(self, map_grids)
                elif mgr.collidepoint(fgr) != 1:
                    pass
            scores[topleft] = g_score
        #print scores, 'path planner scores'
        return scores, distances

    def path_sorter(self, stage):
       #print 'in sorter'
        mg_scores, mgd = self.path_planner(stage)
        cx, cy = self.rect.center
        gx, gy = self.route[0]
        d = abs(cx - gx) + abs(cy - gy)
        s = 50
        #rgx = (gx/100) * 100
        #rgy = (gy/100) * 100
        #rfx = (cx/100) * 100
        #rfy = (cy/100) * 100
        rgx = (gx/s) * s
        rgy = (gy/s) * s
        rfx = (cx/s) * s
        rfy = (cy/s) * s
        path = []
        score = -999999
        #s = 100
        #s = 50
        #print rfx, rfy, 'rfx and rfy'
        #print rgx, rgy, gx, gy, 'rgx and rgy, gx, gy'
        while (rfx, rfy) != (rgx, rgy):
            score = -999999
            lx = rfx - s
            mx = rfx + s
            ly = rfy - s
            my = rfy + s
            px = 0
            py = 0
            xc = [lx, rfx, mx]
            yc = [ly, rfy, my]
            for y in yc:
                for x in xc:
                    if mg_scores.has_key((x, y)) == True and (x, y) != (rfx, rfy):
                        if mgd[(x, y)] < d:
                            if mg_scores[(x, y)] > score:
                                px = x
                                py = y
                                score = mg_scores[(x, y)]
            #                    print 'higher score'
                            elif mg_scores[(x, y)] <= score:
            #                    print 'score was not higher'
                                pass
                        elif mgd[(x, y)] >= d:
                            pass
            #        print x, y, 'x and y in path sorter'
            #if distances[(x, y)] < d:
            d = mgd[(px, py)]
            rfx = px
            rfy = py
            tld = abs((px - gx) + (py - gy))
            tl = (px, py)
            tlr = abs(((px + s) - gx) + (py - gy))
            tr = (px + s, py)
            bld = abs((px - gx) + ((py + s)- gy))
            bl = (px, py + s)
            brd = abs(((px + s) - gx) + ((py + s)- gy))
            br = (px + s, py + s)
            ced = abs(((px + s/2) - gx) + ((py + s/2)- gy))
            ce = (px + s/2, py + s/2)
            cdd = {tld:tl, tlr:tr, bld:bl, brd:br, ced:ce}
            mc = min(cdd)
            path.append(cdd[mc])
##            if mg_scores.has_key((0, 0)) == True:
##                print 'mg_scores has (0, 0)'
##                print path, 'path'
##            else:
##                pass
            del mg_scores[(px, py)]
            #print 'path appended', path, rfx, rfy, rgx, rgy
            #print rfx == rgx
            #print rfy == rgy
            #print path
        #print path, 'path'
        path.insert(len(path), (gx, gy))
        return path
        
        
    def status_display(self):
       print 'name: ,', self.name
       print 'leader: ,', self.leader
       print 'element: ', self.element
       print 'allegiance: ,', self.allegiance
       print 'unit speed: ,', self.move_Speed
       print 'range: ,', self.effect_Range
       for member in self.roster:
           print member.name, member.hit_Points, member.status

    def tracker(self, field_grids): 
        sx, sy = self.rect.center
        #print self.route, 'route'
        q = len(self.route)
        #print self.route
        #w = raw_input('whats the route? ')
        if q >= 1:
            gx, gy = self.route[0]
            ppath = self.ppath_find(field_grids)
            #print ppath, 'ppath'
            p = self.ppath_assess(ppath, field_grids)
            if p == None:
                tx, ty = gx, gy
                #x = input('what the shit?! write a number')
            elif p != None:
               #print p, 'p grid'
                tx, ty = p.rect.center
            #tx, ty = gx, gy
            #print gx, gy, 'target coordinates'
        elif q == 0:
            return self.rect.center
        speed = int(self.move_Speed * self.terrain_Modifier)
        #print sx, sy, speed, self.terrain_Modifier, 'move status'
        #print tx, ty, gx, gy, 'tx ty gx gy'
        if speed < 2:
            speed = 2
        #if speed <= 0:
        #    speed = 2
        nx = sx + int(speed)
        nx2 = sx - int(speed)
        ny = sy + int(speed)
        ny2 = sy - int(speed)
        nxd = sx + int(speed/2)
        nx2d = sx - int(speed/2)
        nyd = sy + int(speed/2)
        ny2d = sy - int(speed/2)
        newx = int(self.rect.center[0])
        newy = int(self.rect.center[1])
        x = 0
        y = 0
        heading = {(0,-2):'n', (0,2):'s', (-2, 0):'w', (2, 0): 'e',
                   (1, -1):'ne', (-1, -1):'nw', (1, 1):'se', (-1, 1):'sw',
                   (0,0):'o'}
        
        if self.status['in transit'] == True:
            if sx not in range((gx - speed), (gx + speed)) and sy not in range((gy - speed), (gy + speed)):
                if abs(nxd - tx) < abs(nx2d - tx):
                    newx = nxd
                    x = 1
                    
                elif abs(nxd - tx) >= abs(nx2d - tx):
                    newx = nx2d
                    x = -1
                    
                if abs(nyd - ty) < abs(ny2d - ty):
                    newy = nyd
                    y = 1
                elif abs(nyd - ty) >= abs(ny2d - ty):
                    newy = ny2d
                    y = -1
                    
            elif sx in range((gx - speed), (gx + speed)) and sy not in range((gy - speed), (gy + speed)):
                newx = sx
                if abs(ny - ty) <= abs(ny2 - ty):
                    newy = ny
                    y = 2
                    x = 0
                elif abs(ny - ty) > abs(ny2 - ty):
                    newy = ny2
                    y = -2
                    x = 0
                    
            elif sx not in range((gx- speed), (gx + speed)) and sy in range((gy - speed), (gy + speed)):
                newy = sy
                if abs(nx - tx) <= abs(nx2 - tx):
                    newx = nx
                    x = 2
                    y = 0
                elif abs(nx - tx) > abs(nx2 - tx):
                    newx = nx2
                    x = -2
                    y = 0
                    
            elif sx in range((gx - speed), (gx + speed)) and sy in range((gy - speed), (gy + speed)):
                newx = gx
                newy = gy
                x = 0
                y = 0
            
        if newx < 0:
            newx = 0
        elif newx > FIELDW:
            newx = FIELDW
        if newy < 0:
            newy = 0
        elif newy > FIELDH:
            newy = FIELDH
        if newx in range((gx - speed), (gx + speed)) and newy in range((gy - speed), (gy + speed)) and len(self.route) > 1:
            #print sx, sy, gx, gy, 2 * speed, 'is checkpoint reached?'
            #q = raw_input('is the checkpoint reached?')
            del self.route[0]
            pass

        elif newx in range((gx - speed), (gx + speed)) and newy in range((gy - speed), (gy + speed)) and len(self.route) == 1:
            del self.status['in transit']
            del self.route[0]
            x = 0
            y = 0
            
        else:
            self.status['in transit'] = True
            
        head = (x,y)
        #print head, 'head'
        if self.heading == heading[head]:
            pass
        elif self.heading != heading[head]:
            self.heading = heading[head]
            y = h_images[self.heading].get_rect()
            new_image = pygame.transform.scale(h_images[self.heading], ((y.width * (len(self.roster)-1),(y.height * (len(self.roster)-1)))))
            self.image = new_image
            self.image_rect = new_image.get_rect()
        

        #print newx, newy
        if newx == 0 and newy == 0:
        #    print sx, sy,'self.rect.center', gx, gy,'gx and gy', speed ,'speed', nx ,'nx', nx2,'nx2', ny,'ny', ny2,'ny2', nxd,'nxd', nx2d, 'nx2d', nyd,'nyd',ny2d,'ny2d'
            x = raw_input('look, the teleportation error happened')
            return (sx + 1, sy +1)
##        if newx == gx and newy == gy:
##            px, py = self.route[0]
##            if newx != px and newy != py:
##                rx = randrange(-1, 2)
##                ry = randrange(-1, 2)
##                newx = newx + rx
##                newy = newy + ry
##                print 'staying in place'
##            elif newx == px and newy == py:
##                del self.status['in transit']
##                del self.route[0]
        return (newx, newy)

    def set_tracker(self,background):
        s = self.move_Speed
        currentx, currenty = self.rect.center
        goalx = False
        goaly = False
        goal = False
        self.route = []
        surf = pygame.display.get_surface()
        previous = self.rect.center
        goal = get_mouseclick()
        if goal == None:
            return goal
        self.route.append(goal)
        goalx, goaly = goal
        surf.blit(background, (0,0))
        for squad in squads:
            q = squads[squad]
            pygame.draw.rect(surf, q.color, q.rect)
            pygame.draw.rect(surf, q.color, q.effect_Rect, 1)
        l =pygame.draw.line(surf, RED, previous, goal,1)
        mpoint = pygame.rect.Rect(goal[0], goal[1], 5, 5)
        pygame.draw.rect(surf, RED, mpoint)
        pygame.display.update()#mpoint, squad_rects.values, l)
        while goal != None:
            if type(goal) == bool:
                pass
            else:
                previous = tuple(goal)
            goal = get_mouseclick()
            #print goal, previous, goalx, goaly, 'goal, previous, goalx, goaly'
            if goal == None:
                break
            else:
                self.route.append(goal)
                l = pygame.draw.line(surf, RED, previous, goal,1)
                mpoint = pygame.rect.Rect(goal[0], goal[1], 5, 5)
                pygame.draw.rect(surf, RED, mpoint)
                pygame.display.update()#mpoint, l)
        a = currentx + s
        b = currentx - s
        c = currenty + s
        d = currenty - s

        if currentx != goalx and currenty != goaly:
            if abs(a - goalx) < abs(b - goalx):
                currentx += s/2
            else:
                currentx -= s/2
            if abs(c - goaly) < abs(d - goalx):
                currenty += s/2
            else:
                currenty -= s/2
        elif currentx != goalx and currenty == goaly:
            if abs(a - goalx) < abs(b - goalx):
                currentx += s
            else:
                currentx -= s
        elif currentx == goalx and currenty != goaly:
            if abs(c - goaly) < abs(d - goaly):
                currenty += s
            else:
                currenty -= s
        newx = currentx
        newy = currenty
        self.status['in transit'] = True
        return newx, newy

    def lost_battle(self, s_towns):
       #print 'in lost battle'
       #print self.rect.center, 'old coordinates'
        c = self.rect.center
        x = self.rect.center[0]
        y = self.rect.center[1]
        r = randrange(0,2)
        l = len(self.roster)
        s_towns['enemy_Base'], s_towns['rebel_Base'] = base_Check(s_towns)
        
##        for town in s_towns:
##            t = s_towns[town]
##            if t.base == True:
##                if t.allegiance == 'loyalist':
##                    s_towns['enemy_Base'] = t
##                elif t.allegiance == 'rebel':
##                    s_towns['rebel_Base'] = t
                    
        if self.leader.hit_Points <= 0:
           #print 9
            if self.allegiance == 'rebel':
                self.status['in transit'] = True
                self.goal = s_towns['rebel_Base'].rect.center
            elif self.allegiance == 'loyalist':
                self.status['in transit'] = True
                self.goal = s_towns['enemy_Base'].rect.center
               #print self.goal
            if l == 1:
                self.status = {'decimated': True}
            elif l > 1:
                casualty = []
                for player in self.roster:
                    pko = player.status.has_key('KO')
                    casualty.append(pko)
                if False not in casualty:
                    self.status = {'decimated' : True}
                    return c
                elif False in casualty:
                    pass
        if self.start[0] <= self.goal[0]:
           #print 1
            x,y = (self.rect.center[0] - 25, self.rect.center[1])
        elif self.start[0] > self.goal[0]:
           #print 2
            x, y = (self.rect.center[0] + 25, self.rect.center[1])
        if self.start[1] <= self.goal[1]:
           #print 3
            x, y = (self.rect.center[0], self.rect.center[1] - 25)
        elif self.start[1] > self.goal[1]:
           #print 4
            x, y = (self.rect.center[0], self.rect.center[1] + 25)
        if self.rect.center[0] <= 0:
           #print 5
            x, y = (0, self.rect.center[1])
        elif self.rect.center[0] > FIELDW:
           #print 6
            x, y = (FIELDW, self.rect.center[1])
        if self.rect.center[1] <= 0:
           #print 7
            x, y = (self.rect.center[0], 0)
        elif self.rect.center[1] > FIELDH:
           #print 8
            x,y = (self.rect.center[0], FIELDH)
        
       #print x, y, 'new coordinates'
       #print 'out of lost_battle'
        return (x,y)

##    def flee(b_field, aggressors):
##        sc = self.rect.center
##        ah = {}
##        headings = ['o', 'n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw']
##        for a in aggressors:
##            s = aggressors[a]
##            ah[s.name] = (s.heading, s.rect.center)
##            if s.heading in headings:
##                headings.remove(s.heading)
##            elif s.heading not in headings:
##                pass
##        


    def camp(self):
       #print self.goal
       #print self.rect.center
        self.goal = self.rect.center
       #print self.goal
       #print self.rect.center
        count = 0
        font = pygame.font.SysFont('castellar', 20)
        if self.status.get('camping') == True:
            for member in self.roster:
                if member.hit_Points == member.hit_Points_Max:
                    count = count + 1
                if member.hit_Points < member.hit_Points_Max and self.operation_Step >= 15:
                    if member.hit_Points > 0:
                        member.hit_Points = member.hit_Points + member.stamina
                        txt = str(member.stamina)
                        hit_display(True, txt, self, True)
                        self.operation_Step = 0

                    elif member.hit_Points == 0:
                        pass
                    if member.hit_Points > member.hit_Points_Max:
                        member.hit_Points = member.hit_Points_Max

               #print member.hit_Points
        
        elif self.status.get('camping') != True:
           #print 'in volley status check loop'
            self.status['camping'] = True
            self.operation_Step = 0
            
            if self.status.has_key('in transit') == True and self.status.get('in transit') == True:
                del self.status['in transit']

        if self.status.get('decimated') == True:
            self.status = {'decimated': True}

        font = pygame.font.SysFont('Arial', 10)

    def camp_options(self, squads):
        if self.status.has_key('camping') == True and self.status['camping'] == True:
            commands = ['change leader', 'edit character', 'camp talk',
                        'hunt and gather', 'move']
            self.menu(commands)
            command = self.menu_select(self, squads)
           #print command
            return command
        else:
            pass

    def decimated(self):
        count = 0
        font = pygame.font.SysFont('castellar', 20)
        
        l = len(self.roster)
        dying = 25
       #print 'in decimated'
        if self.status.has_key('decimated') == True:
           #print 'decimated is true'
            if l == 1:
               #print 'in l = 1 loop'
                member = self.roster[0]
                death = -(member.hit_Points_Max)
                if member.hit_Points > 0:
                    count = count + 1
                if member.hit_Points <= 0 and self.operation_Step >= dying:
                    if member.hit_Points < 0:
                        d = (6 - member.stamina)
                        if d <= 0:
                            d = 1
                        member.hit_Points = member.hit_Points - d
                        txt = str(d)
                       #print d, 'd and that much closer to death'
                        hit_display(True, txt, self, True)
                        self.operation_Step = 0

                    if member.hit_Points < death:
                        member.status['dead'] = True
                        
            elif l > 1:
                for member in self.roster:
                    death = -(member.hit_Points_Max)
                    if member.hit_Points > 0:
                        count = count + 1
                    if member.hit_Points <= 0 and self.operation_Step >= dying:
                        if member.hit_Points <= 0:
                            d = (6 - member.stamina)
                            if d <= 0:
                                d = 1
                           #print d, 'd and that much closer to death'
                            member.hit_Points = member.hit_Points - d
                            txt = str(d)
                            hit_display(True, txt, self, True)
                            self.operation_Step = 0
                        if member.hit_Points < death:
                            member.status['dead'] = True
            if count >= 1:
                del self.status['decimated']
                
        for member in self.roster:
           #print 'checking count'
            if member.hit_Points <= 0:
                pass
            elif member.hit_Points > 0:
                count = count + 1
                
        if count == 0:
           #print 'checking count 0'
            self.status['decimated'] = True
            
        elif count > 0:
           #print 'checking count > 0'
            del self.status['decimated'] 
            self.operation_Step = 0

        if self.status.has_key('decimated') == True:
            if self.status.has_key('in transit') == True and self.status.get('in transit') == True:
                del self.status['in transit']

        font = pygame.font.SysFont('Arial', 10)


    def change_leader(self):
        surf = menu_map_mode()
        new_leader = character_select(surf, self.roster)
        self.name = new_leader.name
        self.leader = new_leader
        self.element = new_leader.element
        self.element_Type = new_leader.element_type
        self.allegiance = new_leader.allegiance
        self.color = ELEMENT_COLOR[self.element]

    def edit_character(self):
        surf = menu_map_mode()
        select = False
        while select != None:
            select = edit_character_menu(self.roster, surf, tp_Inventory)

    def camp_talk(self):
        talk = 'this function is not functional yet...'
        return talk

    def hunt(self):
        hunt = 'this function is not functional yet...'
        return hunt

    def travel_cost(self):
        if self.status.get('in transit') == True:
            for member in self.roster:
                if member.hit_Points < member.hit_Points_Max and self.operation_Step >= 5:
                    member.hit_Points = member.hit_Points - (terrain_Cost - member.stamina)
                    self.operation_Step = 0
                elif self.operation_Step < 5:
                    self.operation_Step = self.operation_Step + .25

    def volley_prep(self):
        i = 0
        for member in self.roster:
            if member.weapon.equipment_type == 'bow' and member.hit_Points > int(member.hit_Points * 0.20):
                i = i + 1
                cost = int(member.hit_Points * member.weapon.strength * 0.05)
                if cost <= 0:
                    cost = 1
               #print member.name, 'payed ', cost, 'for volley'
                member.hit_Points = member.hit_Points - cost
                hit_display(True, cost, self)
        if i == 0:
            del self.status['volley']
        return i

    def volley(self):
       #print 'volley has been selected'
        i = 0
        for member in self.roster:
            if member.weapon.equipment_type == 'bow' and member.hit_Points > int(member.hit_Points * 0.20):
                i = i + 1
        if self.operation_Step >= 10 - i:
            self.operation_Step = 0
            if self.status.get('volley') == (False or None):
               #print 'in volley status check loop'
                self.status['volley'] = True
            for squad in squads:
                if self != squads[squad]:
                   #print self, squads[squad]
                    if doRectsOverlap(self.effect_Rect, squads[squad].effect_Rect) == True or isPointInsideRect(squads[squad].rect.center[0], squads[squad].rect.center[1], self.effect_Rect) == True:
                       #print 'volley is triggered'
                        i = self.volley_prep()
                        if i < 1:
                            break
                        elif i >= 1:
                            hit = self.arrow_fall(i)
                           #print hit, 'volley hit'
                            if hit == True:
                                hurt = randrange(0, 10) * 10
                                victim = randrange(0, (len(squads[squad].roster) - 1))
                                squads[squad].roster[victim].hit_Points = squads[squad].roster[victim].hit_Points - hurt
                               #print squads[squad].roster[victim].name, 'is hit with ', hurt, 'damage'
                                txt = str(hurt)
                                hit_display(hit, txt, squads[squad])
                            if hit == False:
                                pass
                            self.status['volley'] = True
                elif self == squad:
                    pass

    def arrow_fall(self, i):
        a_chance = 100 - (i * 20)
        chance = randrange(1, 101)
       #print chance, 'chance, ', a_chance, 'achance'
        if chance > a_chance:
            return True
        else:
            return False

    def status_check(self, field_grids):
        self.operation_Step = self.operation_Step + 1

        if self.status.get('decimated') == True:
           #print 'calling decimated'
            self.decimated()    

        if self.status.get('in transit') == True:
            self.rect.center = self.tracker(field_grids)
            self.effect_Rect.center = self.rect.center
            if self.status.get('volley') == True :
                del self.status['volley']
            if self.status.get('camping') == True:
                del self.status['camping']

        if self.status.get('volley') == True:
           #print 'volley status check'
            self.volley()
            if self.status.get('in transit') == True :
                del self.status['in transit']
            if self.status.get('camping') == True:
                del self.status['camping']
        
        if self.status.get('camping') == True:
            self.camp()
           #print 'camping'
            if self.status.get('in transit') == True :
                del self.status['in transit']
            if self.status.get('volley') == True:
                del self.status['volley']

    def squad_update(self):
        members = self.roster
        l = len(members)
        i = 0
        x = 0
        y = 0
        q = 0
        h_cap = 0
        z = self.rect.topleft
        for i in range(l):
            x = x + members[i].speed
            if y == members[i].att_Range:
                q = q + 1
            if y > members[i].att_Range:
                y = members[i].att_Range
                
        if l >= 3:
            h_cap = 1
        elif l >= 5:
            h_cap = 2
        elif l >= 6:
            h_cap = 3
        elif l >= 7:
            h_cap = int(l/2) + 1
        self.move_Speed = int(x/l) - h_cap
        self.effect_Range = int(y/l) * 10
        self.rect.width = 5*l
        self.rect.height =  5*l
        
        self.effect_Rect.width =   20 * l + y
        self.effect_Rect.height = 20 * l + y 
        b = 0
        for member in members:
            if member.weapon.equipment_type == 'bow':
                self.field_Abilities['volley'] = self.volley
                b = b + 1
                break
        if b == 0 and self.field_Abilities.has_key('volley') == True:
            del self.field_Abilities['volley']

    def menu(self, options = None):
        i = 0
        self.menu_rects = {}
        menu_orientation = 'evenleft'
        if self.rect.topleft[0] < MENU_RECT_WIDTH:
            if self.rect.topleft[1] < FIELDH - MENU_RECT_WIDTH:
                menu_orientation = 'bottomright'
            elif self.rect.topleft[1] > FIELDH - MENU_RECT_WIDTH:
                menu_orientation = 'topright'
                i = -(MENU_RECT_HEIGHT)
        elif self.rect.topleft[0] > FIELDH - MENU_RECT_WIDTH:
            if self.rect.topleft[1] < FIELDH - MENU_RECT_WIDTH:
                menu_orientation = 'evenleft'
            elif self.rect.topleft[1] > FIELDH - MENU_RECT_WIDTH:
                menu_orientation = 'topleft'
                i = -(MENU_RECT_HEIGHT)
        elif MENU_RECT_WIDTH < self.rect.topleft[0] < FIELDW - MENU_RECT_WIDTH:
                if self.rect.topleft[1] < MENU_RECT_WIDTH:
                    menu_orientation = 'bottomleft'
                elif self.rect.topleft[1] > FIELDW - MENU_RECT_WIDTH:
                    menu_orientation = 'topleft'
                    i = -(MENU_RECT_HEIGHT)
        if options == None:
            commands = self.field_Abilities
        elif options != None:
            commands = options
        r = []
        for command in commands:
            if menu_orientation == 'evenleft':
                self.menu_rects[command] = pygame.rect.Rect(self.rect.topleft[0] - MENU_RECT_WIDTH, self.rect.topleft[1] + i, MENU_RECT_WIDTH, MENU_RECT_HEIGHT)
                pygame.draw.rect(fieldSurface, (WHITE), self.menu_rects[command], 0) 
                fieldSurface.blit(font.render(command, True, (255, 0, 0)), self.menu_rects[command].center)
                i = i + 25
            elif menu_orientation == 'evenright':
                self.menu_rects[command] = pygame.rect.Rect(self.rect.topright[0], self.rect.topright[1] + i, MENU_RECT_WIDTH, MENU_RECT_HEIGHT)
                pygame.draw.rect(fieldSurface, (WHITE), self.menu_rects[command], 0) 
                fieldSurface.blit(font.render(command, True, (255, 0, 0)), self.menu_rects[command].center)
                i = i + 25
            elif menu_orientation == 'bottomleft':
                self.menu_rects[command] = pygame.rect.Rect(self.rect.bottomleft[0] - MENU_RECT_WIDTH, self.rect.bottomleft[1] + i, MENU_RECT_WIDTH, MENU_RECT_HEIGHT)
                pygame.draw.rect(fieldSurface, (WHITE), self.menu_rects[command], 0) 
                fieldSurface.blit(font.render(command, True, (255, 0, 0)), self.menu_rects[command].center)
                i = i + 25
            elif menu_orientation == 'bottomright':
                self.menu_rects[command] = pygame.rect.Rect(self.rect.bottomright[0], self.rect.topright[1] + i, MENU_RECT_WIDTH, MENU_RECT_HEIGHT)
                pygame.draw.rect(fieldSurface, (WHITE), self.menu_rects[command], 0) 
                fieldSurface.blit(font.render(command, True, (255, 0, 0)), self.menu_rects[command].center)
                i = i + 25
            elif menu_orientation == 'topleft':
                self.menu_rects[command] = pygame.rect.Rect(self.rect.topleft[0] - MENU_RECT_WIDTH, self.rect.topleft[1] + i, MENU_RECT_WIDTH, MENU_RECT_HEIGHT)
                pygame.draw.rect(fieldSurface, (WHITE), self.menu_rects[command], 0) 
                fieldSurface.blit(font.render(command, True, (255, 0, 0)), self.menu_rects[command].center)
                i = i + 25
            elif menu_orientation == 'topright':
                self.menu_rects[command] = pygame.rect.Rect(self.rect.topright[0], self.rect.topright[1] + i, MENU_RECT_WIDTH, MENU_RECT_HEIGHT)
                pygame.draw.rect(fieldSurface, (WHITE), self.menu_rects[command], 0) 
                fieldSurface.blit(font.render(command, True, (255, 0, 0)), self.menu_rects[command].center)
                i = i + 25
            r.append(self.menu_rects[command])
            
        pygame.display.update(r)

    def menu_select(self, squ, squads):
        selection = None
        while selection == None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit();
                    
                if event.type == MOUSEBUTTONDOWN:
                    x, y = event.pos
                    
                    if event.button == 3:
                        selection = None
                        return None
                    
                    for ability in self.menu_rects:
                        if self.menu_rects[ability].collidepoint((x,y)) == True:
                           #print ability
                            selection = ability
                            break
                        else:
                            pass
                    if selection == None:
                        pass
        del self.menu_rects
        pygame.display.update()

       #print selection, 'is the selection'
        fieldSurface.fill(BLACK)
       #print squads, 'squads'
        klist = squads.keys()
        keylength = len(klist)
        squads_length = list(squads)
        squads_length = len(squads_length)
        key = klist[0]
        if keylength == 1:
            
            pygame.draw.rect(fieldSurface, squads[key].color, squads[key].rect, 0)
        elif keylength > 1:
            for squa in squads:
               #print squa , 'item is...'
                pygame.draw.rect(fieldSurface, squads[squa].color, squads[squa].rect, 0)

        return ability

    def s_assessment(self):
        n = len(self.roster)
        l = self.leader
        assess = {}
        assess['ldr'] = self.leader
        assess['hp'] = l.hit_Points
        assess['hpm'] = l.hit_Points_Max
        assess['st'] = l.strength
        assess['sp'] = l.speed
        assess['ma'] = l.magic
        assess['sm'] = l.stamina
        assess['di'] = l.discipline
        assess['te'] = l.t_Evade
        assess['mr'] = l.move_Range
        if l.status.has_key('KO') == True:
            assess['KO'] = 1
        elif l.status.has_key('KO') != True:
            assess['KO'] = 0
        for member in self.roster:
            if member == self.leader:
                pass
            elif member!= self.leader:
                m = member
                assess['hp'] = assess['hp'] + m.hit_Points
                assess['hpm'] = assess['hpm'] + m.hit_Points_Max
                assess['st'] = assess['st'] + m.strength
                assess['sp'] = assess['sp'] + m.speed
                assess['ma'] = assess['ma'] + m.magic
                assess['sm'] = assess['sm'] + m.stamina
                assess['di'] = assess['di'] + m.discipline
                assess['te'] = assess['te'] + m.t_Evade
                assess['mr'] = assess['mr'] + m.move_Range
                if m.status.has_key('KO') == True:
                    assess['KO'] = assess['KO'] + 1
                elif m.status.has_key('KO') != True:
                    pass
        return assess

    def bf_assessment(self, map_grids):
        score = 0
        l = len(self.roster)
        img = []
        er = self.effect_Rect
        tlx, tly = er.topleft
        brx, bry = er.bottomright
        for grid in map_grids:
            g = grid
            gtlx, gtly = g.rect.topleft
            if gtlx in range(tlx, brx) and gtly in range(tly, bry):
                img.append(g)
            else:
                pass
            
        for member in self.roster:
            m = member
            me = m.element_type
            for gr in img:
                if me == gr.element_Type:
                    score = score + 1
                elif me == gr.element_Type - 1:
                    score = score - 1
                else:
                    pass

        a_score = score / l
        return a_acore

    def en_assessment(self, squads):
        enemies = 0
        allies = 1
        neutral = 0
        er = self.effect_Rect
        a = self.allegiance
        
        for squad in squads:
            s = squads[squad]
            sa = s.allegiance
            sr = s.rect
            p = sr.center
            if a == sa and er.collidepoint(p) == True:
                allies = allies + 1
            elif a != sa:
                if sa == 'neutral' and er.collidepoint(p) == True:
                    neutral = neutral + 1
                elif sa != 'neutral' and er.collidepoint(p) == True:
                    enemies = enemies + 1

        squad_assess = {'enemies':enemies, 'allies':allies, 'neutral':neutral}
        
        return  squad_assess
                    
    def shp_assess(self):
        self.assess = self.s_assessment()
        sa = self.assess
        if sa['hp'] == 0:
            sa['hp'] = -1
        hpp = sa['hpm']/sa['hp']
        #print sa['hpm'], sa['hp'], "sa['hpm']/sa['hp']"
        if hpp < 0:
            hpp = 0
            
        return hpp

    def priority_set(self):
        self.assess = self.s_assessment()
        hpp_r = self.shp_assess()
        priority = ''
        #print hpp_r, 'hpp assess'

        if hpp_r == 1:
            priority = 'mission' #self.mission = various missions'
        elif hpp_r == 2:
            priority = 'camp' #self.recover = various recovery methods'
        elif hpp_r > 2:
            priority = 'find town'

        return priority

    def find_closest_town(self, towns):
        closest = None
        sx, sy = self.rect.center
        tx = 0
        ty = 0
        tc = 9999
        for town in towns:
            t = towns[town]
            tx, ty = t.rect.center
            md = abs(sx - tx) + abs(sy - ty)
            if md < tc:
                closest = t
            else:
                pass

        return closest

    def find_target_squad(self, squads = None):
        if squads == None:
            return None
        elif squads != None:
            pass
        a = self.allegiance
        #enemies = {}
        #neutrals = {}
        #allies = {}
        in_range = {}
        sx, sy = self.rect.center
        sr = self.effect_Rect
        distances = {}
        for squad in squads:
            s = squads[squad]
            if s != self:
                sa = s.allegiance
                tx, ty = s.rect.center
                tr = s.rect
                if sr.colliderect(tr) == 1:
                    in_range[s.name] = s
                    #if sa == a:
                    #    allies[s.name] = s
                    #elif sa != a:
                    #    if sa == 'neutral':
                    #        neutrals[s.name] = s
                    #    else sa != 'neutral':
                    #        enemies[s.name] = s
                    distances[abs(sx - tx) + abs(sy - ty)] = s.name 
                elif sr.colliderect(tr) != 1:
                    pass
            else:
                pass
        if distances == {}:
            return None
        elif distances != {}:
            t = min(distances)
            ts = distances[t]
            #print t, 't'
            #print ts, 'ts'
            #print distances, 'distances'
            #print 
            target = in_range[ts]
            return target
    
    def behavior(self, squads, towns, map_grids = None):
        priority = self.priority_set()
        #print 'priority is ', priority
        c_target = self.find_target_squad(squads)
        c_town = self.find_closest_town(towns)
        if priority == 'mission':
            #self.goal = c_target.rect.center
            for town in towns:
                t = towns[town]
                if t.allegiance != self.allegiance and t.base == True:
                    pass
                    #self.route = [(t.rect.center)]
            self.status['in transit'] = True
        elif priority == 'camp':
            if c_target == None or c_target.allegiance == self.allegiance:
                self.status['camping'] = True
            if c_target != None:
                if c_target.allegiance != self.allegiance:
                    self.d_route = self.route
                    self.route = [(c_town.rect.center)]
                    self.status['in transit'] = True
        elif priority == 'find town':
            if c_town.occupied == True and c_town.occupant == self:
                self.status['camping'] = True
            elif c_town.occupied != True:
                self.route = [(c_town.rect.center)]
                self.status['in transit'] = True

        return self.status, self.route


class place:

    def __init__(self, name, place_Type, size, allegiance,
                 services, topleft, items = None,
                 items_cost = None, base = False):
        self.name = name
        self.place_Type = place_Type
        self.size = size
        self.allegiance = allegiance
        self.roster = create_Roster(10,self.allegiance)
        self.relationships = {}
        if self.place_Type == 'castle':
            self.image = kingdom
        elif self.place_Type == 'town':
            self.image = village
        self.base = base
       #print self.image
        self.rect = self.image.get_rect()
        self.rect.topleft = topleft
        self.topleft = topleft
        self.services = services 
        self.merchant = 'merchant'
        self.occupy = False
        self.occupant = None
        if self.allegiance == 'neutral':
            self.rect.topleft == ((randrange(0, 100), randrange(450, 450)))
            self.relationships['loyalist'] = 50
            self.relationships['rebel'] = 50
        elif self.allegiance == 'loyalist':
            self.relationships['loyalist'] = 75
            self.relationships['rebel'] = 25
        elif self.allegiance == 'rebel':
            self.relationships['loyalist'] = 25
            self.relationships['rebel'] = 75
        self.data = [self.name, self.place_Type, self.allegiance, 'services'] 
        i = 0
        
        if items == None:
            self.services.remove('merchant')
        self.items = items
        self.items_cost = items_cost

    def auto_squad(self, stage):
        #def __init__(self, members, topleft, rebel_base = None):
       #print 'in auto squad'
        towns = stage.towns
        l = 0
        leader = None
        members = []
        i = 0
        j = 0
        #print 'in auto squad'
        for member in self.roster:
            m = member
            if m.leadership > l:
                l = m.leadership
                leader = m
                ll = leader.leadership
                j = i
            else:
                pass
            i = i + 1
        #print 'leader is, ', leader
        #if i > 1 and len(members) == 0:
        members.append(self.roster.pop(j))
        ml = len(self.roster)
        if ml > 0:
            #print self.roster, 'roster in autosquad'
            meml = len(members)
            while meml < ll:# or ml > 0:
                ml = len(self.roster)
               #print ml, 'ml'
                if ml > 0:
                    m = self.roster.pop(0)
                    members.append(m)
                elif ml == 0:
                    break
                ml = len(self.roster)
                meml = len(members)
                #ml = len(self.roster)
        #print 'members', members
        enemy_base, rebel_base = base_Check(towns)
        group = squad(members, self.rect.center, rebel_base)
        #print group.rect.center, 'rect center'
        
        #squad1 = squad(group, topleft, rebel_base)
        squads[group.name] = group
        squad_rects[group.name] = group.rect
        squad_names.append(group.name)
        for member1 in group.roster:
            for member2 in group.roster:
                if member1 == member2:
                    pass
                elif member1 != member2:
                    if member1.relationships.has_key(member2) == True:
                        pass
                    elif member1.relationships.has_key(member2) == False:
                        member1.relationships[member2] = 50
                        
        group.route = [rebel_base.rect.center]
        group.route = group.path_sorter(stage)
       #print 'out of auto squad'

        return self.roster, group
            
            
        

    def menu(self, choice = None):
        i = 0
        h = 0
        self.menu_rects = {}
        menu_orientation = 'evenleft'
        if self.rect.topleft[0] < MENU_RECT_WIDTH:
            if self.rect.topleft[1] < FIELDH - MENU_RECT_WIDTH:
                menu_orientation = 'bottomright'
            elif self.rect.topleft[1] > FIELDH - MENU_RECT_WIDTH:
                menu_orientation = 'topright'
                i = -(MENU_RECT_HEIGHT)
        elif self.rect.topleft[0] > FIELDH - MENU_RECT_WIDTH:
            if self.rect.topleft[1] < FIELDH - MENU_RECT_WIDTH:
                menu_orientation = 'evenleft'
            elif self.rect.topleft[1] > FIELDH - MENU_RECT_WIDTH:
                menu_orientation = 'topleft'
                i = -(MENU_RECT_HEIGHT)
        elif MENU_RECT_WIDTH < self.rect.topleft[0] < FIELDW - MENU_RECT_WIDTH:
                if self.rect.topleft[1] < MENU_RECT_WIDTH:
                    menu_orientation = 'bottomleft'
                elif self.rect.topleft[1] > FIELDW - MENU_RECT_WIDTH:
                    menu_orientation = 'topleft'
                    i = -(MENU_RECT_HEIGHT)
       #print menu_orientation
        if menu_orientation == 'topleft':
           #print i
            i = -25 * len(self.data)
            h = int(i) 
        if choice == None:
           #print 0
            options = self.data
        elif choice == 'services':
           #print 'in services loop'
            if self.occupy == True:
                if self.occupant != None and self.occupant.allegiance == 'rebel':
                   #print 1
                    options = self.services
                elif self.occupant != None and self.occupant.allegiance == 'loyalist':
                   #print 2
                    options = []
            elif self.occupy == False and self.allegiance == 'rebel':
                if self.base == True:
                    options = self.services
                else:
                   #print 3
                    options = self.services
            elif self.occupy == False and self.allegiance == 'loyalist':
               #print 4
                options = ['create squad', 'merchant']
               #print options
        elif choice == 'merchant':
           #print 5
            options = self.items
           #print options
       #print options
        if options == None:
            pass
        elif options != None:
            key = []
            for act in options:
               #print act
               #print i, h, 'i and h'
                key.append(act)

                if menu_orientation == 'evenleft':
                    self.menu_rects[act] = pygame.rect.Rect(self.rect.topleft[0] - MENU_RECT_WIDTH, self.rect.topleft[1] + i, MENU_RECT_WIDTH, MENU_RECT_HEIGHT)
                    pygame.draw.rect(fieldSurface, (WHITE), self.menu_rects[act], 0) 
                    fieldSurface.blit(font.render(act, True, (255, 0, 0)), self.menu_rects[act].center)
                    i = i + 25

                elif menu_orientation == 'evenright':
                    self.menu_rects[act] = pygame.rect.Rect(self.rect.topright[0], self.rect.topright[1] + i, MENU_RECT_WIDTH, MENU_RECT_HEIGHT)
                    pygame.draw.rect(fieldSurface, (WHITE), self.menu_rects[act], 0) 
                    fieldSurface.blit(font.render(act, True, (255, 0, 0)), self.menu_rects[act].center)
                    i = i + 25

                elif menu_orientation == 'bottomleft':
                    self.menu_rects[act] = pygame.rect.Rect(self.rect.bottomleft[0] - MENU_RECT_WIDTH, self.rect.bottomleft[1] + i, MENU_RECT_WIDTH, MENU_RECT_HEIGHT)
                    pygame.draw.rect(fieldSurface, (WHITE), self.menu_rects[act], 0) 
                    fieldSurface.blit(font.render(act, True, (255, 0, 0)), self.menu_rects[act].center)
                    i = i + 25

                elif menu_orientation == 'bottomright':
                    self.menu_rects[act] = pygame.rect.Rect(self.rect.bottomright[0], self.rect.topright[1] + i, MENU_RECT_WIDTH, MENU_RECT_HEIGHT)
                    pygame.draw.rect(fieldSurface, (WHITE), self.menu_rects[act], 0) 
                    fieldSurface.blit(font.render(act, True, (255, 0, 0)), self.menu_rects[act].center)
                    i = i + 25

                elif menu_orientation == 'topleft':
                    self.menu_rects[act] = pygame.rect.Rect(self.rect.topleft[0] - MENU_RECT_WIDTH, self.rect.topleft[1] + i, MENU_RECT_WIDTH, MENU_RECT_HEIGHT)
                    pygame.draw.rect(fieldSurface, (WHITE), self.menu_rects[act], 0) 
                    fieldSurface.blit(font.render(act, True, (255, 0, 0)), self.menu_rects[act].center)
                    i = i + 25

                elif menu_orientation == 'topright':
                    self.menu_rects[act] = pygame.rect.Rect(self.rect.topright[0], self.rect.topright[1] + i, MENU_RECT_WIDTH, MENU_RECT_HEIGHT)
                    pygame.draw.rect(fieldSurface, (WHITE), self.menu_rects[act], 0) 
                    fieldSurface.blit(font.render(act, True, (255, 0, 0)), self.menu_rects[act].center)
                    i = i + 25

                if (self.rect.topleft[1] + i) >= FIELDH:
                   #print h, 'h'
                    h = h - MENU_RECT_HEIGHT
                    i = int(h)
                   #print i
                   #print 'its more than fieldH'
        r = []
        for act in self.menu_rects:
            a = self.menu_rects[act]
            r.append(a)
        pygame.display.update(r)
        return self.menu_rects

    def menu_select(self):
        selection = None
       #print self.menu_rects
        while selection == None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit();
                if event.type == MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if event.button == 3:
                        selection = None
                        return None
                    for data in self.menu_rects:
                        if self.menu_rects[data].collidepoint((x,y)) == True:
                           #print data
                            selection = data
                            break
                        else:
                            pass
                    if selection == None:
                        pass
                        
       #print selection, 'is the selection'
        return data

    def occupied(self, squad_list):
        occupy = False
        if len(squad_list) > 1:
            for squa in squad_list:
                if self.rect.collidepoint(squad_list[squa].rect.center) == 1:
                   #print self.name
                    self.occupy = True
                    self.occupant = squad_list[squa]
                   #print squad_list[squa]
                    occupy = True
                else:
                    pass
                
        elif len(squad_list) == 1:
            x = squad_list.keys()
            x = x[0]
            if self.rect.collidepoint(squad_list[x].rect.center) == 1:
                self.occupy = True
                self.occupant = squad_list[x]
                occupy = True

        elif len(squad_list) == 0:
        #else:
            occupy = False
            
        if occupy == False:
            self.occupy = False
            self.occupant = None

    def general_store(self, inventory, t_inventory, funds):
        surf = pygame.display.get_surface()
        surf_rect = surf.get_rect()
        self.menu('merchant')
        selection = self.menu_select()
        if selection == None:
            return funds
        
        accept = yes_or_no(surf)
        if accept == True:
            if (funds - self.items_cost[selection]) >= 0:
               #print (funds - self.items_cost[selection])
                inventory.append(self.items[selection])
                t_inventory['all'].append(self.items[selection])
                t_inventory[self.items[selection].et].append(self.items[selection])
                funds = funds - self.items_cost[selection]
               #print funds
                myes = text_box(surf, 'selection purchased', surf_rect.centerx,
                         surf_rect.centery, 10, True)
                
            elif (funds - self.items_cost[selection]) < 0:
               #print funds
                mno = text_box(surf, 'selection not purchased', surf_rect.centerx,
                         surf_rect.centery, 10, True)
        elif accept == False:
            pass
        pygame.display.update()
        return funds

    def recruit(self, total_roster, able_roster, pfunds):
        surf = pygame.display.get_surface()
        surf_rect = surf.get_rect()
        done = None
        while done != False:
            new_recruit = character_select(surf, self.roster)
           #print 1, 'first prompt'
            if new_recruit == None:
                return total_roster, able_roster, pfunds
            
            elif new_recruit != None:
                confirm_prompt = text_box(surf, 'Select this unit?',
                                          surf_rect.centerx, surf_rect.centery - 50, 10, True)
               #print 2, 'second prompt'
                confirm = yes_or_no(surf)
                del confirm_prompt
                
                if confirm == True and (pfunds - new_recruit.cost) > 0:
                    if self.occupant != None and (len(self.occupant.roster) < self.occupant.max_num_of_characters):
                       #print 'appending to occupying squad roster'
                        self.occupant.roster.append(new_recruit)
                        self.occupant.squad_update()
                        
                    else:    
                        able_roster.append(new_recruit)
                    total_roster.append(new_recruit)
                    self.roster.remove(new_recruit)
                    pfunds = pfunds - new_recruit.cost
                    
                elif confirm == False:
                    pass
                
                elif (pfunds - new_recruit.cost) < 0:
                    poor_prompt = text_box(surf, 'Not enough funds...',
                                           surf_rect.centerx, surf_rect.centery - 70, 10, True)
                elif confirm == None:
                    return total_roster, able_roster, pfunds
            done_prompt = text_box(surf, 'Want to recruit another unit?',
                                   surf_rect.centerx, surf_rect.centery - 50, 10, True)
           #print 3, 'third prompt'
            done = yes_or_no(surf)
            del done_prompt

        return total_roster, able_roster, pfunds

        
        
def yes_or_no(surface, text = None):
    menu_surface_rect = surface.get_rect()
    copy = surface.copy()
    ms_rect = menu_surface_rect
    tyes = text_box(surface, 'Yes', ms_rect.center[0], ms_rect.center[1], 10, True)
    tno = text_box(surface, 'No ', tyes.bottomleft[0], tyes.bottomleft[1], 10, True)
    tconfirm = text_box(surface, 'Confirm?', tyes.topleft[0], tyes.topleft[1] - tyes.height, 10, True)
    
    if text != None:
        text = str(text)
        optional_text_box = text_box(surface, text, ms_rect.center[0], ms_rect.center[1] - tyes.height, 10, True)
        
    pygame.display.update()
    select = None
    yes = None
    no = None
    while select == None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit();
            if event.type == MOUSEBUTTONDOWN:
                mx, my = event.pos
                yes = isPointInsideRect(mx, my, tyes)
                no = isPointInsideRect(mx, my, tno)
                if yes == True or no == True:

                    if yes == True:
                        select = True

                    if no == True:
                        select = False

                else:
                    pass
            elif event.type != MOUSEBUTTONDOWN:
                pass
    del tyes, tno, tconfirm
    if text != None:
        del optional_text_box
    surface.blit(copy, ms_rect.topleft)
    pygame.display.update()
    return select

def hit_display(hit, damage, targets = None, heal = False):
    font = pygame.font.SysFont('castellar', 20)
    surface = pygame.display.get_surface()
    menu_surface_rect = surface.get_rect()
    copy = surface.copy()
    ms_rect = menu_surface_rect
    z = targets.rect.midleft
    
    r = targets.rect
    i = 0
    if heal == False:
        color = WHITE
    elif heal == True:
        color = GREEN
    if targets == None:
        return None
    elif targets != None:
        pass
    if hit == True:
        text = str(damage)
    elif hit != True:
        text = 'Miss'
    display_box, word_box = text_box(surface, text, z[0], z[1],
                                     10, False, BLACK, True)
    if display_box.right > WINDOWW:
        display_box.right = int(WINDOWW)
    dc0 = display_box.center[0]
    dc1 = display_box.center[1]

    while (i + display_box.bottom) in range(r.top, r.bottom):
        surface.blit(copy, ms_rect.topleft)
        surface.blit(font.render(text, False, color),
                     (dc0, dc1))
        pygame.display.update()
        i -= 1
        dc1 = dc1 + i
        display_box.center = (dc0, dc1)

        time.sleep(0.1)
    font = pygame.font.SysFont('Arial', 10)
        
def line_up(roster, surface):
    h = 0
    w = 0

    for rost in roster:
        if h < MENUH:
            if w < MENUW:
                surface.blit(rost.image, (w * MENU_G_L, h * MENU_G_L))
                rost.rect = pygame.rect.Rect(w * MENU_G_L, h * MENU_G_L,
                                             100,100)
                
                w = w + 1
               #print h, w, 'h, w'
        if w * MENU_G_L >= MENUW:
            w = 0
            h = h + 1
    pygame.display.update()

def menu_bar(surface, menu_items = None):
    surf_rect = surface.get_rect()
    m_cornerx = surf_rect.centerx / 2
    m_cornery = surf_rect.centery
    if menu_items == None:
        menu_items = ['roster', 'army inventory', 'training', 'options', 'info']
    elif menu_items != None:
        pass
    i = 0
    menu_rects = {}
    select = None

    for item in menu_items:
        menu_rects[item] = pygame.rect.Rect(m_cornerx + i * 50, m_cornery, 50, 50)
        pygame.draw.rect(surface, CYAN, menu_rects[item])
        text_box(surface, item, menu_rects[item].topleft[0],
                 menu_rects[item].topleft[1])
        i = i + 1
    pygame.display.update()
    while select != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit();
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 3:
                    select = True
                    return select
                mx, my = event.pos
                for rect in menu_rects:
                    select = isPointInsideRect(mx, my, menu_rects[rect])
                    
                    if select == True:
                    
                       #print rect
                        return rect, menu_rects[rect]
                    
                    else:

                        pass
                select = True

def roster_menu():
    surf = menu_map_mode()
    menu_options = ['edit character', 'edit squad', 'create squad']
    selection = None
    while selection == None:
        selection = menu_bar(surf, menu_options)
    
    return selection

def edit_character_menu(t_roster, surface, inventory):
    char = None
    
    while char == None:
        char = character_select(surface, t_roster)
        if char == None:
            return char

   #print 'char is ' , char.name
    menu_options = ['status', 'job', 'equip', 'abilities']
    char.menu(menu_options)
    selection = char.menu_select()
    point = None
    equip_type = ['weapon', 'off_Hand', 'helmet', 'armor', 'accessory', 'inventory']

    change_eq = {'weapon':char.weapon, 'off_Hand':char.off_Hand,
                 'helmet':char.helmet, 'armor':char.armor,
                 'accessory':char.accessory, 'inventory':char.inventory }
    
    if selection == 'status':
        char.id_card(surface)
        while point == None:
            point = get_mouseclick()
    elif selection == 'equip':
        eq_rects = char.equipment_card(surface)
        #while point == None:
        point = get_mouseclick()
        if point == None:
            return None
    #while point != None:
        elif point != None:    
            for eq in equip_type:
               #print eq, eq_rects[eq]
                choice = isPointInsideRect(point[0], point[1], eq_rects[eq])
               #print choice
                if choice == True:
                   #print eq, 'this was the selection'
                   #print eq_rects, 'eq rects'
                    if eq == 'inventory':
                        eq = 'item'
                    length = tp_Inventory[eq]
                    if length >= 10:
                        choice = inventory_card(surface, tp_Inventory, eq, char)
                       #print choice#, choice.name

                        if choice != None:

                            if choice.equipment_type in char.equipment_Capable or char.equipment_Capable == {}:
                                confirm = yes_or_no(surface)
                               #print confirm, 'confirm'
                                if confirm == True and eq == choice.et:
                                   #print confirm, eq, 'confirm and eq'
                                    if eq == 'weapon':
                                        char.weapon.unequip_weapon(char, inventory)
                                        choice.equip_weapon(char, inventory)#fix here
                                       #print 'weapon equipped'
                                    elif eq == 'armor':
                                        if char.armor != None:
                                            char.armor.unequip_armor(char, inventory, eq)
                                        choice.equip_armor(char, inventory, eq)
                                        
                                    elif eq == 'helmet':
                                        if char.helmet != None:
                                            char.helmet.unequip_armor(char, inventory, eq)
                                        choice.equip_armor(char, inventory, eq)
                                        
                                    elif eq == 'item':
                                       #print eq, 'item'
                                        choice.equip_Item(char, inventory)

                                   #print confirm
                                else:
                                    text_box(surface, 'stop being silly', 300, 300, 10, True)
                                    get_mouseclick()
                                    pass
                elif choice == None:
                    pass
            else:
                pass

        else:
            eq = None
            selection = None
            pass
       #print eq, 'eq'    
   #print selection, 'selection'
    return selection

def inventory_card(surface, t_inventory, selection = None, char = None):
    surf_rect = surface.get_rect()
    card_rect = pygame.rect.Rect(surf_rect.centerx, surf_rect.centery, surf_rect.width/2, surf_rect.height/2)
    pygame.draw.rect(surface, WHITE, card_rect)
    #i = 0
    j = 0
    i = 0
    inv_rects = {}
   #print t_inventory
    #if len(t_inventory) == 1:
    #    t_inventory = list(t_inventory)
   #print t_inventory
    if selection == 'inventory':
        selection = 'item'
    if selection == None:
        selection = 'all'
    length = len(t_inventory[selection])
    if length > card_rect.height / 30 :
        choice = None
        while choice == None:
            j = 0
            z = i + 8
            inv_rects = {}
            if z >= length:
                i = length - 8
                z = length 
            if i < 0:
                i = 0
                z = i + 8
            inv_rects['up'] = pygame.rect.Rect(card_rect.topleft[0],
                                               card_rect.topleft[1] ,
                                               card_rect.width,
                                               card_rect.height/10 )
            pygame.draw.rect(surface, WHITE, inv_rects['up'])
            pygame.draw.rect(surface, BLACK, inv_rects['up'], 1)
            surface.blit(font.render('up', True, BLACK), (inv_rects['up'].centerx/6 + inv_rects['up'].width, inv_rects['up'].centery))
            inv_rects['down'] = pygame.rect.Rect(card_rect.topleft[0],
                                                 card_rect.bottomleft[1] - card_rect.height/10,
                                                 card_rect.width,
                                                 card_rect.height/10 )
            pygame.draw.rect(surface, WHITE, inv_rects['down'])
            pygame.draw.rect(surface, BLACK, inv_rects['down'], 1)
            surface.blit(font.render('down', True, BLACK), (inv_rects['down'].centerx/6 + inv_rects['down'].width, inv_rects['down'].centery))
            j = j + (card_rect.height / 10)
           #print i, z, length, 'i', 'z', 'length'
            for article in t_inventory[selection][i : z]:
               #print article.name
                inv_rects[article] = pygame.rect.Rect(card_rect.topleft[0],
                                                      card_rect.topleft[1] + j,
                                                      card_rect.width,
                                                      card_rect.height/10 )
                pygame.draw.rect(surface, WHITE, inv_rects[article])
                pygame.draw.rect(surface, BLACK, inv_rects[article], 1)
                surface.blit(font.render(article.name, True, BLACK),
                             (inv_rects[article].centerx/6 + inv_rects[article].width,
                              inv_rects[article].centery))
                j = j + (card_rect.height / 10)
            list_rects = inv_rects.values()
            list_rects.append(card_rect)
            pygame.display.update(list_rects )
            point = get_mouseclick()
            if point == None:
                choice = None
                break
            #choice = None
            #while choice = None
            up = isPointInsideRect(point[0], point[1], inv_rects['up'])
            down = isPointInsideRect(point[0], point[1], inv_rects['down'])
            if up == True:
                i = i - 1
                if i < 0:
                    i = 0
               #print i
            elif up != True:
                if down == True:
                    i = i + 1
                    if i > length - 8:
                        i = length - 8
                   #print i
            if up != True and down != True:
                for article in inv_rects:
                    choice = isPointInsideRect(point[0], point[1], inv_rects[article])
                    if choice == True:
                        return article
                    elif choice == None:
                        pass
            if up == True or down == True:
               #print up, 'up', down, 'down'
                pass
    elif length < card_rect.height / 30 :
        choice = None
       #print selection, t_inventory[selection], 'inv card inventory displayed'
        if selection in t_inventory and selection != None:
            while choice == None:
                for article in t_inventory[selection]:
                    
                    inv_rects[article] = pygame.rect.Rect(card_rect.topleft[0],
                                                          card_rect.topleft[1] + j,
                                                          card_rect.width,
                                                          card_rect.height/10 )
                    pygame.draw.rect(surface, WHITE, inv_rects[article])
                    pygame.draw.rect(surface, BLACK, inv_rects[article], 1)
                    #surface.blit(font.render(article.name, True, BLACK), (inv_rects[article].centerx/6 + inv_rects[article].width, inv_rects[article].centery))
                    if article != None:
                        surface.blit(font.render(article.name, True, BLACK), (inv_rects[article].centerx/6 + inv_rects[article].width, inv_rects[article].centery))
                    elif article == None:
                        surface.blit(font.render('None', True, BLACK), (inv_rects[article].centerx/6 + inv_rects[article].width, inv_rects[article].centery))
                    #i = i + 1
                    j = j + (card_rect.height / 10)
                pygame.display.update()
                point = get_mouseclick()
                if point == None:
                    choice = None
                    break
                for article in inv_rects:
                    choice = isPointInsideRect(point[0], point[1], inv_rects[article])
                    if choice == True:
                        return article
                    elif choice == None:
                        pass
                
    pygame.display.update()
    return choice

def scroll_menu(surface, x, y, width, height, home_list, specific_list_name, char = None, rect_height = 30):
    #print 'in scroll menu'
    surf_rect = surface.get_rect()
    card_rect = pygame.rect.Rect(x, y, width, height) #where to display menu
    #print card_rect, 'card rect'
    
    pygame.draw.rect(surface, WHITE, card_rect)
    
    rects_display = card_rect.height/rect_height    
    #print rects_display, 'rects display'
    #i = 0
    j = 0
    i = 0
    choice = None
    
    inv_rects = {} #rects to print to get mouseclick selection of item
    if specific_list_name == 'inventory': #in case selection from game screen doesn't match up with options selected
        specific_list_name = 'item'
    if specific_list_name == None:
        specific_list_name = 'all'
    length = len(home_list[specific_list_name]) #length of list to figure out what range to use for displaying rects
    if length > rects_display : # decides if we need a scrolling menu at all
        display_area = height - (2 * rect_height)
        rects_display = display_area / rect_height
        #print display_area, rects_display, 'display area and rects_dispplay'
        while choice == None:
            j = 0
            z = i + rects_display 
            inv_rects = {}
            if z >= length:
                i = length - rects_display
                z = length 
            if i < 0:
                i = 0
                z = i + rects_display
            inv_rects['up'] = pygame.rect.Rect(card_rect.topleft[0],
                                               card_rect.topleft[1] ,
                                               card_rect.width,
                                               card_rect.height/rects_display )
            pygame.draw.rect(surface, WHITE, inv_rects['up'])
            pygame.draw.rect(surface, BLACK, inv_rects['up'], 1)
            surface.blit(font.render('up', True, BLACK), (inv_rects['up'].topleft[0], #/6 + inv_rects['up'].width,
                                                          inv_rects['up'].topleft[1]))
            inv_rects['down'] = pygame.rect.Rect(card_rect.topleft[0],
                                                 card_rect.bottomleft[1] - card_rect.height/rects_display,
                                                 card_rect.width,
                                                 card_rect.height/rects_display )
            #print inv_rects['down'], 'inventory rect', 'down', inv_rects['down'].top, inv_rects['down'].left
            pygame.draw.rect(surface, WHITE, inv_rects['down'])
            pygame.draw.rect(surface, BLACK, inv_rects['down'], 1)
            surface.blit(font.render('down', True, BLACK), (inv_rects['down'].topleft[0], #/6 + inv_rects['down'].width,
                                                            inv_rects['down'].topleft[1]))
            j = j + rect_height
            #print i, z, length, 'i', 'z', 'length'
            for article in home_list[specific_list_name][i : z]:
                #print article.name
                inv_rects[article] = pygame.rect.Rect(card_rect.topleft[0],
                                                      card_rect.topleft[1] + j,
                                                      card_rect.width,
                                                      rect_height)
                                                      #card_rect.height/rect_height )
                #print inv_rects[article], 'inventory rect', article.name, inv_rects[article].top, inv_rects[article].left
                collisionDown = inv_rects[article].colliderect(inv_rects['down'])
                #print collisionDown, inv_rects[article], inv_rects['down']
                if collisionDown != 1:
                    pygame.draw.rect(surface, WHITE, inv_rects[article])
                    pygame.draw.rect(surface, BLACK, inv_rects[article], 1)
                    surface.blit(font.render(article.name, True, BLACK),
                                 (inv_rects[article].topleft[0] ,
                                  inv_rects[article].topleft[1]))
                    j = j + rect_height
                elif collisionDown == 1:
                    pass
            list_rects = inv_rects.values()
            list_rects.append(card_rect)
            pygame.display.update( )
            point = get_mouseclick()
            if point == None:
                choice = None
                break
            #choice = None
            #while choice = None
            up = isPointInsideRect(point[0], point[1], inv_rects['up'])
            down = isPointInsideRect(point[0], point[1], inv_rects['down'])
            if up == True:
                i = i - 1
                if i < 0:
                    i = 0
                #print i, z , 'i and z'
            elif up != True:
                if down == True:
                    i = i + 1
                    if i > length - rects_display:
                        i = length - rects_display
                    #print i, z , 'i and z'
            if up != True and down != True:
                for article in inv_rects:
                    choice = isPointInsideRect(point[0], point[1], inv_rects[article])
                    if choice == True:
                       #print article.name
                        return article
                    elif choice == None:
                        pass
            if up == True or down == True:
                #print up, 'up', down, 'down'
                pass
    elif length < card_rect.height / rect_height : # if we don't need a scrolling menu
        #choice = None
        #print specific_list_name, home_list[specific_list_name], 'inv card inventory displayed'
        if specific_list_name in home_list and specific_list_name != None:
            while choice == None:
                for article in home_list[specific_list_name]: # t_inventory[selection]:
                    inv_rects[article] = pygame.rect.Rect(card_rect.topleft[0],
                                                          card_rect.topleft[1] + j,
                                                          card_rect.width,
                                                          card_rect.height/rects_display )
#                    print inv_rects[article], 'inventory rect', article.name, inv_rects[article].top, inv_rects[article].left
                    pygame.draw.rect(surface, WHITE, inv_rects[article])
                    pygame.draw.rect(surface, BLACK, inv_rects[article], 1)
                    if article != None:
                        surface.blit(font.render(article.name, True, BLACK),
                                     (inv_rects[article].topleft[0],#/6 + inv_rects[article].width,
                                      inv_rects[article].topleft[1]))
                    elif article == None:
                        surface.blit(font.render('None', True, BLACK),
                                     (inv_rects[article].centerx,#/6 + inv_rects[article].width,
                                      inv_rects[article].centery))
                    #i = i + 1
                    j = j + (card_rect.height / rects_display)
                pygame.display.update()
                point = get_mouseclick()
                if point == None:
                    choice = None
                    break
                for article in inv_rects:
                    choice = isPointInsideRect(point[0], point[1], inv_rects[article])
                    if choice == True:
                        return article
                    elif choice == None:
                        pass
     
    pygame.display.update()
    
    return choice


def edit_squad_menu(surface):
    menu_options = ['change leader', 'add unit', 'remove unit', 'field abilities']
    selection = menu_bar(surface, menu_options)
    return selection
            
def text_box(surface, text, posx, posy, margin = 10, fill = False, color = BLACK, move = False):
    #print text
    length_box = len(text) * 10
    t_box_rect = pygame.rect.Rect(posx, posy, length_box + margin, 25 + 25 * (int(len(text) / 50)))
    #t_box = pygame.draw.rect(surface, BLACK, t_box_rect, 1)
    if fill == True:
        t_box = pygame.draw.rect(surface, WHITE, t_box_rect, 0)
    else:
        pass
    x = surface.blit(font.render(text, True, color), (t_box_rect.topleft[0] + margin , t_box_rect.topleft[1]))
    #surface.blit(font.render(text, True, BLACK), (t_box_rect.center[0] - (length_box / 4), t_box_rect.center[1]))
    if move == True:
        return t_box_rect, x 
    elif move == False:
        return t_box_rect

def character_select(surface, t_roster):
    selection = None
   #print 'click a character'
    while selection == None:
        surface.fill(WHITE)
        line_up(t_roster, surface)
        point = get_mouseclick()
        if point == None:
           #print 'no character selected'
            break
        else:
            pass
       #print point
        mx = point[0]
        my = point[1]
        for rost in t_roster:
           #print rost.name, rost.rect.topleft
            select = isPointInsideRect(mx, my, rost.rect)
            if select == True:
               #print 'roster char is selected'
               #print rost.name
                rost.id_card(surface)
                confirm = yes_or_no(surface)
                if confirm == True:
                    return rost
                elif confirm != True:
                    selection == None
            elif select != True:
                pass
   #print 'character clicked'
    

def get_mouseclick():
    point = None
    while point == None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit();
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 3:
                    point = None
                    return point
                mx, my = event.pos
                point = (mx, my)
                return point
            else:
                pass

def type_check(item1, item2):
    it1 = type(item1)
    it2 = type(item2)
    if it1 == it2:
        return True
    elif it1 != it2:
        return False

    
def rect_checker(point, rects, d = {}):
   #print rects
    if rects == None:
        return False, False
    rt = type_check(d, rects)
    select = False
    selection = None
    if rt == True:
        pass
    elif rt != True:
        return None
    
    for rec in rects:
       #print rec, rects, 'rec and rects'
        r = rects[rec]
        rc = r.rect.collidepoint(point)
        if rc == 1:
           #print r, point, 'r and point'
            selection = rects[rec]
            select = True
            return select, selection
        elif rc != 1:
            pass
    #print select, d
    return select, selection

def get_input():
    ginput = None
    while ginput == None:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 3:
                    return ginput
                elif event.button != 3:
                    point = event.pos
                    return point
            if event.type == KEYDOWN:
                if event.key == K_m:
                    point = (-1,-1)
                    return point
                elif event.key != K_m:
                    pass
            else:
                pass
    
def get_rmouseclick():
    point = None
    while point == None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit();
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 3:
                    #mx, my = event.pos
                    #point = (mx, my)
                    cancel = True
                    return cancel
            else:
                pass


def refresh_squad_select(surface, potential_squad, available_members):
    px = available_members
    gx = potential_squad
    gx_length = len(gx)
    i, j = 0, 0
    x, y = 0, 4
    surface_rect = surface.get_rect()
    s = surface_rect
    surface.fill(WHITE)
    pygame.draw.line(surface, BLACK, (0, 399), (s.width, 399))
    pygame.draw.line(surface, BLACK, (int(s.width/2), 399),
                     (int(s.width/2), s.height))
    for member in px:
        surface.blit(member.image, (i * MENU_G_L, j * MENU_G_L))
        #player.rect.topleft = (randrange(0, 600, 100), randrange(400,600, 100))
        member.rect.topleft = (i * MENU_G_L, j * MENU_G_L)
        i = i + 1
        if i * MENU_G_L >= 600:
            i = 0
            j = j + 1
    if gx_length == 1:
        surface.blit(gx[0].image, (x * MENU_G_L, y * MENU_G_L))
        #player.rect.topleft = (randrange(0, 600, 100), randrange(400,600, 100))
        gx[0].rect.topleft = (x * MENU_G_L, y * MENU_G_L)
        x = x + 1
        if x * MENU_G_L >= 300:
            x = 0
            y = y + 1
    elif gx_length > 1:
        for member in gx:
            surface.blit(member.image, (x * MENU_G_L, y * MENU_G_L))
            #player.rect.topleft = (randrange(0, 600, 100), randrange(400,600, 100))
            member.rect.topleft = (x * MENU_G_L, y * MENU_G_L)
            x = x + 1
            if x * MENU_G_L >= 300:
                x = 0
                y = y + 1
    elif gx_length < 1:
        pass

    pygame.display.update()
    
def create_Roster(number, side):
    x = 0
    total_roster = []
    y = None
    for x in range(number):
        y = character(2, side)
        total_roster.append(y)
        x = x + 1
    return total_roster

def recruit(town_roster, able_roster):
    surf = menu_map_mode()
    new_recruit = character_select(surf, town_roster)
    able_roster.append(new_recruit)
    town_roster.remove(new_recruit)
    
def create_Squad(able_roster, topleft, rebel_base = None):
    #print 'which characters would you like on your squad'
    group = []
    names = []
    datas = []
    troster = list(able_roster)
    i = 0
    j = []
    complete = False
    leader = None
    #fieldSurface.fill(BLACK)
    pygame.display.update()
    menu = menu_map_mode()
    manpower = 2
    more = None
    #x = raw_input('whats happening? menu mode?')
    h = 0
    l = 0
    w = 0
    for rost in able_roster:
        if h < MENUH:
            if w < MENUW:
                menu.blit(rost.image, (w * MENU_G_L, h * MENU_G_L))
                #player.rect.topleft = (randrange(0, 600, 100), randrange(400,600, 100))
                rost.rect.topleft = (w * MENU_G_L, h * MENU_G_L)
                #print rost.rect.topleft
                #print rost.data
                names.append(rost.name)
                datas.append(rost.data)
                w = w + 1
                #print h, w, 'h, w'
        if w * MENU_G_L >= MENUW:
            w = 0
            h = h + 1
    pygame.draw.line(menu, BLACK, (0,400), (600, 400))
    pygame.display.update()
    squad_total = 0
    new_mouse_motion = False
    nmm = bool(new_mouse_motion)
    initial = True
    char1 = None
    char2 = None
    print_on = False
    print_data = {}
    #t1 = 0
    #t2 = 4
    while squad_total >= 0 and squad_total < manpower:
        #refresh_squad_select(menu, group, troster)
        points = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit();
        #more = raw_input('would you like to add members to the group? ')
            #pygame.draw.line(menu, BLACK, (0,400), (600, 400))
            #pygame.display.update()
            #t1 = 0
            #t2 = 4
            if event.type == MOUSEMOTION:
                mmx1, mmy1 = event.pos
                #print mmx1, mmy1 , 'mmx1 and y'
                difference = False
                nx1 = int(mmx1 / MENU_G_L) * MENU_G_L
                ny1 = int(mmy1 / MENU_G_L) * MENU_G_L
                if initial == True:
                    for rost in troster:
                        hover1 = isPointInsideRect(mmx1, mmy1,
                                                   rost.rect)
                        if hover1 == True:
                            initial = False
                            refresh_squad_select(menu, group, troster)
                            #print rost.data
                            rost.id_card(menu)
                            print_data[rost] = True
                            char = rost
                            #print char.name
                        else:
                            pass
                else:
                    test = isPointInsideRect(mmx1, mmy1,
                                             char.rect)
                    if test == True:
                        pass
                    elif test == False:
                        #del print_data[char]
                        print_data = {}
                        #print char.name
                        for rost in troster:
                    #print rost.rect.center, rost.name
                            hover2 = isPointInsideRect(mmx1, mmy1,
                                                       rost.rect)
                            if hover2 == True:
                                if rost in print_data:
                                    pass
                                elif rost not in print_data:
                                    #print rost.data
                                    refresh_squad_select(menu, group, troster)
                                    rost.id_card(menu)
                                    print_data[rost] = True
                                    char = rost
                                    #print char.name
                            else:
                                pass

                            
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 3:
                    point = None
                    if squad_total == 0:
                        return able_roster
                else:
                    mx, my = event.pos
                    point = (mx, my)
                #print point
                #selection = isPointInsideRect(mx, my, rost.rect)
                #if squad_total == 0 and point = None:
                #    return None
               #print 'mouseclick'
                for rost in troster:
                   #print rost.name
                    #print rost.name
                    #selection = rost.rect.collidepoint(point)
                    selection = isPointInsideRect(mx, my, rost.rect)
                    #print selection
                    if selection == True:
                       #print 'in character selection loop'
                        #print rost.name, 'selected'
                        
                        #menu.blit(rost.image, (t1 * MENU_G_L, t2 * MENU_G_L))
                        #rost.rect.topleft = (t1 * MENU_G_L, t2 * MENU_G_L)
                       #print h, 'the value of h'
                        if l == 0:
                           #print 'in leader loop, h = 0'
                            leader = rost
                           #print leader, 'leader selection'
                            manpower = rost.leadership
                            l = l + 1
                       #print 'out of leader loop'
                        group.append(rost)
                        j.append(i)
                        troster.remove(rost)
                        
                        #names.remove(rost.name)
                        i = i + 1
                        refresh_squad_select(menu, group, troster)
                        #line_up(troster,menu)
                        #t1 = t1 + 1
                        squad_total = squad_total + 1
                        if squad_total < manpower:
                            more = yes_or_no(menu, 'more')
                        elif squad_total == manpower:
                            more = False
                       #print 'more', more
                        if more == True:
                            pass
                        elif more != True:
                           #print 'squad total', squad_total
                            squad_total = manpower
                           #print 'squad total', squad_total

                    if squad_total == manpower:
                        selection = yes_or_no(menu, 'Is this squad ok')
                        if selection == True:
                            squad_total = manpower + 1
                            able_roster = troster
                           #print leader, 'leader is, squad confirmation loop'
                            leader.leader = True
                        elif selection == False:
                            squad_total = 0
                            l = 0
                            leader = None
                            manpower = 2
                            troster = list(able_roster)
                            group = []
                            refresh_squad_select(menu, group, troster)

   #print 'out of selection while loop'                                
    squad1 = squad(group, topleft, rebel_base)
    squads[squad1.name] = squad1
    squad_rects[squad1.name] = squad1.rect
    squad_names.append(squad1.name)
    for member in squad1.roster:
        for member2 in squad1.roster:
            if member == member2:
                pass
            elif member != member2:
                if member.relationships.has_key(member2) == True:
                    pass
                elif member.relationships.has_key(member2) == False:
                    member.relationships[member2] = 50

    return able_roster

def isPointInsideRect(x, y, rect):
    #print 'overlap detection'
    if (x > rect.left) and (x  < rect.right) and (y >rect.top) and (y < rect.bottom):
        return True
    else:
        return False
            
def doRectsOverlap(rect1, rect2):
    #print 'do they overlap'
    #print rect1.topleft, rect2.topleft
    for a, b in [(rect1, rect2), (rect2, rect1)]:
                #check if a's corners are inside b
        if ((isPointInsideRect(a.left, a.top, b)) or
            (isPointInsideRect(a.left, a.bottom, b)) or
            (isPointInsideRect(a.right, a.top, b)) or
            (isPointInsideRect(a.right, a.bottom, b))):
            return True    
#images
sample_Sprites_File_Path = ['C:\Python27\python test folder and drafts\graphic files\ogre fantasy\sample sprites\DarkKnight1F-S.gif',
                            'C:\Python27\python test folder and drafts\graphic files\ogre fantasy\sample sprites\DarkKnight1M-S.gif',
                            'C:\Python27\python test folder and drafts\graphic files\ogre fantasy\sample sprites\OnionKnight1F-S.gif',
                            'C:\Python27\python test folder and drafts\graphic files\ogre fantasy\sample sprites\OnionKnight1M-S.gif',
                            'C:\Python27\python test folder and drafts\graphic files\ogre fantasy\sample sprites\DarkKnight1F-rebel.bmp',
                            'C:\Python27\python test folder and drafts\graphic files\ogre fantasy\sample sprites\DarkKnight1M-rebel.bmp',
                            'C:\Python27\python test folder and drafts\graphic files\ogre fantasy\sample sprites\OnionKnight1F-rebel.bmp',
                            'C:\Python27\python test folder and drafts\graphic files\ogre fantasy\sample sprites\OnionKnight1M-rebel.bmp',
                            'C:\Python27\python test folder and drafts\graphic files\ogre fantasy\sample sprites\K.O. status.bmp']

places = {'castle':'C:\Python27\python test folder and drafts\graphic files\ogre fantasy\sample sprites\castle.bmp',
          'town':r'C:\Python27\python test folder and drafts\graphic files\ogre fantasy\sample sprites\town.bmp'}

kingdom = pygame.image.load(places['castle'])
village = pygame.image.load(places['town'])
dark_KnightLM = pygame.image.load(sample_Sprites_File_Path[1])
dark_KnightLF = pygame.image.load(sample_Sprites_File_Path[0])
onion_KnightLM = pygame.image.load(sample_Sprites_File_Path[3])
onion_KnightLF = pygame.image.load(sample_Sprites_File_Path[2])
dark_KnightRM = pygame.image.load(sample_Sprites_File_Path[5])
dark_KnightRF = pygame.image.load(sample_Sprites_File_Path[4])
onion_KnightRM = pygame.image.load(sample_Sprites_File_Path[7])
onion_KnightRF = pygame.image.load(sample_Sprites_File_Path[6])
ko_Status = pygame.image.load(sample_Sprites_File_Path[8])
ch_Images = [dark_KnightLM, dark_KnightLF, onion_KnightLM, onion_KnightLF, dark_KnightRM, dark_KnightRF, onion_KnightRM, onion_KnightRF, ko_Status ]

#draw a grid on surface
def draw_gridlines(surface, color, window_width, window_height, columns, rows, THICK):
    x = 0
    y = 0
    i = 0
    grid_height = window_height/columns
    grid_width = window_width/rows
    #windowSurface.fill(WHITE)
    #windowSurface.unlock()
    for x in range(0, columns +1 ):
        linex = pygame.draw.line(surface, color, (grid_width * x, 0), (grid_width * x, WINDOWH), THICK)
        x = x + 1
        for y in range(0, rows +1):
            liney = pygame.draw.line(surface, color, (0, grid_height * y), (WINDOWW, grid_height* y), THICK)
            y = y + 1
            del liney
        del linex
    pygame.display.update()
    #windowSurface.lock()
    
    
#lconvert pixels to grid coordinates, hopefully
def pixel_to_grid_mouse_converter(grid_width, grid_height):
    if event.type == MOUSEBUTTONDOWN:
        mousex, mousey = event.pos
        gridx = (mousex/grid_width)+ 1
        gridy = (mousey/grid_height) + 1
        #print grid_width, grid_height
        #print mousex, gridx
        #print mousey, gridy
    return gridx, gridy

def current_grid_coordinates(cx_grid, cy_grid, grid_width, grid_height):
    Current_X = (cx_grid/grid_width)+1
    Current_Y = (cy_grid/grid_height)+1
    return Current_X, Current_Y

def target_grid_coordinates(tx_grid, ty_grid, grid_width, grid_height):
    Target_X = (tx_grid/grid_width) + 1
    Target_Y = (ty_grid/grid_width) + 1
    return Target_X, Target_Y

#return grid_positions, grid_objects, grid_obstacles, all list
class battle_map:

    def __init__(self, level_map, surface):
        self.e_dict = {'b': [7, BLACK, True], 'n':[7, GRAY, None],
                  'i': [2, WHITE, None], 'r':[3, RED, None],
                  'g': [4, GREEN, None], 'b':[5, BLUE, None],
                  'v': [1, PURPLE, None], 'c':[6, CYAN, None],
                  'N':[7, DGRAY, True ], 'I':[2, DWHITE, True],
                  'R':[3, DRED, True], 'G':[4, DGREEN, True],
                  'B':[5, DBLUE, True], 'V':[1, DPURPLE, True],
                  'C':[6, DCYAN, True]}

        #null- roads, towns; infinity ?, fire- mountains; earth - plains, forest; water - rivers, oceans, streams; void- swamps, caves; sky - snow lands, glaciers
        k = self.e_dict.keys()
        i = 0
        j = 0
        self.grid_objects = []
        #self.surface = surface
        grid_position = {}
        self.gp_dict = {}
        self.grid_positions = []
        self.grid_obstacles = []
        with open(level_map, 'r') as g:
            grid_data = g.read()
           #print grid_data

        for element in grid_data:
            if element in k:
                grid_position[i,j] = self.e_dict[element]
               #print element, i, j, grid_position[i, j]
                etype = grid_position[i,j][0]
                color = grid_position[i,j][1]
                obst = grid_position[i,j][2]
                grid = map_element_grid(True, i, j, etype, color, obst)
                pygame.draw.rect(surface, grid.color, grid.rectangle, 0)
                self.gp_dict[(i,j)] = grid
                self.grid_objects.append(grid)
                self.grid_positions.append(grid.current)
                i = i + 1
                if obst == True:
                    self.grid_obstacles.append(grid.current)
                if i == COLUMNS:
                    i = 0
                    j = j + 1
                
        #pygame.display.update()
                    
                    
class map_element_grid:

    _ids = count(0) 
    
    def __init__(self, ordered = None, xid = 0, yid = 0, element_type = None,
                 color = None, obstacle = None):
        self.list_element_type = {1:"void", 2:"infinity", 3:"fire", 4:"earth", 5:"water", 6:"sky", 7:"null"}
        self.element_color = {1:PURPLE, 2:WHITE, 3:RED, 4:GREEN, 5:BLUE, 6:CYAN, 7:GRAY}
        self.delement_color = {1:DPURPLE, 2:DWHITE, 3:DRED, 4:DGREEN, 5:DBLUE, 6:DCYAN, 7:DGRAY}
        
        if ordered == None:
            self.id = self._ids.next()
            self.position = []
            self.yid = int(self.id / 6)
            self.xid = self.id % 6
            self.current = (self.xid, self.yid)
            self.position.append(self.current)
            self.element_type, self.element = self.random_element_type()
            self.obstacle = self.grid_obstacle()
            if self.obstacle == True:    
                self.color = self.delement_color[self.element_type]
            elif self.obstacle == False:
                self.color = self.element_color[self.element_type]
            self.rectangle = pygame.rect.Rect(self.xid * GRID_WIDTH, self.yid * GRID_HEIGHT, GRID_WIDTH, GRID_HEIGHT)

        elif ordered != None:
            self.id = self._ids.next()
            self.position = []
            self.yid = yid
            self.xid = xid
            self.current = (self.xid, self.yid)
            self.position.append(self.current)
            self.element_type = element_type
            self.obstacle = obstacle
            self.element = self.list_element_type[self.element_type]
            if self.obstacle == True:
                self.color = self.delement_color[self.element_type]
            elif self.obstacle == False:
                self.color = self.element_color[self.element_type]
            self.color = color
            self.rectangle = pygame.rect.Rect(self.xid * GRID_WIDTH, self.yid * GRID_HEIGHT, GRID_WIDTH, GRID_HEIGHT)
            self.obstacle = obstacle

    def grid_obstacle(self):
        x = randrange(0, 101)
        if x > 80:
            self.obstacle = True
            self.color = BLACK
            self.element = "null"
            self.element_type = 7
        elif x <= 80:
            self.obstacle = False
        return self.obstacle
    
    def create_grid_element(self):#, xid, yid, GRID_WIDTH, GRID_HEIGHT):
        #grid_element = map_element_grid()
        rectangle = pygame.rect.Rect(self.xid * GRID_WIDTH, self.yid * GRID_HEIGHT, GRID_WIDTH, GRID_HEIGHT)
        element = [self.element_type, self.element_color]
        return rectangle, element

    def random_element_type(self):
    #character_name, element_type, attack, defense, sp_defense, sp_attack, move, att_range, potential
        element_type = {1:"void", 2:"infinity", 3:"fire", 4:"earth", 5:"water", 6:"sky", 7:"null"}
        r = randrange(1,8)
        r_element_type = r
        element = element_type[r]
        return r_element_type, element

#maybe include armor evade for robes? to make evasion tanks?
# for equipment, equipment_effects will be a list of strength, magic, speed,
#brave, faith, w_Evade, move_Range
#maybe have a weapon shifter? a job that can change their weapon, with a list
#of weapons as their actions? i should also include some sort of stagger
#stagger ability...



class weapon(object):
    def __init__ (self, name, points, equipment_type, strength, magic, speed, brave, faith, w_Evade, move_Range, equipment_effects, act = None ):
        self.name = name
        self.equipment_type = equipment_type
        self.strength = strength
        self.magic = magic
        self.speed = speed
        self.brave = brave
        self.faith = faith
        self.w_Evade = w_Evade
        self.move_Range = move_Range
        self.equipment_effects = [self.strength, self.magic, self.speed, self.brave, self.w_Evade, self.move_Range]
        self.status_effects = {}
        self.image = ""
        self.act = act
        if self.equipment_type == 'sword':
            self.att_Range = 1
            self.weapon_power = points
        elif self.equipment_type == 'spear':
            self.att_Range = 2
            self.weapon_power = points
        elif self.equipment_type == 'axe':
            self.att_Range = 1 #figure out how to make a circle for a range
            self.weapon_power = points
        elif self.equipment_type == 'bow':
            self.att_Range = 6
            self.weapon_power = points
        elif self.equipment_type == 'knife':
            self.att_Range = 1
            self.weapon_power = points
        elif self.equipment_type == 'wand':
            self.att_Range = 3
            self.weapon_power = points
        elif self.equipment_type == 'shield':
            self.att_Range = 1
            self.s_Evade = points
        elif self.equipment_type == 'knuckles':
            self.att_Range = 1
            self.weapon_power = points
        self.et = 'weapon'

    def equip_weapon(self, user, t_inventory):#, initial = False):
        user.weapon = self
        user.equipment[0] = self
        user.att_Range = self.att_Range
        t_inventory[self.et].remove(self)
        t_inventory['all'].remove(self)
        if self.act != None:
            self.act.equip_action(user)
        elif self.act == None:
            pass

        if self.equipment_type != 'shield':
            user.abilities['weapon attack'] = True
            weapon_attack = actions('weapon attack', 1, 0, {7:'null'}, 'physical', None, None, 0, user.att_Range, None, 0, None, 100, 1, False, '-')
            user.actions['weapon_attack'] = weapon_attack
            user.actions_CD['physical']['weapon_attack'] = weapon_attack
            

            if self.equipment_type == 'spear':
                #thrust =  actions('thrust', 1, 5, {7:"null"}, 'physical', None, 'stagger', 0, 2, None, 0, 'line', 75, 2, True, '-')
                user.abilities['thrust'] = True
                user.actions['thrust'] = thrust

            if self.equipment_type == 'knife':
                #backstab = actions('backstab', 1, int(user.hit_Points_Max * 0.10),{7:"null"}, 'status', None, 'KO',  0, 1, None, 0, None, 35, 0, False, '-')
                user.abilities['backstab'] = True
                user.actions['backstab'] = backstab

            if self.equipment_type == 'sword':
                #riposte = actions('riposte', 1, 1, {7:"null"}, 'status', None, 'riposte', 0, 0, None, 0, None, 100, 1.2, None, '+')
                user.abilities['riposte'] = True
                user.actions['riposte'] = riposte

            if self.equipment_type == 'knuckles':
                user.abilities['restrain'] = True

            if self.equipment_type == 'axe':
                #split = actions('split', 1, int(user.hit_Points_Max * 0.15), {7:"null"}, 'physical', None, 'stagger', 0, 1, None, 0, None, 65, 2, True, '-')
                user.abilities['split'] = True
                user.actions['split'] = split
                #cyclone =  actions('cyclone', 1, int(user.hit_Points_Max * 0.05), {7:"null"}, 'physical', None, 'stagger', 0, 3, 'square area', 0, 'square', 80, 0.75, True, '-')
                user.abilities['cyclone'] = True
                user.actions['cyclone'] = cyclone

            if self.equipment_type == 'wand':
                #kadabra = actions('kadabra', 1, 10, {7:"null"}, 'physical', None, None, 0, 3, None, 1, None, 75, 1, False, '-')
                user.abilities['kadabra'] = True
                user.actions['kadabra'] = kadabra

            if self.equipment_type == 'bow':
                #charge = actions('charge', 1, int(user.hit_Points_Max * 0.05), {7:"null"}, 'physical', None, None, 20, 6, None, 0,None, 100, 1.3, False, '-')
                user.abilities['charge'] = True
                user.actions['charge'] = charge
                
        else:
            user.abilities['cover'] = user.weapon.cover
            #guard = actions('guard', 1, 1, {7:"null"}, 'status', None, 'guard', 0, 0, None, 0, None, 100, 1, None, '+')
            user.actions['guard'] = guard
            user.s_Evade = user.s_Evade + self.s_Evade
            user.t_Evade = user.t_Evade
           #print 'user s Evade ',user.s_Evade, 'self s Evade', self.s_Evade
            
        if self.equipment_effects != []:
            user.strength = user.strength + self.strength
            user.magic = user.magic + self.magic
            user.speed = user.speed + self.speed
            user.brave = user.brave + self.brave
            user.faith = user.faith + self.faith
            user.w_Evade = self.w_Evade
            user.move_Range = user.move_Range + self.move_Range

        i = 0

    def unequip_weapon(self, user, t_inventory):

        user.att_Range = 1
        if self.equipment_type != 'shield':
            del user.abilities['weapon attack'] 
            del user.actions['weapon_attack'] 

            if self.equipment_type == 'spear':
                del user.abilities['thrust'] 
                del user.actions['thrust'] 

            if self.equipment_type == 'knife':
                del user.abilities['backstab'] 
                del user.actions['backstab'] 

            if self.equipment_type == 'sword':
                #riposte = actions('riposte', 1, 1, {7:"null"}, 'status', None, 'riposte', 0, 0, None, 0, None, 100, 1.2, None, ' ')
                del user.abilities['riposte'] 
                del user.actions['riposte'] 

            if self.equipment_type == 'knuckles':
                del user.abilities['restrain'] 

            if self.equipment_type == 'axe':
                #split = actions('split', 1, int(user.hit_Points_Max * 0.15), {7:"null"}, 'physical', None, 'stagger', 0, 1, None, 0, None, 65, 2, True, '-')
                del user.abilities['split'] 
                del user.actions['split'] 
                #cyclone =  actions('cyclone', 1, int(user.hit_Points_Max * 0.05), {7:"null"}, 'physical', None, 'stagger', 0, 3, 'square area', 0, 'square', 80, 0.75, True, '-')
                del user.abilities['cyclone'] 
                del user.actions['cyclone'] 

            if self.equipment_type == 'wand':
                #kadabra = actions('kadabra', 1, 10, {7:"null"}, 'physical', None, None, 0, 3, None, 1, None, 75, 1, False, '-')
                del user.abilities['kadabra'] 
                del user.actions['kadabra'] 

            if self.equipment_type == 'bow':
                #charge = actions('charge', 1, int(user.hit_Points_Max * 0.05), {7:"null"}, 'physical', None, None, 20, 6, None, 0,None, 100, 1.3, False, '-')
                del user.abilities['charge'] 
                del user.actions['charge'] 
        else:
            del user.abilities['cover'] 
            del user.actions['guard'] 
            user.s_Evade = user.s_Evade - self.s_Evade
            user.t_Evade = user.t_Evade

        if self.equipment_effects != []:
            user.strength = user.strength - self.strength
            user.magic = user.magic - self.magic
            user.speed = user.speed - self.speed
            user.brave = user.brave - self.brave
            user.faith = user.faith - self.faith
            user.w_Evade = self.w_Evade
            user.move_Range = user.move_Range - self.move_Range
        x = user.weapon
        t_inventory['all'].append(x)
        t_inventory[user.weapon.et].append(x)
        user.weapon = None
        user.equipment[0] = None
        
            
    def cover(self, user, target, playerGroup):
       #print "entering cover for", user.name
        if 'shield' == user.weapon.equipment_type:
            if 'link' in user.status:
                x = user.link_identify_id(playerGroup)
                if x != None:
                    x = raw_input('x is none what to do?')
                    x.status['covered'] = True
                    print x.status
                    print "cover function test"
                if x == None:
                    print " x is none, problem in link_identify_id"

    def restrain(self, user, playerGroup):
        if 'knuckles' == user.weapon.equipment_type:
            if 'link' in user.status:
                x = user.link_identify_id(playerGroup)
                if x != None:
                    #y = input('x is none what to do?')
                    x.status['restrained'] = True
                    #print x.status
                    #print "restrain function test"
                if x == None:
                    print " x is none, problem in link_identify_id"

    def ability_range_finder(self, user, **shape):
       #print ' entered weapon range finder'
        i = 0
        j = 0
        x = user.rect.topleft[0]/GRID_WIDTH
        y = user.rect.topleft[1]/GRID_HEIGHT
        potential_Targets = []
        shape = shape.get('shape', None)
        if self.att_Range == 0 and shape == None:
            for i in range(0, COLUMNS):
                for j in range(0, ROWS):
                    if abs(i-x) + abs(j-y) <= self.att_range :
                       #print i, j
                        potential_Targets.append((i,j))
       #print 'entering line loop'
        if self.att_Range != 0 and shape == 'line':
           #print 'passed line loop, before while loop'
            while i <= self.att_Range:
                if (x + i) <= ROWS:
                    potential_Targets.append(((x + i), y))
                if (y + i) <= COLUMNS:
                    potential_Targets.append((x, (y + i)))
                if (x - i) >= 0:
                    potential_Targets.append(((x-i), y))
                if (y - i) >= 0:
                    potential_Targets.append((x, (y-i)))
               #print x+i, x-i
               #print y+i, y-i
               #print i
                i = i +1
			
        if self.att_Range != 0 and shape == 'square':
            diagonal = (ranges-1)/2
           #print diagonal
            length = range(x - diagonal, x + diagonal + 1)
            width = range(y - diagonal, y + diagonal + 1)
           #print length
           #print width
            i = 0
            j = 0
            for i in range(0, len(length)):
                for j in range(0, len(width)):
                    potential_Targets.append((length[i], width[j]))
                    j = j + 1
                i = i +1
                j = 0
    
        return potential_Targets

    def range_display(self, potential_Targets):
        i = 0
        j = []
       #print " getting weapon display of ability targets", potential_Targets
        for i in range(0, len(potential_Targets)):
            grid_Potential_Targets = pygame.Rect((potential_Targets[i][0] * 100),(potential_Targets[i][1] * 100), GRID_WIDTH, GRID_HEIGHT)
            pygame.draw.rect(windowSurface, YELLOW, grid_Potential_Targets, THICK)
        pygame.display.update()
        return potential_Targets

    def raw_weapon_damage(self, user, distance):
        if self.equipment_type == 'sword':
            damage = self.weapon_power * user.strength
        elif self.equipment_type == 'spear':
            r = user.strength * distance
            if r == 0:
                r = 1
            else:
                pass
            x = randrange(-(r), r)
            damage = self.weapon_power * user.strength + x
        elif self.equipment_type == 'axe':
            x = randrange(-3 * self.weapon_power, 3 * self.weapon_power)
            damage = self.weapon_power * user.strength + x
        elif self.equipment_type == 'bow':
            if distance == 0:
                distance = self.att_Range
            x = randrange(-(distance * distance), (distance*distance))
            damage = self.weapon_power * int(user.strength / distance) + x
        elif self.equipment_type == 'knife':
            x = randrange(-user.strength, user.strength)
            damage = self.weapon_power * user.speed + x
        elif self.equipment_type == 'wand':
            if distance == 0:
                x = 1
            elif distance != 0:
                x = randrange(1, distance + 1)
            damage = self.weapon_power * user.magic / x
        elif self.equipment_type == 'shield':
            damage = user.strength 
        elif self.equipment_type == 'knuckles':
            damage = int(self.weapon_power * user.strength/(1 + (1 - user.brave*.01)))
        if damage <= 0:
            damage = 1
       #print damage
        return damage

test_sword1 = weapon('test sword1', 100, 'sword', 0,0,0,0,0,0,0,[])
test_sword2 = weapon('test sword2', 100, 'sword', 0,0,0,0,0,0,0,[])
test_sword3 = weapon('test sword3', 100, 'sword', 0,0,0,0,0,0,0,[])
test_sword4 = weapon('test sword4', 100, 'sword', 0,0,0,0,0,0,0,[])
test_sword5 = weapon('test sword5', 100, 'sword', 0,0,0,0,0,0,0,[])
test_sword6 = weapon('test sword6', 100, 'sword', 0,0,0,0,0,0,0,[])
test_sword7 = weapon('test sword7', 100, 'sword', 0,0,0,0,0,0,0,[])
test_sword8 = weapon('test sword8', 100, 'sword', 0,0,0,0,0,0,0,[])
test_sword9 = weapon('test sword9', 100, 'sword', 0,0,0,0,0,0,0,[])
test_sword10 = weapon('test sword10', 100, 'sword', 0,0,0,0,0,0,0,[])
test_sword11 = weapon('test sword11', 100, 'sword', 0,0,0,0,0,0,0,[])
test_sword12 = weapon('test sword12', 100, 'sword', 0,0,0,0,0,0,0,[])
test_sword13 = weapon('test sword13', 100, 'sword', 0,0,0,0,0,0,0,[])
test_sword14 = weapon('test sword14', 100, 'sword', 0,0,0,0,0,0,0,[])
e_Inventory = []
te_Inventory = {'all':[], 'item':[], 'weapon':[], 'off_Hand':[], 'helmet':[], 'armor':[],
                'accessory':[]}
p_Inventory = []
tp_Inventory = {'all':[test_sword1, test_sword2,
                       test_sword3,test_sword4,
                       test_sword5,test_sword6,
                       test_sword7, test_sword8,
                       test_sword9, test_sword10,
                       test_sword11, test_sword12,
                       test_sword13, test_sword14],
                'item':[],
                'weapon':[test_sword1, test_sword2,
                          test_sword3,test_sword4,
                          test_sword5,test_sword6,
                          test_sword7, test_sword8,
                          test_sword9, test_sword10,
                          test_sword11, test_sword12,
                          test_sword13, test_sword14],
                'off_Hand':[], 'helmet':[], 'armor':[],
                'accessory':[]}


class actions(object):
#element_type = {1:"void", 2:"infinity", 3:"fire", 4:"earth", 5:"water", 6:"sky", 7:"null"}
    def __init__(self, name, points, cost, element_type, effect,
                 effect_string, status_effect, speed, ability_Range,
                 area_Of_Effect, ability_Radius, ability_Shape, accuracy,
                 multiplier, consequence, intention):
        self.name = name
        self.points = points
        self.cost = cost
        self.element_type = element_type
        self.effect = effect #effect types : magic, physical, heal, status, other
        self.effect_string = effect_string # to be evaled and saved as a variable, which will be used to manipulate stats,11/25/2014 maybe not so much 
        self.status_effect = status_effect
        self.speed = speed #if speed is 0, it should be an instant action. i need to
        #create a ct update for action objects, so they will occur the proper
        #amount of turns later, like in FFT ## done v!
        self.ability_Range = ability_Range
        self.area_Of_Effect = area_Of_Effect
        self.ability_Radius = ability_Radius
        self.ability_Shape = ability_Shape
        self.accuracy = accuracy
        self.multiplier = multiplier
        self.consequence = consequence
        self.intention = intention
        self.ct = 0
        self.using = None
        self.targeting = None
        self.distance = 0
        self.data = [self.name, self.points, self.cost, self.effect, self.effect_string, self.status_effect, self.speed, self.ability_Range, self.area_Of_Effect, self.ability_Radius, self.ability_Shape, self.accuracy, self.multiplier, self.consequence, self.intention]

    def __getitem__(self, i):
        return self.data[i]


    def equip_action(self, user):
        user.actions[self.name] = self.use_action #and if action is in active_abilities
        user.actions_CD[self.effect][self.name] = self #might need to change this later for ai purposes
        #print user.actions_CD
        #r = input('print a number, character actions cd')

    def ct_update(self, user):
        if self.speed == 0:
            turn_counter = True
            return turn_counter
        turn_counter = False
        if user.hit_Points > 0:
            if self.ct < 100:
                self.ct = self.ct + self.speed
               #print "ct_update ok"
            if self.ct >= 100:
                self.ct = 0
                turn_counter = True
        else:
            del self
        return turn_counter

    def delayed_action(self, user, targets, distance, action_Timeflow_List,
                       grid_positions, grid_objects, playerGroup):
        user.action_Charging = self.name
        user.status['charging'] = True
        self.using = user
        self.targeting = targets
        self.distance = distance
       #print actions, ' this is the actions list'
        action_Timeflow_List.append(self)
        Battle_Surface_Refresh(grid_positions, grid_objects, playerGroup)
        ca_Turn = False
        return ca_Turn
        

    def action_effect(self, user, targets, distance, grid_positions,
                      grid_objects, playerGroup):
       #print 'entering action_effect loop'
        cost = (self.cost - user.stamina)
        if cost < 0:
            cost = 1
        user.hit_Points = user.hit_Points - cost
        if 'charging' in user.status:
            del user.status['charging']
       #print 'cost of action is', cost, ' to ', user.name
       #print targets, 'targets'
        w = len(targets)
        #print targets[0]
        list1 = []
        string1 = 'string'
        list_type = type(list1)
        string_type = type(string1)
        cha_type = type(user)
       #print cha_type
       #print w
        y = type(targets)
       #print y, 'type targets'
        #if y == list_type and w >= 2:
        #    print 1
        #    pass
        if y == list_type and w == 1:
           #print targets
            targets = targets[0]
           #print 2
           #print targets
        y = type(targets)
       #print targets
       #print y
        #passer = raw_input('what is the targets list printing')
       #print 'total remaining hit points is ', user.hit_Points
        #hit = user.hit_or_miss(target, distance)
        #attack_damage_calculator(user, target, distance, hit, grid_positions, grid_objects, playerGroup)
        surf = pygame.display.get_surface()
        copy = surf.copy()
        s_rect = surf.get_rect()
        headline = text_box(surf, self.name, int(s_rect.center[0]/2), int(s_rect.center[1]/2),
                            10, True, DRED)
        pygame.display.update(headline)
        time.sleep(1)
        surf.blit(copy, s_rect.topleft)
        pygame.display.update()
        if self.effect == 'physical':
           #print 'entering physical action loop'
            hit = self.physical_action(user, targets, distance, grid_positions, grid_objects, playerGroup)
           #print 'exiting physical action loop'
            if False in hit and self.consequence == True:
                self.consequence_action(user, targets)#, distance, grid_positions, grid_objects, playerGroup)

        if self.effect == 'item':
            hit = self.item_action(user, targets, distance, grid_positions, grid_objects, playerGroup)

        elif self.effect == 'status':
            hit = self.status_action(user, targets, distance, grid_positions, grid_objects, playerGroup)
            if False in hit and self.consequence == True:
                self.consequence_action(user, targets)#, distance, grid_positions, grid_objects, playerGroup)

        elif self.effect == 'move':
            hit = self.move_action(user, targets, distance, grid_positions, grid_objects, playerGroup)
            
        experience_calculator(user, targets, hit)
        ca_turn = False
        #time.sleep(3)
        Battle_Surface_Refresh(grid_positions, grid_objects, playerGroup)
        #user.att_Turn = False
       #print 'ca_turn is ', ca_turn
        return ca_turn

#12 21 2014
# in order to have items with a charge delay, like grenade work properly, since
#the actions would affect each character individually, (and as i write this,
#i'm starting to realize it was all unnecessary, but whatever), i had a branch
#in the actions that would account for either one target or many targets.
#if you use something like for thing in things, or for item in items, it would work
#fine if there were more than one item in the list of items, but if there was
#only one, it wouldn't work right, calling out an attribute error, but saying
#'str' type has no attribute x. this is because if there is only one object
#in the list, it will then cycle through the attributes of that object, which
#is why it came up as string, as sex is the first attribute, and is either 'male'
#or 'female', which i should probably fix to include a spectrum instead of a binary

    def physical_action(self, user, targets, distance, grid_positions, grid_objects, playerGroup):
       #print 'physical action loop'
       #print targets
        hit = []
       #print len(targets)
        if len(targets) > 1:
            for target in targets:
               #print target.data
                damage = user.weapon.raw_weapon_damage(user, distance) * self.multiplier
                damage_To_Enemy_Magnifier = element_type_calculator(user, target, grid_positions, grid_objects, playerGroup)
                damage_To_Self_Magnifier = element_type_calculator(target, user, grid_positions, grid_objects, playerGroup)
                result = self.action_hit_or_miss(user, target)
                hit.append(result)
                damage, damage_To_Enemy, damage_To_Self = attack_damage_modifier(user, target, damage, damage_To_Enemy_Magnifier, damage_To_Self_Magnifier)
                damage_To_Enemy, damage_To_Self, user.hit_Points, target.hit_Points = attack_damage_applier(user, target, distance, result, damage, damage_To_Enemy, damage_To_Self, grid_positions, grid_objects, playerGroup)
                hit_display(result, damage_To_Enemy, target)
                if result == False:
                    hit_display(True, damage_To_Self, user)
                elif result == True:
                    hit_display(result, damage_To_Self, user)
                self.relationship_update(user, target)
                time.sleep(1)
        elif len(targets) == 1:
            #print target.data
           #print targets
            #targets = targets[0]
            damage = user.weapon.raw_weapon_damage(user, distance) * self.multiplier
            #print damage
            damage_To_Enemy_Magnifier = element_type_calculator(user, targets, grid_positions, grid_objects, playerGroup)
            #print damage_To_Enemy_Magnifier
            damage_To_Self_Magnifier = element_type_calculator(targets, user, grid_positions, grid_objects, playerGroup)
            #print damage_To_Self_Magnifier
            result = self.action_hit_or_miss(user, targets)
            #print result
            hit.append(result)
            damage, damage_To_Enemy, damage_To_Self = attack_damage_modifier(user, targets, damage, damage_To_Enemy_Magnifier, damage_To_Self_Magnifier)
            #print damage, damage_To_Enemy, damage_To_Self
            damage_To_Enemy, damage_To_Self, user.hit_Points, targets.hit_Points = attack_damage_applier(user, targets, distance, result, damage, damage_To_Enemy,
                                                                                                         damage_To_Self, grid_positions, grid_objects, playerGroup)
           #print damage_To_Enemy, damage_To_Self, user.hit_Points, targets.hit_Points, 'damage to enemy, self, remaining user and target hp'
            hit_display(result, damage_To_Enemy, targets)
            if result == False:
                hit_display(True, damage_To_Self, user)
            elif result == True:
                hit_display(result, damage_To_Self, user)
            self.relationship_update(user, targets)
            time.sleep(2)
       #print 'end of physical action loop'
       #print 'targets', targets
        return hit
        #Battle_Surface_Refresh(grid_positions, grid_objects)
        #ca_turn = False
        #self.att_Turn
        

    def status_action(self, user, targets, distance, grid_positions, grid_objects, playerGroup):
       #print 'status action loop'
        #is hit supposed to be result, here, and result is supposed to be list?
        if self.intention == '+':
            heal = True
        elif self.intention != '+':
            heal = False
        hit = []
        if len(targets) > 1:
            for target in targets:
                detect = attack_detect(user, target)
                if self.name == 'backstab' and detect == True:
                    result = False
                    hit.append(result)
                elif self.name == 'backstab' and detect == False:
                    pass
                result = self.action_hit_or_miss(user, target)
               #print result
                if result == True:
                    target.status[self.status_effect]= True
                    user.hit_Points = user.hit_Points - self.cost
                    target.status_update(grid_positions, grid_objects, playerGroup)
                    txt = self.status_effect
                    ##stat_change = eval(self.effect_string) user.t_Evade
                    hit.append(result)
                    #hit_display(result, txt ,target)
                
                elif result == False:
                    user.hit_Points = user.hit_Points - self.cost
                    txt = 'Miss'
                    hit.append(result)
                    #hit_display(result, txt ,target)

               #print self.status_effect
               #print result, txt, target, heal, 'hit_display variables, result, txt, target, and heal'
                hit_display(result, txt ,target, heal)
                hit_display(True, self.cost, user)
                self.relationship_update(user, target)
                time.sleep(1)
                
#6/28/2015 error occured when using backstab on a linked target, chose to only
#attack one of the units, but that caused the game to bug out due to the fact
#that i hadn't addressed this issue below, appending to hit when it would be
#boolean type
                
        elif len(targets) == 1:
            #targets = targets[0]
            #if len(targets) < 1:
            detect = attack_detect(user, targets)
            if self.name == 'backstab' and detect == True:
                result = False
                hit.append(result)
            elif self.name == 'backstab' and detect == False:
                pass
            result = self.action_hit_or_miss(user, targets)
           #print hit
            if result == True:
                targets.status[self.status_effect]= True
                txt = self.status_effect
                user.hit_Points = user.hit_Points - self.cost
                targets.status_update(grid_positions, grid_objects, playerGroup)
                ##stat_change = eval(self.effect_string) user.t_Evade
                hit.append(result)
                
            elif result == False:
                user.hit_Points = user.hit_Points - self.cost
                txt = 'Miss'
                hit.append(result)
            hit_display(result,txt , targets, heal)
            hit_display(True, self.cost, user)
            self.relationship_update(user, targets)
            time.sleep(2)
        
        return hit

    def magic_action(self, user, targets, distance, grid_positions, grid_objects, playerGroup):
        hit = []
        if len(targets) > 1:
            for target in targets:
                user.hit_Points = user.hit_Points - self.cost
                damage = user.raw_magic_damage(self.cost) * self.multiplier * (user.faith/100) * (target.faith/100)
                damage_To_Enemy_Magnifier = element_type_calculator(user, target, grid_positions, grid_objects, playerGroup) * elemental_Object_Compare(self, target)
                damage_To_Self_Magnifier = element_type_calculator(target, user, grid_positions, grid_objects, playerGroup) * elemental_Object_Contrast(user, self)
                result = self.action_hit_or_miss(user, target)
                hit.append(result)
                damage, damage_To_Enemy, damage_To_Self = attack_damage_modifier(user, target, damage, damage_To_Enemy_Magnifier, damage_To_Self_Magnifier)
                damage_To_Enemy, damage_To_Self, user.hit_Points, target.hit_Points = attack_damage_applier(user, target, distance, result, damage, damage_To_Enemy, damage_To_Self, grid_positions, grid_objects, playerGroup)
                hit_display(result, damage_To_Enemy, target)
                if result == False:
                    hit_display(True, damage_To_Self, user)
                elif result == True:
                    hit_display(result, damage_To_Self, user)
                self.relationship_update(user, target)
                time.sleep(1)
        elif len(targets) == 1:
            #targets = targets[0]
            user.hit_Points = user.hit_Points - self.cost
            damage = user.raw_magic_damage(self.cost) * self.multiplier * (user.faith/100) * (targets.faith/100)
            damage_To_Enemy_Magnifier = element_type_calculator(user, targets, grid_positions, grid_objects, playerGroup) * elemental_Object_Compare(self, targets)
            damage_To_Self_Magnifier = element_type_calculator(targets, user, grid_positions, grid_objects, playerGroup) * elemental_Object_Contrast(user, self)
            result = self.action_hit_or_miss(user, targets)
            hit.append(result)
            damage, damage_To_Enemy, damage_To_Self = attack_damage_modifier(user, targets, damage, damage_To_Enemy_Magnifier, damage_To_Self_Magnifier)
            damage_To_Enemy, damage_To_Self, user.hit_Points, targets.hit_Points = attack_damage_applier(user, targets, distance, result, damage, damage_To_Enemy, damage_To_Self, grid_positions, grid_objects, playerGroup)
            hit_display(result, damage_To_Enemy, targets)
            if result == False:
                hit_display(True, damage_To_Self, user)
            elif result == True:
                hit_display(result, damage_To_Self, user)
            self.relationship_update(user, targets)
            time.sleep(2)
        return hit

    def heal_action(self, user, targets, distance, grid_positions, grid_objects, playerGroup):
        hit = []
        if len(targets) > 1:
            for target in targets:
                user.hit_Points = user.hit_Points - self.cost
                damage = user.raw_magic_damage(self.cost) * self.multiplier * (user.faith/100) * (target.faith/100)
                damage = damage * -1
                damage_To_Enemy_Magnifier = element_type_calculator(user, target, grid_positions, grid_objects, playerGroup) * elemental_Object_Compare(self, target)
                damage_To_Self_Magnifier = element_type_calculator(target, user, grid_positions, grid_objects, playerGroup) * elemental_Object_Contrast(user, self)
                result = self.action_hit_or_miss(user, target)
                hit.append(result)
                damage, damage_To_Enemy, damage_To_Self = attack_damage_modifier(user, target, damage, damage_To_Enemy_Magnifier, damage_To_Self_Magnifier)
                damage_To_Enemy, damage_To_Self, user.hit_Points, target.hit_Points = attack_damage_applier(user, target, distance, result, damage, damage_To_Enemy, damage_To_Self, grid_positions, grid_objects, playerGroup)
                hit_display(result, damage_To_Enemy, target, True)
                if result == False:
                    hit_display(True, damage_To_Self, user)
                elif result == True:
                    hit_display(result, damage_To_Self, user)
                self.relationship_update(user, target)
                time.sleep(1)
        elif len(targets) == 1:
            #targets = targets[0]
            user.hit_Points = user.hit_Points - self.cost
            damage = user.raw_magic_damage(self.cost) * self.multiplier * (user.faith/100) * (targets.faith/100)
            damage = damage * -1
            damage_To_Enemy_Magnifier = element_type_calculator(user, targets, grid_positions, grid_objects, playerGroup) * elemental_Object_Compare(self, targets)
            damage_To_Self_Magnifier = element_type_calculator(targets, user, grid_positions, grid_objects, playerGroup) * elemental_Object_Contrast(user, self)
            result = self.action_hit_or_miss(user, targets)
            hit.append(result)
            damage, damage_To_Enemy, damage_To_Self = attack_damage_modifier(user, targets, damage, damage_To_Enemy_Magnifier, damage_To_Self_Magnifier)
            damage_To_Enemy, damage_To_Self, user.hit_Points, targets.hit_Points = attack_damage_applier(user, targets, distance, result, damage, damage_To_Enemy, damage_To_Self, grid_positions, grid_objects, playerGroup)
            hit_display(result, damage_To_Enemy, targets)
            if result == False:
                hit_display(True, damage_To_Self, user)
            elif result == True:
                hit_display(result, damage_To_Self, user)
            self.relationship_update(user, targets)
            time.sleep(2)
        return hit

    def item_action(self, user, targets, distance, grid_positions, grid_objects, playerGroup):
        if self.points > 0:
            heal = True
        elif self.points < 0:
            heal = False
        result = True
        if len(targets) > 1:
            for target in targets:
                if self.points != 0:
                    item_HP_Change = self.points * self.multiplier
                    target.hit_Points = target.hit_Points + item_HP_Change
                    if target.hit_Points > target.hit_Points_Max:
                        target.hit_Points = target.hit_Points_Max
                   #print item_HP_Change, 'to ', target.name
                    if self.name == 'phoenix down':
                        target.image = target.root_Image
                if self.status_effect is not None:
                    if '-' in self.status_effect:
                        if target.status.has_key(self.status_effect) == True:
                            del targets.status[self.status_effect[1]]
                        elif target.status.has_key(self.status_effect) != True:
                            pass
                        
                    else:
                        target.status[self.status_effect] = True
                        #print self.status_effect
                        #hit_display(result, self.status_effect, target)
                hit_display(result, item_HP_Change, target, heal)
                self.relationship_update(user, target)
                time.sleep(1)
        elif len(targets) == 1:
            target = targets[0]
           #print targets
            #targets = targets[0]
            #print targets
            if self.points != 0:
                item_HP_Change = self.points * self.multiplier
                target.hit_Points = target.hit_Points + item_HP_Change
               #print item_HP_Change, 'to ', targets.name
                if self.name == 'phoenix down':
                    target.image = target.root_Image
            if self.status_effect is not None:
                if '-' in self.status_effect:
                    if target.status.has_key(self.status_effect) == True:
                        del target.status[self.status_effect[1]]
                    elif target.status.has_key(self.status_effect) != True:
                        pass
            else:
                target.status[self.status_effect] = True
            hit_display(result, item_HP_Change, target, heal)
            self.relationship_update(user, target)
            time.sleep(2)
                
        if self.name in user.inventory:
            del user.inventory[self.name]
            del user.actions[self.name]
            #del self
        hit = [True]
        return hit

    def move_action(self, user, targets, distance, grid_positions, grid_objects, playerGroup):
        #q = targets.grid_Char_Rect[0]
        tx = targets.rect.topleft[0]
        z = targets.grid_Char_Rect[1]
        ty = targets.rect.topleft[1]
        cmx = COLUMNS - 1
        rmx = ROWS - 1
        
       #print [int(targets.rect.topleft[0]/GRID_WIDTH), int(targets.rect.topleft[1]/GRID_HEIGHT)]
       #print targets.rect.topleft
       #print targets.grid_Char_Rect
       #print tx, z, ty, cmx, rmx, 'x, tx, y, ty, cmx, rmx,'
       #print self.name
        if self.name == 'retreat':
            hit = [False]
           #print 'hit = false'
            #windowSurface.unlock()
            if tx == 0 or tx == (cmx * GRID_WIDTH):
               #print 'retreating', 1
                if tx == 0:
                    hit = [True]
                    targets.rect.topleft = (tx - 300, ty)
                   #print 'retreating'
                    
                elif tx == cmx * GRID_WIDTH:
                    hit = [True]
                    targets.rect.topleft = (tx + 300, ty)
                   #print 'retreating'
                    
            elif ty == 0 or ty ==  rmx * GRID_HEIGHT:
                if ty == 0:
                    hit = [True]
                    targets.rect.topleft = (tx , ty - 300)
                   #print 'retreating'
                    
                elif ty == rmx * GRID_HEIGHT:
                    hit = [True]
                    targets.rect.topleft = (tx , ty + 300)
                   #print 'retreating'
                    
            if hit == [True]:
                targets.status['retreat'] = True
                
            self.relationship_update(user, targets)
            Battle_Surface_Refresh(grid_positions, grid_objects, playerGroup)
            #windowSurface.lock()
            return hit
        
    #12/22/2014
    #kept getting errors on TypeError: argument of type 'bool' is not iterable
    #on item_actions, turned out to be because I made item actions always return
    #True, and not return a list of hits or misses, since it was always going to
    #return a True, so took a short cut... don't take shortcuts! ended up just
    #writing hit = [True], to fit into everything else that was already in place
    #i may need to change it later, depending on how I have hits and misses work
    #out, in the future

    def consequence_action(self, user, targets, forecast = False):#distance, grid_positions, grid_objects, playerGroup, forercast = False):
        x = randrange(0,100)
        if self.cost > 0:
            cutoff = (100 - (self.accuracy - self.multiplier*10))/self.cost
        elif self.cost == 0:
            cutoff = (100 - (self.accuracy - self.multiplier*10))
        cost = (randrange(int(user.hit_Points_Max*.1), int(user.hit_Points_Max*.25)))
        s_effect = self.status_effect
        if forecast == True:
            #cutoff = 100 - cutoff
            return cutoff, cost, s_effect
        elif forecast != True:
            if x < cutoff and x % 2 == 0:
                user.status[self.status_effect] = True
            elif x < cutoff and x % 2 == 1:
                user.hit_Points = user.hit_Points - cost #(randrange(int(user.hit_Points_Max*.1), int(user.hit_Points_Max*.25))) 
            
##    def consequence_action(self, user, targets, distance, grid_positions, grid_objects, playerGroup):
##        x = randrange(0,100)
##        cutoff = (100 - (self.accuracy - self.multiplier*10))/self.cost
##        if x < cutoff and x % 2 == 0:
##            user.status[self.status_effect] = True
##        elif x < cutoff and x % 2 == 1:
##            user.hit_Points = user.hit_Points - (randrange(int(user.hit_Points_Max*.1), int(user.hit_Points_Max*.25))) 

    def action_hit_or_miss(self, user, target, forecast = False):
        chance = 0
        if self.effect == 'physical':
            detect = attack_detect(user, target)
            if detect == True:
                chance = 100 - (self.accuracy - target.t_Evade)
            elif detect == False:
                pass
        elif self.effect == 'magic' or self.effect == 'heal':
            chance = 100 - (self.accuracy - (target.a_Evade + target.s_Evade + (55 - target.faith)))
        if self.effect == 'status':
            chance = 100 - (self.accuracy + (55 - target.faith))
##        if self.effect == 'item':
##            chance = 0
        if target.status.get('restrained') == True:
            #chance = 100
            pass
        if forecast == True:
            chance = 100 - chance
            return chance
        elif forecast != True:
        #if chance >= 100:
        #    chance = 100
            roll = randrange(0, 101)
           #print roll, chance, 'roll and chance'
            if roll >= chance:
                hit = True
            else:
                hit = False
            return hit

##    def action_hit_or_miss(self, user, target):
##        if self.effect == 'physical':
##            detect = attack_detect(user, target)
##            if detect == True:
##                chance = 100 - (self.accuracy - target.t_Evade)
##            elif detect == False:
##                chance = 0
##        elif self.effect == 'magic' or self.effect == 'heal':
##            chance = 100 - (self.accuracy - (target.a_Evade + target.s_Evade + (55 - target.faith)))
##        if self.effect == 'status':
##            chance = 100 - (self.accuracy + (55 - target.faith))
##        if target.status.get('restrained') == True:
##            chance = 0
##        #if chance >= 100:
##        #    chance = 100
##        roll = randrange(0, 101)
##        print roll, chance, 'roll and chance'
##        if roll >= chance:
##            hit = True
##        else:
##            hit = False
##        return hit

    def relationship_update(self, user, target):
        if user.relationships.has_key(target) == False:
            if user.allegiance == target.allegiance:
                user.relationships[target] = 50
                target.relationships[user] = 50
            elif user.allegiance != target.allegiance:
                user.relationships[target] = 35
                target.relationships[user] = 35
        elif user.relationships.has_key(target) == True:
            if self.intention == '+':
                target.relationships[user] = target.relationships[user] + 1
            elif self.intention == '-':
                target.relationships[user] = target.relationships[user] - 1
            elif self.intention == ' ':
                pass

    def act_assess(self, user, targets, grid_positions, gp_dict, grid_objects, playerGroup, move):
        score = 0
        l = len(targets)
        ntnt = {'-':1, '+':-1}
        total = 0
        totalt = 0
        fort = None
        against = None
        difference = 0
        overkill = 0
        ok = 0
        ai = True
        n = ntnt[self.intention]
        sa = user.allegiance
        link_bonus = 0
        c_check = user.abilities.get('cover')
        r_check = user.abilities.get('restrain')
        if l == 0:
            return None
        elif l == 1:
            
            #self, user, target, grid_positions, gp_dict, grid_objects, playerGroup,  AI = False, move = None):
            target = targets[0]
            fc_dict = self.forecaster1(user, target, grid_positions,
                                       gp_dict, grid_objects, playerGroup,
                                       ai, move)
            
##            fc_dict = {'total_cost':total_cost, 'chance':chance, 'cons_chance':cons_chance,
##                   's_effect':s_effect, 'cons_cost':cost, 'self_cost':damage_To_Self,
##                   'damage_To_Enemy':damage_To_Enemy,}
            #print fc_dict, 'fc dict'
            fort = fc_dict['damage_To_Enemy'] * (fc_dict['chance'] * .01)
            against = (fc_dict['total_cost'] * ((fc_dict['cons_chance'] * .01 + (100 - fc_dict['chance']) * .01))) * -1
            
            #if (c_check or r_check) == True:
            if move == target.grid_Char_Rect:
                
                if (c_check or r_check) == True:
                #if move == target.grid_Char_Rect:
                    fort = 0
                    against = 0
                    if target.allegiance == user.allegiance:
                        if c_check == True and r_check == False:
                            if target.hit_Points > 0:
                                link_bonus = user.hit_Points #(user.hit_Points - target.hit_Points) /3
                            elif target.hit_Points <0 :
                                link_bonus = -200
                            
                        if r_check == True and c_check == False:
                            link_bonus -= -200
                            
                    elif target.allegiance != user.allegiance:
                        if c_check == True and r_check == False:
                            link_bonus -= 200
                        if r_check == True and c_check == False:
                            if target.hit_Points > 0:
                                link_bonus = user.strength * 2 #- target.strength) * 3
                            elif target.hit_Points <= 0:
                                link_bonus = -200

                elif (c_check and r_check) == False:
                    fort = 0
                    against = 0
                    link_bonus = -200
                    print 'bad spot'
            
            #print fort, against, 'fort and against'

            if link_bonus == 0:
                if ntnt[self.intention] == 1:
                    overkill = target.hit_Points - fc_dict['damage_To_Enemy']
                    
                elif ntnt[self.intention] == -1:
                    ok = target.hit_Points_Max - target.hit_Points
                    overkill = target.hit_Points_Max - (target.hit_Points - fc_dict['damage_To_Enemy'])
                    
                if overkill > 0:
                    overkill = 0
                elif overkill < 0:
                    pass

            elif link_bonus != 0:
                pass
            
            #total = (fort + ok)  - (against + overkill)
            total = fort + ok + against + overkill + link_bonus
            #print total, 'total before alleviance gate'
            ta = target.allegiance
            ua = user.allegiance
            if ta == ua:
                if user.relationships.has_key(target.name) == False:
                    user.relationships[target.name] = 50
                else:
                    pass
                if total > 0 and n == 1: #harmful action to ally
                    total = (total * -1) - user.relationships[target.name] #ntnt[self.intention]
                elif total < 0 and n == -1:  #healing action to ally
                    total = (total * -1) + user.relationships[target.name]
                    pass
                #print total, 'total modded by alegiance', target.grid_Char_Rect
            elif ta != ua:
                if user.relationships.has_key(target.name) == False:
                    user.relationships[target.name] = 25
                else:
                    pass
            #print total, fort, ok, against, overkill, 'total, fort ok, against, overkill', self.name, target.grid_Char_Rect

        elif l > 1:
            for target in targets:
                if move != target.grid_Char_Rect:
               #print target, 'target'
                    fc_dict = self.forecaster1(user, target, grid_positions,
                                               gp_dict, grid_objects, playerGroup,
                                               ai, move)
                    #print fc_dict, 'fc dict'
                    fort = fc_dict['damage_To_Enemy'] * (fc_dict['chance'] * .01)
                    against = fc_dict['total_cost'] * ((fc_dict['cons_chance'] + (100 - fc_dict['chance']) * .01)) * -1
                    if ntnt[self.intention] == 1:
                        overkill = target.hit_Points - fc_dict['damage_To_Enemy']
                        
                    elif ntnt[self.intention] == -1:
                        ok = target.hit_Points_Max - target.hit_Points
                        overkill = target.hit_Points_Max - (target.hit_Points - fc_dict['damage_To_Enemy'])
                        
                    if overkill > 0:
                        overkill = 0
                    elif overkill < 0:
                        pass
                
                    #totalt = (fort + ok) - (against + overkill)
                    
                    totalt = fort + ok + against + overkill
                    #print totalt, 'totalt beforfe allegiance gate'
                    ta = target.allegiance
                    ua = user.allegiance
                    if ta == ua:
                        if user.relationships.has_key(target.name) == False:
                            user.relationships[target.name] = 50
                        else:
                            pass
                        if totalt > 0 and n == 1: #harmful action to ally
                            totalt = (totalt * -1) - user.relationships[target.name] #ntnt[self.intention]
                        elif totalt < 0 and n == -1:  #healing action to ally
                            totalt = (totalt * -1) + user.relationships[target.name]
                            
    ##                    if totalt > 0:
    ##                    totalt = totalt * -1 #* ntnt[self.intention]
    ##                    print totalt, 'totalt modded by allegiance'
                    elif ta != ua:
                        if user.relationships.has_key(target.name) == False:
                            user.relationships[target.name] = 25
                        else:
                            pass
                #print total, fort, ok, against, overkill, 'total fort ok, against, overkill', self.name, target.grid_Char_Rect
                    total = total + totalt
                elif move == target.grid_Char_Rect:
                    print 'multiple bad spot'
                    total -= 1000
                #print total, fort, ok, against, overkill, 'total fort ok, against, overkill', self.name, target.grid_Char_Rect
                #print total, totalt, 'total and totalt in multi target list'
        #test_some = raw_input('what is goign on...?')

        return total

    def action_assess(self, user, playerGroup,grid_positions,
                       grid_objects, grid_obstacles, gp_dict ):
        
        cx, cy = user.grid_Char_Rect
        d = -1
        r = user.move_Range + self.ability_Range
        potential_moves = user.path_filter((cx, cy), GRID_WIDTH,
                                           GRID_HEIGHT, grid_obstacles,
                                           user.move_Range, playerGroup)#.att_range, self.move, cx, cy, GRID_WIDTH, GRID_HEIGHT, Move_Turn, Attack_Turn)
        targets = []
        possible_actions = {}
        scores = {}
        act_score = -1000
        b_score = -999
        p_action = {'act': self, 'a_name':self.name, 'score': 0,
                    'move':None, 'targets':None, 'target':None,
                    'tolerance':0}
        tol = p_action['tolerance']
        ally = None
        tl = None
        rad = self.ability_Radius
        #link_bonus = 0
# user = None, radius = 0, gmx = 0, gmy = 0, p_move = None):
#in this case, pmove is the potential movement a character could make, pot_targets should reflect the tiles one could choose to target the action
#we need a second function to see what are the valid targettable tiles
#thats what pot targets is... potential)moves is listed above
        for move in potential_moves:
               #(self, user = None, radius = 0, gmx = 0, gmy = 0, p_move = None): #**shape):
            pot_targets = self.ability_range_finder(user, rad,
                                                    0, 0, move)#,
                                                    #move)
           #print pot_targets, 'pot targets'
            #targets = []
            for target in pot_targets:
                targets = []
                tol = 0
                if rad > 0:
                    tl = []
                    tl.append(target)
                    gmx, gmy = target
                    #print 'radius loop'
                    for i in range(0, COLUMNS):
                        for j in range(0, ROWS):
                            if abs(i-gmx) + abs(j-gmy) <= rad :
                                #potential_Targets.append((i,j))
                                tl.append((i,j))
                       #print potential_Targets
                       #return potential_Targets
                for player in playerGroup:
                    
                   #print player.grid_Char_Rect, 'player.grid_char_rect'
                    if player.grid_Char_Rect in pot_targets:
                        if tl == None:
                            #if player.grid_Char_Rect in target:
                            if player.grid_Char_Rect == target:
                                if self.intention == '-':
                                    if player.allegiance == user.allegiance:
                                        tol -= 2
                                    elif player.allegiance != user.allegiance:
                                        tol += 1
                                elif self.intention == '+':
                                    if player.allegiance == user.allegiance:
                                        tol += 1
                                    elif player.allegiance != user.allegiance:
                                        tol -= 2
                                targets.append(player)
                            #elif player.grid_Char_Rect not in target:
                            elif player.grid_Char_Rect != target:
                                pass
                        elif tl != None:
                            if player.grid_Char_Rect in tl:
                                if self.intention == '-':
                                    if player.allegiance == user.allegiance:
                                        tol -= 2
                                    elif player.allegiance != user.allegiance:
                                        tol += 1
                                elif self.intention == '+':
                                    if player.allegiance == user.allegiance:
                                        tol += 1
                                    elif player.allegiance != user.allegiance:
                                        tol -= 2
                                targets.append(player)
                            elif player.grid_Char_Rect not in tl:
                                pass
                    elif player.grid_Char_Rect not in pot_targets:
                                 #maybe radius check loop goes in here
                        pass
                a_score = self.act_assess(user, targets, grid_positions,
                                          gp_dict, grid_objects, playerGroup, move)
                #if a_score != None:
                    #print a_score, 'a score', targets, target, move, 'targets, target and move'
                if a_score > b_score:# and tol >= 0:
                    b_score = a_score
                    print b_score, move, targets, target, 'b_score, move, targets, target'
                    p_action['score'], p_action['move'], p_action['targets'], p_action['target'], p_action['tolerance'] = b_score, move, targets, target, tol

        return p_action
                
        
        
    def forecaster1(self, user, target, grid_positions, gp_dict, grid_objects, playerGroup,  AI = False, move = None):
        forecast = True
    #    target = target[0]
        hit_chance = self.action_hit_or_miss(user, target, forecast)
        chance = hit_chance
        cons_chance, cost, s_effect = self.consequence_action(user, target, forecast)
        #cons_chance =  cutoff
        total_cost = 0
        ta = target
        thp = target.hit_Points
        ust = user.strength
        usp = user.speed
        thp10 = thp/10
        if thp10 <= 0:
            thp10 = .5 
        status_Dict = {'poison':thp/(ust + usp), 'riposte':int((ta.t_Evade * 3) / thp10),
                       'guard':int((ta.t_Evade * 2) / thp10) }
        if AI == False:
            utlx, utly = user.rect.topleft[0]/100, user.rect.topleft[1]/100
        elif AI == True:
            utlx, utly = move
            
        ttlx, ttly = target.rect.topleft[0]/100, target.rect.topleft[1]/100
        distance = abs(utlx - ttlx)+ abs(utly - ttly)
        damage_To_Self = 0
        damage_To_Enemy = 0
        #need to adapt element_type_calculator to take potential spots
        
        if self.effect == 'physical':
            damage = user.weapon.raw_weapon_damage(user, distance) * self.multiplier
            if AI == False:
                damage_To_Enemy_Magnifier = element_type_calculator(user, target, grid_positions, grid_objects, playerGroup)
                damage_To_Self_Magnifier = element_type_calculator(target, user, grid_positions, grid_objects, playerGroup)
            elif AI != False:
                damage_To_Enemy_Magnifier = element_type_calculator(user, target, grid_positions, grid_objects, playerGroup)#, AI, move)
                damage_To_Self_Magnifier = element_type_calculator(target, user, grid_positions, grid_objects, playerGroup)#, AI, move)
            damage, damage_To_Enemy, damage_To_Self = attack_damage_modifier(user, target, damage, damage_To_Enemy_Magnifier, damage_To_Self_Magnifier)

        if self.effect == 'item':
            damage_To_Enemy = self.points * self.multiplier

        if self.effect == 'magic':
            damage = user.raw_magic_damage(self.cost) * self.multiplier * (user.faith/100) * (target.faith/100)
            if AI == False:
                damage_To_Enemy_Magnifier = element_type_calculator(user, target, grid_positions, grid_objects, playerGroup)
                damage_To_Self_Magnifier = element_type_calculator(target, user, grid_positions, grid_objects, playerGroup)
            elif AI != False:
                damage_To_Enemy_Magnifier = element_type_calculator(user, target, grid_positions, grid_objects, playerGroup)#, AI, move)
                damage_To_Self_Magnifier = element_type_calculator(target, user, grid_positions, grid_objects, playerGroup)#, AI, move)
            damage, damage_To_Enemy, damage_To_Self = attack_damage_modifier(user, target, damage, damage_To_Enemy_Magnifier, damage_To_Self_Magnifier)

        if self.effect == 'status':
            if self.status_effect == 'KO' or self.status_effect[1] == 'KO':
                if self.intention == '-':
                    damage_To_Enemy = target.hit_Points
                elif self.intention == '+':
                    damage_To_Enemy = self.points - target.hit_Points
            elif self.status_effect in target.status or self.status_effect[1] in target.status:
                damage_To_Enemy += status_Dict[self.status_effect]
                    
            
        if self.effect == 'heal':
            damage_To_Enemy = damage_To_Enemy * -1

        
        total_cost = total_cost + cost + damage_To_Self
        fc_dict = {'total_cost':total_cost, 'chance':chance, 'cons_chance':cons_chance,
                   's_effect':s_effect, 'cons_cost':cost, 'self_cost':damage_To_Self,
                   'damage_To_Enemy':damage_To_Enemy}
        if AI == True:
            return fc_dict
        elif AI != True:
            pass
        target.forecast_display(chance, damage_To_Enemy, s_effect)
        user.forecast_display(cons_chance, total_cost, s_effect)

    def forecaster2(self, user, targets, grid_positions, gp_dict, grid_objects, playerGroup):
        forecast = True
        damage_To_Enemy = 0
        damage_To_Self = 0
        for target in targets:
        
            hit_chance = self.action_hit_or_miss(user, target, forecast)
            chance = hit_chance
            cutoff, cost, s_effect = self.consequence_action(user, target, forecast)
            cons_chance = cutoff
            total_cost = 0
            utlx, utly = user.rect.topleft[0]/100, user.rect.topleft[1]/100
            ttlx, ttly = target.rect.topleft[0]/100, target.rect.topleft[1]/100
            distance = abs(utlx - ttlx)+ abs(utly - ttly)
            
            if self.effect == 'physical':
                damage = user.weapon.raw_weapon_damage(user, distance) * self.multiplier
                damage_To_Enemy_Magnifier = element_type_calculator(user, target, grid_positions, grid_objects, playerGroup)
                damage_To_Self_Magnifier = element_type_calculator(target, user, grid_positions, grid_objects, playerGroup)
                damage, damage_To_Enemy, damage_To_Self = attack_damage_modifier(user, target, damage, damage_To_Enemy_Magnifier, damage_To_Self_Magnifier)

            if self.effect == 'magic':
                damage = user.raw_magic_damage(self.cost) * self.multiplier * (user.faith/100) * (target.faith/100)
                damage_To_Enemy_Magnifier = element_type_calculator(user, target, grid_positions, grid_objects, playerGroup) * elemental_Object_Compare(self, target)
                damage_To_Self_Magnifier = element_type_calculator(target, user, grid_positions, grid_objects, playerGroup) * elemental_Object_Contrast(user, self)
                damage, damage_To_Enemy, damage_To_Self = attack_damage_modifier(user, target, damage, damage_To_Enemy_Magnifier, damage_To_Self_Magnifier)

            if self.effect == 'item':
                damage_To_Enemy = self.points * self.multiplier

            if self.effect == 'status':
                if self.status_effect == 'KO' or self.status_effect[1] == 'KO':
                    if self.intention == '-':
                        damage_To_Enemy = target.hit_Points
                    elif self.intention == '+':
                        damage_To_Enemy = self.points - target.hit_Points

            if self.effect == 'heal':
                damage_To_Enemy = damage_To_Enemy * -1
                        
            total_cost = total_cost + cost + damage_To_Self
            target.forecast_display(chance, damage_To_Enemy, s_effect)
        user.forecast_display(cons_chance, total_cost, s_effect)

    def use_action(self, user, action_Timeflow_List, grid_positions, gp_dict, grid_objects, playerGroup):
        x,y = user.rect.topleft
       #print x, y
        cx = x /100
        cy = y /100
       #print cx, cy
        ca_turn = True
        self.att_Turn = True
        potential_Targets = self.range_display(user)
       #print potential_Targets, 'potential targets'
        surf = pygame.display.get_surface()
        #something = raw_input('out of range display, did it yupdate?')
        i = 0
        players = []
        while ca_turn == True:
            for event in pygame.event.get():
                #Battle_Surface_Refresh(grid_positions, grid_objects)
                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    mx, my = event.pos
                    gmx = mx/100
                    gmy = my/100
                    tmx = gmx * 100
                    tmy = gmy * 100
                    list_of_targets = pixel_to_grid_converter(playerGroup)
                    
                    #while ca_turn == True:
                    if self.area_Of_Effect == None and self.ability_Radius == 0:
                        #for target in list_of_targets:
                        distance = abs(cx - gmx) + abs(cy - gmy)
                        if (gmx, gmy) in potential_Targets : # and (gmx, gmy) == target and 
                           #print gmx, gmy,  list_of_targets #, target
                            if (abs(cx - gmx) + abs(cy - gmy)) <= self.ability_Range:
                                for player in playerGroup:
                                   #print player.name
                                    #print target
                                   #print player.rect.topleft
                                    pt = (player.rect.topleft[0]/100, player.rect.topleft[1]/100)
                                    if pt == (gmx, gmy): #target:
                                       #print player.name, 'is the target'
                                        #print group[i]
                                        turn_input = 0
                                        acts_taken = []
                                        acts_taken.append(turn_input)
                                        players.append(player)
                                        
                                    elif pt != (gmx, gmy):
                                        pass
                            l = len(players)
                            if l == 1:
                                players = players[0]
                                #self, user, target, grid_positions, gp_dict, grid_objects, playerGroup,  AI = False, move = None):
                                self.forecaster1(user, players, grid_positions, gp_dict, grid_objects, playerGroup)
                            elif l > 1:
                                self.forecaster2(user, players, grid_positions, gp_dict, grid_objects, playerGroup)
                            #the forecaster needs to go here, while displaying the confirmation box simultaneously
                            surf = pygame.display.get_surface()
                            selection = yes_or_no(surf)
                            if selection == True:
                                ca_turn = False
                                user.att_Turn = False

                                if self.speed == 0:
                                    Battle_Surface_Refresh(grid_positions, grid_objects, playerGroup)
                                    ca_turn = self.action_effect(user, players, distance, grid_positions, grid_objects, playerGroup)
                                    user.att_Turn = False
                                    time.sleep(3)
                                    
                                elif self.speed > 0:
                                    Battle_Surface_Refresh(grid_positions, grid_objects, playerGroup)
                                    ca_turn = self.delayed_action(user, players, distance, action_Timeflow_List, grid_positions, grid_objects, playerGroup)
                                    user.att_Turn = False
                                    time.sleep(3)
                                    
                            elif selection == False:
                                ca_turn = False
                            elif selection != (True or False):
                                selection = yes_or_no(surf)

                        elif (gmx, gmy) not in potential_Targets:
                            pass
                        
                        #i = i + 1
                        #elif (gmx, gmy) != list_of_targets[i] or (gmx, gmy) not in potential_Targets :
                        elif (gmx, gmy) not in potential_Targets:
                        #else: #changed this 2/9/05 to see if ti would fix the targeting out of range issue
                            return ca_turn
                        i = i + 1
                        
                    elif self.area_Of_Effect != None and self.ability_Radius == 0:
                       #print 'area of affect loop'
                        targets = []
                        
                        for player in playerGroup:
                            pt = (player.rect.topleft[0]/100, player.rect.topleft[1]/100)
                            #if pt == target:
                           #print player.name, pt, 'name and pt'
                           #print list_of_targets
                            if (player != user) and (pt in potential_Targets):
                               #print player.name, user.name, pt, 'name and self name and pt and target' #target,
                                targets.append(player)                                    
                                i = i + 1
                                
                       #print targets
                        o = raw_input('what the fuck is going on')
                        l = len(targets)
                        if l == 1:
                            targets = targets[0]
                            self.forecaster1(user, targets, grid_positions, gp_dict, grid_objects, playerGroup)
                        elif l > 1:
                            self.forecaster2(user, targets, grid_positions, gp_dict, grid_objects, playerGroup)
                        selection = None
                        while selection == None:
                            selection = yes_or_no(surf)
                            if selection == True:
                            #if confirmation == ('1' or 'yes'):
                                #j = 0
                                if self.speed == 0:
                                    #for target in targets: #for j in len(targets):
                                    Battle_Surface_Refresh(grid_positions, grid_objects, playerGroup)
                                    self.action_effect(user, targets, 1, grid_positions, grid_objects, playerGroup)
                                    time.sleep(1)
                                    #j = j + 1
                                    ca_turn = False
                                    user.att_Turn = False
                                else:
                                    #for target in targets: #for j in len(targets):
                                    Battle_Surface_Refresh(grid_positions, grid_objects, playerGroup)
                                    self.delayed_action_effect(user, targets, 1, action_Timeflow_List, grid_positions, grid_objects, playerGroup)
                                    time.sleep(1)
                                    #j = j + 1
                                    ca_turn = False
                                    user.att_Turn = False
                            elif selection == False:
                            #elif confirmation == ('2' or 'no'):
                                user.att_Turn = True
                                ca_turn = False
                            elif selection != (True or False):
                            #elif confirmation != ('1' or '2' or 'yes' or 'no'):
                                #confirmation == '0'
                                selection = yes_or_no(surf)

                    elif self.ability_Radius > 0:
                       #print 'in radius loop'
                        if (gmx, gmy) in potential_Targets:
                            potential_Targets2 = self.ability_range_finder(user, self.ability_Radius, gmx, gmy)
                           #print potential_Targets2, 'potential_Targets2'
                            Battle_Surface_Refresh(grid_positions, grid_objects, playerGroup)
                            effect_Area = self.range_display(user, potential_Targets2)
                            #pygame.display.update()
                           #print effect_Area, 'effect area', 
                            targets = []
                           #print effect_Area
                            for player in playerGroup:
                               #print player.name, self.name, 'player and self.name'
                                pt = (player.rect.topleft[0]/100, player.rect.topleft[1]/100)
                                if (pt in  potential_Targets2): #(player.name != user.name) and (pt in  potential_Targets):
                                    targets.append(player)

                            l = len(targets)
                            if l == 1:
                                targets = targets[0]
                                self.forecaster1(user, targets, grid_positions, gp_dict, grid_objects, playerGroup)
                            elif l > 1:
                                self.forecaster2(user, targets, grid_positions, gp_dict, grid_objects, playerGroup)
                                
                            selection = None
                            while selection == None:
                                selection = yes_or_no(surf)
                                if selection == True:
                                    if self.speed == 0:
                                        #for target in targets: #for j in len(targets):
                                        Battle_Surface_Refresh(grid_positions, grid_objects, playerGroup)
                                        self.action_effect(user, targets, 1, grid_positions, grid_objects, playerGroup)
                                        time.sleep(1)
                                        #j = j + 1
                                        ca_turn = False
                                        user.att_Turn = False
                                    else:
                                        #for target in targets: #for j in len(targets):
                                        Battle_Surface_Refresh(grid_positions, grid_objects, playerGroup)
                                        self.delayed_action(user, targets, 1, action_Timeflow_List, grid_positions, grid_objects, playerGroup)
                                        time.sleep(1)
                                        #j = j + 1
                                        ca_turn = False
                                        user.att_Turn = False

                                elif selection == False:
                                    user.att_Turn = True
                                    ca_turn = False
                                elif selection != (True or False):
                                    selection = yes_or_no(surf)
                        elif (gmx, gmy) not in potential_Targets:
                            pass
                            #print confirmation
        Battle_Surface_Refresh(grid_positions, grid_objects, playerGroup)                        
        return ca_turn

    def ai_use_action(self, user, action_Timeflow_List, grid_positions, gp_dict,
                      grid_objects, playerGroup, targets, p_move = None):
        
        x,y = user.rect.topleft
        cx = x /100
        cy = y /100
        ca_turn = True
        #self.att_turn = True
        if user.att_Turn == True:
            potential_Targets = self.range_display(user)
            surf = pygame.display.get_surface()
            i = 0
            l = len(targets)
            
            if self.area_Of_Effect == None and self.ability_Radius == 0:
                dx, dy = targets[0].rect.topleft[0]/ 100, targets[0].rect.topleft[1]/100
                distance = abs(cx - dx) + abs(cy - dy)
                
                if l == 1:
                    targets = targets[0]
                    self.forecaster1(user, targets, grid_positions, gp_dict, grid_objects, playerGroup)
                elif l > 1:
                    self.forecaster2(user, targets, grid_positions, gp_dict, grid_objects, playerGroup)

                Battle_Surface_Refresh(grid_positions, grid_objects, playerGroup)

                if self.speed == 0:
                    ca_turn = self.action_effect(user, targets, distance, grid_positions, grid_objects, playerGroup)
                    
                elif self.speed > 0:
                    ca_turn = self.delayed_action(user, targets, distance, action_Timeflow_List, grid_positions, grid_objects, playerGroup)
            
            elif self.area_Of_Effect != None and self.ability_Radius == 0:
                
                if l == 1:
                    targets = targets[0]
                    self.forecaster1(user, targets, grid_positions, gp_dict, grid_objects, playerGroup)
                elif l > 1:
                    self.forecaster2(user, targets, grid_positions, gp_dict, grid_objects, playerGroup)

                Battle_Surface_Refresh(grid_positions, grid_objects, playerGroup)

                if self.speed == 0: #area effect = none and radius = 0
                    self.action_effect(user, targets, 1, grid_positions, grid_objects, playerGroup)
                    
                elif self.speed > 0:
                    self.delayed_action_effect(user, targets, 1, action_Timeflow_List, grid_positions, grid_objects, playerGroup)
                    
                elif self.ability_Radius > 0:
                    #if (gmx, gmy) in potential_Targets:
                    potential_Targets2 = self.ability_range_finder(user, self.ability_Radius, gmx, gmy) #,p_move)
                    Battle_Surface_Refresh(grid_positions, grid_objects, playerGroup)
                    effect_Area = self.range_display(user, potential_Targets2)
                    for target in playerGroup:
                       #print player.name, self.name, 'player and self.name'
                        pt = (player.rect.topleft[0]/100, player.rect.topleft[1]/100)
                        if (pt in  potential_Targets2): #(player.name != user.name) and (pt in  potential_Targets):
                            targets.append(player)

                    if l == 1:
                        targets = targets[0]
                        self.forecaster1(user, targets, grid_positions, gp_dict, grid_objects, playerGroup)
                    elif l > 1:
                        self.forecaster2(user, targets, grid_positions, gp_dict, grid_objects, playerGroup)

                    Battle_Surface_Refresh(grid_positions, grid_objects, playerGroup)
                    if self.speed == 0:
                        self.action_effect(user, targets, 1, grid_positions, grid_objects, playerGroup)
                    
                    else:
                        self.delayed_action(user, targets, 1, action_Timeflow_List, grid_positions, grid_objects, playerGroup)

            time.sleep(1)
            #j = j + 1
            ca_turn = False
            user.att_Turn = False
            #print 'what the action used?'

                                #print confirmation
            Battle_Surface_Refresh(grid_positions, grid_objects, playerGroup)
        else:
            #print 'the action wasnt used'
            pass
        #return ca_turn

    def ability_range_finder(self, user = None, radius = 0, gmx = 0, gmy = 0, p_move = None): #**shape):
            #what is th epurpose of pmove versus gmx, gmy
        #gmx gmy should relflect the targeted tile, whereas pmove is the potential movement of the character
        #might need have to rework this...
        #actually, needs to serve both user and ai, which is what lead to all this ridiclousness... maybe I should write something new instead of trying to retrofit everything
        i = 0
        j = 0
       #print user, 'user', radius, 'radius', gmx, gmy, 'gmx and gmy', p_move, 'p move'
        if p_move == None:
            x = user.rect.topleft[0]/GRID_WIDTH
            y = user.rect.topleft[1]/GRID_HEIGHT
        elif p_move != None:
            x, y = p_move
        potential_Targets = []
        if (gmx != 0 and gmy != 0) and p_move == None:
            if radius > 0:
               #print 'radius loop'
                for i in range(0, COLUMNS):
                    for j in range(0, ROWS):
                        if abs(i-gmx) + abs(j-gmy) <= radius :
                            potential_Targets.append((i,j))
               #print potential_Targets
                return potential_Targets
        
        if self.ability_Range != 0 and self.ability_Shape == None: #is that supposed to be != to 0?
            for i in range(0, COLUMNS):
                for j in range(0, ROWS):
                    if abs(i-x) + abs(j-y) <= self.ability_Range :
                        potential_Targets.append((i,j))
        elif self.ability_Range == 0 and self.ability_Shape == None:
            potential_Targets.append((x,y))
            
        if self.ability_Range != 0 and self.ability_Shape == 'line':
            while i <= self.ability_Range:
                if (x + i) <= ROWS:
                    potential_Targets.append(((x + i), y))
                if (y + i) <= COLUMNS:
                    potential_Targets.append((x, (y + i)))
                if (x - i) >= 0:
                    potential_Targets.append(((x-i), y))
                if (y - i) >= 0:
                    potential_Targets.append((x, (y-i)))
                i = i +1
			
        if self.ability_Range != 0 and self.ability_Shape == 'square':
            diagonal = (self.ability_Range - 1)/2
            length = range(x - diagonal, x + diagonal + 1)
            width = range(y - diagonal, y + diagonal + 1)
            i = 0
            j = 0
            for i in range(0, len(length)):
                for j in range(0, len(width)):
                    potential_Targets.append((length[i], width[j]))
                    j = j + 1
                i = i +1
                j = 0
        
        return potential_Targets

    def range_display(self, user, potential_Targets = 0): #why is potential_Targets defaulted to 0...?
        if potential_Targets == 0:
           #print 'range display 1'
            potential_Targets = self.ability_range_finder(user)
            i = 0
            j = []
            for i in range(0, len(potential_Targets)):
                grid_Potential_Targets = pygame.Rect((potential_Targets[i][0] * 100),(potential_Targets[i][1] * 100), GRID_WIDTH, GRID_HEIGHT)
                pygame.draw.rect(windowSurface, YELLOW, grid_Potential_Targets, THICK)
                del grid_Potential_Targets
            pygame.display.update()

            return potential_Targets
        else:
           #print 'range display2'
            i = 0
            #Battle_Surface_Refresh(grid_positions, grid_objects)
            for i in range(0, len(potential_Targets)):
                grid_Potential_Targets = pygame.Rect((potential_Targets[i][0] * 100),(potential_Targets[i][1] * 100), GRID_WIDTH, GRID_HEIGHT)
                pygame.draw.rect(windowSurface, YELLOW, grid_Potential_Targets, THICK)
            pygame.display.update()
            return potential_Targets


thrust =  actions('thrust', 1, 5, {7:"null"}, 'physical', None, 'stagger', 0, 2, None, 0, 'line', 75, 2, True, '-')
#backstab = actions('backstab', 1, int(user.hit_Points_Max * 0.10),{7:"null"}, 'status', None, 'KO',  0, 1, None, 0, None, 35, 0, False, '-')
backstab = actions('backstab', 1, 10,{7:"null"}, 'status', None, 'KO',  0, 1, None, 0, None, 35, 0, False, '-')
riposte = actions('riposte', 1, 1, {7:"null"}, 'status', None, 'riposte', 0, 0, None, 0, None, 100, 1.2, None, '+')
split = actions('split', 1, 15, {7:"null"}, 'physical', None, 'stagger', 0, 1, None, 0, None, 65, 2, True, '-')
cyclone =  actions('cyclone', 1, 5, {7:"null"}, 'physical', None, 'stagger', 0, 3, 'square area', 0, 'square', 80, 0.75, True, '-')
kadabra = actions('kadabra', 1, 10, {7:"null"}, 'physical', None, None, 0, 3, None, 1, None, 75, 1, False, '-')
charge = actions('charge', 1,  5, {7:"null"}, 'physical', None, None, 20, 6, None, 0,None, 100, 1.3, False, '-')
guard = actions('guard', 1, 1, {7:"null"}, 'status', None, 'guard', 0, 0, None, 0, None, 100, 1, None, '+')
retreat = actions('retreat', 1, 1, {7:"null"}, 'move', None, 'retreat', 10, 0, None, 0, None, 100, 1, None, ' ')


class armor(object):
    
    def __init__(self, name, points, equipment_type, inventory_slots,
                 strength, magic, speed, brave, faith, move_Range,
                 status_effects, act = None):
        self.name = name
        self.hit_Points = points
        self.equipment_type = equipment_type
        if self.equipment_type in ('light armor', 'heavy armor', 'robe'):
            self.et = 'armor'
        elif self.equipment_type in ('helmet', 'hat'):
            self.et = 'helmet'
        self.inventory_slots = inventory_slots
        #print self.inventory_slots, 'invenbtory slots armor'
        #x = raw_input('what it is?')
        self.strength = strength
        self.magic = magic
        self.speed = speed
        self.brave = brave
        self.faith = faith
        self.move_Range = move_Range
        self.equipment_effects = [self.strength, self.magic, self.speed,
                                  self.brave, self.faith, self.move_Range]
        self.status_effects = {}
        self.image = []
        self.act = act
        #if self.equipment_type == ('light armor' or 'robe' or 'hat'):
        #    retreat = actions('retreat', 1, 1, {7:"null"}, 'move', None,
        #                      'retreat', 0, 0, None, 0, None, 100, 1, None, ' ')
        
    def equip_armor(self, user, t_inventory, eq = None):
        if len(t_inventory) == 1:
            t_inventory = list(t_inventory)
        if eq == 'helmet':
            user.helmet = self
            user.equipment[2] = self
            
            for article in t_inventory:

                if article == self.et:
                    for art in t_inventory[article]:
                        if art == self:
                            t_inventory['all'].remove(art)
                            t_inventory[self.et].remove(art)

        elif eq == 'armor':
            user.armor = self
            user.equipment[3]

            for article in t_inventory:
                if article == self.et:
                    for art in t_inventory[article]:
                        if art == self:
                            t_inventory['all'].remove(art)
                            t_inventory[self.et].remove(art)

        user.hit_Points_Max = user.hit_Points_Max + self.hit_Points
        user.hit_Points = user.hit_Points_Max
        if self.inventory_slots > 0:
            user.inventory_slots = user.inventory_slots + self.inventory_slots

        #if self.equipment_type == ('light armor' or 'robe' or 'hat'):
        if self.act != None:
            user.abilities[self.act.name] = True
            #retreat = actions('retreat', 1, 1, {7:"null"}, 'move', None, 'retreat', (user.speed * 5), 0, None, 0, None, 100, 1, None, ' ')
            user.actions[self.act.name] = self.act

    def unequip_armor(self, user, t_inventory, eq = None):
        user.hit_Points_Max = user.hit_Points_Max - self.hit_Points
        user.hit_Points = user.hit_Points_Max
        i = 0
        j = self.inventory_slots
        slots = user.inventory.keys()
        number = len(slots)
        if j > 0:
            while i <= j:
                name = 'slot' + str((number - 1) - i)
                if user.inventory.has_key(name) == True:
                    article = user.inventory.pop(name)
                    t_inventory['all'].append(article.name[article])
                    t_inventory[article.et].append(article)
                    i = i +1
                elif user.inventory.has_key(name) == False:
                    i = i + 1
        i = 0
        if self.equipment_type == ('light armor' or 'robe'):
            user.abilities.keys()
            del user.abilities['retreat'] 
            #retreat = actions('retreat', 1, 1, {7:"null"}, 'move', None, 'retreat', (user.speed * 5), 0, None, 0, None, 100, 1, None, ' ')
            del user.actions['retreat']
        if eq == 'helmet':
            x = user.helmet
            t_inventory['all'].append(x)
            t_inventory[user.helmet.et].append(x)
            user.helmet = None
            user.equipment[2] = None
        elif eq == 'armor':
            x = user.armor
            t_inventory['all'].append(x)
            t_inventory[user.armor.et].append(x)
            user.armor = None
            user.equipment[3] = None
        user.inventory_slots = user.inventory_slots - self.inventory_slots

class item(object):
    def __init__(self, name, points, element_type, effect, item_Type,
                 effect_string, status_effect, speed, ability_Range,
                 area_Of_Effect, ability_Radius, ability_Shape, accuracy,
                 multiplier, consequence, intention):
        self.name = name
        self.points = points
        self.cost = 0
        self.element_type = element_type
        self.effect = effect #effect types : magic, physical, heal, status, other
        self.effect_string = effect_string # to be evaled and saved as a variable, which will be used to manipulate stats,11/25/2014 maybe not so much 
        self.status_effect = status_effect
        self.equipment_type = 'item'
        self.et = 'item'
        self.speed = speed 
        self.ability_Range = ability_Range
        self.area_Of_Effect = area_Of_Effect
        self.ability_Radius = ability_Radius
        self.ability_Shape = ability_Shape
        self.accuracy = accuracy
        self.multiplier = multiplier
        self.consequence = consequence
        self.intention = intention

    def equip_Item(self, user, t_inventory):
        y = False
        x = self.name
        z = user.inventory_slots
        w = len(user.inventory)
        #print w, z, 'w and z in equip_Item'
        if w < z:
            #print 'w is less than z'
            if user.abilities.get(self.name) == True and user.abilities[self.name] == True:#and len(user.inventory) < (user.inventory_Max_Length):
                user.inventory[self.name]= self
                y = actions( self.name, self.points, self.cost, self.element_type,
                            self.effect, self.effect_string, self.status_effect,
                            self.speed, self.ability_Range, self.area_Of_Effect,
                            self.ability_Radius, self.ability_Shape, self.accuracy,
                            self.multiplier, self.consequence, self.intention)
                user.actions[self.name] = y
                user.actions_CD[y.effect][y.name] = y
                #print 'item equipped and ability'
                t_inventory['all'].remove(self)
                t_inventory[self.et].remove(self)
            elif user.abilities.get(self.name) == False or self.name not in user.abilities:
                user.inventory[self.name]= self
                #print 'item equipped, but not usable by ', user.name
                t_inventory['all'].remove(self)
                t_inventory[self.et].remove(self)
            #print 'items removed from inventory, hopefully'
        else:
            #print 'inventory full'
            pass

##potion = item('potion', 30, {7:'null'}, 'item', 'heal', None, None, 0,
##              1, None, 0, None, 100, 1, False, '+')
##poison = item('poison', -5, {7:'null'}, 'item', 'status', None, 'poison', 0,
##              1, None, 0, None, 100, 1, False, '-')
##grenade = item('grenade', -30, {7:'null'}, 'item', 'hurt', None, None, 20,
##               3, None, 1, None, 100, 1, False, '-')
##phoenix_Down = item('phoenix down', 20, {7:'null'}, 'item', 'status',
##                    None, ('-', 'KO'), 0, 1, None, 0, None, 100, 1, False, '+')
##wood_sword = weapon('wood sword', 100, 'sword', 0,0,0,0,0,0,0,[])
##wood_armor = armor('wood armor', 100, 'heavy armor', 0, 0, 0, 0, 0, 0, 0, [])
##wood_helmet = armor('wood helmet', 100, 'helmet', 0, 0, 0, 0, 0, 0, 0, [])
##items = {'wood sword':wood_sword, 'wood helmet':wood_helmet,
##         'wood armor':wood_armor, 'potion':potion, 'poison':poison,
##         'grenade':grenade, 'phoenix_Down':phoenix_Down}
##items_cost = {'wood sword':50, 'wood helmet':50,
##              'wood armor':50,'potion':20, 'poison':100,
##              'grenade':200, 'phoenix_Down':300}
class potions(object):
    def __init__(self, name, points, item_Range, effect):
        self.name = name
        self.points = points
        self.item_Range = item_Range
        if effect == None or effect == "" or effect == 0:
            self.effect = None
        else:
            self.effect = effect

    def use_potion(self, user, target):
        if 'potion' in user.inventory:
            x = input(' Are you sure you want to use a potion? 1 for yes, 2 for no')# ', target.name, ' ? enter 1 for yes or 2 for no')
            if x == 1 :
                target.hit_Points = target.hit_Points + self.points
                if target.hit_Points > target.hit_Points_Max:
                    target.hit_Points = target.hit_Points_Max
                    user.inventory.remove('potion')
            if x != 1:
                user.att_Turn = True
                #ca_turn = False
        else:
            user.att_Turn = True
           #print "potion not used"
            #ca_turn = False
        #return ca_turn
 
#what about deceased team members becoming equipment, or their spirits habitating their old equipment?

#after so many errors with the character creator, i think it would make a lot more sense to just use dictionarys, so i don't have to worry about the indexing, 10/17/14
class character:

    def __init__(self, y, side):
        if y == 1:
            self.name, self.element_type, self.attack, self.defense, self.sp_defense, self.sp_attack, self.move, self.att_range, self.potential, self.attribute_points, self.impermeable_points, self.image, self.rect, self.speed, self.evade, self.ct, self.hit_Points, self.move_Turn, self.att_Turn, self.status = self.create_character()
            self.data = [self.name, self.element_type, self.attack, self.defense, self.sp_attack, self.sp_defense, self.move, self.att_range, self.potential, self.image, self.rect, self.speed, self.evade, self.ct, self.hit_Points_Max, self.hit_Points, self.Move_Turn, self.att_Turn, self.status]

        if y == 2:
            weapons = ('sword', 'spear', 'axe', 'bow', 'wand', 'knuckles', 'knife', 'shield')
            weapons_act = {'sword':riposte, 'spear':thrust, 'axe':cyclone, 'bow':charge, 'wand':kadabra, 'knuckles':None, 'knife':backstab, 'shield':guard}
            armors = [('heavy armor', 'light armor', 'robe'), (20, 8, 3), (None, retreat, retreat)]
            helmets = [('helmet', 'hat'), (15, 5), (None, retreat)]
            #armors_act = {'heavy armor': None, 'light armor': retreat, 'robe':retreat, 'helmet':None, 'hat':None
            x = randrange(0, 2)
            wg = randrange(0,8)
            #wg = input('0 for sword, spear, axe, bow, wand, knuckles, knife, shield : ')
            ag = randrange(0,3)
            hg = randrange(0,2)
            ig = randrange(0,4)
            self.sex, self.strength, self.magic, self.speed, self.hit_Points, self.stamina, self.leadership, self.discipline, self.intelligence = self.core_stats(x)
            self.leader = False
            self.hit_Points_Max = self.hit_Points
            self.exp = 0
            self.level = 1
            self.name = self.character_name_creator()
            self.element_type, self.element = self.random_element_type()
            self.allegiance = side
            self.rank = 'private'
            self.brave = int(gauss(55, 5))
            self.faith = int(gauss(55, 5))
            self.root_Strength = self.strength
            self.root_Magic = self.magic
            self.root_Speed = self.speed
            self.root_Hit_Points_Max = self.hit_Points
            self.root_Stamina = self.stamina
            self.root_Leadership = self.leadership
            self.c_Evade = int(gauss(10, 1))
            self.s_Evade = 0
            self.a_Evade = 0
            self.w_Evade = 0
            self.t_Evade = self.c_Evade + self.s_Evade + self.a_Evade + self.w_Evade
            self.root_C_Evade = self.c_Evade
            self.root_T_Evade = self.t_Evade
            self.move_Range = 3
            self.att_Range = 1
            self.root_Move_Range = self.move_Range
            self.root_Att_Range = self.att_Range
            self.cost = self.root_Strength + self.root_Magic + self.root_Speed + self.root_Hit_Points_Max + self.root_Stamina + self.root_Move_Range 
            self.status = {}
            self.job = "Character"
            self.available_Jobs = {"Character": True}
            pmn = randrange(0,5)
            smn = randrange(0,5)
            motivations = {0:'gold', 1:'glory', 2:'god', 3:'family', 4:'country'}
            self.motivation1 = motivations[pmn]
            self.motivation2 = motivations[smn]
            self.actions_CD = {'physical':{}, 'item':{}, 'status':{}, 'move':{}}
            #(self, name, points, equipment_type, strength, magic, speed, brave, faith, w_Evade, move_Range, equipment_effects )
            self.weapon = weapon(weapons[wg],3,weapons[wg],0,0,0,0,0,0,0,[], weapons_act[weapons[wg]])
            self.off_Hand = None
            self.armor = armor(armors[0][ag], armors[1][ag], armors[0][ag], 1, 0, 0, 0, 0, 0, 0, [], armors[2][ag])
            self.helmet = armor(helmets[0][hg], helmets[1][hg], helmets[0][hg], 1, 0, 0, 0, 0, 0, 0, [], helmets[2][hg])
            self.accessory = None
            self.equipment_Capable = {}
            self.actions = {}
            self.abilities = {}
            self.active_Abilities = {}
            self.field_Abilities = None
            if self.allegiance == 'loyalist':
                self.image = ch_Images[randrange(0,4)]
            elif self.allegiance == 'rebel':
                self.image = ch_Images[randrange(4,8)]
            self.root_Image = self.image
            self.rect = self.image.get_rect()
            self.grid_Char_Rect = (int(self.rect.topleft[0]/GRID_WIDTH), int(self.rect.topleft[1]/GRID_HEIGHT))
            self.ct = 0
            self.move_Turn = False
            self.att_Turn = False
            self.melee_options = {'move':self.character_move,
                                  'action':self.character_action,
                                  'wait':self.wait,
                                  'status':self.id_card,
                                  'inquire':self.inquire}
            self.inventory = {}
            self.inventory_slots = 0
            #potion = potions('potion', 30, 1, None)
            #self.inventory.append(items[ag])
            self.direction = SOUTH
            #print potion.name
            self.action_charging = 0
            
            potion = item('potion', 30, {7:'null'}, 'item', 'heal', None, None, 0,
                      1, None, 0, None, 100, 1, False, '+')
            poison = item('poison', -5, {7:'null'}, 'item', 'status', None, 'poison', 0,
                      1, None, 0, None, 100, 1, False, '-')
            grenade = item('grenade', -30, {7:'null'}, 'item', 'hurt', None, None, 20,
                      int(self.strength * 2/3), None, 1, None, 100, 1, False, '-')
            phoenix_Down = item('phoenix down', 20, {7:'null'}, 'item', 'status',
                                None, ('-', 'KO'), 0, 1, None, 0, None, 100, 1, False, '+')
            items = (potion, poison, grenade, phoenix_Down)
            inventories = {'rebel':tp_Inventory, 'loyalist':te_Inventory}
            inventories[self.allegiance]['weapon'].append(self.weapon)
            inventories[self.allegiance]['all'].append(self.weapon)
            inventories[self.allegiance]['helmet'].append(self.helmet)
            inventories[self.allegiance]['all'].append(self.helmet)
            inventories[self.allegiance]['armor'].append(self.armor)
            inventories[self.allegiance]['all'].append(self.armor)
            self.equipment = [self.weapon, self.off_Hand, self.helmet,
                              self.armor,self.accessory, self.inventory]
            self.equip_equipment(inventories[self.allegiance])
            self.relationships = {}
            self.abilities[items[ig].name] = True
            inventories[self.allegiance]['item'].append(items[ig])
            inventories[self.allegiance]['all'].append(items[ig])
            items[ig].equip_Item(self,inventories[self.allegiance])
            self.data = [self, self.sex, self.strength, self.magic, self.speed,
                         self.hit_Points, self.hit_Points_Max, self.stamina, self.exp,
                         self.level, self.name, self.element_type,
                         self.element, self.allegiance, self.brave, self.faith, self.speed,
                         self.root_Strength, self.root_Magic, self.root_Speed,
                         self.root_Hit_Points_Max, self.c_Evade, self.s_Evade,
                         self.a_Evade, self.w_Evade, self.move_Range,
                         self.att_Range, self.status, self.job,
                         self.available_Jobs, self.equipment,
                         self.equipment_Capable, self.actions, self.abilities,
                         self.active_Abilities, self.image, self.rect,
                         self.ct, self.move_Turn, self.att_Turn, self.inventory]
            
            self.lst = [self]

    def __len__(self):
        return len(self.lst)

    def __getitem__(self, i):
        return self.data[i]
    

    def create_character(self):
        character_name = raw_input("what is the name of your character? ")
        element_type = input("what elemental type would you like? \n 1 = null \n 2 = fire \n 3 = water \n 4 = earth \n 5 = sky \n 6 = void \n 7 = infinity \n:")
        attribute_points = 15
       #print " you will be given 15 attribute points to allocate to \n allocate to attack, special attack, defense and special defense \n use your points wisely. \n you cannot allocate 0 points to a category \n"
        #att = "attack "
        #dfn = "defense"
        #sp_att = "special attack"
        #sp_def = "special defense"
        while attribute_points > 0:
            attack = input("attack :")
            defense = input ("defense :")
            sp_defense = input ("special defense :")
            sp_attack = input ("special attack :")
            attribute_points = attribute_points - (attack + defense + sp_defense + sp_attack)
            while attribute_points < 0 :
               #print " no cheating! only 15 points allowed"
                attack = input("attack :" )
                defense = input("defense :")
                sp_attack = input ("special attack :")
                sp_defense = input ("special defense :")
           #print " you will be given 6 points for allocating to impermeable attributes \n move range, attack range, and potential \n use your points wisely, every attribute must be at least 1 "
        impermeable_points = 6
        while impermeable_points > 0:
            move = input("move range :")
            att_range = input ("attack range :")
            potential = input ("potential :")
            impermeable_points = impermeable_points - (move + att_range + potential)
            while impermeable_points < 0 :
               #print " no cheating, cheater pants! fix yourself"
                move = input ("move range :")
                att_range = input ("attack range :")
                potential = input ("potential :")
        image = input("which image would you like? pick a number from 0 to including 3")
        image = ch_Images[image]
        rect = image.get_rect()
        speed = randrange(5,8)
        evade = randrange(speed, 3 * speed)
        ct =  ct = randrange(0, (20- (attack + defense + move + att_range)))
        hit_Points_Max = randrange(20 - (attack + sp_attack), 20 + (defense + sp_defense))
        hit_Points = hit_Points
        move_Turn = False
        att_Turn = False
        status = {"normal"}
        return name, element_type, attack, defense, sp_attack, sp_defense, move, att_range, potential, attribute_points, impermeable_points, image, rect, speed, evade, ct, hit_Points_Max, hit_Points, Move_Turn, Att_Turn, status

    def random_character_creator(self):
        name = self.character_name_creator()
       #print "Name: " + name
        element_type = self.random_element_type()
       #print "element type: ", element_type
        attack, defense, sp_attack, sp_defense = self.random_attribute()
       #print "attack: ", attack, "\ndefense: ", defense, "\nsp_defense: ", sp_defense, "\nsp_attack: ", sp_attack
        move, att_range, potential = self.random_impermeable_attribute()
       #print "move: ", move, "\natt_range: ", att_range, "\npotential: ", potential
        image = ch_Images[randrange(0,4)]
        rect = image.get_rect()
        speed = randrange(5,8)
        evade = randrange(speed, 3 * speed)
        ct = randrange(0, (20- (attack + defense + move + att_range)))
       #print ct
        hit_Points_Max = randrange(20 - (attack + sp_attack), 20 + (defense + sp_defense))
       #print "hit Points :", hit_Points_Max
        hit_Points = hit_Points_Max
        Move_Turn = False
        Att_Turn = False
        status = {"normal":True}
        return name, element_type, attack, defense, sp_attack, sp_defense, move, att_range, potential, image, rect, speed, evade, ct, hit_Points_Max, hit_Points, Move_Turn, Att_Turn, status

    def core_stats(self, x):
        if x == 0:
            self.sex = "Male"
            self.strength = int(gauss(5,1))
            if self.strength == 0:
                self.strength = 1
            self.magic = int(gauss(4,1))
            if self.magic == 0:
                self.magic = 1
            self.speed = int(gauss(6,1))
            if self.speed == 0:
                self.speed = 1
            self.hit_Points = int(gauss(40, 5))
        else:
            self.sex = "Female"
            self.strength = int(gauss(4,1))
            if self.strength == 0:
                self.strength = 1
            self.magic = int(gauss(5,1))
            if self.magic == 0:
                self.magic = 1
            self.speed = int(gauss(7,1))
            if self.speed == 0:
                self.speed = 1
            self.hit_Points = int(gauss(30, 5))
            self.sex = "Female"
        self.stamina = int(gauss(3,1))
        self.leadership = int(gauss(3, 0.34))
        self.discipline = int(gauss(5, 0.5))
        self.intelligence = int(gauss(5, 1))
        if self.stamina <= 0:
            self.stamina = 1
        if self.discipline <= 0:
            self.discipline = 1
        if self.intelligence <= 0:
            self.intelligence = 1
        return self.sex, self.strength, self.magic, self.speed, self.hit_Points, self.stamina, self.leadership, self.discipline, self.intelligence

    def character_name_creator(self):
        x = randrange(1, 4)
        vowels = [['a','e','i','o','u','h','y',' '],
		  ['aa','ae', 'ai', 'ao','au', 'ah', 'ay'],
		  ['ea','ee', 'ei','eo','eu','eh','ey'],
		  ['ia','ie','io','iu','ih','iy'],
		  ['oa','oe','oi','oo','ou','oh','oy'],
		  ['ua','ue','ui','uo','uu','uh','uy'],
		  ['ha','he','hi','ho','hu','hw','hy'],
		  ['ya','ye','yi','yo','yu','yw']]
        consonants = [['b','c','d','f','g','h','j','k','l','m','n','p',
		       'q','r','s','t','v','w','x','y','z', ' '],
		      ['bh','bl','br','bw','by'],
		      ['ch','ck','cl','cn','cr','cs','cy'],
		      ['dh','dj','dl','dr','dw','dy'],
		      ['fh','fj','fl','fr','fw','fy'],
		      ['gh','gl','gn','gr','gw','gy'],
		      ['ja','je','ji','jo','ju','jy'],
		      ['kh','kl','kn','kr','kw','ky'],
		      ['la','le','li','lh','lo','lu','ly'],
		      ['ma','me','mi','mh','mo','mu','my'],
		      ['na','ne','ni','nh','no','nu','ny'],
		      ['pa','pe','pi','ph','pl','po','pu','py'],
		      ['qa','qe','qi','qh','qo','qu','qy'],
		      ['rr','ra','re','ri','rh','rl','ro','ru','ry'],
		      ['sa','se','si','sh','sl','so','su','sh','sc','sk','sl','sm','sn','sq','sr','st','sv','sy'],
		      ['ta','te','ti','th','to','tu','tr','ts','tw','ty'],
		      ['va','ve','vi','vh','vl','vo','vr','vu','vy'],
		      ['wa','we','wi','wh','wl','wo','wu','wr','wy'],
		      ['xa','xe','xi','xh','xo','xu','xy'],
		      ['za','ze','zi','zh','zo','zu','zy', 'zw']]
        rand_name = ""
        i = 0
        p = randrange(0,2)
        for i in range(x):
            v = randrange(0,8)
            #print v, 'v'
            #print vowels[v]
            v2 = randrange(0, (len(vowels[v])))
            #print v, v2, 'v and v2'
            #print vowels[v][v2], 'vowels[v][v2]'
            c = randrange(0,20)
            #print c, 'c'
            #print consonants[c]
            c2 = randrange(0, (len(consonants[c])))
            #print consonants[c]
            #print c, c2, 'c and c2'
            vowel = vowels[v][v2]
            consonant = consonants[c][c2]
            if p == 0:
                rand_name = rand_name + consonant + vowel
                i = i + 1
            if p == 1:
                rand_name = rand_name + vowel + consonant
                i = i + 1
        if rand_name[-1] == " ":
            rand_name = rand_name[0:-1]
        if rand_name[0] == " ":
            rand_name = rand_name[1:len(rand_name)]
        return rand_name

    def random_element_type(self):
    #character_name, element_type, attack, defense, sp_defense, sp_attack, move, att_range, potential
        element_type = {1:"void", 2:"infinity", 3:"fire", 4:"earth", 5:"water", 6:"sky", 7:"null"}
        r = randrange(1,8)
        r_element_type = r
        element = element_type[r]
        return r_element_type, element

    def random_attribute(self):
        first_attribute = randrange(1,4)
        if first_attribute == 1:
            attack = randrange(1,12)
            defense = randrange(1, 1 + (12 - attack))
            sp_defense = randrange(1, 1 + (13 - (attack + defense)))
            sp_attack = randrange(1, 1 + 14 - (attack + defense + sp_defense))
            remaining_points = 15 - (attack + defense + sp_defense + sp_attack)
            if remaining_points > 0:
                x = randrange(1,4)
                if x ==1:
                    attack = attack + remaining_points
                if x ==2:
                    defense = defense + remaining_points
                if x ==3:
                    sp_defense = sp_defense + remaining_points
                if x ==4:
                    sp_attack = sp_attack + remaining_points
        if first_attribute == 2:
            defense = randrange(1,12)
            sp_defense = randrange(1, 1 + (12 - defense))
            sp_attack = randrange(1, 1 + (13 - (sp_defense + defense)))
            attack = randrange(1, 1 + 14 - (sp_attack + defense + sp_defense))
            remaining_points = 15 - (attack + defense + sp_defense + sp_attack)
            if remaining_points > 0:
                x = randrange(1,4)
                if x ==1:
                    attack = attack + remaining_points
                if x ==2:
                    defense = defense + remaining_points
                if x ==3:
                    sp_defense = sp_defense + remaining_points
                if x ==4:
                    sp_attack = sp_attack + remaining_points
        if first_attribute == 3:
            sp_defense = randrange(1,12)
            sp_attack = randrange(1, 1 + (12 - sp_defense))
            attack = randrange(1, 1 + (13 - (sp_attack + sp_defense)))
            defense = randrange(1, 1 + 14 - (attack + sp_defense + sp_attack))
            remaining_points = 15 - (attack + defense + sp_defense + sp_attack)
            if remaining_points > 0:
                x = randrange(1,4)
                if x ==1:
                    attack = attack + remaining_points
                if x ==2:
                    defense = defense + remaining_points
                if x ==3:
                    sp_defense = sp_defense + remaining_points
                if x ==4:
                    sp_attack = sp_attack + remaining_points
        if first_attribute == 4:
            sp_attack = randrange(1,12)
            attack = randrange(1, 1 + (12 - sp_attack))
            sp_defense = randrange(1, 1 + (13 - (attack + sp_attack)))
            defense = randrange(1, 1 + 14 - (sp_attack + attack + sp_defense))
            remaining_points = 15 - (attack + defense + sp_defense + sp_attack)
            if remaining_points > 0:
                x = randrange(1,4)
                if x ==1:
                    attack = attack + remaining_points
                if x ==2:
                    defense = defense + remaining_points
                if x ==3:
                    sp_defense = sp_defense + remaining_points
                if x ==4:
                    sp_attack = sp_attack + remaining_points
        return attack, defense, sp_attack, sp_defense

    def random_impermeable_attribute(self):
        first_attribute = randrange(1,3)
        if first_attribute == 1:
            move = randrange(1,4)
            att_range = randrange(1, 1 + (4 - move))
            potential = randrange(1, 1 + (5 - (move + att_range)))
            remaining_points = 6 - (move + att_range + potential)

            if remaining_points > 0:
                x = randrange(1,3)
                if x ==1:
                    move = move + remaining_points
                if x ==2:
                    att_range = att_range + remaining_points
                if x ==3:
                    potential = potential + remaining_points

        if first_attribute == 2:
            att_range = randrange(1,4)
            potential = randrange(1, 1 + (4 - att_range))
            move = randrange(1, 1 + (5 - (potential + att_range)))
            remaining_points = 6 - (move + att_range + potential)

            if remaining_points > 0:
                x = randrange(1,3)
                if x ==1:
                    move = move + remaining_points
                if x ==2:
                    att_range = att_range + remaining_points
                if x ==3:
                    potential = potential + remaining_points

        if first_attribute == 3:
            potential = randrange(1,4)
            move = randrange(1, 1 + (4 - potential))
            att_range = randrange(1, 1 + (5 - (potential + att_range)))
            remaining_points = 6 - (move + att_range + potential)

            if remaining_points > 0:
                x = randrange(1,3)
                if x ==1:
                    move = move + remaining_points
                if x ==2:
                    att_range = att_range + remaining_points
                if x ==3:
                    potential = potential + remaining_points
        return move, att_range, potential

    def equip_equipment(self, t_inventory):
        #inv_slots = 0
        if self.weapon != None:
            self.weapon.equip_weapon(self, t_inventory)
        if self.armor != None:
            self.armor.equip_armor(self, t_inventory, 'armor')
            #print inv_slots + self.armor.inventory_slots, 'inv slots and armor slots'
            #inv_slots = inv_slots + self.armor.inventory_slots
        if self.helmet != None:
            self.helmet.equip_armor(self, t_inventory, 'helmet')

    def unequip_equipment(self, t_inventory):
        inv_slots = 0
        #if self.weapon != None:
        self.weapon.unequip_weapon(self, t_inventory)
        #if self.armor != None:
        self.armor.unequip_armor(self, t_inventory, 'armor')
        inv_slots = inv_slots + self.armor.inventory_slots
        #if self.helmet != None:
        self.helmet.unequip_armor(self, t_inventory, 'helmet')
        inv_slots = inv_slots + self.helmet.inventory_slots
        #self.inventory_slots = self.inventory_slots - inv_slots


    def hit_or_miss(self, target, distance):
        x = randrange(0, 101)
       #print x
       #print distance
       #print (target.t_Evade + 5 * distance)
        if x > (target.t_Evade + 5 * distance):
            return True
        else:
            return False

    def weapon_attack(self, t, group, grid_positions, grid_objects, playerGroup):#group, i, distance, grid_positions, grid_objects, playerGroup):
        x,y = self.rect.topleft
        cx = x /100
        cy = y /100
        
        valid_Targets = self.range_display(t)
        ca_turn = True
        while ca_turn == True:
            for event in pygame.event.get():
               #print " entering weapon attack loop"
                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    mx, my = event.pos
                    gmx = mx/100
                    gmy = my/100
                    tmx = gmx * 100
                    tmy = gmy * 100
                   #print "cx and cy are ", cx, cy
                   #print "print mx and my are ", mx, my
                   #print "print gmx and gmy ", gmx, gmy
                   #print "mouse press good"
                   #print "abs (", cx, " -", gmx, " ) + abs(", cy, " - ", gmy, ") = ",(abs(cx - gmx) + abs(cy - gmy))
                   #print "self.att_range = ", self.att_Range
                    list_of_targets = pixel_to_grid_converter(playerGroup)
                    i = 0
                   #print len(list_of_targets)
                   #print valid_Targets
                   #print len(valid_Targets)
                        
                    for i in range(0, len(list_of_targets)):
                       #print "(gmx, gmy): ", (gmx, gmy)
                        #print "list of targets: ", list_of_targets[i]
                        distance = abs(cx - gmx) + abs(cy - gmy)
                        if (gmx, gmy) == list_of_targets[i]:
                            if (abs(cx - gmx) + abs(cy - gmy)) <= self.att_Range:
                               #print "player",i+1, " is the target"
                               #print group[i].name, "is the target"
                                turn_input = 0
                                while turn_input == 0:
                                    turn_input = input("proceed with attack? 1 for weapon attack,  and 2 to cancel")
                                    if turn_input == 1:
                                        hit = self.hit_or_miss(group[i], distance)
                                       #print hit
                                        attack_damage_calculator(self, group[i], distance, hit, grid_positions, grid_objects, playerGroup)
                                        self.status_update()
                                        group[i].status_update()
                                        ca_turn = False
                                        #Battle_Surface_Refresh(grid_positions, grid_objects)
                                        self.att_Turn = False
                                        time.sleep(3)
                                    if turn_input == 2:
                                        self.att_Turn = True
                                        ca_turn = False
                                        #Battle_Surface_Refresh(grid_positions, grid_objects)
                                    if turn_input > 2 or turn_input < 1 :
                                       #print "incorrect value, try again"
                                        turn_input = 0
                        else:
                           #print 'target out of range'
                            i = i + 1
        return ca_turn

    def magic_attack(self, group, i, distance, grid_positions, grid_objects, playerGroup):
        sacrifice = input("How much HP would you like to spend for the magic cost? ")
        hit = self.hit_or_miss(group[i], distance)
        magic_damage_calculator(self, group[i], sacrifice, hit, grid_positions, grid_objects, playerGroup, distance)
        self.status_update()
        group[i].status_update()
        ca_turn = False
        Battle_Surface_Refresh(grid_positions, grid_objects, playerGroup)
        self.att_Turn = False
        time.sleep(3)
        return ca_turn

    def level_up(self):
        if self.exp >= 100:
            self.level = self.level + 1
            self.exp = 0
           #print self.name, " has leveled up their life!"
            #self.root_strength = self.root_strength (+ or * not sure yet) job_Strength_Growth_Rate
            #growth_remainder = self.root_strength - int(self.root_strength)
            #if growth_remainder >= 1:
            #    growth_remainder = 1
            #    self.root_strength = self.root_strength + growth_remainder
            #self.root_magic
            #self.root_speed
            #self.hit_Points_Max
        return self.level, self.exp

    def highlight_character(self):
        #Battle_Surface_Refresh(grid_positions, grid_objects)
        #windowSurface.unlock()
        rect = pygame.draw.rect(windowSurface, ORANGE, self.rect, THICK)
        pygame.display.update()
        #windowSurface.lock()
        #del rect
       #print 'highlighted character'

    def unhighlight_character(self):
        #Battle_Surface_Refresh(grid_positions, grid_objects)
        rect = pygame.draw.rect(windowSurface, BLACK, self.rect, THICK)
        pygame.display.update()
        #del rect
       #print 'unhighlighted character'

    def possible_path(self, start, length, width, move_Range, playerGroup):
       #print 'in possible paths'
        i = 0
        j = 0
        possible_paths = []
        s_sum = start[0] + start[1]
        for i in range (0, length):
            cancel = False
            for j in range(0, width):
                if (abs(start[0] - i) + abs(start[1] - j)) <= move_Range:
                    possible_paths.append((i,j))
                j = j + 1
            i = i + 1   
        return possible_paths

    def bogey_check(self, playerGroup, width):
       #print 'bogey_check'
        bogeys = []
        if len(playerGroup) > 1:
            pass
        elif len(playerGroup) <= 1:
            return bogeys
        for player in playerGroup:
            if player == self:
                pass
            elif player != self:
                if (player.allegiance != self.allegiance) and player.status.has_key('KO') == False:
                    x = player.rect[0]/width
                    y = player.rect[1]/width
                    bogeys.append((x,y))
        return bogeys
            
    def pathfinder(self, start, length, width, obstacles, move_Range, playerGroup):
        #print 'in pathfinder'
        path = []
        paths = []
        beg = start
        start = tuple(start)
        ends = self.possible_path(start, length, width, move_Range, playerGroup)
        for end in ends:
            end = list(end)
            start = beg
            x = list(start)
            y = 0
            path = [tuple(start)]
            move_count = 0
            x_d = start[0] - end[0]
            y_d = start[1] - end[1]
            x_check = False
            y_check = False
            while move_count < move_Range and (x_check == False and y_check == False) and x != end:
            #    print x, y, end, start, beg
            #    print move_count, move_Range, x_check, y_check
                if end in obstacles:
                    x_check = True
                    y_check = True
            #        print 'end in obstacles'
                elif x[0] != end[0] and move_count < move_Range:# and end not in obstacles:
            #        print 'in loop'
                    y = x
                    if x_d > 0:
                        x[0] = x[0] - 1
                    elif x_d < 0:
                        x[0] = x[0] + 1
                    if obstacles == [] or (x[0], x[1]) not in obstacles:
                        #tuple(x)
                        z = (x[0], x[1])
                        path.append(z)
                        move_count = move_count + 1
                    elif (x[0], x[1]) in obstacles:
                        if x_d > 0:
                            x[0] = x[0] + 1
                        elif x_d < 0:
                            x[0] = x[0] - 1
                        if y_d > 0:
                            x[1] = x[1] - 1
                        elif y_d < 0:
                            x[1] = x[1] + 1
                        elif y_d == 0:
                            x_check = True
                            y_check = True
                            move_count = move_Range + 1
                        if obstacles == [] or (x[0], x[1]) not in obstacles:
                            #tuple(x)
                            z = (x[0], x[1])
                            path.append(z)
                            move_count = move_count + 1
                        elif (x[0], x[1]) in obstacles:
                            y_check = True
                            pass
                elif x[1] != end[1] and move_count < move_Range: # and end not in obstacles:
            #        print 'in 2nd loop'
                    y = x
                    if y_d > 0:
                        x[1] = x[1] - 1
                    elif y_d < 0:
                        x[1] = x[1] + 1
                    if obstacles == [] or (x[0], x[1]) not in obstacles:
                        #tuple(x)
                        z = (x[0], x[1])
                        path.append(z)
                        move_count = move_count + 1
                    elif (x[0], x[1]) in obstacles:
                        if y_d > 0:
                            x[1] = x[1] + 1
                        elif y_d < 0:
                            x[1] = x[1] - 1
                        if x_d > 0:
                            x[0] = x[0] - 1
                        elif x_d < 0:
                            x[0] = x[0] + 1
                        elif x_d == 0:
                            x_check = True
                            y_check = True
                            move_count = move_Range + 1
                        if obstacles == [] or (x[0], x[1]) not in obstacles:
                            #tuple(x)
                            z = (x[0], x[1])
                            path.append(z)
                            move_count = move_count + 1
                        elif (x[0], x[1]) in obstacles:
                            x_check = True
                            
                #if end in obstacles:
                #    x_check = True
                #    y_check = True
                #    print 'end in obstaclees'
   
            #print path, 'path, end of while loop'
            if (x_check or y_check) == False and end not in obstacles:
                #print 'approved'
                #path = tuple(path)
                #print path
                paths.append(path)
            elif (x_check and y_check) == True:
                #print 'denied'
                pass
        return paths

    def path_filter(self, start, length, width, obstacles, move_Range, playerGroup):
        #print 'in path_filter'
        dest = []
        cleared = None 
        bogeys = self.bogey_check(playerGroup, width)
        spots = self.pathfinder(start, length, width, obstacles, move_Range, playerGroup)
        #print spots
        for spot in spots:
            for spo in spot:
                if spo not in dest:
                    #print start, spo, 'start and spo before enter path check'
                    start = (start[0], start[1])
                    cleared = self.path_check(start, spo, move_Range,obstacles, bogeys)
        #            print cleared, start, spo, spot, ' cleared start spo and spot in path filter '
                    if cleared == True:
                        #print spo[0], WINDOWW/GRID_WIDTH, spo[1], WINDOWH/GRID_HEIGHT
                        if (spo[0] > WINDOWW/GRID_WIDTH) or (spo[1] > WINDOWH/GRID_HEIGHT):
                        #    print 'pf1'
                            pass
                        elif (spo[0] < WINDOWW/GRID_WIDTH) and (spo[1] < WINDOWH/GRID_HEIGHT):
                        #    print 'pf2'
                            dest.append(spo)
                    elif cleared == False:
                        pass
                elif spo in dest:
                    pass
        return dest
    
    def range_finder(self, grid_obstacles):#.att_range, self.move, cx, cy, GRID_WIDTH, GRID_HEIGHT, Move_Turn, Attack_Turn):
        #print 'in range_finder'
        i = 0
        j = 0
        potential_Moves = []
        potential_Targets = []
        for i in range(0, COLUMNS):
            for j in range(0, ROWS):
                    if self.move_Turn == True:
                        if abs(i-(self.rect.topleft[0]/GRID_WIDTH)) + abs(j-(self.rect.topleft[1]/GRID_HEIGHT)) <= self.move_Range :
                            if (i,j) not in grid_obstacles:
                               #print i, j
                                potential_Moves.append((i,j))
                            elif (i,j) in grid_obstacles:
                                #print i, j, 'in grid_obstacles'
                                pass
                    if self.att_Turn == True:
                        if abs(i-(self.rect.topleft[0]/GRID_WIDTH)) + abs(j-(self.rect.topleft[1]/GRID_HEIGHT)) <= self.att_Range :
         #                   print i, j
                            potential_Targets.append((i,j))
                    j = j + 1
            i = i + 1
        #print potential_Moves, potential_Targets
        return potential_Moves, potential_Targets

    def path_check(self, start, end, move, obstacles, bogeys = []):
        #print 'in path_check'
        #print obstacles, 'obstacles'
        path = [end]
        path2 = [end]
        penalty = 0
        penalty2 = 0
        i2 = 0
        j2 = 0
        i = 0
        j = 0
        x = start[0]
        y = start[1]
        w = end[0]
        z = end[1]
        total = 0
        total2 = 0
        spot = ()
        spot2 = ()
        bogey_distance = {}
        cleared = None

        if len(bogeys) >1:
            for bogey in bogeys:
                bogey_distance[bogey] = abs(x - bogey[0]) + abs(y - bogey[1])
        elif len(bogeys) == 1:
            bogey_distance[bogeys[0]] = abs(x - bogeys[0][0]) + abs(y - bogeys[0][1])
        distance = abs(x - w) + abs(y - z)
        valid = None
        valid2 = None
        #print distance
        #print end, spot, start, 'end spot start'
        if distance <= move:
            pass
        else:
            valid = False
            valid2 = False
            #print 'move is not valid'
            #return valid, valid2
        if end == start:
            valid = True
            valid2 = False
            #print 'of course thats valid'
            spot = start
            #return valid, valid2
        #while (i + j) <= move:
        while spot != start:
            #spot = (w + i, z + j)
            #path.append(spot)
            while (w + i) != x:
                if w > x:
                    i -= 1
                elif w < x:
                    i += 1
                spot = (w + i, z + j)
                #if spot[0] > GRID_WIDTH/100 or s
                #path.append(spot)
                if spot in bogeys:
                    if bogey_distance[spot] == (move - 2):
                        penalty +=2
                    else:
                        penalty += 1
                if spot in obstacles:
                    #print 'spot in obstacles'
                    penalty += int(move + 1)
                    #print 'penalty is ', penalty
                else:
                    pass
            while (z + j)!= y:
                if z > y:
                    j -= 1
                elif z < y:
                    j += 1
                spot = (w + i, z + j)
                path.append(spot)
                if spot in bogeys:
                    if bogey_distance[spot] == (move - 2):
                        penalty +=2
                    else:
                        penalty += 1
                        
                if spot in obstacles:
                    #print 'spot in ibstacles'
                    penalty += int(move + 1)
                    #print 'penalty is ', penalty
                else:
                    pass
        total = distance + penalty
        if total <= move:
            valid = True
        elif total > move:
            valid = False
        #if valid == False:
        #    plist.remove(end)
        if valid == False:

            while spot2 != start:
            #spot = (w + i, z + j)
            #path.append(spot)
                while (z + j2) != y:
                    if z > y:
                        j2 -= 1
                    elif z < y:
                        j2 += 1
                    spot2 = (w + i2, z + j2)
                    path2.append(spot2)
                    if spot2 in bogeys:
                        if bogey_distance[spot2] == (move - 2):
                            penalty2 += 2
                        else:
                            penalty2 += 1
                    if spot2 in obstacles:
                        #print 'spot2 in obstacles'
                        penalty2 += int(move +1)
                        #print 'penalty2 is, ', penalty2 
                    else:
                        pass
                while (w + i2)!= x:
                    if w > x:
                        i2 -= 1
                    elif w < x:
                        i2 += 1
                    spot2 = (w + i2, z + j2)
                    path2.append(spot2)
                    if spot2 in bogeys:
                        if bogey_distance[spot2] == (move - 2):
                            penalty2 +=2
                        else:
                            penalty2 += 1
                    if spot2 in obstacles:
                        #print 'spot2 in obstacles'
                        penalty2 += int(move + 1)
                        #print 'penalty2 is ', penalty2

                    else:
                        pass
        total2 = distance + penalty2
        if total2 <= move:
            valid2 = True
        elif total2 > move:
            valid2 = False
        #if valid == False:
        #    plist.remove(end)
        if valid == False and valid2 == False:
            #plist.remove(end)
            cleared = False
        elif valid == True or valid2 == True:
            cleared = True
        return cleared

    def range_display(self, act, grid_obstacles, playerGroup):
        #this function takes the grid coordinates from range finder, convert
        #them to pixel coordinates, and the displays them in either blue for
        #movement or yellow for attack to show the user what is a valid target      start, length, width, obstacles, move_Range
       #print grid_obstacles
        start = [(self.rect.topleft[0]/GRID_WIDTH), (self.rect.topleft[1]/GRID_HEIGHT)]
        potential_Moves = self.path_filter(start, GRID_HEIGHT, GRID_WIDTH, grid_obstacles, self.move_Range, playerGroup)#.att_range, self.move, cx, cy, GRID_WIDTH, GRID_HEIGHT, Move_Turn, Attack_Turn)
        i = 0
        j = []
        #print " getting display", potential_Moves
        if act == 'move':
            for i in range(0, len(potential_Moves)):
                #if potential_Moves[i] not in grid_obstacles:
                grid_Potential_Moves = pygame.Rect((potential_Moves[i][0] * 100),(potential_Moves[i][1] * 100), GRID_WIDTH, GRID_HEIGHT)
                pygame.draw.rect(windowSurface, ORANGE, grid_Potential_Moves, THICK)
            pygame.display.update()
            return potential_Moves
        
        elif act == 'action':
            for i in range(0, len(potential_Targets)):
                grid_Potential_Targets = pygame.Rect((potential_Targets[i][0] * 100),(potential_Targets[i][1] * 100), GRID_WIDTH, GRID_HEIGHT)
                pygame.draw.rect(windowSurface, YELLOW, grid_Potential_Targets, THICK)
                pygame.display.update()
            return potential_Targets
        #print " is display good?"
        

    def link_identify_id(self, playerGroup):
        for player in playerGroup:
            if player.rect.topleft == self.rect.topleft and player != self:
                #print "player",i, 'is the target'
                return player
            else:
                pass
        return None
    #updated on 7/22/2015, trying to incorporate ability for melees to have more than two squads
    
    def ct_update(self, grid_positions, grid_objects, playerGroup):
        self.status_update(grid_positions, grid_objects, playerGroup)
       #print self.status
        turn_counter = False
        if self.hit_Points > 0:
            if self.ct < 100:
                self.ct = self.ct + self.speed
                #print "ct_update ok"
            if self.ct >= 100:
                self.ct = 0
                turn_counter = True
        return turn_counter

    def status_update(self, grid_positions, grid_objects, playerGroup):
        if self.hit_Points > self.hit_Points_Max:
            self.hit_Points = self.hit_Points_Max
            
        if self.hit_Points <= 0 or 'KO' in self.status:
            self.hit_Points = 0
            self.image = ch_Images[8]
            self.status['KO'] = True
            if 'critical' in self.status:
                del self.status['critical']
            if 'link' in self.status:
                del self.status['link']
            #del self.status['normal']
            self.void_temp_buffs()
            if 'restrained' in self.status:
                del self.status['restrained']
            #print self.status
            Battle_Surface_Refresh(grid_positions, grid_objects, playerGroup)
            return self.hit_Points, self.image, self.status
        if self.hit_Points <= self.hit_Points_Max/5 and self.hit_Points != 0:
            self.status['critical'] = True
        if 'retreat' in self.status:
            #self.status = {}
            self.status['retreat'] = True
            self.ct = 0
        if 'charging' in self.status and self.action_charging != 0:
            self.status['charging'] = True
        elif 'charging' in self.status and self.action_charging == 0:
            del self.status['charging']
        if 'guard' in self.status:
            if self.ct  + self.speed < 100:
                self.status['guard'] = True
                self.t_Evade = self.root_T_Evade * 2
        if 'riposte' in self.status:
            if self.ct + self.speed < 100:
                self.status['riposte'] = True
                self.t_Evade = self.root_T_Evade * 3
            #if self.ct + self.speed
        if 'link' in self.status:
            x = self.link_identify_id(playerGroup)
            if x == None:
                del self.status['link']
            elif 'cover' in x.abilities and 'link' in (self.status and x.status):
                self.status['covered'] = True
        if 'restrained' in self.status:
            x = self.link_identify_id(playerGroup)
            if x == None:
                del self.status['restrained']
            if self.status.get('link') == None:
                self.status['link'] = True
            elif 'restrain' in x.abilities and 'link' in (self.status and x.status):
            #    print x.abilities, 'is restrain there?'
                self.status['restrained'] = True
        if 'covered' in self.status:
            x = self.link_identify_id(playerGroup)
            if x == None:
                del self.status['covered']
            if self.status.get('link') == None:
                self.status['link'] = True
            elif 'cover' in x.abilities and 'link' in (self.status and x.status):
            #    print x.abilities, 'is cover there?'
                self.status['covered'] = True
        if None in self.status:
            del self.status[None]

        return self.status
                                                #act, grid_positions,
                                                #grid_objects, grid_obstacles,
                                                #playerGroup, ai, ai_Move, None)

    def character_move(self, act, grid_positions, grid_objects,
                       grid_obstacles, playerGroup, ai = False, ai_move = None, targets = None):
        x,y = self.rect.topleft
       #print x, y
        cx = x /100
        cy = y /100
       #print cx, cy
        cm_turn = True
        self.move_Turn = True
       #print grid_obstacles
        #if act is != 'move' or 'action', rangedisplay will return nothing
        valid_Moves = self.range_display(act, grid_obstacles, playerGroup)
        surf = pygame.display.get_surface()
        while cm_turn == True:
            #self.Move_Turn = True
            #self.range_display()
            if ai == False:
                for event in pygame.event.get():
                   #print " entering character_move loop"
                    if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                        pygame.quit()
                        sys.exit()
                    if event.type == MOUSEBUTTONDOWN:
                        mx, my = event.pos
                        gmx = mx/GRID_WIDTH
                        gmy = my/GRID_HEIGHT
                        tmx = gmx * GRID_WIDTH
                        tmy = gmy * GRID_HEIGHT
                       #print "cx and cy are ", cx, cy
                       #print "print mx and my are ", mx, my
                       #print "print gmx and gmy ", gmx, gmy
                       #print "mouse press good"
                       #print "abs (", cx, " -", gmx, " ) + abs(", cy, " - ", gmy, ") = ",(abs(cx - gmx) + abs(cy - gmy))
                       #print "self.move = ", self.move_Range
                        distance = (abs(cx - gmx) + abs(cy - gmy))
                        if (abs(cx - gmx) + abs(cy - gmy)) <= self.move_Range and (gmx, gmy) in valid_Moves:
                            #confirmation = raw_input('would you like to move there? 1 - yes or 2 - no : ')
                            confirmation = yes_or_no(surf)
                            if confirmation == True: #('1' or 'yes'): #'yes' or 'yeah' or 'y':
                               #print confirmation
                                hit, link_attempt = self.link_attempt(act, gmx, gmy, distance, playerGroup, ai)
                                if hit == True or hit == None:
                                    self.rect.topleft = (tmx, tmy)
                                    Battle_Surface_Refresh(grid_positions, grid_objects, playerGroup)#windowSurface.blit(self.image, (tmx, tmy))
                                    #pygame.display.update()
                                    cm_turn = False
                                    self.move_Turn = False #this statement causes a conflict with the link_attempt and causes it to not even enter the loop
                                    if self.abilities.get('cover') == True:
                                       #print "covering"
                                        self.weapon.cover(self, playerGroup)
                                    if self.abilities.get('restrain') == True:
                                       #print 'restraining'
                                        self.weapon.restrain(self, playerGroup)
                                    if hit == None and link_attempt == False:
                                        cm_turn = False
                                        self.move_Turn = True
                                        self.rect.topleft = (x, y)
                                        Battle_Surface_Refresh(grid_positions, grid_objects, playerGroup)#windowSurface.blit(self.image, (tmx, tmy))
                                    
                                if hit == False:
                                    cm_turn = False
                                    self.move_Turn = False
                                    self.rect.topleft = (x, y)
                                    Battle_Surface_Refresh(grid_positions, grid_objects, playerGroup)
                            elif confirmation == False: 
                               #print confirmation
                               #print 'x and y are, ', x, y
                                self.rect.topleft = (x, y) #x
                                Battle_Surface_Refresh(grid_positions, grid_objects, playerGroup)
                               #print 'self.rect.topleft is ', self.rect.topleft
                               #print 'x and y are ', x, y
                                cm_turn = False
                                self.move_Turn = True
                            
                            hit = None
                           #print hit, 'thats what hit is', cm_turn, self.move_Turn
            elif ai == True:
                amx, amy = ai_move
                mx, my = amx * GRID_WIDTH, amy * GRID_HEIGHT
                gmx = mx/GRID_WIDTH
                gmy = my/GRID_HEIGHT
                tmx = gmx * GRID_WIDTH
                tmy = gmy * GRID_HEIGHT
                distance = (abs(cx - gmx) + abs(cy - gmy))
                print cx, cy, gmx, gmy, self.move_Range, valid_Moves, 'cx, cy, gmx, gmy, self.move_Range, valid_Moves'
                if (abs(cx - gmx) + abs(cy - gmy)) <= self.move_Range and (gmx, gmy) in valid_Moves:
                    confirmation = True
                    if confirmation == True: #('1' or 'yes'): #'yes' or 'yeah' or 'y':
                       #print confirmation
                        hit, link_attempt = self.link_attempt(act, gmx, gmy, distance, playerGroup, ai)
                        if hit == True or hit == None:
                            self.rect.topleft = (tmx, tmy)
                            Battle_Surface_Refresh(grid_positions, grid_objects, playerGroup)#windowSurface.blit(self.image, (tmx, tmy))
                            cm_turn = False
                            self.move_Turn = False #this statement causes a conflict with the link_attempt and causes it to not even enter the loop
                            if self.abilities.get('cover') == True:
                               #print "covering"
                                self.weapon.cover(self, playerGroup)
                            if self.abilities.get('restrain') == True:
                               #print 'restraining'
                                self.weapon.restrain(self, playerGroup)
                            if hit == None and link_attempt == False:
                                cm_turn = False
                                self.move_Turn = True
                                self.rect.topleft = (x, y)
                                Battle_Surface_Refresh(grid_positions, grid_objects, playerGroup)#windowSurface.blit(self.image, (tmx, tmy))
                            
                        if hit == False:
                            cm_turn = False
                            self.move_Turn = False
                            self.rect.topleft = (x, y)
                            Battle_Surface_Refresh(grid_positions, grid_objects, playerGroup)
                    elif confirmation == False: 
                       #print confirmation
                       #print 'x and y are, ', x, y
                        self.rect.topleft = (x, y) #x
                        Battle_Surface_Refresh(grid_positions, grid_objects, playerGroup)
                       #print 'self.rect.topleft is ', self.rect.topleft
                       #print 'x and y are ', x, y
                        cm_turn = False
                        self.move_Turn = True
                    
                    hit = None
                   #print hit, 'thats what hit is', cm_turn, self.move_Turn
        self.grid_Char_Rect = (self.rect.topleft[0]/GRID_WIDTH, self.rect.topleft[1]/GRID_HEIGHT)
        return self.rect.topleft
        #need to build an individual move grid function... 10/4/2014, built
        

    def link_attempt(self, act, gmx, gmy, distance, playerGroup, ai = False):
       #print 'in link attempt loop'
        group = playerGroup
        if self.att_Turn == False:
            return None, None
        elif self.att_Turn == True:
            pass
        if act == 'move' and self.move_Turn == True and self.att_Turn == True :
           #print 'in if loop (checking t, self.move_turn and self.att_turn'
            group = playerGroup
            list_of_grid_targets = pixel_to_grid_converter(playerGroup)
            i = 0
           #print 'beginning loop to check other characters if they will link'
           #print ' list of grid targets', list_of_grid_targets
            #hit = None
            for i in range(0, len(list_of_grid_targets)):
               #print 'checking for loop ', i                
                if (gmx, gmy) == list_of_grid_targets[i] and group[i].name != self.name:
                   #print group[i].name, ' ', list_of_grid_targets[i]
                   #print self.name, ' ', gmx, gmy
                    surf = pygame.display.get_surface()
                    if ai == False:
                        link = yes_or_no(surf) #raw_input("would you like to attempt to link with that character? \nenter yes or no: ")
                    elif ai != False:
                        link = True
                    if link == True: #"yes" or link == "ye" or link == "y":
                        hit = self.hit_or_miss(group[i], distance)
                        link_attempt = True
                        if hit == True:
                           #print "link attempt succesful"
                            self.move_Turn = False
                            self.att_Turn = False
                            self.status['link'] = True
                            group[i].status['link'] = True
                           #print "self.status[""link""] = True target.status[""link""] = True"
                            return hit, link_attempt
                        elif hit == False:
                           #print "link attempt was unsuccessful"
                            self.move_Turn = False
                            self.att_Turn = False
                            return hit, link_attempt
                        else:
                            hit = None
                            link_attempt = None
                    if link == False: #"no" or link == "n" or link == "":
                        link_attempt = False
                        self.move_Turn = True
                        #self.att_Turn = True
                        #hit = None
                        return None, link_attempt
                
                    else:
                        link = yes_or_no(surf)
                else:
                    i = i + 1
            return None, None
        #return group[i]

    
    def character_action(self, act, action_Timeflow_List, grid_positions, gp_dict, grid_objects, playerGroup):
        x,y = self.rect.topleft
       #print x, y
        cx = x /100
        cy = y /100
       #print cx, cy
        ca_turn = True
        self.att_Turn = True

        while ca_turn == True:
            self.menu('action')
            choice = self.menu_select()
           #print self.abilities, ' self.abilities'
           #print self.actions, 'self.actions'
           #print choice
            if choice in self.actions:
               #print " entering if loop of choice loop"
                ca_turn = self.actions[choice].use_action(self, action_Timeflow_List, grid_positions, gp_dict, grid_objects, playerGroup)
                
            else:
                ca_turn = False

    
    def raw_attack_damage(self, distance):
        if distance < 1:
            distance = 1
        if self.weapon not in self.equipment:
            value = self.strength * 2 + randrange(-2 * self.att_Range,2 * self.att_Range)
        else:
            value = self.weapon.raw_weapon_damage(self, distance)
        if value <= 0:
                 value = 1
        return value

    def raw_magic_damage(self, sacrifice):
        value = sacrifice * self.magic 
        return value

    def raw_attack_reducer(self):
        value = -(self.defense)
        return value

    def raw_sp_attack_reducer(self):
        value = -(self.sp_defense)
        return value

    def face_direction(self, grid_positions, grid_objects, playerGroup):
        south = SOUTH
        north = NORTH
        east = EAST
        west = WEST
        self.image = self.root_Image
        direction = {'south':0, 'north':180, 'east':90, 'west':270}
        kdir = {K_DOWN:0, K_UP:180, K_RIGHT:90, K_LEFT:270}
        cdir = {K_DOWN:'south', K_UP:'north', K_RIGHT:'east', K_LEFT:'west'}
        y = 'yes'
        surf = pygame.display.get_surface()
        s_rect = surf.get_rect()
        selection = False
        text_box(surf, 'Choose Direction to Face', s_rect.centerx,
                 s_rect.centery, 10, True)
        pygame.display.update()
        while selection != True:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit(); sys.exit();
                    elif event.type == KEYDOWN:
                        if event.key in cdir:
                           #print event.key
                            x = event.key
                            self.direction = {}
                            self.direction = {cdir[x]:kdir[x]}
                            new_Image = pygame.transform.rotate(self.image,
                                                                kdir[x])
                            self.image = new_Image

                            windowSurface.blit(self.image, self.rect.topleft)
                            pygame.display.update()
                            selection = True

        y = yes_or_no(surf)

        if y ==True:
           return True
        
        elif y != True:
            return False

    def health_bar(self):
        surf = pygame.display.get_surface()
        blx, bly = self.rect.bottomleft
        hw = self.rect.width
        LEC =  LIST_ELEMENT_COLOR
        health_Rect = pygame.rect.Rect(blx, bly - 10, hw, 10)
        hp_percent = int(100.0 * (float(self.hit_Points)) /(float(self.hit_Points_Max)) )
        #print 'hp percnt', hp_percent
        hp_Rect = pygame.rect.Rect(blx, bly - 10, hp_percent, 10)
        pygame.draw.rect(surf, BLACK, health_Rect, 0)
        pygame.draw.rect(surf, LEC[self.element_type], hp_Rect, 0)
        

    def void_temp_buffs(self):
        if self.status.get('guard') == True:
            del self.status['guard']
            self.t_Evade = self.root_T_Evade
            hit_display(True, 'guard', self)
        if self.status.get('riposte') == True:
            del self.status['riposte']
            self.t_Evade = self.root_T_Evade
            hit_display(True, 'riposte', self)
        if self.status.get('charging') == True:
            del self.status['charging']
            hit_display(True, 'charge', self, True)
        if self.status.get('stagger') == True:
            del self.status['stagger']
            hit_display(True, 'stagger', self, True)

    def check_restraints(self, playerGroup):
        if self.status.get('restrained') == True:
            x = self.link_identify_id(playerGroup)
            str_Diff = x.strength - self.strength
            chance = randrange(0, 101)
            brk_Cost = str_Diff * int(self.hit_Points_Max * 0.075)
            if brk_Cost <= 0:
                brk_Cost = 1
            txt = 'Rstrnd'
            
            if chance < ((str_Diff * 5) + 50):
                self.move_Turn = False
                self.att_Turn = False
               #print 'could not break the restraint, lost ', brk_Cost, ' hit points' 
                self.hit_Points = self.hit_Points - abs(brk_Cost)
                heal = False
                
            elif chance > ((str_Diff * 5) + 50):
               #print 'broke restraint, lost ', (brk_Cost/2), ' hit points'
                del self.status['restrained']
                self.hit_Points = self.hit_Points - abs(brk_Cost /2)
                heal = True
                hit_display(True, txt, self, heal)
                pass

            hit_display(True, brk_Cost, self)
        elif self.status.get('restrained') != True:
            pass

    def check_poison(self):
        if self.status.get('poison') == True and self.status['poison'] == True:
            hp_Loss = int(self.hit_Points_Max * 0.10)
            self.hit_Points = self.hit_Points - hp_Loss
            hit_display(True, hp_Loss, self)
           #print self.name, 'lost ', hp_Loss, ' hit points'
            
    def menu(self, choice = None):
        i = 0
        self.menu_rects = {}
        menu_orientation = 'evenleft'
        if self.rect.topleft[0] <= MENU_RECT_WIDTH:
            menu_orientation = 'evenright'
            if self.rect.topleft[1] < FIELDH - MENU_RECT_WIDTH:
                menu_orientation = 'bottomright'
            elif self.rect.topleft[1] >= FIELDH - MENU_RECT_WIDTH:
                menu_orientation = 'topright'
                i = -(MENU_RECT_HEIGHT)
        elif self.rect.topleft[0] > FIELDH - MENU_RECT_WIDTH:
            if self.rect.topleft[1] < FIELDH - MENU_RECT_WIDTH:
                menu_orientation = 'evenleft'
            elif self.rect.topleft[1] > FIELDH - MENU_RECT_WIDTH:
                menu_orientation = 'topleft'
                i = -(MENU_RECT_HEIGHT)
        elif MENU_RECT_WIDTH < self.rect.topleft[0] < FIELDW - MENU_RECT_WIDTH:
                if self.rect.topleft[1] < MENU_RECT_WIDTH:
                    menu_orientation = 'bottomleft'
                elif self.rect.topleft[1] > FIELDW - MENU_RECT_WIDTH:
                    menu_orientation = 'topleft'
                    i = -(MENU_RECT_HEIGHT)
       #print self.rect.topleft

        if choice == None:
            options = self.melee_options
        elif choice == 'action':
            options = self.actions
        elif choice != 'action' or choice != None:
            options = choice
        surf = pygame.display.get_surface()

        for act in options:
            
            if menu_orientation == 'evenleft':
                self.menu_rects[act] = pygame.rect.Rect(self.rect.topleft[0] - MENU_RECT_WIDTH, self.rect.topleft[1] + i, MENU_RECT_WIDTH, MENU_RECT_HEIGHT)
                pygame.draw.rect(surf, (WHITE), self.menu_rects[act], 0) 
                surf.blit(font.render(act, True, (255, 0, 0)), self.menu_rects[act].center)
                i = i + 25
            elif menu_orientation == 'evenright':
                self.menu_rects[act] = pygame.rect.Rect(self.rect.topright[0], self.rect.topright[1] + i, MENU_RECT_WIDTH, MENU_RECT_HEIGHT)
                pygame.draw.rect(surf, (WHITE), self.menu_rects[act], 0) 
                surf.blit(font.render(act, True, (255, 0, 0)), self.menu_rects[act].center)
                i = i + 25
            elif menu_orientation == 'bottomleft':
                self.menu_rects[act] = pygame.rect.Rect(self.rect.bottomleft[0] - MENU_RECT_WIDTH, self.rect.bottomleft[1] + i, MENU_RECT_WIDTH, MENU_RECT_HEIGHT)
                pygame.draw.rect(surf, (WHITE), self.menu_rects[act], 0) 
                surf.blit(font.render(act, True, (255, 0, 0)), self.menu_rects[act].center)
                i = i + 25
            elif menu_orientation == 'bottomright':
                self.menu_rects[act] = pygame.rect.Rect(self.rect.bottomright[0], self.rect.topright[1] + i, MENU_RECT_WIDTH, MENU_RECT_HEIGHT)
                pygame.draw.rect(surf, (WHITE), self.menu_rects[act], 0) 
                surf.blit(font.render(act, True, (255, 0, 0)), self.menu_rects[act].center)
                i = i + 25
            elif menu_orientation == 'topleft':
                self.menu_rects[act] = pygame.rect.Rect(self.rect.topleft[0] - MENU_RECT_WIDTH, self.rect.topleft[1] + i, MENU_RECT_WIDTH, MENU_RECT_HEIGHT)
                pygame.draw.rect(surf, (WHITE), self.menu_rects[act], 0) 
                surf.blit(font.render(act, True, (255, 0, 0)), self.menu_rects[act].center)
                i = i + 25
            elif menu_orientation == 'topright':
                self.menu_rects[act] = pygame.rect.Rect(self.rect.topright[0], self.rect.topright[1] + i, MENU_RECT_WIDTH, MENU_RECT_HEIGHT)
                pygame.draw.rect(surf, (WHITE), self.menu_rects[act], 0) 
                surf.blit(font.render(act, True, (255, 0, 0)), self.menu_rects[act].center)
                i = i + 25
            
        pygame.display.update()

    def menu_select(self):
        selection = None
        while selection == None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit();
                if event.type == MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if event.button == 3:
                        return None
                    for act in self.menu_rects:
                        if self.menu_rects[act].collidepoint((x,y)) == True:
                           #print act
                            selection = act
                            break
                        else:
                            pass
                    if selection == None:
                        pass

        return act

    def proximity_assess(self, playerGroup):
        sx, sy = self.rect.topleft
        srx = sx/GRID_WIDTH
        sry = sy/GRID_HEIGHT
        mr = self.move_Range + 1
        a_close = False
        e_close = False
        px = {}
        for player in playerGroup:
            px, py = player.rect.topleft
            prx = px / GRID_WIDTH
            pry = py / GRID_HEIGHT
            d = abs(prx - srx) + abs(pry - sry)
            if d > mr:
                pass
            elif d <= mr:
                if player.allegiance == self.allegiance:
                    a_close = True
                elif player.allegiance != self.allegiance:
                    e_close = True

        return a_close, e_close
        

        
                
        

    def ai_Turn(self, action_Timeflow_List, grid_positions, gp_dict, grid_objects, 
                grid_obstacles, playerGroup, ai = False):
        score = -9999
        print self.att_Turn, self.move_Turn, 'act and move turns '

        #b_action = None
        b_action = {'physical':None, 'item':None,
                    'status':None, 'move':None}
        
        b_score = -9999
        act = 'move'
        mission = None
        m, status = self.self_assess()
        if self.weapon.name == 'shield':
            mission = 'status'
        if m == (1 or 2) and self.weapon.name != 'shield':
            mission = 'physical'
        if m > 2 and 'potion' in self.inventory:
            mission = 'item'
        if m == 4 and self.armor.name == 'light armor':
            mission = 'move'
        m = -9999
        m_act = None
       #print self.actions_CD, 'self.actions_CD'
        for a_types in self.actions_CD:
            a_type = self.actions_CD[a_types]
            for at in a_type:
                a = a_type[at]
                score_dict = a.action_assess(self, playerGroup, grid_positions,
                                             grid_objects, grid_obstacles, gp_dict)
                e = score_dict['act'].effect
                #print score_dict
                if b_action[e] == None:
                    b_action[e] = score_dict
                    #print b_action, 'b_action', mission, 'mission'
                else:
                    pass
                #p_action = {'act': self, 'a_name':self.name, 'score': 0,
                #    'move':None, 'targets':None, 'target':None,
                #    'tolerance':0}
               #print score_dict, 'score dict'
                score = score_dict['score']
                if score > b_action[e]['score']:
                    #b_score = score 
                    b_action[e] = score_dict
                else:
                    pass
                if score > m:
                    m_act = score_dict
        if mission == None:
            b_action = m_act
            print m_act, 'mact'
        elif mission != None:
            b_action = b_action[mission]
                        
        #print b_action, 'baction'
        #if b_action[mission] != None:
        #    b_action = b_action[mission]
        #elif b_action[mission] == None:
        #    s = 0
        #    for act in b_action:
        #        a = b_action[act]
        #        so = a['score']
        #        if so > s:
                    #mi = act
        #            b_action = b_action[act]
        print b_action, 'b_action', mission, 'mission'
        if b_action == None:
            wtf = raw_input('what is wrong now...')
        ai_Move = b_action['move']
        ai_Action = b_action['act']
        ai_Targets = b_action['targets']
        ai_Name = b_action['a_name']
        ai_Target = b_action['target']
        ai_Tolerance = b_action['tolerance']
        ai_Score = b_action['score']
        risk_tol = (self.hit_Points / 10) * -1
        #print b_action, 'b_action', mission, 'mission'
                                              #self, act, grid_positions, grid_objects,
                                              #grid_obstacles, playerGroup, ai = False, ai_move = None, targets = None):
        if ai_Move != self.grid_Char_Rect:
            self.rect.topleft = self.character_move(act, grid_positions,
                                                    grid_objects, grid_obstacles,
                                                    playerGroup, ai, ai_Move, None)
            self.move_Turn = False
        #if b_score > 0:
        if self.att_Turn == True:
            if ai_Tolerance > 0 and ai_Score > risk_tol:
                ai_Action.ai_use_action(self, action_Timeflow_List, grid_positions,
                                        gp_dict, grid_objects, playerGroup,
                                        ai_Targets )
                self.att_Turn = False
        else:
            pass
            #self.move_Turn = False
        #elif b_score < 0:
        #    self.att_Turn = True

        #self.move_Turn = False
        #self.att_Turn = False             

    #action_Timeflow_List, grid_positions, grid_objects, grid_obstacles, playerGroup, ai    
    def character_turn(self, action_Timeflow_List, grid_positions, grid_objects,
                       gp_dict, grid_obstacles, playerGroup, ai = False):
       #print grid_obstacles
        self.void_temp_buffs()    
        self.move_Turn = True
        self.att_Turn = True
        self.check_restraints(playerGroup)

        self.highlight_character()
        self.menu()
        act = None
        if ai == True:
           #print 'in ai loop'
            self.ai_Turn(action_Timeflow_List, grid_positions, gp_dict, grid_objects,
                         grid_obstacles, playerGroup, ai)
            act = True
           #print playerGroup, 'playergroup in ai loop of character_turn'

        while act == None or (self.move_Turn == True or self.att_Turn == True):
            self.menu_adjust()
            self.menu()
            act = self.menu_select()
            Battle_Surface_Refresh(grid_positions, grid_objects, playerGroup)

            if act == 'move' and self.move_Turn == True:
                self.rect.topleft = self.character_move(act, grid_positions, grid_objects, grid_obstacles, playerGroup)

            if act == 'action' and self.att_Turn == True:
                self.character_action(act, action_Timeflow_List, grid_positions, gp_dict, grid_objects, playerGroup)
                
            if act == 'wait':
                self.wait()
                
            if act == 'status':
                y = pygame.display.get_surface()
                self.id_card(y)

            if act == 'inquire':
                self.inquire(playerGroup)

        end_Turn = False
        self.check_poison()
        while end_Turn == False:
            end_Turn = self.face_direction(grid_positions, grid_objects, playerGroup)
       #print 'end of turn'
        self.unhighlight_character()

    def menu_adjust(self):
        if self.move_Turn == True and self.att_Turn == True:
            self.melee_options = {'move':self.character_move,
                                  'action':self.character_action,
                                  'wait':self.wait,
                                  'status':self.id_card,
                                  'inquire':self.inquire}

        if self.move_Turn == True and self.att_Turn == False:
            self.melee_options = {'move':self.character_move, 
                                  'wait':self.wait,
                                  'status':self.id_card,
                                  'inquire':self.inquire}

        if self.move_Turn == False and self.att_Turn == False:
            self.melee_options = {'wait':self.wait,
                                  'status':self.id_card,
                                  'inquire':self.inquire}

        if self.move_Turn == False and self.att_Turn == True:
            self.melee_options = {'action':self.character_action,
                                  'wait':self.wait,
                                  'status':self.id_card,
                                  'inquire':self.inquire}

    def wait(self):
        #if t == 3:
        surf = pygame.display.get_surface()
        confirm = yes_or_no(surf)
        if confirm == True:
            if self.move_Turn == True and self.att_Turn == True:
                self.move_Turn = False
                self.att_Turn = False
                self.ct = 75                    
            if self.move_Turn == False or self.att_Turn == False:
                self.move_Turn = False
                self.att_Turn = False
                self.ct = 40
        elif confirm == False:
            pass
        elif confirm != (True or False):
            pass

    def equipment_card(self, surface):
        surf_rect = surface.get_rect()
        card_rect = pygame.rect.Rect(0, surf_rect.centery, surf_rect.width/2, surf_rect.height/2)
        pygame.draw.rect(surface, WHITE, card_rect)
        i = 0
        j = 0
        equip_type = ['weapon', 'off_Hand', 'helmet',
                      'armor', 'accessory', 'inventory']
        self.ec_rects = {}
        for article in self.equipment:
           #print article
            self.ec_rects[equip_type[i]] = pygame.rect.Rect(card_rect.topleft[0], card_rect.topleft[1] + j, card_rect.width, card_rect.height/6 )
            pygame.draw.rect(surface, WHITE, self.ec_rects[equip_type[i]])
            pygame.draw.rect(surface, BLACK, self.ec_rects[equip_type[i]], 1)
            surface.blit(font.render(equip_type[i], True, BLACK), (self.ec_rects[equip_type[i]].centerx/5, self.ec_rects[equip_type[i]].centery))

            if article == None or article == {}:
                surface.blit(font.render('None', True, BLACK), (self.ec_rects[equip_type[i]].center))

            elif article != {} and equip_type[i] == 'inventory' :
                names = article.keys()
                snames = str(names)
                surface.blit(font.render(snames, True, BLACK), (self.ec_rects[equip_type[i]].center))
            elif article != None :
                surface.blit(font.render(article.name, True, BLACK), (self.ec_rects[equip_type[i]].center))
            i = i + 1
            j = j + (card_rect.height / 6)
        pygame.display.update()
       #print self.ec_rects
        return self.ec_rects
        
    def id_card(self, surface):
        qualities_dict1 = [{'Lvl':self.level}, {'HP':self.hit_Points},
                           {'Str':self.strength}, {'Spd':self.speed},
                           {'Brv':self.brave}, {'Mve':self.move_Range},
                           {'Ldrs': self.leadership} ]
        qualities_dict2 = [{'Name':self.name},{'HP Max':self.hit_Points_Max},
                           {'Mag':self.magic}, {'Sta':self.stamina},
                           {'Fth':self.faith}, {'Evd':self.t_Evade},
                           {'Ld':self.leader}]
        attributes_dict = [{'Job':self.job},
                           {'LMN':self.element},
                           {'Sts':self.status},
                           {'Rnk':self.rank},
                           {'Wpn':self.weapon.name},
                           {'Off':self.off_Hand},
                           {'Hlm':self.helmet.name},
                           {'Amr':self.armor.name},
                           {'Acc':'accessory'},
                           {'Inv':self.inventory.keys()}]
        i = 0
        j = 0
        id_rect = Rect(300,400,300,200)
        pygame.draw.rect(surface, WHITE, id_rect)
        ref1 = (300,500)
        ref2 = (350,500)
        ref3 = (400,400)
        for i in range(0,len(qualities_dict1)):
            keys1 = qualities_dict1[i].keys()
            values1 = qualities_dict1[i].values()
            keys2 = qualities_dict2[i].keys()
            values2 = qualities_dict2[i].values()
            location = int(100/(len(qualities_dict1))) * i
            text1 = zipper(keys1, values1)
            text2 = zipper(keys2, values2)
            text_box(surface, text1, ref1[0], ref1[1] + location)
            text_box(surface, text2, ref2[0], ref2[1] + location)
            i = i + 1
        for j in range(0,len(attributes_dict)):
            keys3 = attributes_dict[j].keys()
            values3 = attributes_dict[j].values()
            location2 = (100/(len(attributes_dict))) * j
            text3 = zipper(keys3, values3)
            text_box(surface, text3, ref3[0], ref3[1] + location2)
            j = j + 1
        pygame.display.update()

    def mini_card(self, surface):
        qualities_dict = [{'Name':self.name},
                          {'Job':self.job},
                          {'Wpn':self.weapon.name},
                          {'Str':self.strength},
                          {'Mag':self.magic},
                          {'Evd':self.t_Evade},
                          {'Mve':self.move_Range}]
                           
        i = 0
        j = 0
        x, y = self.rect.topleft
        w = self.rect.width
        h = w = self.rect.height
        id_rect = Rect(x, y, w, h)
        pygame.draw.rect(surface, WHITE, id_rect)
        ref1 = (x,y)
        length = len(qualities_dict)
        for i in range(0,len(qualities_dict)):
            keys1 = qualities_dict[i].keys()
            values1 = qualities_dict[i].values()
            location = int(100/length) * i
            text1 = zipper(keys1, values1)
            text_box(surface, text1, ref1[0], ref1[1] + location)#, 25)
            i = i + 1
        pygame.display.update()
        return id_rect

    def forecast_display(self, chance, damage, s_effect):
        surf = pygame.display.get_surface()
        fc_text_titles = ['CH%', 'Dmg', 'St Eff']
        fc_text_values = [chance, damage, s_effect]
        ftt = fc_text_titles
        ftv = fc_text_values
        r = self.rect
        point = r.midleft
        px, py = point
        h = (r.bottom - py) - 10
        w = r.width
        i = 0
        display_rect = pygame.rect.Rect(px, py, w, h)
        dr = display_rect
        pygame.draw.rect(surf, WHITE, dr)
        for i in range(0,len(ftt)):
            keys1 = ftt[i]
            values1 = ftv[i]
            location = 10 * i
            text1 = zipper(keys1, values1)
            text_box(surf, text1, px, py + location)#, 25)
            i = i + 1
            
        

    def inquire(self, playerGroup):
        point = True
        surf = pygame.display.get_surface()
        id_rect = None
        while point != None:
            point = get_mouseclick()
            if point == None:
                break
            else:
                pass
            for player in playerGroup:
                if player.rect.collidepoint(point) == 1:
                    player.health_bar()
                    id_rect = player.mini_card(surf)
                else:
                    surf.blit(player.image, player.rect.topleft)
                    player.health_bar()
            pygame.display.update()

    def self_assess(self):
        key = {1:'great', 2:'ok', 3:'urgent', 4:'critical', 0:'KO', -1:'KO' }
        hp = self.hit_Points
        hpm = self.hit_Points_Max
        v = hp/hpm

        if v in key:
            pass

        elif v not in key:
            if v > 1:
                v = 1
            elif v < -1:
                v = -1

        value = key[v]
        
        return v, value

    def personal_assess(self, squads):
        weak_ally = None
        weak_enemy = None
        strong_ally = None
        strong_enemy = None
        wa_count = 99999
        we_count = 99999
        sa_count = -9999
        se_count = -9999
        ain_wrange = {}
        ein_wrange = {}
        ain_mrange = {}
        ein_mrange = {}
        cx, cy = self.rect.topleft
        key = {1:'great', 2:'ok', 3:'urgent', 4:'critical'}
        
        wrange = self.move_Range + self.att_Range + 1
        mr = self.move_Range + 1
        for squad in squads:
            r = squad
            #for r in s.roster:
            rx, ry = r.rect.topleft
            dx = abs(cx - rx)
            dy = abs(cx - ry)
            d = (dx + dy)/100
                
            if s.allegiance == self.allegiance:
                if d <= wrange:
                    ain_wrange[r.name] = r
                if d <= mr + 1:
                    ain_mrange[r.name] = r
                if r.hit_Points < wa_count:
                    wa_count = r.hit_Points
                    weak_ally = r
                if r.hit_Points > sa_count:
                    sa_count = r.hit_Points
                    strong_ally = r
            elif s.allegiance != self.allegiance:
                if d <= wrange:
                    ein_wrange[r.name] = r
                if d <= mr + 1:
                    ein_mrange[r.name] = r
                if r.hit_Points < we_count:
                    we_count = r.hit_Points
                    weak_enemy = r
                if r.hit_Points > se_count:
                    sa_count = r.hit_Points
                    strong_enemy = r

        assessment = {'ally':{'strong':strong_ally, 'weak':weak_ally},
                      'enemy':{'strong':strong_enemy, 'weak':weak_enemy}}
        
        return assessment

    def decision_assess(self, assessment):
        ally_s = assessment['ally']['strong']
        ally_w = assessment['ally']['weak']
        enemy_s = assessment['enemy']['strong']
        enemy_s = assessment['enemy']['weak']
        
        aw_num, aw_cond = ally_w.self_assess()
        as_num, as_cond = ally_s.self_assess()
        ew_num, ew_cond = enemy_w.self_assess()
        es_num, es_cond = enemy_s.self_assess()
        #if self condition is bad,
             #heal self
        #elif if self condition is ok
             #if weakest ally condition is bad,
                  #if self has a healing action, heal them,
                  #elif if heal is not in actions
                      #pass
        #elif self condition is better than ok
             #if weakest enemy condition is less than ok and strongest unit is less than ok
                  #choice between units based on terrain
             #elif weakest enemy condition is much worse
                  #attack weak unit
        

       # if aw_num > 2:
       #     if 'heal' in self.
        
    def approach_assess(self, act, assessment, valid_moves):
        ally_s = assessment['ally']['strong']
        ally_w = assessment['ally']['weak']
        enemy_s = assessment['enemy']['strong']
        enemy_s = assessment['enemy']['weak']
                
def zipper(key, value):
    text = ''
    raw = str(key) + ' ' + str(value)
    #print raw
    for element in raw:
        #print element
        if element.isalnum() == True or element.isspace() == True:
            text = text + element
        else:
            pass
    return text
            
def grid_maker(level = None, surface = None):
    strings = type('thing')
    lists = type([])
    nothing = type(None)
    level_type = type(level)
    grid_positions = []
    grid_objects = []
    grid_obstacles = []
    gp_dict = {}
    
    if level_type == lists:
        e_dict = {'b': [7, BLACK, True], 'n':[7, GRAY, None],
                  'i': [2, WHITE, None], 'r':[3, RED, None],
                  'g': [4, GREEN, None], 'b':[5, BLUE, None],
                  'v': [1, PURPLE, None], 'c':[6, CYAN, None],
                  'N':[7, DGRAY, True ], 'I':[2, DWHITE, True],
                  'R':[3, DRED, True], 'G':[4, DGREEN, True],
                  'B':[5, DBLUE, True], 'V':[1, DPURPLE, True],
                  'C':[6, DCYAN, True]}
        k = e_dict.keys()
        i = 0
        j = 0
        for element in level:
            grid_position = {}
            grid_object = field_grid_to_battle_map_converter(element, i, j,
                                                             element.obstacle)
            grid_position[i,j] = grid_object
            grid_objects.append(grid_object)
            grid_positions.append(grid_object.current)
            gp_dict[(i,j)] = grid_object
            pygame.draw.rect(surface, grid_object.color, grid_object.rectangle, 0)
            i = i + 1
            if grid_object.obstacle == True:
                grid_obstacles.append(grid_object.current)
            if i == COLUMNS:
                i = 0
                j = j + 1
            
    elif level_type == strings:
        bmap = battle_map(level, surface)
        grid_positions = bmap.grid_positions
        grid_objects = bmap.grid_objects
        grid_obstacles = bmap.grid_obstacles
        gp_dict = bmap.gp_Dict

    elif level == None:

        i = 0
        j = 0
        for i in range(0,COLUMNS * ROWS):
            grid_object = map_element_grid()
            rectangle, element_of_grid = grid_object.create_grid_element()
            pygame.draw.rect(windowSurface, grid_object.color, grid_object.rectangle, 0)
            grid_positions.append(grid_object.current)
            grid_objects.append(grid_object)
           #print grid_object.current
           #print grid_object.color
           #print grid_object.obstacle
            i = i + 1
            if grid_object.obstacle == True:
                grid_obstacles.append(grid_object.current)
        map_element_grid._ids = count(0)
    pygame.display.update()
   #print grid_obstacles
    return grid_positions, grid_objects, grid_obstacles, gp_dict

def field_grid_to_battle_map_converter(fg_object, x, y, obstacle = False):
    bm_grid = map_element_grid(True, x, y, fg_object.color_Code, fg_object.color, obstacle)
    return bm_grid


def active_grid_check(grid_positions, grid_objects, playerGroup):
    active_Grids = []
    active_Grids_Elements = []
    i = 0
    j = 0
    for player in playerGroup:
        if player.status.has_key('retreat') == True:
            active_Grids.append([playerGroup[i], i, None, -1])
            active_Grids_Elements.append([playerGroup[i].element_type, None])
        elif playerGroup[i].status.has_key('retreat') == False:
            for j in range(0, len(grid_objects)):
                if playerGroup[i].rect.topleft == grid_objects[j].rectangle.topleft:
                    active_Grids.append([playerGroup[i], i, grid_objects[j], j])
                    active_Grids_Elements.append([playerGroup[i].element_type, grid_objects[j].element_type])
                j = j + 1
        i = i +1
   #print active_Grids
   #print active_Grids_Elements
    for i in range(0, len(playerGroup)):
        if playerGroup[i].status.has_key('retreat') == True:
            active_Grids.append([playerGroup[i], i, None, -1])
            active_Grids_Elements.append([playerGroup[i].element_type, None])
        elif playerGroup[i].status.has_key('retreat') == False:
            for j in range(0, len(grid_objects)):
                if playerGroup[i].rect.topleft == grid_objects[j].rectangle.topleft:
                    active_Grids.append([playerGroup[i], i, grid_objects[j], j])
                    active_Grids_Elements.append([playerGroup[i].element_type, grid_objects[j].element_type])
                j = j + 1
        i = i +1
   #print active_Grids
   #print active_Grids_Elements
    return active_Grids, active_Grids_Elements

def grid_refresh(grid_positions, grid_objects):

    rects = []
    for grid_object in grid_objects:
        r = pygame.draw.rect(windowSurface, grid_object.color, grid_object.rectangle, 0)
        pygame.draw.rect(windowSurface, BLACK, grid_object.rectangle, THICK)
        del r

    draw_gridlines(windowSurface, BLACK, WINDOWW, WINDOWH, COLUMNS, ROWS, THICK)
    pygame.display.update()
    
def range_display_off(colored_rects):
        i = 0
        j = []
       #print " removing colored rects display", colored_rects
        for i in range(0, len(colored_rects)):
            uncolored_rect = pygame.Rect((colored_rects[i][0] * 100),(colored_rects[i][1] * 100), GRID_WIDTH, GRID_HEIGHT)
            pygame.draw.rect(windowSurface, BLACK, uncolored_rect, THICK)
            j.append(uncolored_rect)
            i = i + 1
        pygame.display.update()
       #print j
        return j
            

def Battle_Surface_Refresh(grid_positions, grid_objects, playerGroup):
    grid_refresh(grid_positions, grid_objects)
    draw_gridlines(windowSurface, BLACK, WINDOWW, WINDOWH, COLUMNS, ROWS, THICK)

    for player in playerGroup:
        windowSurface.blit(player.image, player.rect.topleft)
        player.health_bar()
    pygame.display.update()
   #print "battle surface refresh exit"

    
def pixel_to_grid_converter(playerGroup):
    refined_Character_Space = []
    for player in playerGroup:
        (x, y) = player.rect.topleft
        (grid_X, grid_Y) = (x/GRID_WIDTH, y/GRID_HEIGHT)
        refined_Character_Space.append((grid_X, grid_Y))

    return refined_Character_Space

def attack_damage_calculator(ch1, ch2, distance, hit, grid_positions, grid_objects, playerGroup):
   #print ch2.hit_Points
    damage = ch1.raw_attack_damage(distance)
    #print "damage", damage
    damage_To_Enemy_Magnifier = element_type_calculator(ch1, ch2, grid_positions, grid_objects, playerGroup)
    damage_To_Self_Magnifier = element_type_calculator(ch2, ch1, grid_positions, grid_objects, playerGroup)
    #print "damage to enemey magnifier", damage_To_Enemy_Magnifier
    #print "damage to self magnifier", damage_To_Self_Magnifier
    damage, damage_To_Enemy, damage_To_Self = attack_damage_modifier(ch1, ch2, damage, damage_To_Enemy_Magnifier, damage_To_Self_Magnifier)
    damage_To_Enemy, damage_To_Self, ch1.hit_Points, ch2.hit_Points = attack_damage_applier(ch1, ch2, hit, damage, damage_To_Enemy, damage_To_Self)

    experience_calculator(ch1, ch2, hit)
    
    return damage_To_Enemy, damage_To_Self, ch1.hit_Points, ch2.hit_Points

def attack_damage_modifier(ch1, ch2, damage, damage_To_Enemy_Magnifier, damage_To_Self_Magnifier):
    if damage <= 0:
        damage = 1
    damage_To_Enemy = int(damage * damage_To_Enemy_Magnifier)
    damage_To_Self = int(damage * damage_To_Self_Magnifier)
    if 'guard' in ch2.status:
       #print ch2.name, ' has guarded'
       #print damage_To_Enemy
        damage_To_Enemy = int(damage_To_Enemy * 3/4)
    if damage_To_Enemy < 1:
        damage_To_Enemy = 1
    if 'covered' in ch2.status:
        damage_To_Enemy = 0
    if damage_To_Self < 0:
        damage_To_Self = 0
    if 'stagger' or 'charging' in ch2.status:
        damage_To_Enemy = damage_To_Enemy * 2
    return damage, damage_To_Enemy, damage_To_Self
   #print damage

def attack_damage_applier(ch1, ch2, distance, hit, damage, damage_To_Enemy, damage_To_Self, grid_positions, grid_objects, playerGroup):
    if hit == True:
       #print "HIT!"
        ch2.hit_Points = ch2.hit_Points - damage_To_Enemy
        damage_To_Self = (int(damage_To_Self / 10) + 1)
        ch1.hit_Points = ch1.hit_Points - (int(damage_To_Self / 10) + 1)
       #print damage_To_Enemy, " was done to ", ch2.name
        #print (int(damage_To_Self / 10) + 1), "was done to", ch1.name
        #print ch2.name, " hit points remaining: ", ch2.hit_Points
        #print ch1.name, " hit points remaining: ", ch1.hit_Points
    
    elif hit == False:
        #print "MISS"
        damage_To_Self = int(damage_To_Enemy/3)
        ch1.hit_Points = ch1.hit_Points - int(damage_To_Enemy/3)
        #print int(damage_To_Enemy/3) , "was done to", ch1.name
        if 'riposte' in ch2.status and distance <= ch2.att_Range:
        #    print 'riposte!'
            riposte_Damage = int(ch2.weapon.raw_weapon_damage(ch2, distance) * ch2.actions['riposte'].multiplier)
            ch1.hit_Points = ch1.hit_Points - riposte_Damage
            damage_To_Self = damage_To_Self + riposte_Damage
        #    print riposte_Damage, 'was done to ', ch1.name
        #print ch2.name, " hit points remaining: ", ch2.hit_Points
        #print ch1.name, " hit points remaining: ", ch1.hit_Points

    ch1.status_update(grid_positions, grid_objects, playerGroup)
    ch2.status_update(grid_positions, grid_objects, playerGroup)
    
    return damage_To_Enemy, damage_To_Self, ch1.hit_Points, ch2.hit_Points

def attack_detect(ch1, ch2):
    detect = False
    if ch1.rect.topleft[0] >= ch2.rect.topleft[0] and 'east' in ch2.direction:
        detect = True
    if ch1.rect.topleft[0] > ch2.rect.topleft[0] and 'west' in ch2.direction:
        detect = False
    if ch1.rect.topleft[0] < ch2.rect.topleft[0] and 'east' in ch2.direction:
        detect = False
    if ch1.rect.topleft[0] <= ch2.rect.topleft[0] and 'west' in ch2.direction:
        detect = True
    if ch1.rect.topleft[1] > ch2.rect.topleft[1] and 'north' in ch2.direction:
        detect = False
    if ch1.rect.topleft[1] >= ch2.rect.topleft[1] and 'south' in ch2.direction:
        detect = True
    if ch1.rect.topleft[1] <= ch2.rect.topleft[1] and 'north' in ch2.direction:
        detect = True
    if ch1.rect.topleft[1] < ch2.rect.topleft[1] and 'south' in ch2.direction:
        detect = False
    #print ch1.rect.topleft, 'ch1 topleft'
    #print ch2.rect.topleft, 'ch2 topleft'
    #print detect, 'detect'
    return detect
    

def magic_damage_calculator(ch1, ch2, sacrifice, hit, grid_positions, grid_objects, playerGroup, distance):
    damage = ch1.raw_magic_damage(sacrifice)
   #print "damage", damage
    damage_To_Enemy_Magnifier = element_type_calculator(ch1, ch2, grid_positions, grid_objects, playerGroup)
    damage_To_Self_Magnifier = element_type_calculator(ch2, ch1, grid_positions, grid_objects, playerGroup)
   #print "damage to enemey magnifier", damage_To_Enemy_Magnifier
   #print "damage to self magnifier", damage_To_Self_Magnifier
    damage_To_Enemy = int(damage * damage_To_Enemy_Magnifier)
    damage_To_Self = int(sacrifice * damage_To_Self_Magnifier)
    
    if hit == True:
       #print "Magic Hit"
        ch2.hit_Points = ch2.hit_Points - damage_To_Enemy
        ch1.hit_Points = ch1.hit_Points - (sacrifice * damage_To_Self_Magnifier)
       #print damage_To_Enemy, " was done to ", ch2.name
       #print int(sacrifice * damage_To_Self_Magnifier), " was done to ", ch1.name
       #print ch2.name, " hit points remaining: ", ch2.hit_Points
       #print ch1.name, " hit points remaining: ", ch1.hit_Points
    if hit == False:
       #print "Miss"
        ch1.hit_Points = ch1.hit_Points - sacrifice
       #print ch1.name, " hit points remaining: ", ch1.hit_Points

    experience_calculator(ch1, ch2, hit)
    
    return damage_To_Enemy, damage_To_Self

def experience_calculator(ch1, targets, hit):
    i = 0
   #print hit
    if len(targets) > 1:
        for target in targets:
            y = 0
            x = ch1.level - target.level
            if y < x:
                y = x
        
        experience = 10 - y
        shared_Experience = int(experience/(len(targets)))
        if experience <= 0:
            experience = 1
       #print hit
        if True in hit :
            ch1.exp = ch1.exp + experience
           #print ch1.name, " gained ", experience, " experience points"
            ch1.level_up()
        else:
            for target in targets:
                target.exp = target.exp + shared_Experience
               #print target.name, " gained ", shared_Experience, " experience points"
                target.level_up()
                
    elif len(targets) == 1:
        x = ch1.level - targets.level
        experience = 10 - x
        if hit[0] == True :
            ch1.exp = ch1.exp + experience
           #print ch1.name, " gained ", experience, " experience points"
            ch1.level_up()
        elif hit[0] == False and ch1.name != targets.name:
            targets.exp = targets.exp + experience
           #print targets.name, " gained ", experience, " experience points"
            targets.level_up()
        elif ch1.name == targets.name and hit[0] == False:
            pass

def element_type_calculator(ch1, ch2, grid_positions, grid_objects, playerGroup):
    element_type = {1:"void", 2:"infinity", 3:"fire", 4:"earth", 5:"water", 6:"sky", 7:"null"}
    active_Grids, active_Grids_Elements = active_grid_check(grid_positions, grid_objects, playerGroup)
    #print "here are the active grids ", active_Grids
    #print "here are the active grid elements", active_Grids_Elements
    #print ch2
    magnifier = 1
    i = 0
    j = 0
    while ch1 != playerGroup[i]:
    #    print i
        i = i + 1
    #print "ch1 = player",i+1
    #print ch2
    #print ch2.name
    while ch2 != playerGroup[j]:
    #    print playerGroup[j].name
        j = j + 1
    #print "ch2 = player",j+1
    #print "object details"
    #print i, j, "i and j"

    x = elemental_Object_Compare(ch1, ch2)
    #print active_Grids[0]
    #print len(active_Grids), 'active grids length'
    #print x, 'x'
    #print playerGroup, 'playergroup'
    #print active_Grids[i][2], i,'active_Grids[i][2]'
    #print active_Grids[j][2], j,'active_Grids[j][2]'
    y = elemental_Object_Compare(active_Grids[i][2], active_Grids[j][2])
    #print y
    z = elemental_Object_Contrast(ch1, active_Grids[i][2])
    #print z
    w = elemental_Object_Contrast(ch2, active_Grids[j][2])
    #print w
    if w < 0.5:
         w = 0.5
    magnifier = (z * x * y) /  w
    if magnifier < 0:
        magnifier = 0
    #print magnifier
    return magnifier

def elemental_Object_Contrast(Object1, Object2):
    magnifier = 1
    if Object1.element_type == (Object2.element_type - 1):
        magnifier = magnifier - .5

    if Object1.element_type == (Object2.element_type + 1):
        magnifier = magnifier - .5

    if Object1.element_type == 7 or Object2.element_type == 7 :
        magnifier = magnifier

    if Object1.element_type == Object2.element_type:
        magnifier = magnifier + 1

    if Object1.element_type == 1 and Object2.element_type == 3:
        magnifier = magnifier - 0.5
        
    if Object1.element_type == 7 and Object2.element_type == 7:
        magnifier = magnifier
    #print "element 1 is ", Object1.element, Object1.element_type 
    #print "element 2 is ", Object2.element, Object2.element_type
    
    return magnifier

def elemental_Object_Compare(Object1, Object2):
    magnifier = 1
    #print 'elemental obkect compare'
    if Object1.element_type == (Object2.element_type - 1):
        magnifier = magnifier - .5

    if Object1.element_type == (Object2.element_type + 1):
        magnifier = magnifier + .5

    if Object1.element_type == 7 or Object2.element_type == 7 :
        magnifier = magnifier

    if Object1.element_type == Object2.element_type:
        magnifier = magnifier - 0.5

    if Object1.element_type == 1 and Object2.element_type == 3:
        magnifier = magnifier - 0.5
        
    if Object1.element_type == 7 and Object2.element_type == 7:
        magnifier = magnifier
        
    if Object1.element_type == 6 and Object2.element_type == 7:
        magnifier = magnifier + 0.5

    #print "element 1 is ", Object1.element, Object1.element_type
    #print "element 2 is ", Object2.element, Object2.element_type
    return magnifier

def team_check(group):
    group_Valid = True
    tally = []
    for player in group.roster:
        
        if player.hit_Points > 0 and player.status.has_key('retreat') == False :
            tally.append(True)
        elif player.hit_Points <= 0 or player.status.has_key('retreat') == True:
            tally.append(False)
    if True not in tally:
        group_Valid = False
    elif True in tally:
        group_Valid = True

    return group_Valid

def battle_completion(*teams ):
    results = []
    rebs = []
    loys = []
    neus = []

    allegiances = {'rebel':rebs, 'loyalist':loys, 'neutral':neus}
    for sides in teams:
        #print sides, 'team'
        
        for side in sides:
            s = sides[side]

            for group in s:
                g = s[group]
                
                for a in allegiances:
                    if a == g.allegiance:
                        result = team_check(g)
                        allegiances[a].append(result)
                    elif a != g.allegiance:
                        pass
                    
    for a in allegiances:
        if True in allegiances[a]:
            pass
        elif allegiances[a] != []:
            if True not in allegiances[a]:
                return a
    return True

def battle_determination(allegiances, belligerents ):
    valid_r = True
    valid_l = True
    Valid_n = None
    rebs = 0
    loys = 0
    neus = 0
    counts = {'rebel':rebs, 'loyalist':loys, 'neus':neus}
    for belligerent in belligerents:
        ba = belligerent.allegiance
        adc = len(allegiences[ba][dead])
        for allegiant in counts:
            if ba == allegiant:
                counts[ba] = counts[ba] + 1
                if counts[ba] == adc:
                    return allegiant
        if ba == 'rebel':
            counts[ba] = counts[ba] + 1
        elif ba == 'loyalist':
            loys = loys + 1
        elif ba == 'neutral':
            neus = neus + 1

    i = 0
    loser = 10 
    for i in range(len(results)):
        if results[i] == True:
            pass
        elif results[i] == False:
            loser = i
        i = i + 1

    return loser

def start_position(team1, team2, rect_list):
    t1_fpos = (team1.rect.center[0], team1.rect.center[1])
    t2_fpos = (team2.rect.center[0], team2.rect.center[1])
    x = 0
    y = 0
    t1_spos = 'o'
    t2_spos = 'o'
    obstacle_check = {}
    sections = {'nw':[(0,0), (0,1), (1,0), (1,1)],
                'n':[(2,0), (2,1), (3,0), (3,1)],
                'ne':[(4,0), (4,1), (5,0), (5,1)],
                'w':[(0,2), (1,2), (0,3), (1,3)],
                'o':[(2,2), (2,3), (3,2), (3,3)],
                'e':[(4,2), (4,3), (5,2), (5,3)],
                'sw':[(0,4), (0,5), (1,4), (1,5)],
                's':[(2,4), (2,5), (3,4), (3,5)],
                'se':[(4,4), (4,5), (5,4), (5,5)]}
    h2p = {'nw':'se', 'n':'s', 'ne':'sw', 'e':'w', 'o':'o', 'w':'e',
           'sw':'ne', 's':'n', 'se':'nw'}
    if t1_fpos[0] > t2_fpos[0]:
        if t1_fpos[1] > t2_fpos[1]:
            t1_spos = 'se'
            t2_spos = 'nw'
        elif t1_fpos[1] < t2_fpos[1]:
            t1_spos = 'ne'
            t2_spos = 'sw'
        elif t1_fpos[1] == t2_fpos[1]:
            t1_spos = 'e'
            t2_spos = 'w'
    elif t1_fpos[0] < t2_fpos[0]:
        if t1_fpos[1] > t2_fpos[1]:
            t1_spos = 'sw'
            t2_spos = 'ne'
        elif t1_fpos[1] < t2_fpos[1]:
            t1_spos = 'nw'
            t2_spos = 'se'
        elif t1_fpos[1] == t2_fpos[1]:
            t1_spos = 'w'
            t2_spos = 'e'
    elif t1_fpos[0] == t2_fpos[0]:
        if t1_fpos[1] > t2_fpos[1]:
            t1_spos = 's'
            t2_spos = 'n'
        elif t1_fpos[1] < t2_fpos[1]:
            t1_spos = 'n'
            t2_spos = 's'
        elif t1_fpos[1] == t2_fpos[1]:
            t1_spos = 'w'
            t2_spos = 'e'
    t1_sp = sections[t1_spos]
    t2_sp = sections[t2_spos]
    return t1_sp, t2_sp
                          
def start_position2(squadGroup, start_points, rect_list, b_field):
    x = b_field.topleft[0]
    y = b_field.topleft[1]
    w = b_field.width
    h = b_field.height
    grid_w = b_field.width/3
    grid_h = b_field.height/3
    rw = b_field.width %3
    rh = b_field.height %3
    start_section = {}
    section_rects = {'nw':pygame.rect.Rect(x, y, grid_w, grid_h ),
                'n':pygame.rect.Rect(x + grid_w, y, grid_w, grid_h ),
                'ne':pygame.rect.Rect(x + grid_w * 2, y, grid_w + rw, grid_h ),
                'w':pygame.rect.Rect(x, y + grid_h, grid_w, grid_h ),
                'o':pygame.rect.Rect(x + grid_h, y + grid_h , grid_w, grid_h ),
                'e':pygame.rect.Rect(x + grid_w * 2, y + grid_h, grid_w + rw, grid_h),
                'sw':pygame.rect.Rect(x, y + grid_h * 2, grid_w, grid_h + rh),
                's':pygame.rect.Rect(x + grid_w, y + grid_h * 2, grid_w, grid_h + rh),
                'se':pygame.rect.Rect(x + grid_w *2, y + grid_h * 2, grid_w + rw, grid_h + rh)}
    #h2p = ['nw', 'n', 'ne', 'e', 'o', 'w', 'sw', 's', 'n', 'se']
    h2p = {'nw':'se', 'n':'s', 'ne':'sw', 'e':'w', 'o':'o', 'w':'e',
           'sw':'ne', 's':'n', 'se':'nw'}
    sections = {'nw':[(0,0), (0,1), (1,0), (1,1)],
                'n':[(2,0), (2,1), (3,0), (3,1)],
                'ne':[(4,0), (4,1), (5,0), (5,1)],
                'w':[(0,2), (1,2), (0,3), (1,3)],
                'o':[(2,2), (2,3), (3,2), (3,3)],
                'e':[(4,2), (4,3), (5,2), (5,3)],
                'sw':[(0,4), (0,5), (1,4), (1,5)],
                's':[(2,4), (2,5), (3,4), (3,5)],
                'se':[(4,4), (4,5), (5,4), (5,5)]}

    
    for squad in squadGroup:
        if squad.status.has_key('in transit') == False:
            x = start_points[squad.name]
            for section in section_rects:
                if section_rects[section].collidepoint(x) == 1:
                    start_section[squad.name] = sections[section]
                elif section_rects[section].collidepoint(x) != 1:
                    pass
        elif squad.status.has_key('in transit') == True:
            start = h2p[squad.heading]
            start_section[squad.name] = sections[start]

    return start_section

#made a modification to timeflow to account for more than 2 squads
def time_flow(belligerents, start_points, rect_list, b_field, s_towns ):
    playerGroup = []
    squadGroup = []
    rebels = []
    loyalists = []
    neutrals = []
    for side in belligerents:
        for squad_name in belligerents[side]:
            squad = belligerents[side][squad_name]
            squadGroup.append(squad)
            for member in squad.roster:
                a = member.allegiance
                playerGroup.append(member)
                if  a == 'rebel':
                    rebels.append(member)
                elif a == 'loyalist':
                    loyalists.append(member)
                elif a == 'neutral':
                    neutrals.append(member)
    
    i = 0
    grid_positions, grid_objects, grid_obstacles, grid_dict = grid_maker(rect_list, windowSurface)
   #print grid_obstacles
    draw_gridlines(windowSurface, BLACK, WINDOWW, WINDOWH, COLUMNS, ROWS, THICK)
    start_positions = start_position2(squadGroup, start_points, rect_list, b_field)

    for squad in squadGroup:
       #print squadGroup
       #print start_positions, 'start positions'
        for player in squad.roster:
            spot1 = randrange(0,4)
           #print player.rect.topleft, 'player rect topleft'
            spot = (start_positions[squad.name][spot1][0] * 100,
                    start_positions[squad.name][spot1][1] * 100) 
            player.rect.topleft = spot
            player.grid_Char_Rect = ((player.rect.topleft[0]/100),(player.rect.topleft[1]/100)) 
            windowSurface.blit(player.image, player.rect.topleft)
            
    pygame.display.update()
   #print ' in time flow'
   #print grid_obstacles
    flow = True
    pygame.display.set_caption('battle map')
    chars = playerGroup
   #print grid_obstacles
    active_Grids = active_grid_check(grid_positions, grid_objects, playerGroup)
    action_Timeflow_List = []
   #print 'about to enter while flow loop'
   #print grid_obstacles
    loser = 10
   #print "here are the active grids", active_Grids
    #print grid_obstacles
    while flow == True:
        end = False
        if actions != []:
            for action in action_Timeflow_List:
                action_turn = action.ct_update(action.using)
                #print action.name, 'by ', action.using.name, ' ct is ', action.ct
                if action_turn == True:
                #    print action_Timeflow_List
                    action.action_effect(action.using, action.targeting, action.distance, grid_positions, grid_objects, playerGroup)
                    action_Timeflow_List.remove(action)
                    action.using.action_Charging = 0
        loser = battle_completion(belligerents)
        if loser == True:
            pass
        elif loser != True:
            break

        for char in chars:
            char.health_bar()
        pygame.display.update()
        for char in chars:
            ai = False
            if char.allegiance != 'rebel':
                ai = True
            char_turn = char.ct_update(grid_positions, grid_objects, playerGroup)
            #print char.name, 'ct is ', char.ct
            if 'retreat' not in char.status and char_turn == True:
                #char.highlight_character()
                act = char.character_turn(action_Timeflow_List, grid_positions, grid_objects, grid_dict, grid_obstacles, playerGroup, ai)
                loser = battle_completion(belligerents)
                if loser == True:
                    pass
                elif loser != True:
                    break

    for side in belligerents:
        #print side
        for squad in belligerents[side]:
        #    print squad
            b = belligerents[side]
        #    print b
        #    print b[squad]
            if b[squad].allegiance == loser:
                b[squad].rect.center = b[squad].lost_battle(s_towns)
               #print b[squad], 'is a loser'
                if b[squad].status.has_key('in transit') == True:
                    del b[squad].status['in transit']
                    b[squad].goal = b[squad].rect.center
                elif b[squad].status.has_key('in transit') == False:
                    pass
                if len(b[squad].roster) > 1:
                    for player in b[squad].roster:
                        ps = player.status
                        if ps.has_key('retreat') == True:
                            del ps['retreat']
                        elif ps.has_key('retreat') == False:
                            pass
                elif len(b[squad].roster) == 1:
                    bsr0 = b[squad].roster[0].status
                    if bsr0.has_key('retreat') == True:
                        del bsr0['retreat']
                    elif bsr0.has_key('retreat') == False:
                        pass
    return belligerents, flow, loser

class MSDie:

    def __init__(self, sides):
        self.sides = sides
        self.value = 1

    def roll(self):
        self.value = randrange(1, self.sides+1)

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

#items
potion = item('potion', 30, {7:'null'}, 'item', 'heal', None, None, 0,
              1, None, 0, None, 100, 1, False, '+')
poison = item('poison', -5, {7:'null'}, 'item', 'status', None, 'poison', 0,
              1, None, 0, None, 100, 1, False, '-')
grenade = item('grenade', -30, {7:'null'}, 'item', 'hurt', None, None, 20,
               3, None, 1, None, 100, 1, False, '-')
phoenix_Down = item('phoenix down', 20, {7:'null'}, 'item', 'status',
                    None, ('-', 'KO'), 0, 1, None, 0, None, 100, 1, False, '+')
items = (potion, poison, grenade, phoenix_Down)
items_cost = {'wood sword':50, 'wood helmet':50,
                  'wood armor':50,'potion':20, 'poison':100,
                  'grenade':200, 'phoenix_Down':300}    
wood_sword = weapon('wood sword', 100, 'sword', 0,0,0,0,0,0,0,[])
wood_armor = armor('wood armor', 100, 'heavy armor', 0, 0, 0, 0, 0, 0, 0, [])
wood_helmet = armor('wood helmet', 100, 'helmet', 0, 0, 0, 0, 0, 0, 0, [])
test_sword1 = weapon('test sword1', 100, 'sword', 0,0,0,0,0,0,0,[])
test_sword2 = weapon('test sword2', 100, 'sword', 0,0,0,0,0,0,0,[])
test_sword3 = weapon('test sword3', 100, 'sword', 0,0,0,0,0,0,0,[])
test_sword4 = weapon('test sword4', 100, 'sword', 0,0,0,0,0,0,0,[])
test_sword5 = weapon('test sword5', 100, 'sword', 0,0,0,0,0,0,0,[])
test_sword6 = weapon('test sword6', 100, 'sword', 0,0,0,0,0,0,0,[])
test_sword7 = weapon('test sword7', 100, 'sword', 0,0,0,0,0,0,0,[])
test_sword8 = weapon('test sword8', 100, 'sword', 0,0,0,0,0,0,0,[])
test_sword9 = weapon('test sword9', 100, 'sword', 0,0,0,0,0,0,0,[])
test_sword10 = weapon('test sword10', 100, 'sword', 0,0,0,0,0,0,0,[])
test_sword11 = weapon('test sword11', 100, 'sword', 0,0,0,0,0,0,0,[])
test_sword12 = weapon('test sword12', 100, 'sword', 0,0,0,0,0,0,0,[])
test_sword13 = weapon('test sword13', 100, 'sword', 0,0,0,0,0,0,0,[])
test_sword14 = weapon('test sword14', 100, 'sword', 0,0,0,0,0,0,0,[])

#towns
tattoine = place('tattoine', 'town', 10, 'rebel',
                       ['enlistment', 'create squad', 'merchant'],
                       (550, 550), items, items_cost, True)
deathStar = place('deathStar', 'castle', 10, 'loyalist',
                    ['enlistment', 'create squad', 'merchant'],
                    (75, 30), items, items_cost, True)
cloudCity = place('cloudCity', 'town', 10, 'rebel',
                ['enlistment', 'merchant'],
                (450, 125), None, None, False)
hamen_towns = {'tattoine': tattoine, 'deathStar':deathStar, 'cloudCity':cloudCity}

mounttown = place('mountTowns', 'town', 10, 'rebel',
                  ['enlistment', 'create squad', 'merchant'],
                  (80, 50), items, items_cost, True)
enemase = place('enemase', 'castle', 10, 'loyalist',
                    ['enlistment', 'create squad', 'merchant'],
                    (535, 530), items, items_cost, True)
mountain_towns = {'mountTowns': mounttown, 'enemase':enemase}

swallowFalss = place('swallowFalss', 'town', 10, 'rebel',
                       ['enlistment', 'create squad', 'merchant'],
                       (100, 500), items, items_cost, True)
mortred = place('mortred', 'castle', 10, 'loyalist',
                    ['enlistment', 'create squad', 'merchant'],
                    (550, 50), items, items_cost, True)
acidBase = place('acidBase', 'town', 10, 'rebel',
                ['enlistment', 'merchant'],
                (200, 100), None, None, False)
swamp_towns = {'swallowFalss': swallowFalss, 'mortred':mortred, 'acidBase':acidBase}

p = p_Char('Randy', 10, 1000, 'rebel', 1)

mopla_stage = field_Map_Level(fieldSurface, 10,
                           'C:\Python27\python test folder and drafts\ogre Fantasy\mount_plains.txt', mountain_towns)
snow_stage = field_Map_Level(fieldSurface, 10,
                           'C:\Python27\python test folder and drafts\ogre Fantasy\msnowlevel.txt', swamp_towns)
t9_stage = field_Map_Level(fieldSurface, 10,
                           'C:\Python27\python test folder and drafts\ogre Fantasy\mest9.txt', swamp_towns)
test_stage = field_Map_Level(fieldSurface, 10,
                              'C:\Python27\python test folder and drafts\ogre Fantasy\mestlevel.txt',mountain_towns)
swamp_stage = field_Map_Level(fieldSurface, 10,
                              'C:\Python27\python test folder and drafts\ogre Fantasy\swamplevel.txt', swamp_towns)
mountains_stage = field_Map_Level(fieldSurface, 10,
                        'C:\Python27\python test folder and drafts\mield_level3.txt', mountain_towns)#,
hamen_stage = field_Map_Level(fieldSurface, 10,
                        'C:\Python27\python test folder and drafts\mield_level2.txt', hamen_towns)#,
                        #towns, 1000, 'loyalist', {}, 11)
mopl_stage = stage_object('mount plains', mopla_stage, (200, 300), 0)
snow_stage = stage_object('snow', snow_stage, (100, 100), 0)
t9_stage = stage_object('test', t9_stage, (200, 200), 0)
t_stage = stage_object('test', test_stage, (300, 300), 0)
m_stage = stage_object('mountain', mountains_stage, (400, 400), 0)
h_stage = stage_object('hamen', hamen_stage, (450, 450), 1)
s_stage = stage_object('swamp', swamp_stage, (300, 475), 1)
stages = {'mountains':m_stage, 'hamen':h_stage, 'swamps':s_stage,
          'test':t_stage, 't9':t9_stage, 'snow':snow_stage,
          'mount plains':mopl_stage}

world_map_mode(p, stages)
