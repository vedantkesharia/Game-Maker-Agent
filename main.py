# import agentops
from agents import GameAgents
from tasks import GameTasks
from crewai import Crew
from dotenv import load_dotenv
load_dotenv()

# agentops.init(tags=["game_builder"])

tasks = GameTasks()
agents = GameAgents()

print("## Welcome to the Game Crew")
print('-------------------------------')
# game = """Snake is a classic arcade game where the player controls a snake that continuously moves around the screen. 
# The objective is to navigate the snake to eat randomly placed food items, causing the snake to grow in length with each item consumed. 
# The game ends if the snake runs into the screen boundaries or collides with its own body, requiring careful maneuvering to achieve a high score."""

# game ="""Tic Tac Toe is a classic two-player game where the objective is to be the first to get three of your marks in a row on a 3x3 grid.
# The game is played on a grid consisting of 9 squares, arranged in three rows and three columns.
# One player uses X and the other player uses O, taking turns to place their mark in an empty square.
# The goal is to align three of your marks vertically, horizontally, or diagonally before your opponent does.
# The game ends in a win for the player who achieves this or in a draw if all squares are filled without a winning combination."""

game = """The Dino Game is a simple and addictive endless runner game where the player controls a pixelated dinosaur that continuously runs through a desert landscape.

The objective is to avoid obstacles such as cacti by jumping to keep the dinosaur running for as long as possible.
The obstacles are also not too close too each other, either too far away.
The game speeds up and becomes more challenging over time, requiring quick reflexes and precise timing.
The game ends if the dinosaur collides with an obstacle, and the goal is to achieve the highest possible score by surviving as long as you can."""

# Create Agents
senior_engineer_agent = agents.senior_engineer_agent()
qa_engineer_agent = agents.qa_engineer_agent()
chief_qa_engineer_agent = agents.chief_qa_engineer_agent()

# Create Tasks
code_game = tasks.code_task(senior_engineer_agent, game)
review_game = tasks.review_task(qa_engineer_agent, game)
approve_game = tasks.evaluate_task(chief_qa_engineer_agent, game)

# Create Crew responsible for Copy
crew = Crew(
    agents=[
        senior_engineer_agent,
        qa_engineer_agent,
        chief_qa_engineer_agent
    ],
    tasks=[
        code_game,
        review_game,
        approve_game
    ],
    verbose=True
)

game = crew.kickoff()

# Print results
print("\n\n########################")
print("## Here is the result")
print("########################\n")
print("final code for the game:")
print(game)
