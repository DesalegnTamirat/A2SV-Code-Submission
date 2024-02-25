class Solution:
    def bestClosingTime(self, customers: str) -> int:
        all_y = 0
        for customer in customers:
            if customer == "Y":
                all_y += 1
        # on the 0th hour the penality is all Y in customers
        minimum_penality = all_y
        penality = all_y
        hour = 0
        for i, customer in enumerate(customers):
            # going forward panlity increase if N else increase
            if customer == "Y":
                penality -= 1
            else:
                penality += 1
            
            if penality < minimum_penality:
                minimum_penality = penality
                hour = i + 1
        
        return hour




                

        [0, 0, 0, 1, 0]
        [3, 2, 1, 1, 0]
        [0, 1, 2, 1, 1]
