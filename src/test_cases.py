# test_cases.py
from file_handler import load_csv
from analyzer import (
    average_column,
    max_column,
    min_column,
    search_rows,
    frequency_count,
    search_by_id,
    search_by_name
)

def to_list(x):
    """Normalize return to a list for easy checking."""
    if x is None:
        return []
    if isinstance(x, list):
        return x
    if isinstance(x, dict):
        return [x]
    try:
        return list(x)
    except Exception:
        return [x]

def run_tests():
    data = load_csv("data/students_sample.csv")
    if not data:
        print("ERROR: Could not load data. Make sure data/students_sample.csv exists.")
        return

    total = 0
    passed = 0

    print("\n--- Running test cases ---")

    # 1. Average Age
    total += 1
    avg_age = average_column(data, "age")
    try:
        if abs(float(avg_age) - 19.5) < 0.05:
            print(f"Test 1 PASS - Average age ≈ {avg_age}")
            passed += 1
        else:
            print(f"Test 1 FAIL - Average age = {avg_age} (expected ≈ 19.5)")
    except:
        print("Test 1 FAIL - average_column returned non-numeric value")

    # 2. Max Score
    total += 1
    max_score = max_column(data, "score")
    try:
        if float(max_score) == 92:
            print(f"Test 2 PASS - Max score = {max_score}")
            passed += 1
        else:
            print(f"Test 2 FAIL - Max score = {max_score} (expected 92)")
    except:
        print("Test 2 FAIL - max_column returned non-numeric value")

    # 3. Min Score
    total += 1
    min_score = min_column(data, "score")
    try:
        if float(min_score) == 67:
            print(f"Test 3 PASS - Min score = {min_score}")
            passed += 1
        else:
            print(f"Test 3 FAIL - Min score = {min_score} (expected 67)")
    except:
        print("Test 3 FAIL - min_column returned non-numeric value")

    # 4. Frequency (gender)
    total += 1
    gender_count = frequency_count(data, "gender")
    expected_gender = {'Male': 4, 'Female': 4}
    if isinstance(gender_count, dict) and gender_count == expected_gender:
        print(f"Test 4 PASS - Gender count = {gender_count}")
        passed += 1
    else:
        print(f"Test 4 FAIL - Gender count = {gender_count} (expected {expected_gender})")

    # 5. Search by name (using search_rows)
    total += 1
    res = search_rows(data, "name", "Imran")
    res_list = to_list(res)
    if any(str(r.get("name", "")).strip().lower() == "imran" for r in res_list):
        print(f"Test 5 PASS - search_rows found Imran: {res_list}")
        passed += 1
    else:
        print(f"Test 5 FAIL - search_rows did not find Imran (got: {res})")

    # 6. search_by_name
    total += 1
    res2 = search_by_name(data, "Imran")
    res2_list = to_list(res2)
    if any(str(r.get("name", "")).strip().lower() == "imran" for r in res2_list):
        print(f"Test 6 PASS - search_by_name found Imran: {res2_list}")
        passed += 1
    else:
        print(f"Test 6 FAIL - search_by_name did not find Imran (got: {res2})")

    # 7. search_by_id
    total += 1
    res3 = search_by_id(data, "S004")
    res3_list = to_list(res3)
    if any(str(r.get("id", "")).strip() == "S004" for r in res3_list):
        print(f"Test 7 PASS - search_by_id found id=S004: {res3_list}")
        passed += 1
    else:
        print(f"Test 7 FAIL - search_by_id did not find id=S004 (got: {res3})")

    print(f"\nSummary: Passed {passed} out of {total} tests.")

if __name__ == "__main__":
    run_tests()
