"""

이분탐색은 아래 코드를 외우는게 편하다 !

정렬된 배열에서 O(logN)만에 찾을 수 있다
> 한번에 반(1/2)씩 날려버리기 때문에

Parametric Search : 문제에 ~의 최댓값을 구하시오 혹은 ~의 최솟값을 구하시오  >> Parametric Search로 접근해 볼 필요가 있다 !!

"""

def bise(a, l, r, x):
    while l <= r:
        mid = (l + r) // 2
        if a[mid] == x:
            return True
        if a[mid] < x: l = mid + 1
        else: r = mid - 1