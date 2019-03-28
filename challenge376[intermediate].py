start = int(input("First year: "))
end = int(input("Second year: "))
if start == end:
    print(0)
    exit()
tot = 0
startCycle = start % 4
if startCycle == 0:
    tot += 1
start100Cycle = start % 100
if start100Cycle == 0:
    tot -= 1
start900Cycle = start % 900
if start900Cycle == 200 or start900Cycle == 600:
    tot += 1

dif = end - start - 1

expected = dif / 4
tot += int(expected)
expectedExceptions = dif/100
tot -= int(expectedExceptions)
expectedExceptionExceptions = dif/900
tot += 2*int(expectedExceptionExceptions)
remainder = dif % 4
if remainder + startCycle >= 4:
    tot += 1
remainder100 = dif % 100
if remainder100 + start100Cycle >= 100:
    tot -= 1
remainder900 = dif % 900
if start900Cycle+remainder900 > 200 > start900Cycle:
    tot += 1
if start900Cycle+remainder900 > 600 > start900Cycle:
    tot += 1
if start900Cycle+remainder900 > 1100 > start900Cycle:
    tot += 1
if start900Cycle+remainder900 > 1500 > start900Cycle:
    tot += 1

print(tot)
