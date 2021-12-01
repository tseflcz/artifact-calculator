import tkinter as tk
from tkinter import ttk

name={
     '固定生命值':"lifeStatic",
     '%生命值':"lifePercentage",
     '固定攻击力':"attackStatic",
     '%攻击力':"attackPercentage",
     '固定防御力':"defendStatic",
     '%防御力':"defendPercentage",
     '暴击率':"critical",
     '暴击伤害':"criticalDamage",
     '元素精通':"elementalMastery",
     '元素充能效率':"recharge",
     '物理/元素伤害加成':'bonus',
     '治疗加成':'cureEffect'
}
base={
     "lifeStatic": 299,           ## 固定生命值
     "lifePercentage": 5.8,     ## %生命值
     "attackStatic": 19,          ## 固定攻击力
     "attackPercentage":5.8,    ## %攻击力
     "defendStatic": 23,          ## 固定防御力
     "defendPercentage":7.3,    ## %防御力
     "critical": 3.9,           ## 全暴击率
     "criticalDamage": 7.8,     ## 暴击伤害
     "elementalMastery": 23,      ## 元素精通
     "recharge": 6.5,           ## 元素充能效率
}
weight={
     "lifeStatic": 0.5,           ## 固定生命值
     "lifePercentage": 1,         ## %生命值
     "attackStatic": 0.5,         ## 固定攻击力
     "attackPercentage":1,        ## %攻击力
     "defendStatic": 0.5,         ## 固定防御力
     "defendPercentage":1,        ## %防御力
     "critical": 1.2,             ## 全暴击率
     "criticalDamage": 1.2,       ## 暴击伤害
     "elementalMastery": 1,       ## 元素精通
     "recharge": 1,               ## 元素充能效率
}


def main():
    artifact={
        'mainTag': {'name': name[miantag.get()]},
        'normalTags': [{'name': name[normaltag1.get()], 'value': eval(tag1value.get())},
                        {'name': name[normaltag2.get()], 'value': eval(tag2value.get())},
                        {'name': name[normaltag3.get()], 'value': eval(tag3value.get())},
                        {'name': name[normaltag4.get()], 'value': eval(tag4value.get())}
                       ]}
    weight = {
        "lifeStatic": eval(lifeStatic.get()),  ## 固定生命值
        "lifePercentage": eval(lifePercentage.get()),  ## %生命值
        "attackStatic": eval(attackStatic.get()),  ## 固定攻击力
        "attackPercentage": eval(attackPercentage.get()),  ## %攻击力
        "defendStatic": eval(defendStatic.get()),  ## 固定防御力
        "defendPercentage": eval(defendPercentage.get()),  ## %防御力
        "critical": eval(critical.get()),  ## 全暴击率
        "criticalDamage": eval(criticalDamage.get()),  ## 暴击伤害
        "elementalMastery": eval(elementalMastery.get()),  ## 元素精通
        "recharge": eval(recharge.get()),  ## 元素充能效率
    }

    score={'life':0,'attack':0,'defend':0,'critical':0,'elementalMastery':0,'recharge':0}
    for j in range(len(artifact['normalTags'])):
        if artifact['normalTags'][j]['name']=="lifeStatic" or artifact['normalTags'][j]['name']=="lifePercentage":
            score['life']+=weight[artifact['normalTags'][j]['name']]*artifact['normalTags'][j]['value']/base[artifact['normalTags'][j]['name']]
        if artifact['normalTags'][j]['name']=="attackStatic" or artifact['normalTags'][j]['name']=="attackPercentage":
            score['attack']+=weight[artifact['normalTags'][j]['name']]*artifact['normalTags'][j]['value']/base[artifact['normalTags'][j]['name']]
        if artifact['normalTags'][j]['name']=="defendStatic" or artifact['normalTags'][j]['name']=="defendPercentage":
            score['defend']+=weight[artifact['normalTags'][j]['name']]*artifact['normalTags'][j]['value']/base[artifact['normalTags'][j]['name']]
        if artifact['normalTags'][j]['name']=="critical" or artifact['normalTags'][j]['name']=="criticalDamage":
            score['critical']+=weight[artifact['normalTags'][j]['name']]*artifact['normalTags'][j]['value']/base[artifact['normalTags'][j]['name']]
        if artifact['normalTags'][j]['name']=="elementalMastery":
            score['elementalMastery']+=weight[artifact['normalTags'][j]['name']]*artifact['normalTags'][j]['value']/base[artifact['normalTags'][j]['name']]
        if artifact['normalTags'][j]['name']=="recharge":
            score['recharge']+=weight[artifact['normalTags'][j]['name']]*artifact['normalTags'][j]['value']/base[artifact['normalTags'][j]['name']]
    print(score)

    maintag=artifact['mainTag']['name']
    if maintag=='attackPercentage':
        totalscore=score['critical']+score['attack']+score['elementalMastery']+score['recharge']
    elif maintag=='defendPercentage':
        totalscore=score['critical']+score['defend']+score['elementalMastery']+score['recharge']+0.5*score['attack']
    elif maintag=='lifePercentage':
        totalscore=score['critical']+score['life']+score['elementalMastery']+score['recharge']+0.5*score['attack']
    else:
        maintag=max(list(score.items())[0:3],key=lambda x:x[1])
        if maintag[1]!=0:
            if maintag[0]=='attack':
                totalscore=score['critical']+score['attack']+score['elementalMastery']+score['recharge']
            if maintag[0]=='defend':
                totalscore=score['critical']+score['defend']+score['elementalMastery']+score['recharge']+0.5*score['attack']
            if maintag[0]=='life':
                totalscore=score['critical']+score['life']+score['elementalMastery']+score['recharge']+0.5*score['attack']
        else:
            totalscore=score['critical']+score['elementalMastery']+score['recharge']
    print(totalscore)


    score1.set('生|{:.2f} 攻|{:.2f} 防|{:.2f}'.format(score['life'],score['attack'],score['defend']))
    score2.set('暴|{:.2f} 精|{:.2f} 充|{:.2f}'.format(score['critical'],score['elementalMastery'],score['recharge']))
    score3.set('总|{:.2f}'.format(totalscore))
    tk.Label(root, textvariable=score1).grid(row=7, column=1, padx=5, pady=5)
    tk.Label(root, textvariable=score2).grid(row=7, column=2, padx=5, pady=5)
    tk.Label(root, textvariable=score3).grid(row=7, column=0, padx=5, pady=5)

