import subprocess
import pygame
import time


# Function to ping the specified IP address
def ping(ip):
    response = subprocess.run(['ping', '-c', '1', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return response.returncode == 0


# Function to blank the screen
def blank_screen():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    screen.fill((0, 0, 0))
    pygame.display.flip()


# Function to unblank the screen
def unblank_screen():
    pygame.quit()


# IP address to ping
ip_address = "TOBIASLAPTOP"  # Change this to the IP address you want to ping

# Main loop
while True:
    if ping(ip_address):
        unblank_screen()
    else:
        blank_screen()
    time.sleep(5)  # Wait for 5 seconds before next ping
