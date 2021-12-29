import tkinter as tk
from tkinter import ttk

primaryTag = "primaryTag"
secondaryTags = "secondaryTags"
name = "name"
value = "value"

life = "life"
lifeStatic = "lifeStatic"
lifePercentage = "lifePercentage"
attack = "attack"
attackStatic = "attackStatic"
attackPercentage = "attackPercentage"
defend = "defend"
defendStatic = "defendStatic"
defendPercentage = "defendPercentage"
critical = "critical"
criticalDamage = "criticalDamage"
elementalMastery = "elementalMastery"
recharge = "recharge"
bonus = "bonus"
cureEffect = "cureEffect"
default = "default"

tag_name = {
    '固定生命值': lifeStatic,
    '%生命值': lifePercentage,
    '固定攻击力': attackStatic,
    '%攻击力': attackPercentage,
    '固定防御力': defendStatic,
    '%防御力': defendPercentage,
    '暴击率': critical,
    '暴击伤害': criticalDamage,
    '元素精通': elementalMastery,
    '元素充能效率': recharge,
    '物理/元素伤害加成': bonus,
    '治疗加成': cureEffect,
}

tag_base = {
    lifeStatic: 299,  # 固定生命值
    lifePercentage: 5.8,  # %生命值
    attackStatic: 19,  # 固定攻击力
    attackPercentage: 5.8,  # %攻击力
    defendStatic: 23,  # 固定防御力
    defendPercentage: 7.3,  # %防御力
    critical: 3.9,  # 全暴击率
    criticalDamage: 7.8,  # 暴击伤害
    elementalMastery: 23,  # 元素精通
    recharge: 6.5,  # 元素充能效率
}

tag_weight = {
    lifeStatic: 0.5,  # 固定生命值
    lifePercentage: 1,  # %生命值
    attackStatic: 0.5,  # 固定攻击力
    attackPercentage: 1,  # %攻击力
    defendStatic: 0.5,  # 固定防御力
    defendPercentage: 1,  # %防御力
    critical: 1.2,  # 全暴击率
    criticalDamage: 1.2,  # 暴击伤害
    elementalMastery: 1,  # 元素精通
    recharge: 1,  # 元素充能效率
}

cal_score = {
    lifeStatic: life,
    lifePercentage: life,
    attackStatic: attack,
    attackPercentage: attack,
    defendStatic: defend,
    defendPercentage: defend,
    critical: critical,
    criticalDamage: critical,
    elementalMastery: elementalMastery,
    recharge: recharge,
}

cal_total_score = {
    default: {
        critical: 1,
        elementalMastery: 1,
        recharge: 1,
    },
    attack: {
        critical: 1,
        attack: 1,
        elementalMastery: 1,
        recharge: 1,
    },
    defend: {
        critical: 1,
        defend: 1,
        elementalMastery: 1,
        recharge: 1,
        attack: 0.5,
    },
    life: {
        critical: 1,
        life: 1,
        elementalMastery: 1,
        recharge: 1,
        attack: 0.5,
    },
    attackPercentage: {
        critical: 1,
        attack: 1,
        elementalMastery: 1,
        recharge: 1,
    },
    defendPercentage: {
        critical: 1,
        defend: 1,
        elementalMastery: 1,
        recharge: 1,
        attack: 0.5,
    },
    lifePercentage: {
        critical: 1,
        life: 1,
        elementalMastery: 1,
        recharge: 1,
        attack: 0.5,
    },
}

debug = True


def calc_num_of_entries(raw: list) -> dict:
    score = {life: 0, attack: 0, defend: 0, critical: 0, elementalMastery: 0, recharge: 0}
    for item in raw:
        item_name = item[name]
        item_value = item[value]
        item_score = tag_weight[item_name] * item_value / tag_base[item_name]
        score[cal_score[item_name]] += item_score

    if debug:
        print(f"calc_num_of_entries: {score}")

    return score


def get_item_tag(num_of_entries: dict, item_tag) -> str:
    res = ""
    if item_tag in [attackPercentage, defendPercentage, lifePercentage]:
        res = item_tag

    else:
        tmp = max(list(num_of_entries.items())[0:3], key=lambda x: x[1])
        if tmp[1] != 0:
            if tmp[0] == attack:
                res = attack

            if tmp[0] == defend:
                res = defend

            if tmp[0] == life:
                res = life
        else:
            res = defend

    if debug:
        print(f"get_item_tag input: {num_of_entries, item_tag}, output: {res}")

    return res


def calc_total_num_of_entries(num_of_entries: dict, item_tag) -> float:
    total_score = 0
    item_tag = get_item_tag(num_of_entries, item_tag)
    for k, v in cal_total_score[item_tag].items():
        total_score += num_of_entries[k] * v

    if debug:
        print(f"calc_total_num_of_entries {total_score}")

    return total_score


def parse_tag_value(raw: str) -> float:
    percent_num = raw.endswith("%")
    if percent_num:
        raw = raw.replace("%", "")

    res = float(raw)

    return res


