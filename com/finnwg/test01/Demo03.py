# -*- coding: utf-8 -*-
# @Time : 2021/4/21 16:15
# @Author : 17853
# @File : Demo03.py
# @Software: PyCharm

# 开发小游戏《唐僧大战白骨精》

# 显示欢迎消息
print('-' * 20 + '欢迎光临《唐僧大战白骨精》' + '-' * 20)

# 显示身份选择信息
print('请选择你的身份：')
print('\t1.唐僧')
print('\t2.白骨精')
# 游戏身份选择
player_choose = input('请选择[1-2]：')

print('-' * 66)

# 根据用户判断来显示不同的提示信息
if player_choose == '1' :
    # 选择1
    print('你已经选择了1，你将以-> 唐僧 <-的身份来进行游戏!')
elif player_choose == '2' :
    # 选择2
    print('你竟然选择了白骨精，太不要脸了，你将以-> 唐僧 <-的身份来进行游戏!')
else :
    # 选择其他
    print('你的输入有误，系统将自动分配身份，你将以-> 唐僧 <-的身份来进行游戏!')

# 进入游戏
# 创建变量保存玩家信息
player_life = 2  # 玩家生命值
player_attack = 2  # 玩家攻击力

# 创建变量保存boos信息
boos_life = 10  # boos生命值
boos_attack = 10  # boos攻击力

print('-' * 66)
# 显示玩家的信息
print(f'-> 唐僧 <-，你的生命值是 {player_life},你的攻击力是 {player_attack}')

print('-' * 66)
while True :
    # 显示游戏选项，开始游戏
    print('请选择你要进行的选项……')
    print('\t1.升级')
    print('\t2.打boos')
    print('\t3.逃跑')
    
    print('-' * 66)

    game_choose = input('请选择要做的操作[1-3]：')

    if game_choose == '1' :
        # 增加玩家生命值
        player_life += 2
        player_attack += 2
        print(f'-> 唐僧 <-恭喜你升级了，你的生命值是 {player_life},你的攻击力是 {player_attack}')
        print('-' * 66)
    elif game_choose == '2' :
        # 判断boos/唐僧是否被打死
        print(f'-> 唐僧 <-,你对-> boos <-进行了攻击，对-> boos <-造成了{player_attack}点伤害')
        boos_life -= player_attack
        if boos_life <= 0 :
            print(f'-> 唐僧 <-恭喜你打死了白骨精，获得胜利！！！')
            break
        print(f'-> 唐僧 <-,你被-> boos <-攻击了，被-> boos <-造成了{boos_attack}点伤害')
        player_life -= boos_attack
        if player_life <= 0 :
            print(f'-> 唐僧 <-,你被被白骨精打死了，游戏结束')
            break
    elif game_choose == '3' :
        # 逃跑，游戏结束
        print(f'-> 唐僧 <-,臭不要脸，竟然跑了):,游戏结束')
        break
    else :
        print('-' * 66)
        print('你的输入有误，请重新进行选择！')




















