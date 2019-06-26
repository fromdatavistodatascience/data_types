"""
Let's learn about Python types!
"""

import json

with open("raw_data/data.json", "r") as json_file:
    text = json_file.read()
    data = json.loads(text)

main_keys = data.keys()
print(f"The main keys are: {main_keys}")

language_code = data["LanguageCode"]
print(language_code)

search_parameters = data["SearchParameters"]
print(search_parameters)

search_result = data["SearchResult"]
#print(search_result)

search_results_keys = search_result.keys()
print(f"The search_results are {search_results_keys}")

search_result_count = search_result["SearchResultCount"]
print(search_result_count)

search_result_count_all = search_result["SearchResultCountAll"]
print(search_result_count_all)

search_result_items = search_result["SearchResultItems"]
print(search_result_items)

#search_item_keys = search_result_items.keys()
#print(f"The keys in search_results_items are {search_item_keys}")

test_item = type(search_result_items[0])
print(f"""
test_item contains {test_item} and is of type {type(test_item)}
""")

print(len(search_result_items))

list_of_types = [type(item)
                 for item in search_result_items]
print(list_of_types)

unique_types = set(list_of_types)
print(f"The unique types in list_of_types is: {unique_types}")

