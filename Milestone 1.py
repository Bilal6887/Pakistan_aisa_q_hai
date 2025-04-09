years = [1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
countries = ['Pakistan','India','China','Turkey','Israel','Switzerland','Netherlands']
countryInflationIndex = [0,34,68,102,136,170,204]
inflation = [4.681218546,8.837937018,7.844264737,9.052131553,11.79127034,9.509041462,9.97366476,12.36819439,12.34357852,10.37380859,11.37549289,6.228004154,4.142637181,4.366664513,3.148261446,3.290344726,2.914134701,7.444624693,9.06332737,7.921084401,7.598684411,20.28612109,13.64776506,12.93887056,11.91609271,9.682351861,7.692156119,7.189384028,2.529328173,3.765119164,4.08537368,5.078057259,10.5783618,9.739993139,8.801125813,9.383471862,7.074280029,8.971232503,13.87024618,11.78781704,6.326890488,10.24793556,10.22488616,8.977152338,7.164252115,13.23083898,4.66982038,4.00943591,3.779293122,4.297152039,3.805858995,3.767251735,4.24634362,5.796523376,6.372881356,8.349267049,10.88235294,11.98938992,8.858360966,9.312445605,11.06367478,6.649500151,4.906973441,4.948216341,3.328173375,3.945068664,3.723276483,6.623436776,7.233835531,18.81181794,18.24563836,3.052290121,3.556685652,6.35398134,14.61007864,24.25698972,16.79122517,8.313160289,2.786465055,-0.773186012,-1.401472683,0.347811227,0.719125609,-0.731970902,1.127603487,3.824637431,1.776414077,1.649430995,4.816767674,5.92525137,-0.728165251,3.175324753,5.553898923,2.619524326,2.621050017,1.921641628,1.437023809,2.000001822,1.593136001,2.0747904,2.899234164,2.419421895,38.85584348,68.80964338,63.27255249,60.30386913,65.97856799,70.07610387,66.09384298,105.2149865,89.11331722,80.41215114,85.66936165,84.64134348,64.86748764,54.91537058,54.40018876,44.96412095,21.60243845,8.598261681,8.179160368,9.597242123,8.75618091,10.44412838,6.250976631,8.566444206,6.471879671,8.891569965,7.493090305,8.854572714,7.670853648,7.775134153,11.14431108,16.3324639,15.17682157,12.27895745,19.09385113,16.44021739,20.3033839,17.26479146,19.02398677,12.02223767,10.98014888,12.27874045,9.940258878,11.39622642,8.956639566,5.496828753,5.175055994,1.053575432,1.15350488,5.756578947,0.725764645,-0.411734431,1.312661499,2.060803918,0.459816074,4.55721393,3.340312143,2.716640575,3.478572709,1.689481892,1.576211979,0.486495554,-0.634390651,-0.546034946,0.244953121,0.817323896,0.844128709,-0.5884303,1.44032188,1.872468597,3.155269797,5.403959092,5.859596635,4.037030208,3.292621803,0.852116995,1.799827769,0.811634065,0.520225423,0.017938438,0.806444381,1.558529197,0.98902033,0.642711507,0.638272931,0.802908731,1.171954203,1.059509283,0.732350603,2.426041171,-0.480481936,0.688238707,0.231349208,-0.692552018,-0.217323155,-0.013202539,-1.143908672,-0.434618664,0.53378784,0.936335464,0.36288618,-0.725874933,-0.691203091,0.737943046,1.082160156,2.454089859,3.158197519,3.183585695,2.584181156,2.801526937,1.923224572,2.113787871,2.109245627,1.959136323,2.157179181,2.360522338,4.155841272,3.287531047,2.09199839,1.263647392,1.688130179,1.101501065,1.613858598,2.486501983,1.18977687,1.275305696,2.341070178,2.455547653,2.506898527,0.97603508,0.600248147,0.316666667,1.381458714,1.703497947,2.633699102,1.272460378]
numberOfYears = len(years)
numberOfCountries = len(countries)
def start_index(countryname,countries):
    for i in range(len(countries)):
        if countryname == countries[i]:
            return i
def totalavginflation(countrydata):
    sum = 0
    for j in range(len(countrydata)):
        sum = sum + countrydata[j]
        avg = sum / len(countrydata)
    return avg
totalavg = []
extra = 0
def extra(years):
    extra1=0
    z = int(input("From which year you want inflation average"))
    for i in range(len(years)):
        if z == years[i]:
            extra1 = i
    return extra1
extra1 = int(extra(years))
print(extra1)
for i in range(len(countries)):
    value = start_index(countries[i],countries)
    countrydata=inflation[countryInflationIndex[value]+extra1:countryInflationIndex[value]+numberOfYears]
    totalavg.append(totalavginflation(countrydata))
print(totalavg)
def sorting_list(totalavg):
    sorted_list=[]
    sorted_indices = []
    for M in range(len(totalavg)):
        chota = totalavg[0]
        index = 0
        for N in range(len(totalavg)):
            if totalavg[N] < chota:
                chota = totalavg[N]
                index = N
        sorted_list.append(chota)
        totalavg[index]=1000
        sorted_indices.append(index)
    return(sorted_list,sorted_indices)
sorted_list,sorted_indices=sorting_list(totalavg)
rank =1
for i in range(len(sorted_indices)):
    print ("sasta country",rank ,"goes to ",countries[sorted_indices[i]],"with average inflation ",sorted_list[i])
    rank +=1