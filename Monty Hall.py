#  Write a program that simualates the Monty Hall Problem and prove numerically why you should always switch.
#  Two inputs: number of games and switch/stay
"""
Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?
"""

def MontyHall(num_games, switch_stay):
    """
    num_games: Positive integer. Number of games to be played

    switch_stay: string 'switch' or 'stay'. Which action to take

    return: Probability of winning the game
    """
    # import random module
    import random

    # Initial conditions
        # Set up win count = 0
        # Set up lose count = 0
        # Set up play count = number of games to play
        # Set up doors
    win_count = 0
    lose_count = 0
    play_count = num_games
    doors = ['car', 'goat', 'goat']

    # Playing the game
    while play_count > 0:
        # Initial conditions per game
            # Player chooses random door
        pick1 = random.choice(doors)

        # If pick1 == car
        if pick1 == 'car':
            # Stay, Win Game
            if switch_stay == 'stay':
                win_count += 1
            # Switch, Lose Game
            else:
                lose_count += 1

        # If pick1 = goat
        # Game host will always show other goat
        else:
            # Stay, Lose Game
            if switch_stay == 'stay':
                lose_count += 1
            # Switch, Win Game
            else:
                win_count += 1
            
        # Update game count by 1
        play_count -= 1

    # When all games are played
        # Find the % of won games
        # Print out probability of winning for switch/stay
    win_prob = (win_count / num_games) * 100
    print('The probability of winning if you played', num_games, 'games and ', end = '')
    print(switch_stay, 'is:', str(win_prob) + '%')

MontyHall(1000,'switch')
MontyHall(1000,'stay')