import unittest

from Mailroom_lesson07 import createlist,getlist,sumdonor

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

	def test_sumdonor(self):
		createlist()
		self.assertTrue(sumdonor("Paul Allen") == 1050)
		self.assertFalse(sumdonor("Jeff Bezos") == 250000000)
		with self.assertRaises(KeyError):
			sumdonor("Porky Pig")



if __name__ == '__main__':
	unittest.main()