# 初始化玩家
print("正在初始化玩家...")

class Player:
    def __init__(self, player_id):
        self.id=player_id
        self.money=50
        self.showhand=False

    # 牌局行為
    # 維持
    def check_m():
        return "check"
    # 加注
    def raise_m(num_in_game):
        return num_in_game
    # 棄牌
    def foul():
        return "foul"
    # 大小盲
    def blind(self, size):
        if size=="b":
            return "bb"
        if size=="s":
            return "sb"