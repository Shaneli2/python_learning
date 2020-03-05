import random

# 石头１，　剪刀２　布３
player = int(input("请输入（石头１／剪刀２／布３）：　"))

while player != 9:

    if player > 3:
        player = 3
    elif player < 1:
        player = 1

    if player <= 1:
        player_show = "石头"
    elif player == 2:
        player_show = "剪刀"
    else:
        player_show = "布"

    computer = random.randint(1, 3)

    if computer == 1:
        computer_show = "石头"
    elif computer == 2:
        computer_show = "剪刀"
    else:
        computer_show = "布"

    if ((player == 1 and computer == 2)
            or (player == 2 and computer == 3)
            or (player == 3 and computer == 1)):
        print("你出了 %s ，电脑出了 %s . 本局 你 赢！" % (player_show, computer_show))
    elif ((computer == 1 and player == 2)
          or (computer == 2 and player == 3)
          or (computer == 3 and player == 1)):
        print("你出了 %s ，电脑出了 %s . 本局 电脑 赢." % (player_show, computer_show))
    else:
        print("你出了 %s ，电脑出了 %s . 本局 平局" % (player_show, computer_show))

    player = int(input("请输入（石头１／剪刀２／布３）：　"))

print("游戏已退出！")
