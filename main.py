import pygame

pygame.init()

screen_width = 8*80
screen_height = 8*80
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Chess practicer")
clock = pygame.time.Clock()

run = True

clicked = False
selected_piece_boolean = False
success_selection_boolean = False

chess_board_img = pygame.transform.scale(pygame.image.load("assets/chess_board.png"), (screen_width, screen_height))

default_set = [
    ["rook_bl", "knight_bl", "bishop_bl", "queen_bl", "king_bl", "bishop_bl", "knight_bl", "rook_bl"],
    ["pawn_bl", "pawn_bl", "pawn_bl", "pawn_bl", "pawn_bl", "pawn_bl", "pawn_bl", "pawn_bl"],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["pawn_wh", "pawn_wh", "pawn_wh", "pawn_wh", "pawn_wh", "pawn_wh", "pawn_wh", "pawn_wh"],
    ["rook_wh", "knight_wh", "bishop_wh", "queen_wh", "king_wh", "bishop_wh", "knight_wh", "rook_wh"]
]

def check_clicked(list):
    global clicked
    global selected_piece_boolean
    global selected_piece_obj
    global selected_piece_str
    global success_selection_boolean
    global org_pos_of_sel_piece_row
    global org_pos_of_sel_piece_col
    mx, my = pygame.mouse.get_pos()

    if pygame.mouse.get_pressed()[0] == True:
            row = int(my//(screen_height/8))
            col = int(mx//(screen_height/8))
            

            if list[row][col] != "" or success_selection_boolean == True:
                if clicked == False:
                    selected_piece_obj = pygame.image.load(f"assets/{list[row][col]}.png")
                    selected_piece_str = list[row][col]
                    org_pos_of_sel_piece_row = row
                    org_pos_of_sel_piece_col = col
                    list[row][col] = ""
                if row < 0 or row > 7 or col < 0 or col > 7:
                     list[org_pos_of_sel_piece_row][org_pos_of_sel_piece_col] = selected_piece_str
                     success_selection_boolean = False
                screen.blit(selected_piece_obj, (mx-(selected_piece_obj.get_width()/2), my-(selected_piece_obj.get_height()/2))) 
                success_selection_boolean = True
                clicked = True
            
            
    if pygame.mouse.get_pressed()[0] == False and clicked == True:
            if success_selection_boolean == True:
                row = int(my//(screen_height/8))
                col = int(mx//(screen_height/8)) 
                list[row][col] = selected_piece_str
                success_selection_boolean = False
            clicked = False

    

    

def display_chesspieces(list):
    for row in range (0, 8):
        for col in range (0, 8):
            if list[row][col] != "":
                screen.blit(pygame.image.load(f"assets/{list[row][col]}.png"), ((screen_width/8)*col, (screen_height/8)*row))
    



while run:
    screen.blit(chess_board_img, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    display_chesspieces(default_set) 
    check_clicked(default_set)

    pygame.display.update()
    clock.tick(60)
pygame.quit()