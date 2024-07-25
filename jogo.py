class Participant:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.choice = ""

    def choose(self):
        self.choice = input("{name}, digite pedra, papel, tesoura, lagarto ou Spock: ".format(name= self.name))
        print("{name} selects {choice}".format(name=self.name, choice = self.choice))

    def toNumericalChoice(self):
        switcher = {
            "pedra": 0,
            "papel": 1,
            "tesoura": 2,
            "lagarto": 3,
            "spock": 4
        }
        return switcher[self.choice]

    def incrementPoint(self):
        self.points += 1

class GameRound:
    def __init__(self, p1, p2):
        self.rules = [
            [0, -1, 1, 1, -1],
            [1, 0, -1, -1, 1],
            [-1, 1, 0, 1, -1],
            [-1, 1, -1, 0, 1],
            [1, -1, 1, -1, 0]
        ]

        p1.choose()
        p2.choose()
        result = self.compareChoices(p1,p2)
        if result >0:
            p1.incrementPoint()
        elif result<0:
            p2.incrementPoint()
        print("Round resulted in a {result}".format(result = self.getResultAsString(result) ))

    def compareChoices(self, p1, p2):
        return self.rules[p1.toNumericalChoice()][p2.toNumericalChoice()]
    def getResultAsString(self, result):
        res = {
            0: "empate",
            1: "vencedor",
            -1: "perdedor"
        }       
        return res[result]

    def awardPoints(self):
        print("implement")


class Game:
    def __init__(self):
        self.endGame = False
        self.participant = Participant("Spock")
        self.secondParticipant = Participant("Kirk")
        
    def start(self):
        while not self.endGame:
            GameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()

    def checkEndCondition(self):
        answer = input("Continar jogo S/N: ")
        if answer == 'S':
            GameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()
        else:
            print("Jogo terminado, {p1name} has {p1points}, and {p2name} has {p2points}".format(p1name = self.participant.name, p1points= self.participant.points, p2name=self.secondParticipant.name, p2points=self.secondParticipant.points))
            self.determineWinner()
            self.endGame = True

    def determineWinner(self):
        resultString = "É um empate"
        if self.participant.points > self.secondParticipant.points:
            resultString = "O vencedor é {name}".format(name=self.participant.name)
        elif self.participant.points < self.secondParticipant.points:
            resultString = "O vencedor é {name}".format(name=self.secondParticipant.name)
        print(resultString)

game = Game()
game.start()