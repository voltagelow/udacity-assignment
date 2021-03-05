# udacity-assignment

## Command to execute Code 
python boardGameValidation.py

### User Defined Variables 
#### Board(b) 
  Is a 2 Dimension matrix represented as list , ex b1=[[2,1,4,3],[1,4,3,2],[3,2,1,4],[4,3,2,1]]
#### Constraints(c)
  Represented as a hashmap where key id operator(gt=>greaterthen , lt=>less then..etc) and val as list of tuple represent 2 points in matrix,can be extended to other operations like multiply, divide and user defined expressions.
  ex c1={"gt":[(1,1),(1,2)],'gt':[(2,3),(3,3)]}
 
python boardGameValidation.py =>  will execute all the test cases defined in the script you can edit the existing ones or extend the same in a similar manner.

On Success 
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK

If any test cases failed we will see the number of failures and exact point of failure too, ex

======================================================================
FAIL: test_board (__main__.TestBoardGame)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "boardGameValidation.py", line 82, in test_board
    self.assertEqual(ac1,a.isValid(b1,c1))
AssertionError: False != True

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
