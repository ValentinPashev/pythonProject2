class SteamUser:
    def __init__(self, username, games):
        self.username = username
        self.games = list(games)
        self.played_hours = 0

    def play(self, game, hours):
        if game in self.games:
            self.played_hours += hours
            return f"{self.username} is playing {game}"

        return f"{game} is not in library"

    def buy_game(self, game_):
        if game_ not in self.games:
            self.games.append(game_)
            return f"{self.username} bought {game_}"

        return f"{game_} is already in your library"

    def status(self):
        return f"{self.username} has {len(self.games)} games. Total play time: {self.played_hours}"


user = SteamUser("Peter", ["Rainbow Six Siege", "CS:GO", "Fortnite"])
print(user.play("Fortnite", 3))
print(user.play("Oxygen Not Included", 5))
print(user.buy_game("CS:GO"))
print(user.buy_game("Oxygen Not Included"))
print(user.play("Oxygen Not Included", 6))
print(user.status())