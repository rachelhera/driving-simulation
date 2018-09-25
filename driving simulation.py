print("Enter time spent on road(s)")
t = int(input())
print("Enter acceleration(m/s2)")
a = int(input())
print("Enter distance to destination(m)")
d = int(input())

v = a*t

s = (t*v)/2


for i in range(0, t + 1):
    x = (((a*i)*i)/2)//10
    print("Duration: " + str(i) + "Distance: " +("*" * int(x)))
    i = i + 1

#speed limit(m/s)
m = 60

if v > m:
    print("The person went over the speed limit.(Max speed was" + str(v) + "m/s)")
else:
    print("The person did not go over the speed limit. (Max speed was" + str(v) + "m/s)")

if s >= d:
    print("The person reached the destiation.(Reached " + str(s) + "m)")
else:
    print("the person did not reach the destination.(Reached" + str(s) + "m)")

