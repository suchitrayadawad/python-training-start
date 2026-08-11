"""
Name: SUCHITRA YADAWAD
Training ID: PYT_07/26_WD_PM_BATCH1
Module Title: Session 4 - Data Structures II
"""


# -------------------- Task 1 --------------------
print("-" * 10 + " Task 1 " + "-" * 10)

inventory = {
    "sku_01": 50,
    "sku_02": 150,
    "sku_03": 75
}

inventory.update({"sku_04": 200})

sku_02_stock = inventory["sku_02"]

sku_05_stock = inventory.get("sku_05",0)

print("SKU_02 stock:",sku_02_stock)
print("SKU_05 stock:",sku_05_stock)
print("All IDs:",inventory.keys())
print("All stock counts:",inventory.values())
print("Inventory items:",list(inventory.items()))


# -------------------- Task 2 --------------------
print("\n" + "-" * 10 + " Task 2 " + "-" * 10)

api_response = {
    "status": "success",
    "data": [
        {
            "id": 1,
            "info": {
                "email": "user1@work.com",
                "tags": ["admin", "dev"]
            }
        },
        {
            "id": 2,
            "info": {
                "email": "user2@work.com",
                "tags": ["guest"]
            }
        }
    ]
}

user_1_email = api_response["data"][0]["info"]["email"]

user_1_secondary_tag = api_response["data"][0]["info"]["tags"][1]

last_user_id = api_response["data"][-1]["id"]

print("First user's email:", user_1_email)
print("First user's second tag:", user_1_secondary_tag)
print("Last user's ID:", last_user_id)

print("Type of api_response['data']:", type(api_response["data"]))
print("Type of api_response['data'][0]['info']:",
      type(api_response["data"][0]["info"]))


# -------------------- Task 3 --------------------
print("\n" + "-" * 10 + " Task 3 " + "-" * 10)

raw_log = "  ERROR_CODE: 404 | STATUS: NOT_FOUND | SOURCE: SERVER_01  "

cleaned_log = raw_log.strip()
cleaned_log = cleaned_log.replace("_", " ")
vertical_bar_index = cleaned_log.find("|")
cleaned_log = cleaned_log.lower()

print("Index of vertical bar:", vertical_bar_index)
print("Cleaned log:", cleaned_log)


# -------------------- Task 4 --------------------
print("\n" + "-" * 10 + " Task 4 " + "-" * 10)

csv_data = "Apple,iPhone,1200,Silver"

product_details = csv_data.split(",")

product_details[2] = "1300"

reconstructed_string = ";".join(product_details)

header_string = "BRAND;MODEL;PRICE;COLOR"

final_csv = header_string + "\n" + reconstructed_string

print(final_csv)


# -------------------- Task 5 --------------------
print("\n" + "-" * 10 + " Task 5 " + "-" * 10)

personal_info = {
    "name": "John",
    "age": 30
}

job_info = {
    "salary": 5000,
    "role": "Analyst"
}

full_profile = personal_info | job_info

removed_age = full_profile.pop("age")

personal_info.clear()

print("Full profile:", full_profile)
print("Removed age:", removed_age)
print("Length of personal_info:", len(personal_info))


