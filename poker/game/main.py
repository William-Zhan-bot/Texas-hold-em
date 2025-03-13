# 導入Poker模組
from functions.cards import init_cards
from functions.players import Player

print("遊戲開始")
num_of_player=int(input("請輸入玩家數量(最小2，最大10):\n"))

# 判斷玩家數量是否合理
if num_of_player>10 or num_of_player<2:
    num_of_player=10
print(f"玩家數量設定為 {num_of_player}")

# 玩家清單
print("正在初始化玩家.建立玩家清單...")
player_list=[Player(i+1) for i in range(num_of_player)]
# print(player_list)

# 導入牌組
print("正在初始化牌組...")
cards=init_cards()
print(cards[12].suit, cards[12].number)

# 開始牌局
print("牌局開始")


