from refactor import test_data, create_donors_report

TEST_DATA = test_data()

def test_1():
	result = create_donors_report(test_data())

	print(results)

	assert len(result) == len(TEST_DATA)
#supposed to be a random assert statement
	donor = result[1]
	assert result[-1] == donor[2] / donor[1]

	assert result[0][2] > result[-1][1]
	assert False