import pygame
import random

# 게임 초기화
pygame.init()
screen_width = 300
screen_height = 600
block_size = 30
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tetris")

# 색상 정의
colors = [
    (0, 0, 0),    # 배경색 (검정)
    (255, 0, 0),  # 빨강
    (0, 255, 0),  # 초록
    (0, 0, 255),  # 파랑
    (255, 255, 0),# 노랑
    (255, 165, 0),# 주황
    (128, 0, 128) # 보라
]

# 테트로미노 모양 정의
shapes = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]],  # J
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]]   # Z
]

class Tetromino:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.shape = random.choice(shapes)
        self.color = random.randint(1, len(colors) - 1)

    def rotate(self):
        """ 블록 회전 """
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

def create_grid(locked_positions={}):
    """ 20x10 그리드 생성 및 잠긴 블록 추가 """
    grid = [[(0, 0, 0) for _ in range(10)] for _ in range(20)]
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if (x, y) in locked_positions:
                grid[y][x] = locked_positions[(x, y)]
    return grid

def draw_window(surface, grid, current_piece):
    """ 화면을 지우고, 그리드와 현재 블록을 그림 """
    surface.fill((0, 0, 0))
    
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            pygame.draw.rect(surface, grid[y][x], (x * block_size, y * block_size, block_size, block_size), 0)

    # 현재 블록도 함께 그리기
    for pos in convert_shape_format(current_piece):
        x, y = pos
        if y >= 0:
            pygame.draw.rect(surface, colors[current_piece.color], (x * block_size, y * block_size, block_size, block_size), 0)

    draw_grid_lines(surface)
    pygame.display.update()

def draw_grid_lines(surface):
    """ 격자 라인 그리기 """
    for y in range(20):
        pygame.draw.line(surface, (128, 128, 128), (0, y * block_size), (screen_width, y * block_size))
    for x in range(10):
        pygame.draw.line(surface, (128, 128, 128), (x * block_size, 0), (x * block_size, screen_height))

def convert_shape_format(shape):
    """ 테트로미노의 위치를 변환하여 반환 """
    positions = []
    for i, row in enumerate(shape.shape):
        for j, cell in enumerate(row):
            if cell == 1:
                positions.append((shape.x + j, shape.y + i))
    return positions

def valid_space(shape, grid):
    """ 현재 블록이 유효한 공간에 있는지 검사 """
    for x, y in convert_shape_format(shape):
        if x < 0 or x >= 10 or y >= 20 or grid[y][x] != (0, 0, 0):
            return False
    return True

def clear_rows(grid, locked_positions):
    """ 블록이 가득 찬 행을 삭제하고 위 블록을 아래로 이동 """
    rows_to_clear = [y for y in range(20) if all(grid[y][x] != (0, 0, 0) for x in range(10))]
    
    for row in rows_to_clear:
        del locked_positions[row]  # 해당 행 삭제
        for key in sorted(locked_positions.keys(), reverse=True):
            if key < row:
                locked_positions[key + 1] = locked_positions.pop(key)  # 위 블록들을 한 칸씩 내리기
    return len(rows_to_clear)  # 삭제된 줄 개수 반환

def main():
    locked_positions = {}
    grid = create_grid(locked_positions)

    run = True
    current_piece = Tetromino(4, 0)
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.3

    while run:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()

        # 블록 자동 내려오기
        if fall_time / 1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not valid_space(current_piece, grid):
                current_piece.y -= 1
                for pos in convert_shape_format(current_piece):
                    locked_positions[pos] = colors[current_piece.color]
                clear_rows(grid, locked_positions)  # 행 제거
                current_piece = Tetromino(4, 0)  # 새 블록 생성

        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  # 왼쪽 이동
                    current_piece.x -= 1
                    if not valid_space(current_piece, grid):
                        current_piece.x += 1
                elif event.key == pygame.K_RIGHT:  # 오른쪽 이동
                    current_piece.x += 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1
                elif event.key == pygame.K_DOWN:  # 즉시 하강
                    while valid_space(current_piece, grid):
                        current_piece.y += 1
                    current_piece.y -= 1
                elif event.key == pygame.K_UP:  # 회전
                    current_piece.rotate()
                    if not valid_space(current_piece, grid):
                        current_piece.rotate()
                        current_piece.rotate()
                        current_piece.rotate()  # 원상복구

        draw_window(screen, grid, current_piece)

    pygame.quit()

# 실행
if __name__ == "__main__":
    main()
