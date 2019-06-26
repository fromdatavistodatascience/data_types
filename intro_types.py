"""
Let's learn about Python types!
"""

import json

with open("raw_data/data.json", "r") as json_file:
    text = json_file.read()
    data = json.loads(text)

main_keys = data.keys()
print(f"The main keys are: {main_keys}")

language_code = data['LanguageCode']
print(language_code)

search_parameters = data["SearchParameters"]
print(search_parameters)

search_results = data["SearchResult"]
#print(search_results)

search_results_keys = search_results.keys()
print(f"The search_result keys are: {search_results_keys}")

search_result_count = search_results['SearchResultCount']
print(search_result_count)

search_result_count_all = search_results["SearchResultCountAll"]
print(search_result_count_all)

search_result_items = search_results["SearchResultItems"]
print(search_result_items)

#search_item_keys = search_result_items.keys()
#print(f"The keys in search_result_items are: {search_item_keys}")

test_item = search_result_items[0]
print(f"""
test_item contains {test_item} and is of type {type(test_item)}
<line break 1>
<line break 2>
Go see inception, end game, and the fault in our stars!
""")

print(len(search_result_items))

list_of_types = [type(item) for item in search_result_items]
print(list_of_types)

unique_types = set(list_of_types)
print(f"The unique types in list_of_types is: {unique_types}")