def main():
    try:
        artifact = {
            primaryTag: {name: tag_name[primary_tag.get()]},
            secondaryTags: [
                {name: tag_name[secondary_tag1.get()], value: parse_tag_value(tag1value.get())},
                {name: tag_name[secondary_tag2.get()], value: parse_tag_value(tag2value.get())},
                {name: tag_name[secondary_tag3.get()], value: parse_tag_value(tag3value.get())},
                {name: tag_name[secondary_tag4.get()], value: parse_tag_value(tag4value.get())}
            ]
        }

        global tag_weight
        tag_weight = {
            lifeStatic: float(tk_lifeStatic.get()),  # 固定生命值
            lifePercentage: float(tk_lifePercentage.get()),  # %生命值
            attackStatic: float(tk_attackStatic.get()),  # 固定攻击力
            attackPercentage: float(tk_attackPercentage.get()),  # %攻击力
            defendStatic: float(tk_defendStatic.get()),  # 固定防御力
            defendPercentage: float(tk_defendPercentage.get()),  # %防御力
            critical: float(tk_critical.get()),  # 全暴击率
            criticalDamage: float(tk_criticalDamage.get()),  # 暴击伤害
            elementalMastery: float(tk_elementalMastery.get()),  # 元素精通
            recharge: float(tk_recharge.get()),  # 元素充能效率
        }

    except Exception as e:
        print(e)
        return

    num_of_entries = calc_num_of_entries(artifact[secondaryTags])

    total_score = calc_total_num_of_entries(num_of_entries, artifact[primaryTag][name])

    score1.set(
        f'生|{num_of_entries[life]:.2f} '
        f'攻|{num_of_entries[attack]:.2f} '
        f'防|{num_of_entries[defend]:.2f}'
    )
    score2.set(
        f'暴|{num_of_entries[critical]:.2f} '
        f'精|{num_of_entries[elementalMastery]:.2f} '
        f'充|{num_of_entries[recharge]:.2f}'
    )
    score3.set(
        f'总|{total_score:.2f}'
    )

    tk.Label(root, textvariable=score1).grid(row=7, column=1, padx=5, pady=5)
    tk.Label(root, textvariable=score2).grid(row=7, column=2, padx=5, pady=5)
    tk.Label(root, textvariable=score3).grid(row=7, column=0, padx=5, pady=5)


root = tk.Tk()  # 创建一个Tkinter.Tk()实例
root.title('单个圣遗物词条计算工具')

primary_tag = tk.StringVar()
secondary_tag1 = tk.StringVar()
tag1value = tk.StringVar()
secondary_tag2 = tk.StringVar()
tag2value = tk.StringVar()
secondary_tag3 = tk.StringVar()
tag3value = tk.StringVar()
secondary_tag4 = tk.StringVar()
tag4value = tk.StringVar()
score1 = tk.StringVar()
score2 = tk.StringVar()
score3 = tk.StringVar()

tk_critical = tk.StringVar()
tk_critical.set(tag_weight[critical])
tk_criticalDamage = tk.StringVar()
tk_criticalDamage.set(tag_weight[criticalDamage])

tk_attackPercentage = tk.StringVar()
tk_attackPercentage.set(tag_weight[attackPercentage])
tk_attackStatic = tk.StringVar()
tk_attackStatic.set(tag_weight[attackStatic])

tk_lifePercentage = tk.StringVar()
tk_lifePercentage.set(tag_weight[lifePercentage])
tk_lifeStatic = tk.StringVar()
tk_lifeStatic.set(tag_weight[lifeStatic])

tk_defendPercentage = tk.StringVar()
tk_defendPercentage.set(tag_weight[defendPercentage])
tk_defendStatic = tk.StringVar()
tk_defendStatic.set(tag_weight[defendStatic])

tk_elementalMastery = tk.StringVar()
tk_elementalMastery.set(tag_weight[elementalMastery])
tk_recharge = tk.StringVar()
tk_recharge.set(tag_weight[recharge])

tk.Label(root, text='请选择主词条').grid(row=1, column=0, padx=5, pady=5)
primary_tag_box = ttk.Combobox(root, textvariable=primary_tag)
primary_tag_box.grid(row=1, column=1, padx=5, pady=5)
primary_tag_box['values'] = [
    '固定生命值', '固定攻击力', '%攻击力', '%生命值', '%防御力', '元素精通', '元素充能效率',
    '暴击率', '暴击伤害', '物理/元素伤害加成', '治疗加成',
]
primary_tag_box['state'] = "readonly"
tk.Label(root, text='主词条作为判断条件，不计算分数').grid(row=1, column=2, padx=5, pady=5)

secondary_tag_box = [
    '暴击率', '暴击伤害', '%攻击力', '元素精通', '元素充能效率',
    '%生命值', '%防御力', '固定生命值', '固定攻击力', '固定防御力',
]

