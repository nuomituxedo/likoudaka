# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        #Step 1: recursively (DFS) map each node with its value, row and col
        #res becomes a list containing lists of such value, row, col pairs
        def mapper(root, res, row, col):
            if not root:
                return
            res.append([root.val, row, col])
            mapper(root.left, res, row+1, col-1)
            mapper(root.right, res, row+1, col+1)
            return res
        
        #nodes is a list containing lists. Each list contains a node's value, row, col 
        nodes = mapper(root, [], 0, 0)
        
        #Step 2: create a dictionary where key is the col value, values is a list of node values 
        verticalOrderTraversal = {}
        for node in nodes:
            val = node[0]
            row = node[1]
            col = node[2]
            if col in verticalOrderTraversal:
                if row in verticalOrderTraversal[col]:
                    verticalOrderTraversal[col][row].append(val)
                    print('exisitng row, add val to list',verticalOrderTraversal[col][row] )
                else:
                    newList = [val]
                    verticalOrderTraversal[col][row] = newList
                    print('adding new row', newList, verticalOrderTraversal[col][row] )
            else:
                newColDict = {}
                newColDict[row] = [val]
                verticalOrderTraversal[col] = newColDict
                
                
        #Sort the dictionary by column key
        sortedTraversal = dict(sorted(verticalOrderTraversal.items(), key=lambda x:x[0]))
        
        #Sort the dictionary by row key
        for col in sortedTraversal:
            sortedTraversal[col] = dict(sorted(sortedTraversal[col].items(), key=lambda x:x[0]))
            
        #Step 3: create the final result from the dictionary with sorted keys
        resultList = []
        for col in sortedTraversal.keys():
            item = []
            for row in sortedTraversal[col]:
                #before adding the value list to resultList, remember to sort the list
                for value in sorted(sortedTraversal[col][row]):
                    item.append(value)
            resultList.append(item)
        return resultList
        
        