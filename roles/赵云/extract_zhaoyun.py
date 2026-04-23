#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""提取赵云在三国演义中所有相关段落"""

import os
import re

# 配置路径 - 使用相对路径
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
YUANZHU_DIR = os.path.join(SCRIPT_DIR, "yuanzhu")
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "赵云全文提取.txt")

def extract_zhaoyun_content():
    """提取所有包含赵云相关称呼的段落"""

    # 赵云的所有称呼
    keywords = ["赵云", "子龙", "赵子龙", "常山赵子龙", "虎威将军"]

    # 获取所有txt文件并排序
    files = sorted([f for f in os.listdir(YUANZHU_DIR) if f.endswith('.txt')])

    all_content = []
    all_content.append("=" * 80)
    all_content.append("三国演义 - 赵云相关段落全文提取")
    all_content.append("=" * 80)
    all_content.append("")

    for filename in files:
        filepath = os.path.join(YUANZHU_DIR, filename)

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # 检查是否包含任何赵云相关称呼
        if any(kw in content for kw in keywords):
            # 提取章回标题
            lines = content.strip().split('\n')
            title = lines[0] if lines else filename

            all_content.append("-" * 80)
            all_content.append(f"【{title}】")
            all_content.append("-" * 80)

            # 提取包含任一关键词的行
            for line in lines[1:]:
                if any(kw in line for kw in keywords):
                    # 清理行号
                    cleaned_line = re.sub(r'^\d+\s*', '', line)
                    if cleaned_line.strip():
                        all_content.append(cleaned_line)

            all_content.append("")

    # 写入输出文件
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(all_content))

    print(f"提取完成！共处理 {len(files)} 回")

    # 统计包含赵云的回数
    count = sum(1 for f in files if any(kw in open(os.path.join(YUANZHU_DIR, f), 'r', encoding='utf-8').read() for kw in keywords))
    print(f"赵云出现的回数: {count}/120")

if __name__ == "__main__":
    extract_zhaoyun_content()