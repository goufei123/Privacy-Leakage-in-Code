import json
import re
from fileinput import filename
from collections import defaultdict

model_name = "gpt-4.1"
# 输入和输出文件名
input_filename = f"./Output/Cases/test_case_{model_name}.jsonl"
output_filename = f"./Output/Attributes/attributes_info_{model_name}.jsonl"
filename_final = f'./Output/Attributes/attributes_{model_name}.jsonl'
# input_filename = "test_case_gpt-4o.jsonl"
# output_filename = "attributes_info_gpt4o.jsonl"
# filename_final = 'attributes_gpt4o.jsonl'

NORMALIZATION_MAP = {
    "name": "Name",
    "address": "Address",
    "phonenumber": "Phone Number",
    "phone": "Phone Number",
    "phonenum": "Phone Number",
    "phone_number": "Phone Number",
    "dateofbirth": "Date of Birth",
    "date_of_birth": "Date of Birth",
    "username": "User Name",
    "user_name": "User Name",
    "password": "Password",
    "email": "Email",
    "identity": "Identity",
    "medicalrecord": "Medical Record",
    "medical_record": "Medical Record",
    "code": "Two-Factor Authentication Code",
    "twofactorauthenticationcode": "Two-Factor Authentication Code",
    "two_factor_authentication_code": "Two-Factor Authentication Code",
    "data": "Biometric Data",
    "biometricdata": "Biometric Data",
    "biometric_data": "Biometric Data",
    "userpreferences": "User Preferences",
    "user_preferences": "User Preferences",
    "perferences": "User Preferences",
    "history": "Search History",
    "searchhistory": "Search History",
    "search_history": "Search History",
    "location": "Location",
    "ipaddress": "IP address",
    "ip_address": "IP address",
    "bankstatement": "Bank Statement",
    "bank_statement": "Bank Statement",
    "credit": "Credit Card Number",
    "credit_card": "Credit Card Number",
    "creditcard": "Credit Card Number",
    "creditcardnumber": "Credit Card Number",
    "credit_card_number": "Credit Card Number",
    "apikey": "API Key",
    "api_key": "API Key",
    "database": "Database Connection Strings",
    "databaseconnectionstrings": "Database Connection Strings",
    "database_connection_strings": "Database Connection Strings",
    "system_config": "System Configuration",
    "systemconfig": "System Configuration",
    "config": "System Configuration",
    "congigrueation": "System Configuration",
    "systemconfiguration": "System Configuration",
    "system_configuration": "System Configuration",
    "sshkey": "SSH Key",
    "ssh_key": "SSH Key"
}

def normalize_attribute(attr: str) -> str:
    # 去掉前后空白、以及可能包裹的引号和反引号
    attr_cleaned = attr.strip().replace("`", "").replace('"', '').replace("'", "")
    key = re.sub(r"[_\-]", "", attr_cleaned).lower()
    if key in NORMALIZATION_MAP:
        return NORMALIZATION_MAP[key]
    else:
        # 默认转换成每个单词首字母大写的格式
        parts = re.split(r"[\s_\-]+", attr_cleaned)
        return " ".join(word.capitalize() for word in parts if word)

def clean_string(s: str) -> str:
    # 去除前面的 "** "（如果存在）
    prefix = "** "
    if s.startswith(prefix):
        s = s[len(prefix):]
    if not s.endswith('#'):
        if '#' in s:
            s = s.split('#')[0]
            s.strip()

    if s.startswith("'") and s.endswith("'") and len(s) >= 2:
        s = s[1:-1]

    elif s.startswith("`") and s.endswith("`") and len(s) >= 2:
        s = s[1:-1]

    elif s.startswith("\"") and s.endswith("\"") and len(s) >= 2:
        s = s[1:-1]

    return s

def main():
    records = []
    with open(input_filename, "r", encoding="utf-8") as infile:
        for line in infile:
            line = line.strip()
            if not line:
                continue
            try:
                data = json.loads(line)
            except json.JSONDecodeError as e:
                print(f"JSON解析失败: {e}")
                continue

            testcase_str = data['test_case']
            if "\n\n" in testcase_str:
                testcase_str = testcase_str.split("\n\n")[0]
            start = testcase_str.find(':')
            testcase_str = testcase_str[start+1:]

            pattern = re.compile(r"""
                    [\-\*\s]*                      
                    `?(?P<attribute>[\w\-_]+)`?      
                    \s*:\s*
                    (?P<content> 
                       (?:
                           (?! 
                               [,\n]\s* 
                               `?[\w\-_]+`? 
                               \s*:\s*             
                           )
                           .                      
                       )+
                    )
                    (?=(?:[,\n]\s*`?[\w\-_]+`?\s*:\s*) | $)
                """, re.VERBOSE | re.DOTALL)

            str_lines = re.split("\n", testcase_str)
            for l in str_lines:
                matches = pattern.finditer(l)
                for m in matches:
                    attribute = m.group("attribute").strip()
                    content = m.group("content").strip()
                    if content.startswith('"') and content.endswith('"'):
                        content = content[1:-1].strip()
                    records.append({
                        "attribute": normalize_attribute(attribute),
                        "content": clean_string(content)
                    })

    sorted_list = sorted(records, key=lambda item: item["attribute"])

    with open(output_filename, "w", encoding="utf-8") as outfile:
        for item in sorted_list:
            outfile.write(json.dumps({
                "attribute": item['attribute'],
                "content": item['content']
            }, ensure_ascii=False) + "\n")

def sort_jsonl(filename, out_filename):
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
    data = [json.loads(line) for line in lines if line.strip()]
    sorted_data = sorted(data, key=lambda item: item["attribute"])
    with open(out_filename, "w", encoding="utf-8") as f:
        for item in sorted_data:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")

def get_attribute_num(file):
    attributes = {}
    with open(file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            data= json.loads(line)
            if data["attribute"] not in attributes:
                attributes[data["attribute"]] = 1
            else:
                attributes[data["attribute"]] += 1

    return attributes

def get_date(file):
    attribute_content = defaultdict(set)

    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            try:
                data = json.loads(line)
                attr = data.get("attribute")
                content = data.get("content")
                if attr and content:
                    attribute_content[attr].add(content)
            except json.JSONDecodeError:
                continue  # 忽略格式错误的行

    # 打印每个 attribute 的唯一 content 数量，从大到小排序
    sorted_attributes = sorted(attribute_content.items(), key=lambda x: len(x[1]), reverse=True)
    for attr, contents in sorted_attributes:
        print(f"{attr}: {len(contents)}")


if "__main__" == __name__:
    # main()
    # sort_jsonl(output_filename, filename_final)
    # attributes = get_attribute_num(filename_final)
    # for attr in attributes:
    #     print(attr, attributes[attr])
    get_date('./Output/Judge/Filter_testcase_gpt-4.0_ori.jsonl')
