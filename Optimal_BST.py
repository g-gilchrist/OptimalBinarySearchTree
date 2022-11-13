INT_MAX = 999999999
 
def optimalSearchTree(keys, freq, numKeys):
    # creates an empty 2 dimensional array filled with zeros
    cost = [[0 for x in range(numKeys)] for y in range(numKeys)]
 
    # Fills 2 deminsional array with frequencies
    for index in range(numKeys):
        cost[index][index] = freq[index]
       
    # Fills 2 deminsional array with the optimal cost from node to node
    # Utilizing the Length variable we create an equation that fills the adjacency matrix utilizing the length of the keys
    # We crate a variable for row index and column index to iterate through the adjacency matrix
    # we set the cost initially to infinity, or a really high number
    for Length in range(2, numKeys + 1):
        for rowIndex in range(numKeys - Length + 2):                                           
            columnIndex = rowIndex + Length - 1
            if rowIndex >= numKeys or columnIndex >= numKeys:
                break
            cost[rowIndex][columnIndex] = INT_MAX
            
           
            # in a for loop we set the costRoot to zero, and iterate through the matrix setting cost node to the frequency in the adjacency matrix
            # as we iterate through the list we are checking to see if the cost node is less than the frequencies set in the matrix
            # Previously we had set some of the nodes in our matrix to infinity, so now we are checking those same nodes for a smaller frequency
            for currentNode in range(rowIndex, columnIndex + 1):
                costNode = 0                
                if (currentNode > rowIndex):
                    costNode += cost[rowIndex][currentNode - 1]                    
                if (currentNode < columnIndex):
                    costNode += cost[currentNode + 1][columnIndex]
                costNode += sum(freq, rowIndex, columnIndex)               
                if (costNode < cost[rowIndex][columnIndex]):
                    cost[rowIndex][columnIndex] = costNode
     
    print("\n""Adjacency Matrix:")    
    # printing the adjacency matrix                
    for i in range(len(cost)):
        print(cost[i])
    # returning the cost of the optimal BST
    return cost[0][numKeys - 1]
 
 
# We multiply the frequency by the height, add frequency in a range multiple times
def sum(freq, rowIndex, columnIndex):
 
    optimalSum = 0
    for k in range(rowIndex, columnIndex + 1):
        optimalSum += freq[k]
    
    return optimalSum



def main():
    keys = [10,12,20]
    freq = [34,8,50]
    numKeys = len(keys)

    print("\n"f"Cost of Optimal BST is {optimalSearchTree(keys, freq, numKeys)}")

main()