root = tk.Tk()  # 创建一个Tkinter.Tk()实例
root.title('单个圣遗物词条计算工具')

miantag = tk.StringVar()
normaltag1 = tk.StringVar()
tag1value = tk.StringVar()
normaltag2 = tk.StringVar()
tag2value = tk.StringVar()
normaltag3 = tk.StringVar()
tag3value = tk.StringVar()
normaltag4 = tk.StringVar()
tag4value = tk.StringVar()
score1 = tk.StringVar()
score2 = tk.StringVar()
score3 = tk.StringVar()

critical = tk.StringVar()
critical.set(weight['critical'])
criticalDamage = tk.StringVar()
criticalDamage.set(weight['criticalDamage'])

attackPercentage = tk.StringVar()
attackPercentage.set(weight['attackPercentage'])
attackStatic = tk.StringVar()
attackStatic.set(weight['attackStatic'])

lifePercentage = tk.StringVar()
lifePercentage.set(weight['lifePercentage'])
lifeStatic = tk.StringVar()
lifeStatic.set(weight['lifeStatic'])

defendPercentage = tk.StringVar()
defendPercentage.set(weight['defendPercentage'])
defendStatic = tk.StringVar()
defendStatic.set(weight['defendStatic'])

elementalMastery = tk.StringVar()
elementalMastery.set(weight['elementalMastery'])
recharge = tk.StringVar()
recharge.set(weight['recharge'])


tk.Label(root, text='请选择主词条').grid(row=1, column=0, padx=5, pady=5)
miantagbox=ttk.Combobox(root, textvariable=miantag)
miantagbox.grid(row=1, column=1, padx=5, pady=5)
miantagbox['values']=['固定生命值','固定攻击力','%攻击力','%生命值','%防御力','元素精通','元素充能效率','暴击率','暴击伤害','物理/元素伤害加成','治疗加成']
miantagbox['state']="readonly"
tk.Label(root, text='主词条作为判断条件，不计算分数').grid(row=1, column=2, padx=5, pady=5)

tk.Label(root, text='请选择副词条1').grid(row=2, column=0, padx=5, pady=5)
tag1box=ttk.Combobox(root, textvariable=normaltag1)
tag1box.grid(row=2, column=1, padx=5, pady=5)
tag1box['values']=['暴击率','暴击伤害','固定生命值','固定攻击力','固定防御力','%攻击力','%生命值','%防御力','元素精通','元素充能效率']
tag1box['state']="readonly"
tk.Entry(root, textvariable=tag1value).grid(row=2, column=2, padx=5, pady=5)

