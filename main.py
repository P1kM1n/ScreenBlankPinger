import subprocess
import pygame
import time
import socket
import logging
import os


# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


# Function to ping the specified IP address or hostname
def ping(target):
    command = f"ping -n 1 {target}"
    response = os.system(command)
    success = response == 0
    logger.debug(f"Ping to {target} {'succeeded' if success else 'failed'}")
    return success


# Function to blank the screen
def blank_screen():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen.fill((0, 0, 0))
    pygame.display.flip()


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
    while True:
        if ping(target):
            unblank_screen()
        else:
            blank_screen()
        time.sleep(1)  # Wait for 1 second before next ping


# Main program
if __name__ == "__main__":
    # Input IP address or hostname
    target = "raspberrypi"

    main(target)
