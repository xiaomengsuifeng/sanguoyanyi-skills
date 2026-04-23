#!/usr/bin/env python3
import os, re
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
YUANZHU_DIR, OUTPUT_FILE = os.path.join(SCRIPT_DIR, "yuanzhu"), os.path.join(SCRIPT_DIR, "张辽全文提取.txt")
keywords = ["张辽", "文远", "张文远"]
files = sorted([f for f in os.listdir(YUANZHU_DIR) if f.endswith('.txt')])
all_content = ["=" * 80, "三国演义 - 张辽相关段落全文提取", "=" * 80, ""]
for f in files:
    with open(os.path.join(YUANZHU_DIR, f), 'r', encoding='utf-8') as file:
        content = file.read()
    if any(kw in content for kw in keywords):
        lines = content.strip().split('\n')
        all_content.extend(["-" * 80, f"【{lines[0]}】", "-" * 80])
        for line in lines[1:]:
            if any(kw in line for kw in keywords):
                cl = re.sub(r'^\d+\s*', '', line)
                if cl.strip(): all_content.append(cl)
        all_content.append("")
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f: f.write('\n'.join(all_content))
print(f"张辽: {sum(1 for f in files if any(kw in open(os.path.join(YUANZHU_DIR, f), 'r', encoding='utf-8').read() for kw in keywords))}/120")