class File():
    def __init__(self, game):
        self.game = game

    def export(self):  # Ne fonctionne pas sur mon PC fixe et seulement dans le dossier OneDrive
        player_one_keys = self.game.player_one.keys
        player_two_keys = self.game.player_two.keys

        try:

            with open('config.txt', 'w') as config:
                for i in range(len(player_one_keys)):
                    config.write(str(player_one_keys[i]) + ' ')

                for i in range(len(player_two_keys)):
                    config.write(str(player_two_keys[i]) + ' ')

                config.flush()
                config.close()

        except OSError:
            return

    def load(self):
        with open('config.txt', 'r') as config:
            line = config.readlines()

            player_one_keys = list()
            player_two_keys = list()

            line = line[0].split(' ')

            for i in range(6):
                player_one_keys.append(int(line[i]))

            for i in range(6, 12):
                player_two_keys.append(int(line[i]))

            config.close()

        self.game.player_one.keys = player_one_keys
        self.game.player_two.keys = player_two_keys
