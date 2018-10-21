print('请选择水位：high/low')
level = input()                     # 获取用户输入的水位
# --- 洗衣过程 ---
if level == 'low':                    # 低水位流程
    print('加水20L')
    print('搅拌30分钟')
elif level == 'high':                  # 高水位流程
    print('加水50L')
    print('搅拌60分钟')
# --- 甩干过程 ---
print('请输入甩干次数：')
times = int(input())               # 获取用户输入的次数
for i in range(times):               # 循环漂洗，甩干
    print('放水且甩干')
    print('加水30L')
    print('搅拌5分钟')
print('甩干完毕')
