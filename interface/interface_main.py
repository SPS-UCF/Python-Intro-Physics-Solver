from models.kinematics import newtonian_model as nm

print("\n\n--------------------------------------")
print("Welcome to the Physics Problem Solver!")
print("--------------------------------------")
print("""[function name]\t\t:\t[code]\t:\t\t[required parameters]\n
distance\t\t\t:\t(dis)\t:\tinitial velocity, acceleration, time
final velocity\t\t:\t(fvd)\t:\tinitial velocity, acceleration, distance
final velocity\t\t:\t(fvt)\t:\tinitial velocity, acceleration, time
horizontal range\t:\t(hr)\t:\tinitial velocity, angle, gravity
horizontal range\t:\t(hri)\t:\tinitial velocity, angle, initial height, gravity""")
print("--------------------------------------\n")

userFunc = input("Enter a function code:\n")

params = []
if userFunc == "distance":
    for i in range(3):
        params.append(int(input("Enter parameter %d\t" % (i+1))))
    nm.distance(params[0], params[1], params[2])

if userFunc == "fvd":
    for i in range(3):
        params.append(int(input("Enter parameter %d\t" % (i+1))))
    nm.vel_final_dist(params[0], params[1], params[2])

if userFunc == "fvt":
    for i in range(3):
        params.append(int(input("Enter parameter %d\t" % (i+1))))
    nm.vel_final_time(params[0], params[1], params[2])
