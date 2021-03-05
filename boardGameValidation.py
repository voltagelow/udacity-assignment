import logging
import datetime
import unittest

class Constraints(object):
    def __init__(self):
        logging.basicConfig(filename="{}.log".format(self.__class__.__name__+'_'+str(datetime.datetime.now().strftime("%Y%m%d"))),level=logging.INFO)
        logging.info('Called constraints....')
    def mul(self,i,j):
        '''Unimplemented methods'''
        pass
    def div(self,i,j):
        '''unimplemented method'''
        pass
    def gt(self,i,j):
        return False if self.M[i[0]-1][i[1]-1] < self.M[j[0]-1][j[1]-1] else True
    def lt(self,i,j):
        return False if self.M[i[0]-1][i[1]-1] > self.M[j[0]-1][j[1]-1] else True
    def checkConstraints(self):
        passed=True
        for k,v in self.const.items():
            if not getattr(self,k)(v[0],v[1]):
                logging.info('Constraint failed for operator {} for values {}'.format(k,v))
                passed=False
        return passed   
    
    def valid_board(self):
        valid=True
        for i in range(len(self.M)):
            res1 = self.valid_row(i)
            res2 = self.valid_col(i)
            
            if not res1 or not res2:
                valid=False 
        return valid

    def valid_row(self,row):
        grid=self.M
        temp = grid[row]
        if len(temp) != len(set(temp)):
            return False
        else:
            return True
        
    def valid_col(self,col):
        grid=self.M
        temp = [row[col] for row in grid]

        if len(temp) != len(set(temp)):
            return False
        else:
            return True
        
    def isValid(self,*args,**kwargs):
        self.M=args[0]
        self.const=args[1]
        if self.checkConstraints():
            return self.valid_board()
        else:
            return False


class TestBoardGame(unittest.TestCase):
    def test_board(self):
        b1=[[2,1,4,3],[1,4,3,2],[3,2,1,4],[4,3,2,1]] 
        c1={"gt":[(1,1),(1,2)],'gt':[(2,3),(3,3)]}

        b2=[[1,3,5,7],[8,3,2,9],[2,5,7,11],[5,9,3,6]]
        c2={"gt":[(3,2),(3,3)],'lt':[(4,4),(3,4)]}

        b3=[[4,3,2,1],[9,5,7,6],[11,7,3,9],[8,9,6,3]]
        c3={"gt":[(1,1),(1,2)],'gt':[(2,3),(3,3)]}

        b4=[[2,1,4,3],[1,4,3,2],[3,2,1,4],[4,3,2,1]]
        c4={"gt":[(1,1),(1,2)],'gt':[(2,3),(3,3)]}

        a=Constraints()
        ac1=True
        ac2=False
        ac3=True
        ac4=True
        self.assertEqual(ac1,a.isValid(b1,c1))
        self.assertEqual(ac2,a.isValid(b2,c2))
        self.assertEqual(ac3,a.isValid(b3,c3))
        self.assertEqual(ac4,a.isValid(b4,c4))

if __name__ == '__main__':
    # constraint={"gt":[(1,1),(1,2)],'gt':[(2,3),(3,3)]}
    # a=Constraints()
    # m=[[2,1,4,3],[1,4,3,2],[3,2,1,4],[4,3,2,1]]
    # a.isValid(m,constraint)
    unittest.main()