tk.Label(root, text='请选择副词条1').grid(row=2, column=0, padx=5, pady=5)
secondary_tag1box = ttk.Combobox(root, textvariable=secondary_tag1)
secondary_tag1box.grid(row=2, column=1, padx=5, pady=5)
secondary_tag1box['values'] = secondary_tag_box
secondary_tag1box['state'] = "readonly"
tk.Entry(root, textvariable=tag1value).grid(row=2, column=2, padx=5, pady=5)

tk.Label(root, text='请选择副词条2').grid(row=3, column=0, padx=5, pady=5)
secondary_tag2box = ttk.Combobox(root, textvariable=secondary_tag2)
secondary_tag2box.grid(row=3, column=1, padx=5, pady=5)
secondary_tag2box['values'] = secondary_tag_box
secondary_tag2box['state'] = "readonly"
tk.Entry(root, textvariable=tag2value).grid(row=3, column=2, padx=5, pady=5)

tk.Label(root, text='请选择副词条3').grid(row=4, column=0, padx=5, pady=5)
secondary_tag3box = ttk.Combobox(root, textvariable=secondary_tag3)
secondary_tag3box.grid(row=4, column=1, padx=5, pady=5)
secondary_tag3box['values'] = secondary_tag_box
secondary_tag3box['state'] = "readonly"
tk.Entry(root, textvariable=tag3value).grid(row=4, column=2, padx=5, pady=5)

tk.Label(root, text='请选择副词条4').grid(row=5, column=0, padx=5, pady=5)
secondary_tag4box = ttk.Combobox(root, textvariable=secondary_tag4)
secondary_tag4box.grid(row=5, column=1, padx=5, pady=5)
secondary_tag4box['values'] = secondary_tag_box
secondary_tag4box['state'] = "readonly"
tk.Entry(root, textvariable=tag4value).grid(row=5, column=2, padx=5, pady=5)

tk.Label(root, text='词条权重设置').grid(row=1, column=4, padx=5, pady=5)
tk.Label(root, text='词条按4档计算').grid(row=1, column=5, padx=5, pady=5)
tk.Label(root, text='按平均档权重设为1.18').grid(row=1, column=6, padx=5, pady=5)

tk.Label(root, text='暴击').grid(row=2, column=3, padx=5, pady=5)
tk.Entry(root, textvariable=tk_critical).grid(row=2, column=4, padx=5, pady=5)
tk.Label(root, text='爆伤').grid(row=2, column=5, padx=5, pady=5)
tk.Entry(root, textvariable=tk_criticalDamage).grid(row=2, column=6, padx=5, pady=5)

tk.Label(root, text='大攻击').grid(row=3, column=3, padx=5, pady=5)
tk.Entry(root, textvariable=tk_attackPercentage).grid(row=3, column=4, padx=5, pady=5)
tk.Label(root, text='小攻击').grid(row=3, column=5, padx=5, pady=5)
tk.Entry(root, textvariable=tk_attackStatic).grid(row=3, column=6, padx=5, pady=5)

tk.Label(root, text='大生命').grid(row=4, column=3, padx=5, pady=5)
tk.Entry(root, textvariable=tk_lifePercentage).grid(row=4, column=4, padx=5, pady=5)
tk.Label(root, text='小生命').grid(row=4, column=5, padx=5, pady=5)
tk.Entry(root, textvariable=tk_lifeStatic).grid(row=4, column=6, padx=5, pady=5)

tk.Label(root, text='大防御').grid(row=5, column=3, padx=5, pady=5)
tk.Entry(root, textvariable=tk_defendPercentage).grid(row=5, column=4, padx=5, pady=5)
tk.Label(root, text='小防御').grid(row=5, column=5, padx=5, pady=5)
tk.Entry(root, textvariable=tk_defendStatic).grid(row=5, column=6, padx=5, pady=5)

tk.Label(root, text='精通').grid(row=6, column=3, padx=5, pady=5)
tk.Entry(root, textvariable=tk_elementalMastery).grid(row=6, column=4, padx=5, pady=5)
tk.Label(root, text='充能').grid(row=6, column=5, padx=5, pady=5)
tk.Entry(root, textvariable=tk_recharge).grid(row=6, column=6, padx=5, pady=5)

tk.Button(root, text='开始计算', command=main).grid(row=6, column=0, padx=5, pady=5)

tk.Label(root, text='百分比数值请不要输入百分号').grid(row=6, column=1, padx=5, pady=5)
tk.Label(root, text='如3.9%暴击率输入3.9').grid(row=6, column=2, padx=5, pady=5)
tk.Label(root, text='灵梦丶冰笙 制作').grid(row=7, column=3, padx=5, pady=5)
tk.Label(root, text='欢迎大佬提出建议和意见').grid(row=7, column=4, padx=5, pady=5)
tk.Label(root, text='计算公式详见').grid(row=7, column=5, padx=5, pady=5)
tk.Label(root, text='github.com/tseflcz/artifact-calculator').grid(row=7, column=6, padx=5, pady=5)

root.mainloop()
