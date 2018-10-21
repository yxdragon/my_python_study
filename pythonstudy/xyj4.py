def wash(level):
    # --- 洗衣过程 ---
    if level == 'low':
        print('加水20L')
        print('搅拌30分钟')
    elif level == 'high':
        print('加水50L')
        print('搅拌60分钟')

def dry(times):
    # --- 甩干过程 ---
    print('放水且甩干')
    for i in range(times):
        print('加水30L')
        print('搅拌5分钟')
        print('甩干')

def wash_dry(obj, level='low', times=1):   # 带等于号的是默认值，如果不传则使用默认
    '''
    这是一个洗衣机，
    请放入衣物，
    设定水位，
    设定甩干次数
    '''
    print('======= 开始洗衣 =======')
    wash(level)
    dry(times)
    print('%s 洗干净了'%obj)          # %s是字符串格式化，将替代为后面obj的内容
'''
wash_dry('毛衣', 'low', 5)
wash_dry('被子', 'high', 5)
'''
