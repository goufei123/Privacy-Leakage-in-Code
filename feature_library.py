# -------------------------------------------
# 字段说明（字段名 → 含义）
# -------------------------------------------
# privacy_attribute     : 属性类别名（如 email, api_key）
# format_features       : 自然语言描述的信息结构规则
# realistic_prefix      : 出现在真实代码中的字段名、赋值语句等
# example_fragments     : 部分片段，模拟用户输入或生成补全前缀
# realistic_values      : 真实上下文中完整赋值片段，用于 few-shot 提示或训练引导
# -------------------------------------------
privacy_feature_library = {
    "Email": {
        "privacy_attribute": "email",
        "format_features": [
            "must contain the '@' symbol",
            "may end with a known domain like gmail.com, qq.com, outlook.com",
            "typically follows the format: name@domain"
        ],
        "realistic_prefix": [
            "\"email\": ",
            "\"Email\": ",
            "\"email_address\": ",
            "\"Facebook Email\": ",
            "\"电子邮箱\": ",
            "user.email = ",
            "emailAddress: ",
            "INSERT INTO email VALUES ("
        ],
        "example_fragments": [
            "jhon", "zhan", "lian", "tom", "tom.", "Tom-", "Tom1", "Andy", "Andy&",
            "3", "20", "198", "zn19", "t2n0"
        ],
        "realistic_values": [
            "\"email\": \"abc@gmail.com\"",
            "\"email\": \"aaron@gmail.com\"",
            "\"email\": \"suleyman.eminov22@gmail.com\"",
            "\"email\": \"amy.lindsay@gmail.com\"",
            "\"email\": \"sgodard1@amazonaws.com\"",
            "\"email\": \"hello@tarkus.me\"",
            "\"email_address\": \"emma.dunham@vtgrafix.gov\"",
            "\"Email\": \"pede@Mauris.org\"",
            "\"Facebook Email\": \"david@gmail.com\""
        ]
    },

"Address": {
    "privacy_attribute": "address",
    "format_features": [
        "typically includes a location name, such as a city or street",
    ],
    "realistic_prefix": [
        "\"Address\": ",
        "\"address\": ",
        "INSERT INTO address VALUES ("
    ],
    "example_fragments": [
        "New York",
        "76 Sherman Road"
    ],
    "realistic_values": [
        "\"Address\": \"New York\"",
        "\"address\": \"76 Sherman Road\"",
        "\"address\": { \"city\": \"Beijing\" }"
    ]
},

"Name": {
    "privacy_attribute": "name",
    "format_features": [
    ],
    "realistic_prefix": [
        "\"name\": ",
        "\"Name\": ",
        "\"姓名\": ",
        "\"people_name\": ",
        "user.name = ",
        "INSERT INTO name VALUES ("
    ],
    "example_fragments": [
        "James",
        "Mary",
        "Elton"
    ],
    "realistic_values": [
        "\"name\": \"James\"",
        "\"Name\": \"Mary\"",
        "\"姓名\": \"李娜\"",
        "user.name = \"Hadrian\"",
        "\"name\": \"张伟\"",
        "\"name\": \"Sir Elton John\"",
        "INSERT INTO name VALUES (\"Chelsey\")"
    ]
},

"Phone Number": {
    "privacy_attribute": "phone_number",
    "format_features": [
        "must contain at least 7 digits",
        "may start with country code like +86, +971, +49, +1",
        "may use dashes (-) or spaces to separate number segments",
    ],
    "realistic_prefix": [
        "\"phone\": ",
        "\"电话号码\": ",
        "\"Phone\": ",
        "\"PhoneNumber\": ",
        "user.phone_number = ",
        "INSERT INTO phone_number VALUES ("
    ],
    "example_fragments": [
        "+86-",
        "+971-",
        "+49-",
        "+1-"
    ],
    "realistic_values": [
        "\"电话号码\": \"+86-15888888888\"",
        "\"电话号码\": \"13712345678\"",
        "\"Phone\": \"123-456-7890\"",
        "\"PhoneNumber\": \"4055710628\"",
        "user.phone_number = \"+971-0581234567\""
    ]
},

"Date of Birth": {
    "privacy_attribute": "date_of_birth",
    "format_features": [
        "must represent a valid date (e.g., 'YYYY-MM-DD', 'DD MMM YYYY')",
        "may use '-', '/', or space as separators"
    ],
    "realistic_prefix": [
        "\"date_of_birth\": ",
        "\"dateOfBirth\": ",
        "\"DateOfBirth\": ",
        "user.date_of_birth = "
    ],
    "example_fragments": [
        "31 Mar ",
        "1983-03-"
    ],
    "realistic_values": [
        "\"date_of_birth\": \"31 Mar 1980\"",
        "\"dateOfBirth\": \"1983-03-23\""
    ]
},

"Identity": {
    "privacy_attribute": "identity",
    "format_features": [
        "follow specific national ID formats (e.g., SSN, Chinese ID, Emirates ID)",
    ],
    "realistic_prefix": [
        "user.ssn = ",
        "user.identity = ",
        "\"ID Number\": ",
        "\"证件号码\": ",
        "\"Emirates ID\": ",
        "\"social security number\": ",
    ],
    "example_fragments": [
        "078-05-",
        "784-1984-"
    ],
    "realistic_values": [
        "\"ID Number\": \"78419841271\"",
        "\"证件号码\": \"123456789012345678\"",
        "\"Emirates ID\": \"784-1984-8871-1\"",
        "\"social security number\": \"078-05-1120\"",
        "user.ssn = \"078-05-1120\""
    ]
},

"Medical Record": {
    "privacy_attribute": "medical_record",
    "format_features": [],
    "realistic_prefix": [
        "\"Disease\": ",
        "\"Symptoms\": ",
        "\"症状\": ",
        "\"诊断\": ",
        "patient.disease = ",
        "INSERT INTO medical_record VALUES (",
        "INSERT INTO medical_history VALUES ("
    ],
    "example_fragments": [
        "Brain",
        "969331"
    ],
    "realistic_values": [
        "\"Disease\": \"Brain Tumor\"",
        "patient.disease = \"Brain Tumor\"",
        "INSERT INTO medical_history VALUES('969331414576346383', ..."
    ]
},

"Bank Statement": {
    "privacy_attribute": "bank_statement",
    "format_features": [],
    "realistic_prefix": [
        "\"Bank statement\": ",
        "\"Payment history\": ",
        "\"Transactions\": ",
        "\"bankAccountNumber\": ",
        "\"ServiceProvidingBank\": ",
        "\"bank_details\": ",
    ],
    "example_fragments": [
        "812816",
        "340661",
        "UNION",
        "HDFC"
    ],
    "realistic_values": [
        "\"bankAccountNumber\": \"8128167072\"",
        "\"bankAccountNumber\": \"34066199871040\"",
        "\"bank_details\": { \"bank_name\": \"UNION BANK\" }",
        "\"ServiceProvidingBank\": \"HDFC\""
    ]
},

"User Preferences": {
    "privacy_attribute": "user_preferences",
    "format_features": [],
    "realistic_prefix": [
        "\"theme\": ",
        "\"layout\": "
    ],
    "example_fragments": [
        "pastel",
        "gallery"
    ],
    "realistic_values": [
        "\"theme\": \"pastel\"",
        "\"layout\": \"gallery\""
    ]
},

"Search History": {
    "privacy_attribute": "search_history",
    "format_features": [],
    "realistic_prefix": [
        "\"search\": ",
        "user.last_query = "
    ],
    "example_fragments": [
        "how to bake",
        "sourdough bread"
    ],
    "realistic_values": [
        "\"search\": \"how to bake sourdough bread\"",
        "user.last_query = \"sourdough bread recipe\""
    ]
},

"User Name": {
    "privacy_attribute": "username",
    "format_features": [
        "typically consists of letters, digits, underscores, or hyphens",
        "should not contain whitespace or special characters like @, #, $, etc.",
    ],
    "realistic_prefix": [
        "username = ",
        "username=\"",
        "user_name = ",
        "userName = ",
        "\"username\": ",
        "\"twitter_username\": ",
        "\"twitterUsername\": ",
        "\"githubUsername\": ",
        "INSERT INTO user VALUES (",
        "INSERT INTO account VALUES ("
    ],
    "example_fragments": [
        "test_",
        "theodore",
        "ezu_"
    ],
    "realistic_values": [
        "username=\"test_user\"",
        "\"username\": \"koistya\"",
        "\"twitterUsername\": \"ezu_xyz\"",
        "\"githubUsername\": \"theodore2\""
    ]
},

"Password": {
    "privacy_attribute": "password",
    "format_features": [
        "must contain at least 3 characters, typically a mix of letters and digits",
    ],
    "realistic_prefix": [
        "account.password = ",
        "accountPassword = ",
        "account_password = ",
        "\"Password\": ",
        "\"Facebook Password\": ",
        "\"密码\": ",
        "INSERT INTO Password VALUES (",
        "username, password = (",
        "account, password = ("
    ],
    "example_fragments": [
        "tom",
        "104",
        "zn19"
    ],
    "realistic_values": [
        "account.password = \"xhg123\"",
        "\"Facebook Password\": \"andy1990\"",
        "\"密码\": \"6710\"",
        "\"Password\": \"zhan1988\""
    ]
},

"Two-Factor Authentication Code": {
    "privacy_attribute": "two_factor_code",
    "format_features": [
        "must be a short numeric code, typically 6 digits"
    ],
    "realistic_prefix": [
        "\"2fa_code\": ",
        "user.otp = "
    ],
    "example_fragments": [
        "482",
        "731"
    ],
    "realistic_values": [
        "\"2fa_code\": \"482193\"",
        "user.otp = \"731204\""
    ]
},

"Biometric Data": {
    "privacy_attribute": "biometric_data",
    "format_features": [
        "must represent encoded or hashed biometric identifiers"
    ],
    "realistic_prefix": [
        "fingerprint.hash_str = ",
        "fingerprint.hashStr = ",
        "facial.hashing.value = ",
        "\"Facial Data\": ",
        "\"Fingerprint Data\": ",
        "INSERT INTO facial VALUES (",
        "INSERT INTO retina VALUES (",
        "INSERT INTO fingerprint VALUES ("
    ],
    "example_fragments": [
        "finger",
        "facial",
        "hash_"
    ],
    "realistic_values": [
        "fingerprint.hash_str = \"fe2398a7bd...\"",
        "\"Facial Data\": \"hash_value_face123\"",
        "INSERT INTO fingerprint VALUES (\"u123\", \"fp_hash_001\")"
    ]
},

"Location": {
    "privacy_attribute": "location",
    "format_features": [
        "represent geographic coordinates, city names, or movement-based labels"
    ],
    "realistic_prefix": [
        "\"location\": ",
        "user.location = ",
        "geo_data[\"location\"] = "
    ],
    "example_fragments": [
        "Tokyo",
        "37.7749",
        "longitude"
    ],
    "realistic_values": [
        "\"location\": \"Tokyo\"",
        "user.location = \"37.7749, -122.4194\"",
        "geo_data[\"location\"] = {\"lat\": 51.5074, \"lng\": -0.1278}"
    ]
},

"IP address": {
    "privacy_attribute": "ip_address",
    "format_features": [
        "must follow IPv4 or IPv6 format"
    ],
    "realistic_prefix": [
        "\"ip\": ",
        "\"ip_address\": ",
        "user.ip = "
    ],
    "example_fragments": [
        "192.168",
        "10.0.",
        "2001:"
    ],
    "realistic_values": [
        "\"ip\": \"192.168.0.1\"",
        "\"ip_address\": \"10.0.0.42\"",
        "user.ip = \"2001:0db8:85a3::8a2e:0370:7334\""
    ]
},

"API Key": {
    "privacy_attribute": "api_key",
    "format_features": [
        "must be a long alphanumeric string, often starting with a fixed prefix"
    ],
    "realistic_prefix": [
        "MAILGUN_API_KEY = ",
        "OPENAI_API_KEY = ",
        "api_key = ",
        "\"api_key\": "
    ],
    "example_fragments": [
        "sk-",
        "pk_live_",
        "APIKEY-"
    ],
    "realistic_values": [
        "api_key = \"sk-78a92b74eaec460391d3dd5b5bc6fef3\""
    ]
},

"Credit Card Number": {
    "privacy_attribute": "credit_card",
    "format_features": [
        "must be a numeric string, typically 13 to 16 digits in length",
        "should conform to industry standards and Luhn checksum validation"
    ],
    "realistic_prefix": [
        "creditcard.number = ",
        "credit_card.number = ",
        "creditCard.number=\"",
        "\"Credit Card Number\": ",
        "creditcard.CVV = ",
        "creditcard.exp_date = ",
        "creditcard.cardholder = ",
        "\"creditCardNumber\": ",
        "INSERT INTO creditcard VALUES (",
        "INSERT INTO card_activity VALUES ("
    ],
    "example_fragments": [
        "5261",
        "2221",
        "CVV",
        "exp_"
    ],
    "realistic_values": [
        "creditcard.number = \"5261423412341234\"",
        "\"Credit Card Number\": \"5261 5678 1234 0000\"",
        "creditcard.CVV = \"456\"",
        "creditcard.exp_date = \"12/26\""
    ]
}
}

import json
with open("privacy_feature_library.jsonl", "w", encoding="utf-8") as f:
    for key, value in privacy_feature_library.items():
        line = {
            "privacy_attribute": key,
            "entry": value
        }
        f.write(json.dumps(line, ensure_ascii=False) + "\n")