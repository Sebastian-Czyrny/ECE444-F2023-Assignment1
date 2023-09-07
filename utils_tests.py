import utils

utils = utils.Utils()

# Test reversed: int, float, string
reversed_tests_passed = 0
REVERSED_TESTS_TOTAL = 3
res = utils.reversed(1234)
if res == 4321: reversed_tests_passed += 1



res = utils.reversed(3.14)
if res == None: reversed_tests_passed += 1

res = utils.reversed("hello world")
if res == None: reversed_tests_passed += 1
print(f"======= Completed Testing REVERSED: Passed {reversed_tests_passed} / {REVERSED_TESTS_TOTAL} =======")

#test formatter: int, float, string
formatter_tests_passed = 0
FORMATTER_TESTS_TOTAL = 4
res = utils.formatter(16)
if res[0] == 10000 and res[1] == 20: formatter_tests_passed += 1

res = utils.formatter(456)
if res[0] == 111001000 and res[1] == 710: formatter_tests_passed += 1

res = utils.formatter(3.14)
if res == None: formatter_tests_passed += 1

res = utils.formatter("hello world")
if res == None: formatter_tests_passed += 1

print(f"======= Completed Testing formatter: Passed {formatter_tests_passed} / {FORMATTER_TESTS_TOTAL} =======")

