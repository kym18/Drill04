from pico2d import *

open_canvas()

tuk = load_image('TUK_GROUND.png')
character = load_image('news.png')


# 캐릭터의 상태 변수 초기화
global moving_right, moving_left, moving_up, moving_down, speed, x, y, running, frame
moving_right = False
moving_left = False
moving_up = False
moving_down = False
speed = 5
x, y = 400, 405
running = True
frame = 0
dir =0

def character_moving():  # 1015   490
    global running, moving_right, moving_left, moving_up, moving_down
    global x, y, speed, frame
    if moving_left:
        character.clip_draw(frame * 85 + 595, 324, 60, 79, x, y)
        x -= speed
        frame = (frame + 1) % 3
        if x <= 20:
            moving_left = False

    elif moving_right:
        character.clip_draw(frame * 85, 163, 63, 79, x, y)
        x += speed
        frame = (frame + 1) % 11
        if x >= 760:
            moving_right = False

    elif moving_up:
        character.clip_draw(frame * 85, 81, 60, 79, x, y)
        y += speed
        frame = (frame + 1) % 6
        if y >= 570:
            moving_up = False

    elif moving_down:
        character.clip_draw(frame * 85 + 515, 81, 60, 79, x, y)
        y -= speed
        frame = (frame + 1) % 6
        if y <= 30:
            moving_down = False

    else:  # 대기
        character.clip_draw(frame * 85 + 427 , 410, 73, 80, x, y)
        frame = (frame + 1) % 7


def handle_events():
    global running, moving_right, moving_left, moving_up, moving_down, dir
    # 키 입력 처리
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            close_canvas()
            exit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                moving_right = True
            elif event.key == SDLK_LEFT:
                moving_left = True
            elif event.key == SDLK_UP:
                moving_up = True
            elif event.key == SDLK_DOWN:
                moving_down = True
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                moving_right = False
            elif event.key == SDLK_LEFT:
                moving_left = False
            elif event.key == SDLK_UP:
                moving_up = False
            elif event.key == SDLK_DOWN:
                moving_down = False

while running:
    clear_canvas()
    tuk.draw(400, 90)

    character_moving()
    update_canvas()
    handle_events()
    delay(0.05)

close_canvas()
