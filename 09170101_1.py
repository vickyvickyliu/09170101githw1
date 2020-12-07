r=int(input("請輸入半徑："))
PI=3.14159
area=PI*r**2
frstreaml=open("d:\out1.txt", mode="a")
print("/半徑{0:3d}圓面積是{1:10.2f}/".format(r,area),file=frstreaml)
print("/半徑{0:>3d}圓面積是{1:>10.2f}/".format(r,area),file=frstreaml)      
print("/半徑{0:<3d}圓面積是{1:<10.2f}/".format(r,area))      
print("/半徑{0:^3d}圓面積是{1:^10.2f}/".format(r,area))
frstreaml.close()

import math
r=int(input("請輸入半徑："))
PI=3.14159
area=PI*r**2
frstreaml=open("d:\out1.txt", mode="a")
print("/半徑{0:3d}圓面積是{1:10.2f}/".format(r,math.pi*r**2),file=frstreaml)
print("/半徑{0:>3d}圓面積是{1:>10.2f}/".format(r,math.pi*r**2),file=frstreaml)      
print("/半徑{0:<3d}圓面積是{1:<10.2f}/".format(r,math.pi*r**2))      
print("/半徑{0:^3d}圓面積是{1:^10.2f}/".format(r,math.pi*r**2))
frstreaml.close()
