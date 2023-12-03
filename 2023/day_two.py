def main():
    """
    Advent Of Code 2023 day 2
    :return:
    """
    sumIds = 0
    sumPower = 0
    file = open('input/dayTwo.txt', "r")
    for line in file:
        data = line.split(":")
        id = data[0].split()[1]
        games = data[1].strip().split(';')
        game_data = list()
        curr_games = list()
        for game in games:
            game_dict = {}
            for color in game.strip().split(','):
                game_dict[color.split()[1]] = int(color.split()[0])
            curr_games.append(game_dict)
        game_data.append((int(id), curr_games))
        for id, games in game_data:
            valid = True
            game_power = {'red': 0, 'blue': 0, 'green': 0}
            for game in games:
                if game.get('red', 0) > 12 or game.get('green', 0) > 13 or game.get('blue', 0) > 14:
                    valid = False
                game_power['red'] = max(game.get('red', 0), game_power['red'])
                game_power['green'] = max(game.get('green', 0), game_power['green'])
                game_power['blue'] = max(game.get('blue', 0), game_power['blue'])
            if valid:
                sumIds += id
            game_power_total = game_power['red'] * game_power['blue'] * game_power['green']
            sumPower += game_power_total
    file.close()
    print('Part 1:', str(sumIds))
    print('Part 2:', str(sumPower))


if __name__ == '__main__':
    main()
