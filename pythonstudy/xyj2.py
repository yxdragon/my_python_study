print('请选择水位：high/low')
level = input()              # input用于接收用户输入内容
# --- 洗衣过程 ---
if level == 'low':             # 低水位选择
    print('加水20L')
    print('搅拌30分钟')
elif level == 'high':           # 高水位选择
    print('加水50L')
    print('搅拌60分钟')
# --- 甩干过程 ---
print('放水且甩干')
print('加水30L')
print('搅拌5分钟')
print('甩干')
