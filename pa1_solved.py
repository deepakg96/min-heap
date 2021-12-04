'''
---------------------------------------------------------------------------
HOW TO RUN THIS FILE
---------------------------------------------------------------------------
python pa1_solved.py <input_file>
For example: python pa1_solved.py input1.txt

You can use redirection to redirect stdout to file like shown below,
python pa1_dgowda.py input1.txt > out1.txt
Then you can use vimdiff to see the difference in output files.

----------------------------------------------------------------------------
ASSUMPTIONS AND SHORTCOMINGS
----------------------------------------------------------------------------
Assumptions: 1) Input is always fed via command line using inputX.txt files. 
			 2) inputX.txt files conatin no errors.
			 3) inputX.txt is always of the form,
				A 10
				A 20
				E
				A 1
				E
				E

Shortcomings: 1) Parsing file content using readlines() may not be efficient.
		      2) Consumes time to parse big inputX.txt files.


'''


import sys

class minheap():
	def __init__(self):
		self.arr = [0]*20000000
		self.size =	0

	def leftchildindex(self,parent_index):
		return 2*parent_index + 1

	def rightchildindex(self,parent_index):
		return 2*parent_index + 2
	
	def parentindex(self, child_index):
		return (child_index - 1)/2

	def hasleftchild(self, index):
		return self.leftchildindex(index) < self.size

	def hasrightchild(self, index):
		return self.rightchildindex(index) < self.size
	
	def hasparent(self, index):
		return self.parentindex(index) >= 0

	def leftchild(self, index):
		return self.arr[self.leftchildindex(index)]

	def rightchild(self, index):
		return self.arr[self.rightchildindex(index)]

	def parent(self, index):
		return self.arr[self.parentindex(index)]

	def remove(self):
		if(self.size == 0):
			return
		first_elem = self.arr[0]
		self.arr[0]=self.arr[self.size - 1]
		self.size-=1
		self.arr.pop()
		self.heapify_down()
		return first_elem

	def insert(self, item):
		self.arr.insert(self.size, item)
		self.size+=1
		self.heapify_up()

	def heapify_up(self):
		last_index = self.size - 1
		while(self.hasparent(last_index) and self.parent(last_index) > self.arr[last_index]):
			self.arr[self.parentindex(last_index)], self.arr[last_index] = self.arr[last_index], self.arr[self.parentindex(last_index)]
			last_index=self.parentindex(last_index)

		
	def heapify_down(self):
		root_index = 0
		if len(self.arr) <= 0:
			return
		while(self.hasleftchild(root_index)):
			smallerchildindex=self.leftchildindex(root_index)
			if (self.rightchildindex(root_index) and (self.rightchild(root_index) < self.leftchild(root_index))):
				smallerchildindex=self.rightchildindex(root_index)

			if(self.arr[root_index] < self.arr[smallerchildindex]):
				break
			else:
				self.arr[root_index], self.arr[smallerchildindex] = self.arr[smallerchildindex], self.arr[root_index]
			root_index=smallerchildindex

	def printarr(self):
		for i in self.arr:
			print i
	
	def printindex(self,index):
		print(self.arr[index])


mh=minheap()

filename=sys.argv[1]
fp=open(filename,"r")

lines=fp.read().splitlines()

for x in lines:
	elem=' '
	if (len(x) > 1):
		elem=int(x.split(' ')[1])

	if(str(x.split(' ')[0]) == "A"):
		mh.insert(elem)
	else:
		print(mh.remove())

fp.close()

'''
DONOT-UNCOMMENT-THIS
TEST 1 --
mh.insert(300)
print(mh.remove())

mh.insert(200)
mh.insert(600)
mh.insert(500)
print(mh.remove())

mh.insert(100)
print(mh.remove())
print(mh.remove())
print(mh.remove())

TEST 2 --
mh.insert(354)
print(mh.remove())

mh.insert(676)
mh.insert(395)
print(mh.remove())
mh.insert(688)

print(mh.remove())

mh.insert(838)
mh.insert(427)
mh.insert(632)
print(mh.remove())
print(mh.remove())
print(mh.remove())

mh.insert(207)
print(mh.remove())

mh.insert(690)
print(mh.remove())

mh.insert(750)
print(mh.remove())
print(mh.remove())

TEST 3 --
mh.insert(10)
print(mh.remove())

mh.insert(-1)
mh.insert(999)
mh.insert(-28)
print(mh.remove())
print(mh.remove())
'''
