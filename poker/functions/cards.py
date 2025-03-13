# 初始化撲克牌
# 物件
class card:
    def __init__(self, suit, number):
        self.suit=suit
        self.number=number
# 初始化52張牌
def init_cards():
    # list產生
    suits=['spade','heart','daimond','club']
    card_number=[i for i in range(1,14)]

    # final lust
    card_list=[]
    for suit in suits:
        for num in card_number:
            card_list.append(card(suit, num))
    return card_list