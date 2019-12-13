from process import *

class runner:
	def __init__(self, runType):
		self.runType = runType

	def runStart(self):
		if self.runType == 0:
			testDataMake()
		elif self.runType == 1:
			trainDataMake()
		elif self.runType == 2:
			testDataMake()
			trainDataMake()
		else:
			print("Worng runType")

if __name__ == '__main__':
	testRun = runner(2)
	testRun.runStart()
