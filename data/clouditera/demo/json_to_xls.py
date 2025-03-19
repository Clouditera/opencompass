import pandas as pd
import json


def parse_jsonl(file_path):
    data = []
    # 打开文件

    with open(file_path, 'r') as file:
        for line in file:
            json_obj = json.loads(line)

            # 初始化选项字典
            options = {'A': '', 'B': '', 'C': '', 'D': ''}

            # 检查每个选项是否存在，并构建options字典
            for key in options.keys():
                if key in json_obj:
                    options[key] = json_obj[key]

            # 检查'question'和'answer'键是否存在
            if 'question' in json_obj and 'answer' in json_obj:
                question = json_obj['question']
                answer = json_obj['answer']
                # 将提取的数据添加到列表中
                data.append(
                    {'Question': question, 'A': options['A'], 'B': options['B'], 'C': options['C'], 'D': options['D'],
                     'Answer': answer})
            else:
                print("Missing 'question' or 'answer' key in JSON object.")

    return data




def write_to_excel(data, output_file):
    # 使用pandas创建DataFrame
    df = pd.DataFrame(data)

    # 将DataFrame写入Excel文件
    df.to_excel(output_file, index=False)


def parse_txt(file_name):
    # 假设你的Excel文件名为output.xlsx
    excel_file = file_name
    output_txt = 'data.txt'

    # 读取Excel文件
    df = pd.read_excel(excel_file)

    # 检查必要的列是否存在
    required_columns = ['Question', 'A', 'B', 'C', 'D', 'Answer']
    if not all(column in df.columns for column in required_columns):
        print("Error: One or more required columns are missing in the Excel file.")
        return
    # 将所有的NaN值替换为空字符串
    df = df.fillna('')
    # 打开一个新的文本文件准备写入
    with open(output_txt, 'w') as txt_file:
        # 遍历DataFrame中的每一行
        for index, row in df.iterrows():
            # 创建一个字典来存储当前行的数据
            data = {
                'question': row['Question'],
                'A': row['A'],
                'B': row['B'],
                'C': row['C'],
                'D': row['D'],
                'answer': row['Answer']
            }
            # 将字典转换为JSON字符串
            json_str = json.dumps(data, ensure_ascii=False)
            # 写入文件
            txt_file.write(json_str + '\n')

    print(f'Data has been written to {output_txt}')


if __name__ == '__main__':
    data=parse_jsonl('CrashLog-CrashType.jsonl')
    write_to_excel(data, ' 95..xlsx')
   #parse_txt('fuzz2.xlsx')