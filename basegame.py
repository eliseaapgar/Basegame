import pygame


class BaseGame:
    def __init__(self, width=800, height=600, title="This is my Game"):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.running = True
        self.FPS = 60
        self.bg_color = (1, 115, 113)  # Default background color: dark aquamarine

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill(self.bg_color)
            pygame.display.flip() #Update the display
            self.clock.tick(self.FPS) # Control the frame rate
if __name__ == "__main__":
    # Test 1: Create a game instance with custom parameters
    game = BaseGame(width=1024, height=768, title="The world's best (worst) game ever!")
    game.run() # This starts the game loop so the window will not close immediately after successful tests
    print("Test 1 Successful: Game has been created with custom params.")

    print(f"Game Title: {pygame.display.get_caption()[0]}")
    print(f"Screen Size: {game.screen.get_size()}")
    print(f"Background Color: {game.bg_color}")
    print(f"FPS: {game.FPS}")
    print(f"Is Running: {game.running}")
    # Expected Output: Successful creation of the game with the specific parameters listed in the terminal.

    # Test 2: Verification of default parameters
    default_game = BaseGame()
    print("Test 2 Successful: Game has been created with default params.")
    print(f"Default Game Title: {pygame.display.get_caption()[0]}")
    print(f"Default Screen Size: {default_game.screen.get_size()}")
    print(f"Default Background Color: {default_game.bg_color}")
    print(f"Default FPS: {default_game.FPS}")
    print(f"Default Is Running: {default_game.running}")
    # Expected Output: Successful creation of the game with the default parameters listed in the terminal. No errors encountered.

    # Test 3: Check if pygame is initialized
    if pygame.get_init():
        print("Test 3 Successful: Pygame is initialized.")
    else:
        print("Test 3 Failed: Pygame is not initialized.")
    # Expected Output: Confirmation that Pygame is initialized



