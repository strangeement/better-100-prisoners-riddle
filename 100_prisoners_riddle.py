#
# A better solution to the 100 prisoners riddle
# It involves a simple change in strategy that improves odds from
# 31% to 33% in a 100 sample size and up to 52% in a 10 sample size
#

import random
 
def main():
    nb_loops = int(1_000)
 
    print("Commence hacking with", nb_loops, "loops ...")
    print("10 boxes:")
    run_prisoners_riddle(10, nb_loops, False, "victory without last card strategy")
    run_prisoners_riddle(10, nb_loops, True, "victory with last card strategy")
    print("20 boxes:")
    run_prisoners_riddle(20, nb_loops, False, "victory without last card strategy")
    run_prisoners_riddle(20, nb_loops, True, "victory with last card strategy")
    print("40 boxes:")
    run_prisoners_riddle(40, nb_loops, False, "victory without last card strategy")
    run_prisoners_riddle(40, nb_loops, True, "victory with last card strategy")
    print("50 boxes:")
    run_prisoners_riddle(50, nb_loops, False, "victory without last card strategy")
    run_prisoners_riddle(50, nb_loops, True, "victory with last card strategy")
    print("100 boxes:")
    run_prisoners_riddle(100, nb_loops, False, "victory without last card strategy")
    run_prisoners_riddle(100, nb_loops, True, "victory with last card strategy")
 
 
def run_prisoners_riddle(nb_drawers, nb_loops, use_last_card_strategy, affix):
    nb_victories = 0
    for _ in range(nb_loops):
        game = PrisonersGame(nb_drawers, use_last_card_strategy)
        nb_victories += all(game.play())

    print("{:.2%} {}    ".format(nb_victories / nb_loops, affix))
 
class PrisonersGame:
    def __init__(self, nb_drawers, use_last_card_strategy):
        assert nb_drawers % 2 == 0
        self.nb_drawers = nb_drawers
        self.max_attempts = int(self.nb_drawers / 2)
        self.drawer_ids = list(range(1, nb_drawers + 1))
        shuffled = self.drawer_ids[:]
        random.shuffle(shuffled)
        self.drawers = dict(zip(self.drawer_ids, shuffled))
        self.use_last_card_strategy = use_last_card_strategy
 
    def play_optimum(self, player_number):
        card = player_number
        for attempt in range(self.max_attempts):
            if self.drawers[card] == player_number:
                return True
            else:
                card = self.drawers[card]

        # Opened all the boxes by here
        # Strategery: report the last card number as last resort
        if self.use_last_card_strategy and self.drawers[card] == player_number:
            return True
 
        return False
 
    def play(self):
        return [self.play_optimum(player) for player in self.drawer_ids]

if __name__ == '__main__':
    main()