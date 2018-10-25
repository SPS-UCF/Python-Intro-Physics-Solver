from models.kinematics import newtonian_model as nm
from models.em import em_model as em

print("\n\n--------------------------------------")
print("Welcome to the Physics Problem Solver!")
userFunc = ""

while userFunc != "exit":
    print("--------------------------------------")
    print("[function name]\t\t:\t[code]\t:\t[required parameters]\n"
          "distance\t\t\t:\tdis\t\t:\tinitial velocity, acceleration, time\n"
          "final velocity\t\t:\tfvd\t\t:\tinitial velocity, acceleration, distance\n"
          "final velocity\t\t:\tfvt\t\t:\tinitial velocity, acceleration, time\n"
          "*horizontal range\t:\thr\t\t:\tinitial velocity, angle, gravity\n"
          "*maximum height\t\t:\tmx\t\t:\tinitial velocity, angle, initial height, gravity\n"
          "coulomb force\t\t:\tcf\t\t:\tcharge 1, charge 2, distance r\n"
          "*electric field\t\t:\tef\t\t:\tcharge, distance r, x coordinate, y coordinate")
    print("--------------------------------------\n")

    userFunc = input("Enter a function code:\n")
    params = []

    # newtonian models
    if userFunc == "dis":
        for i in range(3):
            params.append(int(input("Enter parameter %d\t" % (i + 1))))
        nm.distance(params[0], params[1], params[2])

    if userFunc == "fvd":
        for i in range(3):
            params.append(int(input("Enter parameter %d\t" % (i + 1))))
        nm.vel_final_dist(params[0], params[1], params[2])

    if userFunc == "fvt":
        for i in range(3):
            params.append(int(input("Enter parameter %d\t" % (i + 1))))
        nm.vel_final_time(params[0], params[1], params[2])

    if userFunc == "hr":
        for i in range(3):
            params.append(int(input("Enter parameter %d\t" % (i + 1))))
        nm.horizontal_range(params[0], params[1], params[2])

    if userFunc == "mx":
        for i in range(4):
            params.append(int(input("Enter parameter %d\t" % (i + 1))))
        nm.maximum_height(params[0], params[1], params[2], params[3])

    # em models
    if userFunc == "cf":
        for i in range(3):
            params.append(input("Enter parameter %d\t" % (i + 1)))
        em.coulomb_force(float(params[0]), float(params[1]), float(params[2]))
        # remove this eventually, just to check function
        a = em.coulomb_force(float(params[0]), float(params[1]), float(params[2]))
        print("%.4g" % a)

    if userFunc == "ef":
        for i in range(4):
            params.append(int(input("Enter parameter %d\t" % (i + 1))))
        em.electric_field(params[0], params[1], params[2], params[3])
