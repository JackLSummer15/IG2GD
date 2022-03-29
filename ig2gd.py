import os, struct, json

print('IMPOSSIBLE GAME TO GEOMETRY DASH BY: JACKLSUMMER15')
try:
    os.mkdir('input')
    os.mkdir('output')
    input('The directories have been made. Insert any level that is either json or dat into the input folder.')
    exit()
except:
    pass

levelplaceholder='kS38,1_40_2_125_3_255_11_255_12_255_13_255_4_-1_6_1000_7_1_15_1_18_0_8_1|1_0_2_102_3_255_11_255_12_255_13_255_4_-1_6_1001_7_1_15_1_18_0_8_1|1_0_2_102_3_255_11_255_12_255_13_255_4_-1_6_1009_7_1_15_1_18_0_8_1|1_255_2_255_3_255_11_255_12_255_13_255_4_-1_6_1002_5_1_7_1_15_1_18_0_8_1|1_125_2_0_3_255_11_255_12_255_13_255_4_-1_6_1005_5_1_7_1_15_1_18_0_8_1|1_125_2_0_3_255_11_255_12_255_13_255_4_-1_6_1006_5_1_7_1_15_1_18_0_8_1|,kA13,0,kA15,0,kA16,0,kA14,,kA6,0,kA7,0,kA17,0,kA18,0,kS39,0,kA2,0,kA3,0,kA8,0,kA4,0,kA9,0,kA10,0,kA11,0;'

#teleport objects because the impossible game 2 uses blocks for the ground
teleport='1,747,2,15,3,15,32,0.5,54,1105;'

for level in os.listdir('input'):
    filename=level.split('.')[0]
    print('converting '+filename)
    output=open('output/'+filename+'.plist','w')
    output.write(levelplaceholder)
    if level.endswith('.json'): #impossible game 2
        output.write(teleport)
        ig2lvl=json.load(open('input/'+level))
        blocks=ig2lvl[2][0][3][1]
        spikes=ig2lvl[2][0][3][2]
        collectables=ig2lvl[2][0][3][11]
        print('adding '+str(len(blocks))+' blocks...')
        for block in blocks:
            width=block[0]
            height=block[1]+1005
            output.write('1,1,2,'+str(width)+',3,'+str(height)+';')
        print('adding '+str(len(spikes))+' spikes...')
        for spike in spikes:
            width=spike[0]
            height=spike[1]+1005
            angle=spike[2]*90
            output.write('1,8,2,'+str(width)+',3,'+str(height)+',6,'+str(angle)+';')
        print('adding '+str(len(collectables))+' collectables...')
        for collectable in collectables:
            width=collectable[0]
            height=collectable[1]+1005
            output.write('1,1614,2,'+str(width)+',3,'+str(height)+',36,1,51,0;')

    elif level.endswith('.dat'): #impossible game 1
        with open('input/'+level,'rb') as l:
            l.read(5)
            objectcount=struct.unpack('>h',l.read(2))[0]
            print('adding '+str(objectcount)+' objects...')
            for object in range(objectcount):
                objectid=struct.pack('>c',l.read(1))[0]
                l.read(1)
                l.read(1)
                width=struct.unpack('>h',l.read(2))[0]#+330
                l.read(1)
                l.read(1)
                height=struct.unpack('>h',l.read(2))[0]+15
                if objectid==1: #spike
                    output.write('1,8,2,'+str(width)+',3,'+str(height)+';')
                elif objectid==0: #block
                    output.write('1,1,2,'+str(width)+',3,'+str(height)+';')
                elif objectid==2: #pit
                    for pitwidth in range(width,height,30):
                        output.write('1,1715,2,'+str(pitwidth)+',3,2.5;')
            l.read(2)
            levelend=struct.unpack('>h',l.read(2))[0]
            l.read(3)
            bkgcount=struct.pack('>c',l.read(1))[0]
            print(str(bkgcount)+' background triggers...')
            for bkg in range(bkgcount):
                l.read(2)
                bkgwidth=struct.unpack('>h',l.read(2))[0]
                l.read(4)
                bkgcolor=struct.pack('>c',l.read(1))[0]
                if bkgcolor==0: #blue
                    output.write('1,29,2,'+str(bkgwidth)+',3,-15,36,1,7,0,8,102,9,255,10,0.5,35,1,23,1000;')
                    output.write('1,30,2,'+str(bkgwidth)+',3,-45,36,1,7,0,8,102,9,255,10,0.5,35,1,23,1001;')
                elif bkgcolor==1: #yellow
                    output.write('1,29,2,'+str(bkgwidth)+',3,-15,36,1,7,255,8,255,9,0,10,0.5,35,1,23,1000;')
                    output.write('1,30,2,'+str(bkgwidth)+',3,-45,36,1,7,255,8,255,9,0,10,0.5,35,1,23,1001;')
                elif bkgcolor==2: #green
                    output.write('1,29,2,'+str(bkgwidth)+',3,-15,36,1,7,0,8,255,9,0,10,0.5,35,1,23,1000;')
                    output.write('1,30,2,'+str(bkgwidth)+',3,-45,36,1,7,0,8,255,9,0,10,0.5,35,1,23,1001;')
                elif bkgcolor==3: #violet
                    output.write('1,29,2,'+str(bkgwidth)+',3,-15,36,1,7,177,8,0,9,252,10,0.5,35,1,23,1000;')
                    output.write('1,30,2,'+str(bkgwidth)+',3,-45,36,1,7,177,8,0,9,252,10,0.5,35,1,23,1001;')
                elif bkgcolor==4: #pink
                    output.write('1,29,2,'+str(bkgwidth)+',3,-15,36,1,7,255,8,0,9,191,10,0.5,35,1,23,1000;')
                    output.write('1,30,2,'+str(bkgwidth)+',3,-45,36,1,7,255,8,0,9,191,10,0.5,35,1,23,1001;')
                elif bkgcolor==5: #black
                    output.write('1,29,2,'+str(bkgwidth)+',3,-15,36,1,7,0,8,0,9,0,10,0.5,35,1,23,1000;')
                    output.write('1,30,2,'+str(bkgwidth)+',3,-45,36,1,7,0,8,0,9,0,10,0.5,35,1,23,1001;')
            #1,29,2,width,3,height,36,1,7,red,8,green,9,blue,10,duration,35,1,23,1000; #bkg trigger
            #1,30,2,width,3,height,36,1,7,red,8,green,9,blue,10,duration,35,1,23,1001; #ground trigger

    output.close()
