class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        perms = [[]]

        #for n in nums:
            #nexPerm = []
            #for p in perms:
                #for i in range(len(p) + 1):
                    #copy = p.copy()
                    #copy.insert(i,n)
                    #nexPerm.append(copy)
                #perms = nexPerm
        #return perms

        def get_permutations(items):

            if len(items) <= 1:
                return [items]
        
            all_perms = []
    
    # Loop through the list, picking each item as the starting element
            for i in range(len(items)):
                current_item = items[i]
        
        # Extract all other items except the current one
                remaining_items = items[:i] + items[i+1:]
        
        # Recursively get permutations for the remaining items
                for p in get_permutations(remaining_items):
                    all_perms.append([current_item] + p)
            
            return all_perms

        return get_permutations(nums)