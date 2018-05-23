import unittest

from Mailroom3 import createlist, getlist, searchdonors 

class MyFuncTestCase(unittest.TestCase):
	
	def test_createlist(self):
		createlist()
		output = getlist()
		self.assertEqual(output["Bill Gates"],[10000,12000]) 
		self.assertTrue(output["Bill Gates"] == [10000,12000]) 
		self.assertFalse(output["Bill Gates"] == [10000,12001])
		with self.assertRaises(KeyError):
			output["Carrot Top"]

#This was a failed testing scenario as the original function already handles the exception
	# def test_searchdonors(self):
	# 	createlist()
	# 	output = getlist()
	# 	with self.assertRaises(KeyError):
	# 		searchdonors("Carrot Top")




if __name__ == '__main__':
	unittest.main()