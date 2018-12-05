import math

print('Welcome in PipeDiameter program. It helps you to choose the right size of pipe for'
      ' sewerage pressure systems.')
flow=round(float(input('Please enter your sewage flow [(m^3)/s]:')),2)
speed_assumed = 1
calc_diameter=round(math.sqrt(((4*flow)/((math.pi)*speed_assumed))*1000),2)
print(str(calc_diameter)+' mm')

nominal_diameters=[90,110,125,160,180,200,225,250,315,355,400,450,500,560,630,710,800]
inner_diameters=[(90-2*5,4),(110-2*6,6),(125-2*7,4),(160-2*9,5),(180-2*10,7),(200-2*11,9),
                 (225-2*13,4),(250-2*14,8),(315-2*18,7),(355-2*21,1),(400-2*23,7),(450-2*26,7),
                 (500-2*29,7),(560-2*33,2),(630-2*37,4),(710-2*42,1),(800-2*47,4)]

i = 0
while True:
    if nominal_diameters[i] <= calc_diameter <= nominal_diameters[i + 1]:
        nominal_diameter = nominal_diameters[i]
        break
    i = i + 1

print(nominal_diameter)