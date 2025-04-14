import random

# 所有符文结构定义
runes = {
    "精密": {
        "基石": ["强攻", "致命节奏", "迅捷步伐", "征服者"],
        "第二层": ["过量治疗", "凯旋", "气定神闲"],
        "第三层": ["传说：欢欣", "传说：韧性", "传说：血统"],
        "第四层": ["致命一击", "砍倒", "坚毅不倒"]
    },
    "主宰": {
        "基石": ["电刑", "掠食者", "黑暗收割", "恶意中伤"],
        "第二层": ["猛然冲击", "血之滋味", "幽灵魄罗", "僵尸守卫"],
        "第三层": ["眼球收集器", "贪欲猎手", "无情猎手", "终极猎手"]
    },
    "巫术": {
        "基石": ["艾黎", "奥术彗星", "相位猛冲"],
        "第二层": ["法力流系带", "灵光披风", "迅捷"],
        "第三层": ["超然", "绝对专注", "焦灼"]
    },
    "坚决": {
        "基石": ["不灭之握", "余震", "守护者"],
        "第二层": ["爆破", "生命源泉", "护盾猛击"],
        "第三层": ["调节", "骸骨镀层", "复苏"],
        "第四层": ["坚定", "过度生长", "复苏"]
    },
    "启迪": {
        "基石": ["冰川增幅", "启封的秘籍", "万灵之石"],
        "第二层": ["完美时机", "神奇之鞋", "未来市场"],
        "第三层": ["小兵去质器", "饼干配送", "时间扭曲补药"],
        "第四层": ["星界洞悉", "行近速率", "宇宙洞悉"]
    }
}

def random_runes():
    main_path = random.choice(list(runes.keys()))
    sub_paths = [p for p in runes if p != main_path]
    sub_path = random.choice(sub_paths)

    main = runes[main_path]
    sub = runes[sub_path]

    result = {
        "主路径": main_path,
        "基石符文": random.choice(main["基石"]),
        "主系符文": [
            random.choice(main.get("第二层", [])),
            random.choice(main.get("第三层", [])),
            random.choice(main.get("第四层", [])) if "第四层" in main else None
        ],
        "副路径": sub_path,
        "副系符文": random.sample(
            sub.get("第二层", []) + sub.get("第三层", []), 2
        )
    }

    # 打印结果
    print(f"主路径：{result['主路径']}")
    print(f"基石符文：{result['基石符文']}")
    print(f"主系符文：{', '.join([r for r in result['主系符文'] if r])}")
    print(f"副路径：{result['副路径']}")
    print(f"副系符文：{', '.join(result['副系符文'])}")

# 示例运行
random_runes()
