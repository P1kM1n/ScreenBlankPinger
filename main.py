import pygame
import time
import socket
import logging
import subprocess
import os
from pygame.locals import *

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


# Function to ping the specified IP address or hostname
def ping(target):
    try:
        subprocess.run(['ping', '-c', '1', target], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        logger.debug(f"Ping to {target} succeeded")
        return True
    except subprocess.CalledProcessError:
        logger.debug(f"Ping to {target} failed")
        return False


# Function to blank the screen
def blank_screen():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen.fill((0, 0, 0))
    pygame.display.flip()
    return screen


# Function to unblank the screen
def unblank_screen():
    pygame.quit()


# Function to resolve hostname to IP address
def resolve_hostname(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.gaierror:
        logger.error("Unable to resolve hostname.")
        return None


# Main function
def main(target):
    # Main loop
    screen = blank_screen()
    click_count = 0
    while True:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                click_count += 1
                if click_count == 3:
                    pygame.quit()
                    return
            elif event.type == QUIT:
                pygame.quit()
                return

        if ping(target):  # Ensure target is passed as a string
            unblank_screen()
        else:
            screen = blank_screen()
            click_count = 0

        time.sleep(1)  # Wait for 1 second before next ping



# Main function
def main(target):
    # Main loop


    while True:
        if ping(target):
            unblank_screen()
        else:
            blank_screen()
        time.sleep(1)  # Wait for 1 second before next ping


# Main program
if __name__ == "__main__":
    # Input IP address or hostname
    target = "192.168.0.1"

    main(target)