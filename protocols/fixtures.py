from teams import Team

def result(team_1: Team, team_2: Team, prob: bool = False):
    winner = lambda x, y: x.winner(y)
    if not prob:
        return winner(x, y)

def main():
    team_1 = Team(1)
    team_2 = Team(2)
    print(result(team_1, team_2))

if __name__ == '__main__':
    main()
       

