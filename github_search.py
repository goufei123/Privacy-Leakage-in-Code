import requests
import json
import time
import pandas as pd
from tqdm import tqdm


def search_github_code(query, headers):
    base_url = "https://api.github.com/search/code"
    # params = {"q": query}
    url = f"{base_url}?q={query}"

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data.get("total_count", 0)
    else:
        print(f"查询 '{query}' 出错，状态码：{response.status_code}, 响应内容：{response.text}")
        return 0


def jsonl_to_excel(data, output_file: str):
    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False)
    print(f"转换完成，Excel 文件已保存为: {output_file}")

def search_process(model_name, start_index=0):
    headers = {"Accept": "application/vnd.github+json",
               "Authorization": "Bearer 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",
               "X-GitHub-Api-Version": "2022-11-28"}

    input_path = f'./Output/Judge/Filter_testcase_{model_name}.jsonl'
    excel_output_path = f'./Output/Search/testcase_search_{model_name}.xlsx'
    jsonl_output_path = f'./Output/Search/testcase_search_{model_name}.jsonl'

    start_index = 0

    output_data = []

    with open(input_path, 'r', encoding='utf-8') as input_f:
        lines = input_f.readlines()

    with open(jsonl_output_path, 'a', encoding='utf-8') as out_jsonl:
        for idx, line in enumerate(tqdm(lines)):
            if idx < start_index:
                continue
            data = json.loads(line)
            count = search_github_code(data['content'], headers)
            data['github_match_count'] = count
            print(f"查询 \"{data['content']}\" 返回的记录数量：{count}")

            if count > 0:
                output_data.append(data)
                out_jsonl.write(json.dumps(data, ensure_ascii=False) + "\n")

            time.sleep(7)

    jsonl_to_excel(output_data, excel_output_path)


def already_jsonl_to_excel(input_file: str, output_file: str) -> None:
    data = []
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                data.append(json.loads(line))
            except json.JSONDecodeError as e:
                print(f"Skipping invalid line: {e}")

    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False)
    print(f"Excel file saved to: {output_file}")

def main():
    models = [
              # "gpt-4.0",
              "gpt-3.5",
              # "gpt-4.1",
              # "deepseek-r1"
              # "deepseek-v3"
              ]
    already_jsonl_to_excel(f'./evaluate/yes.jsonl', f'./evaluate/input.xlsx')
    # for model in models:
    #     search_process(model)


if __name__ == "__main__":
    main()