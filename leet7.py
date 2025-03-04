class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """

        def possible(bloomDay, day, m, k):
            n = len(bloomDay)  # size of the array
            cnt = 0
            noOfB = 0
            # count the number of bouquets
            for i in range(n):
                if bloomDay[i] <= day:
                    cnt += 1
                else:
                    noOfB += cnt // k
                    cnt = 0
            noOfB += cnt // k
            return noOfB >= m
        def roseGarden(bloomDay, k, m):
            val = m * k
            n = len(bloomDay)  # size of the array
            if val > n:
                return -1  # impossible case
            # find maximum and minimum
            mini = float('inf')
            maxi = float('-inf')
            for i in range(n):
                mini = min(mini, bloomDay[i])
                maxi = max(maxi, bloomDay[i])

            low = mini
            high = maxi
            while low <= high:
                mid = (low + high) // 2
                if possible(bloomDay, mid, m, k):
                    high = mid - 1
                else:
                    low = mid + 1
            return low
        return roseGarden(bloomDay, k, m)