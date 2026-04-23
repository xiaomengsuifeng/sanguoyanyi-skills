#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""提取姜维在三国演义中所有相关段落"""

import os
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
YUANZHU_DIR = os.path.join(SCRIPT_DIR, "yuanzhu")
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "姜维全文提取.txt")

def extract_jiangwei_content():
    keywords = ["姜维", "伯约", "姜伯约", "天水姜维"]

    files = sorted([f for f in os.listdir(YUANZHU_DIR) if f.endswith('.txt')])

    all_content = []
    all_content.append("=" * 80)
    all_content.append("三国演义 - 姜维相关段落全文提取")
    all_content.append("=" * 80)
    all_content.append("")

    for filename in files:
        filepath = os.path.join(YUANZHU_DIR, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        if any(kw in content for kw in keywords):
            lines = content.strip().split('\n')
            title = lines[0] if lines else filename

            all_content.append("-" * 80)
            all_content.append(f"【{title}】")
            all_content.append("-" * 80)

            for line in lines[1:]:
                if any(kw in line for kw in keywords):
                    cleaned_line = re.sub(r'^\d+\s*', '', line)
                    if cleaned_line.strip():
                        all_content.append(cleaned_line)

            all_content.append("")

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(all_content))

    print(f"提取完成！共处理 {len(files)} 回")
    count = sum(1 for f in files if any(kw in open(os.path.join(YUANZHU_DIR, f), 'r', encoding='utf-8').read() for kw in keywords))
    print(f"姜维出现的回数: {count}/120")

if __name__ == "__main__":
    extract_jiangwei_content()