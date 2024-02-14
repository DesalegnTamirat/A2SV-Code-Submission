class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # storing the node and it connected one
        node_connected = {}
        for node, step in enumerate(nums):
            connected = (node + step) % len(nums)
            if connected >= 0:
                node_connected[node] = connected
            else:
                node_connected[node] = connected + len(nums)
        
        for node in node_connected:
            connected = node_connected[node]
            # only one node connected to itself
            if node == connected:
                continue
            # if loop it will come back to itselfbefore the n hits zero
            n = len(nums)
            sign = nums[node] // abs(nums[node])
            while n > 0:
                # checks if the same sign
                if nums[connected] // abs(nums[connected]) != sign:
                    break
                if node == connected:
                    return True
                connected = node_connected[connected]
                n -= 1
        
        return False



        