tk.Label(root, text='请选择副词条2').grid(row=3, column=0, padx=5, pady=5)
tag2box=ttk.Combobox(root, textvariable=normaltag2)
tag2box.grid(row=3, column=1, padx=5, pady=5)
tag2box['values']=['暴击率','暴击伤害','固定生命值','固定攻击力','固定防御力','%攻击力','%生命值','%防御力','元素精通','元素充能效率']
tag2box['state']="readonly"
tk.Entry(root, textvariable=tag2value).grid(row=3, column=2, padx=5, pady=5)

tk.Label(root, text='请选择副词条3').grid(row=4, column=0, padx=5, pady=5)
tag3box=ttk.Combobox(root, textvariable=normaltag3)
tag3box.grid(row=4, column=1, padx=5, pady=5)
tag3box['values']=['暴击率','暴击伤害','固定生命值','固定攻击力','固定防御力','%攻击力','%生命值','%防御力','元素精通','元素充能效率']
tag3box['state']="readonly"
tk.Entry(root, textvariable=tag3value).grid(row=4, column=2, padx=5, pady=5)

tk.Label(root, text='请选择副词条4').grid(row=5, column=0, padx=5, pady=5)
tag4box=ttk.Combobox(root, textvariable=normaltag4)
tag4box.grid(row=5, column=1, padx=5, pady=5)
tag4box['values']=['暴击率','暴击伤害','固定生命值','固定攻击力','固定防御力','%攻击力','%生命值','%防御力','元素精通','元素充能效率']
tag4box['state']="readonly"
tk.Entry(root, textvariable=tag4value).grid(row=5, column=2, padx=5, pady=5)

tk.Label(root, text='词条权重设置').grid(row=1, column=4, padx=5, pady=5)
tk.Label(root, text='词条按4档计算').grid(row=1, column=5, padx=5, pady=5)
tk.Label(root, text='按平均档权重设为1.18').grid(row=1, column=6, padx=5, pady=5)

tk.Label(root, text='暴击').grid(row=2, column=3, padx=5, pady=5)
tk.Entry(root, textvariable=critical).grid(row=2, column=4, padx=5, pady=5)
tk.Label(root, text='爆伤').grid(row=2, column=5, padx=5, pady=5)
tk.Entry(root, textvariable=criticalDamage).grid(row=2, column=6, padx=5, pady=5)

tk.Label(root, text='大攻击').grid(row=3, column=3, padx=5, pady=5)
tk.Entry(root, textvariable=attackPercentage).grid(row=3, column=4, padx=5, pady=5)
tk.Label(root, text='小攻击').grid(row=3, column=5, padx=5, pady=5)
tk.Entry(root, textvariable=attackStatic).grid(row=3, column=6, padx=5, pady=5)

tk.Label(root, text='大生命').grid(row=4, column=3, padx=5, pady=5)
tk.Entry(root, textvariable=lifePercentage).grid(row=4, column=4, padx=5, pady=5)
tk.Label(root, text='小生命').grid(row=4, column=5, padx=5, pady=5)
tk.Entry(root, textvariable=lifeStatic).grid(row=4, column=6, padx=5, pady=5)

tk.Label(root, text='大防御').grid(row=5, column=3, padx=5, pady=5)
tk.Entry(root, textvariable=defendPercentage).grid(row=5, column=4, padx=5, pady=5)
tk.Label(root, text='小防御').grid(row=5, column=5, padx=5, pady=5)
tk.Entry(root, textvariable=defendStatic).grid(row=5, column=6, padx=5, pady=5)

tk.Label(root, text='精通').grid(row=6, column=3, padx=5, pady=5)
tk.Entry(root, textvariable=elementalMastery).grid(row=6, column=4, padx=5, pady=5)
tk.Label(root, text='充能').grid(row=6, column=5, padx=5, pady=5)
tk.Entry(root, textvariable=recharge).grid(row=6, column=6, padx=5, pady=5)

tk.Button(root, text='开始计算', command=main).grid(row=6, column=0, padx=5, pady=5)

tk.Label(root, text='百分比数值请不要输入百分号').grid(row=6, column=1, padx=5, pady=5)
tk.Label(root, text='如3.9%暴击率输入3.9').grid(row=6, column=2, padx=5, pady=5)
tk.Label(root, text='灵梦丶冰笙 制作').grid(row=7, column=3, padx=5, pady=5)
tk.Label(root, text='欢迎大佬提出建议和意见').grid(row=7, column=4, padx=5, pady=5)
tk.Label(root, text='计算公式详见').grid(row=7, column=5, padx=5, pady=5)
tk.Label(root, text='github.com/tseflcz/artifact-calculator').grid(row=7, column=6, padx=5, pady=5)

root.mainloop()
