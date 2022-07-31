# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def serializeNode(node, serializedString):
            if node == None:
                serializedString += 'None,'
            else:
                serializedString += str(node.val) + ','
                serializedString = serializeNode(node.left, serializedString)
                serializedString = serializeNode(node.right, serializedString)
            
            return serializedString

        return serializeNode(root, '')

                
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def deserializeNode(serializedStringList):
            if serializedStringList[0] == 'None':
                serializedStringList.pop(0)
                return None
            
            node = TreeNode(serializedStringList[0])
            serializedStringList.pop(0)
            node.left = deserializeNode(serializedStringList)
            node.right = deserializeNode(serializedStringList)
            return node
        
        #convert serialized string to a list of string values, 
        #each string represents the value of a node
        serializedStringList = data.split(',')
        print(serializedStringList)
        root=deserializeNode(serializedStringList)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))