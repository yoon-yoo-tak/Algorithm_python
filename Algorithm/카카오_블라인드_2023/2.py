import math

def solution(cap, n, deliveries, pickups):
    remain_deliver, remain_pickup = 0, 0
    prefix, suffix = [0] * n, [0] * n

    for i in range(n - 1, -1, -1):
        if deliveries[i] > remain_deliver:
            deliveries[i] -= remain_deliver
            remain_deliver = deliveries[i] % cap
            prefix[i] += math.ceil(deliveries[i] / cap)
        else:
            remain_deliver -= deliveries[i]

        if pickups[i] > remain_pickup:
            pickups[i] -= remain_pickup
            remain_pickup = pickups[i] % cap
            suffix[i] += math.ceil(pickups[i] / cap)
        else:
            remain_pickup -= pickups[i]

    deliver_count, pickup_count = 0, 0
    for i in range(n - 1, -1, -1):
        mi = min(pickup_count, prefix[i])
        prefix[i] -= mi
        pickup_count -= mi

        mi = min(deliver_count, suffix[i])
        suffix[i] -= mi
        deliver_count -= mi

        deliver_count += prefix[i]
        pickup_count += suffix[i]
    return sum((prefix[i] + suffix[i]) * 2 * (i + 1) for i in range(n))


print(solution(2, 7, [1,0,2,0,1,0,2], [0,2,0,1,0,2,0]))  # 30