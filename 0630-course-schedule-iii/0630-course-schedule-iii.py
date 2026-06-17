class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x:x[1])
        days = 0
        pq = []
        for i,j in courses:
            days += i
            heapq.heappush(pq,-i)

            if days > j:
                days -= -heapq.heappop(pq)
        return len(pq)