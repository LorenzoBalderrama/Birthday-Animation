import os
import time
import sys
from random import randint, choice

# ANSI color codes
COLORS = {
    'RED': '\033[91m',
    'GREEN': '\033[92m',
    'YELLOW': '\033[93m',
    'BLUE': '\033[94m',
    'PURPLE': '\033[95m',
    'CYAN': '\033[96m',
    'WHITE': '\033[97m',
    'RESET': '\033[0m'
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_heart(color):
    return [
        f"{color}  $$$$$ $$$$$  {COLORS['RESET']}",
        f"{color} $$$$$$$$$$$$$$ {COLORS['RESET']}",
        f"{color}$$$$$$$$$$$$$$$${COLORS['RESET']}",
        f"{color} $$$$$$$$$$$$$$ {COLORS['RESET']}",
        f"{color}  $$$$$$$$$$$  {COLORS['RESET']}",
        f"{color}    $$$$$$$    {COLORS['RESET']}",
        f"{color}      $$$      {COLORS['RESET']}",
        f"{color}       $       {COLORS['RESET']}"
    ]

def create_cake():
    cake = [
        f"{COLORS['YELLOW']}    ( ) ( ) ( ) ( ){COLORS['RESET']}",
        f"{COLORS['RED']}  |-|-|-|-|-|-|-|-|{COLORS['RESET']}",
        f"{COLORS['YELLOW']}  |{COLORS['WHITE']} H A P P Y {COLORS['YELLOW']}|{COLORS['RESET']}",
        f"{COLORS['YELLOW']}  |{COLORS['WHITE']} BIRTHDAY!{COLORS['YELLOW']}|{COLORS['RESET']}",
        f"{COLORS['YELLOW']}  |-|-|-|-|-|-|-|-|{COLORS['RESET']}",
        f"{COLORS['CYAN']}~~~~~~~~~~~~~~~~~~~~~~{COLORS['RESET']}",
        f"{COLORS['CYAN']}\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\{COLORS['RESET']}"
    ]
    return cake

def create_sparkle(width, height):
    canvas = [[' ' for _ in range(width)] for _ in range(height)]
    sparkles = ['*', '✦', '✧', '♥', '✺', '⋆']
    colors = [COLORS['YELLOW'], COLORS['CYAN'], COLORS['PURPLE'], COLORS['RED']]
    
    # Add random sparkles
    for _ in range(width * height // 50):
        x = randint(0, width-1)
        y = randint(0, height-1)
        canvas[y][x] = f"{choice(colors)}{choice(sparkles)}{COLORS['RESET']}"
    
    return canvas

def merge_layers(background, foreground, pos_x, pos_y):
    for y, row in enumerate(foreground):
        if pos_y + y < len(background):
            for x, char in enumerate(row):
                if pos_x + x < len(background[0]) and char != ' ':
                    background[pos_y + x][pos_x + x] = char

def animate_scene(duration=10):  # Duration in seconds
    width = os.get_terminal_size().columns
    height = os.get_terminal_size().lines
    frame = 0
    start_time = time.time()
    
    try:
        while time.time() - start_time < duration:
            clear_screen()
            
            # Create background with sparkles
            canvas = create_sparkle(width, height)
            
           # Cake
            cake = create_cake()
            cake_x = width // 2 - 10
            cake_y = height // 2
            
            # Add hearts
            left_heart = create_heart(COLORS['RED'])
            right_heart = create_heart(COLORS['BLUE'])
            
            # Calculate positions with slight movement
            heart_offset = abs(round(math.sin(frame * 0.1) * 2))
            
            # Render everything
            for y in range(height):
                line = ''
                for x in range(width):
                    line += canvas[y][x]
                print(line)
            
            frame += 1
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        pass
    finally:
        clear_screen()
        print(f"{COLORS['YELLOW']}Happy Birthday! 🎂✨{COLORS['RESET']}")

if __name__ == "__main__":
    import math  
    animate_scene(5)  # Time it runs for