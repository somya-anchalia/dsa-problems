import json, os
from difflib import SequenceMatcher
import requests
import json


# Task 1 ==========================================================

# def compare(officer_one, officer_two):
#     # Extracting the last name od the officers to get potential duplicates
#     officer_one_last_name = officer_one["name"].split(",")[0]
#     officer_two_last_name = officer_two["name"].split(",")[0]

#     # We need to modify the compare() function to identify duplicates not just by last name
#     # but by also adding a check for date of birth and role to reduce false positives.
#     if (officer_one_last_name == officer_two_last_name
#         and officer_one["date_of_birth"] == officer_two["date_of_birth"]
#         and officer_one["role"] == officer_two["role"]):
#         return True
#     else:
#         return False

# Task 2 ==========================================================

def similarity(a, b):
    """
    Compute a similarity score between two strings
    """
    return SequenceMatcher(None, a, b).ratio()

def compare(officer_one, officer_two, threshold=0.5):

    """
    Compares two officer entries to determine if they are potential duplicates
    based on name, date of birth, and role similarity.
    """

    """
    Threshold can be adjusted to increase the accuracy of comparing names
    """
    threshold=0.6
    # threshold=0.8

    """
    Create feature vectors or scores for comparison
    """
    name_similarity = similarity(officer_one["name"], officer_two["name"])
    
    """
    Determine a threshold to decide if they are duplicates
    """
    if (name_similarity >= threshold 
        and officer_one["date_of_birth"] == officer_two["date_of_birth"]
        and officer_one["role"] == officer_two["role"]):
        return True
    else:
        return False

# Task 3 ==========================================================
"""
Directions: 
Step 1 - Populate the "api_key" variable on line 110 in the "main" function
Step 2 - Set "api_key_provided" variable on line 111 to "True"
Step 3 - Run the python script using command: "python main.py"

"""

def fetch_officers_from_api(company_number, api_key):
    url = f"https://api.company-information.service.gov.uk/company/{company_number}/officers"
    headers = {'Authorization': api_key}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()  # this will return a list of officers
    else:
        response.raise_for_status()


# Task 4 ==========================================================
"""
Unit Testing can be found in the test_cases.py file in the same directory.
To execute test cases, simply use following command "python test_cases.py"
"""

# Task 5 ==========================================================
"""
Code comments have been added for better understanding
"""

# Task 6: Refactoring ==========================================================
"""
1. Simplified Loop: Replace nested loops with combinations to avoid self-comparison and repetitive comparisons.
2. Error Handling: Add try-except for JSON loading and API calls.
3. Constants: Use constants for thresholds and paths.
"""

def main():
    """
    Main function to find potential duplicate officers and output them
    """
    with open("../officers.json") as file:
        officers = json.load(file)

    duplicate_list = []
    print(len(officers))

    """
    Provide your actual API key here and set api_key_provided variable to True
    """
    api_key = 'YOUR_API_KEY_HERE'
    api_key_provided = False

    """
    Add more officers data from the House Rest API using the company number of existing officers
    """
    if api_key_provided:
        for officer in officers:
            officers_data = fetch_officers_from_api(officer["company_number"], api_key)
            officers.extend(officers_data)

    for i in range(len(officers)):
        for j in range(len(officers)):
            if i != j and officers[i]["id"] != officers[j]["id"]:
                potential_duplicate = compare(officers[i], officers[j])
                if potential_duplicate and not any(
                    officers[j]["id"] + officers[i]["id"] in item
                    for item in duplicate_list
                ):
                    duplicate_list.append([officers[i], officers[j]])

    for d in duplicate_list:
        print(d)

    with open("duplicates.json", "w") as file:
        json.dump(duplicate_list, file)

if __name__ == "__main__":
    main()
