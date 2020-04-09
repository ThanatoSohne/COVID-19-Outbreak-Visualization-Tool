from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep

mnDOH = 'https://www.health.state.mn.us/diseases/coronavirus/situation.html'

mnClient = req(mnDOH)

site_parse = soup(mnClient.read(), "lxml")
mnClient.close()

tables = site_parse.find("div", {"class": "clearfix"}).findAll("tbody")[3]

tags = tables.findAll('td')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
mn = "MINNESOTA"
co = ' County'


csvfile = "COVID-19_cases_mndoh.csv"
headers = "County, State, Latitude, Longitude, Cases \n"

file = open(csvfile, "w")
file.write(headers)

hold = []

for td in tags:
    take = td.get_text()
    hold.append(take)

file.write(hold[0] + ", " + mn + ", " + str(liegen.geocode(hold[0] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[0] + co + ", " + mn).longitude) + ", " 
           + hold[1] + ", " + hold[2] + "\n")
sleep(1)
file.write(hold[3] + ", " + mn + ", " + str(liegen.geocode(hold[3] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[3] + co + ", " + mn).longitude) + ", " + hold[4] 
           + ", " + hold[5] +"\n")
sleep(1)
file.write(hold[6] + ", " + mn + ", " + str(liegen.geocode(hold[6] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[6] + co + ", " + mn).longitude) + ", " + hold[7] 
           + ", " + hold[8] +"\n")
sleep(1)
file.write(hold[9] + ", " + mn + ", " + str(liegen.geocode(hold[9] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[9] + co + ", " + mn).longitude) + ", " + hold[10] 
           + ", " + hold[11] +"\n")
sleep(1)
file.write(hold[12] + ", " + mn + ", " + str(liegen.geocode(hold[12] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[12] + co + ", " + mn).longitude) + ", " + hold[13] 
           + ", " + hold[14] +"\n")
sleep(1)
file.write(hold[15] + ", " + mn + ", " + str(liegen.geocode(hold[15] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[15] + co + ", " + mn).longitude) + ", " + hold[16] 
           + ", " + hold[17] +"\n")
sleep(1)
file.write(hold[18] + ", " + mn + ", " + str(liegen.geocode(hold[18] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[18] + co + ", " + mn).longitude) + ", " + hold[19] 
           + ", " + hold[20] +"\n")
sleep(1)
file.write(hold[21] + ", " + mn + ", " + str(liegen.geocode(hold[21] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[21] + co + ", " + mn).longitude) + ", " + hold[22] 
           + ", " + hold[23] +"\n")
sleep(1)
file.write(hold[24] + ", " + mn + ", " + str(liegen.geocode(hold[24] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[24] + co + ", " + mn).longitude) + ", " + hold[25] 
           + ", " + hold[26] +"\n")
sleep(1)
file.write(hold[27] + ", " + mn + ", " + str(liegen.geocode(hold[27] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[27] + co + ", " + mn).longitude) + ", " + hold[28] 
           + ", " + hold[29] +"\n")
sleep(1)
file.write(hold[30] + ", " + mn + ", " + str(liegen.geocode(hold[30] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[30] + co + ", " + mn).longitude) + ", " + hold[31] 
           + ", " + hold[32] +"\n")
sleep(1)
file.write(hold[33] + ", " + mn + ", " + str(liegen.geocode(hold[33] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[33] + co + ", " + mn).longitude) + ", " + hold[34] 
           + ", " + hold[35] +"\n")
sleep(1)
file.write(hold[36] + ", " + mn + ", " + str(liegen.geocode(hold[36] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[36] + co + ", " + mn).longitude) + ", " + hold[37] 
           + ", " + hold[38] +"\n")
sleep(1)
file.write(hold[39] + ", " + mn + ", " + str(liegen.geocode(hold[39] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[39] + co + ", " + mn).longitude) + ", " + hold[40] 
           + ", " + hold[41] +"\n")
sleep(1)
file.write(hold[42] + ", " + mn + ", " + str(liegen.geocode(hold[42] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[42] + co + ", " + mn).longitude) + ", " + hold[43] 
           + ", " + hold[44] +"\n")
sleep(1)
file.write(hold[45] + ", " + mn + ", " + str(liegen.geocode(hold[45] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[45] + co + ", " + mn).longitude) + ", " + hold[46] 
           + ", " + hold[47] +"\n")
sleep(1)
file.write(hold[48] + ", " + mn + ", " + str(liegen.geocode(hold[48] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[48] + co + ", " + mn).longitude) + ", " + hold[49] 
           + ", " + hold[50] +"\n")
sleep(1)
file.write(hold[51] + ", " + mn + ", " + str(liegen.geocode(hold[51] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[51] + co + ", " + mn).longitude) + ", " + hold[52] 
           + ", " + hold[53] +"\n")
sleep(1)
file.write(hold[54] + ", " + mn + ", " + str(liegen.geocode(hold[54] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[54] + co + ", " + mn).longitude) + ", " + hold[55] 
           + ", " + hold[56] +"\n")
sleep(1)
file.write(hold[57] + ", " + mn + ", " + str(liegen.geocode(hold[57] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[57] + co + ", " + mn).longitude) + ", " + hold[58] 
           + ", " + hold[59] +"\n")
sleep(1)
file.write(hold[60] + ", " + mn + ", " + str(liegen.geocode(hold[60] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[60] + co + ", " + mn).longitude) + ", " + hold[61] 
           + ", " + hold[62] +"\n")
sleep(1)
file.write(hold[63] + ", " + mn + ", " + str(liegen.geocode(hold[63] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[63] + co + ", " + mn).longitude) + ", " + hold[64] 
           + ", " + hold[65] +"\n")
sleep(1)
file.write(hold[66] + ", " + mn + ", " + str(liegen.geocode(hold[66] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[66] + co + ", " + mn).longitude) + ", " + hold[67] 
           + ", " + hold[68] +"\n")
sleep(1)
file.write(hold[69] + ", " + mn + ", " + str(liegen.geocode(hold[69] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[69] + co + ", " + mn).longitude) + ", " + hold[70] 
           + ", " + hold[71] +"\n")
sleep(1)
file.write(hold[72] + ", " + mn + ", " + str(liegen.geocode(hold[72] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[72] + co + ", " + mn).longitude) + ", " + hold[73] 
           + ", " + hold[74] +"\n")
sleep(1)
file.write(hold[75] + ", " + mn + ", " + str(liegen.geocode(hold[75] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[75] + co + ", " + mn).longitude) + ", " + hold[76] 
           + ", " + hold[77] +"\n")
sleep(1)
file.write(hold[78] + ", " + mn + ", " + str(liegen.geocode(hold[78] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[78] + co + ", " + mn).longitude) + ", " + hold[79] 
           + ", " + hold[80] +"\n")
sleep(1)
file.write(hold[81] + ", " + mn + ", " + str(liegen.geocode(hold[81] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[81] + co + ", " + mn).longitude) + ", " + hold[82] 
           + ", " + hold[83] +"\n")
sleep(1)
file.write(hold[84] + ", " + mn + ", " + str(liegen.geocode(hold[84] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[84] + co + ", " + mn).longitude) + ", " + hold[85] 
           + ", " + hold[86] +"\n")
sleep(1)
file.write(hold[87] + ", " + mn + ", " + str(liegen.geocode(hold[87] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[87] + co + ", " + mn).longitude) + ", " + hold[88] 
           + ", " + hold[89] +"\n")
sleep(1)
file.write(hold[90] + ", " + mn + ", " + str(liegen.geocode(hold[90] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[90] + co + ", " + mn).longitude) + ", " + hold[91] 
           + ", " + hold[92] +"\n")
sleep(1)
file.write(hold[93] + ", " + mn + ", " + str(liegen.geocode(hold[93] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[93] + co + ", " + mn).longitude) + ", " + hold[94] 
           + ", " + hold[95] +"\n")
sleep(1)
file.write(hold[96] + ", " + mn + ", " + str(liegen.geocode(hold[96] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[96] + co + ", " + mn).longitude) + ", " + hold[97] 
           + ", " + hold[98] +"\n")
sleep(1)
file.write(hold[99] + ", " + mn + ", " + str(liegen.geocode(hold[99] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[99] + co + ", " + mn).longitude) + ", " + hold[100] 
           + ", " + hold[101] +"\n")
sleep(1)
file.write(hold[102] + ", " + mn + ", " + str(liegen.geocode(hold[102] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[102] + co + ", " + mn).longitude) + ", " + hold[103] 
           + ", " + hold[104] +"\n")
sleep(1)
file.write(hold[105] + ", " + mn + ", " + str(liegen.geocode(hold[105] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[105] + co + ", " + mn).longitude) + ", " + hold[106] 
           + ", " + hold[107] +"\n")
sleep(1)
file.write(hold[108] + ", " + mn + ", " + str(liegen.geocode(hold[108] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[108] + co + ", " + mn).longitude) + ", " + hold[109] 
           + ", " + hold[110] +"\n")
sleep(1)
file.write(hold[111] + ", " + mn + ", " + str(liegen.geocode(hold[111] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[111] + co + ", " + mn).longitude) + ", " + hold[112] 
           + ", " + hold[113] +"\n")
sleep(1)
file.write(hold[114] + ", " + mn + ", " + str(liegen.geocode(hold[114] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[114] + co + ", " + mn).longitude) + ", " + hold[115] 
           + ", " + hold[116] +"\n")
sleep(1)
file.write(hold[117] + ", " + mn + ", " + str(liegen.geocode(hold[117] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[117] + co + ", " + mn).longitude) + ", " + hold[118] 
           + ", " + hold[119] +"\n")
sleep(1)
file.write(hold[120] + ", " + mn + ", " + str(liegen.geocode(hold[120] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[120] + co + ", " + mn).longitude) + ", " + hold[121] 
           + ", " + hold[122] +"\n")
sleep(1)
file.write(hold[123] + ", " + mn + ", " + str(liegen.geocode(hold[123] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[123] + co + ", " + mn).longitude) + ", " + hold[124] 
           + ", " + hold[125] +"\n")
sleep(1)
file.write(hold[126] + ", " + mn + ", " + str(liegen.geocode(hold[126] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[126] + co + ", " + mn).longitude) + ", " + hold[127] 
           + ", " + hold[128] +"\n")
sleep(1)
file.write(hold[129] + ", " + mn + ", " + str(liegen.geocode(hold[129] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[129] + co + ", " + mn).longitude) + ", " + hold[130] 
           + ", " + hold[131] +"\n")
sleep(1)
file.write(hold[132] + ", " + mn + ", " + str(liegen.geocode(hold[132] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[132] + co + ", " + mn).longitude) + ", " + hold[133] 
           + ", " + hold[134] +"\n")
sleep(1)
file.write(hold[135] + ", " + mn + ", " + str(liegen.geocode(hold[135] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[135] + co + ", " + mn).longitude) + ", " + hold[136] 
           + ", " + hold[137] +"\n")
sleep(1)
file.write(hold[138] + ", " + mn + ", " + str(liegen.geocode(hold[138] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[138] + co + ", " + mn).longitude) + ", " + hold[139] 
           + ", " + hold[140] +"\n")
sleep(1)
file.write(hold[141] + ", " + mn + ", " + str(liegen.geocode(hold[141] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[141] + co + ", " + mn).longitude) + ", " + hold[142] 
           + ", " + hold[143] +"\n")
sleep(1)
file.write(hold[144] + ", " + mn + ", " + str(liegen.geocode(hold[144] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[144] + co + ", " + mn).longitude) + ", " + hold[145] 
           + ", " + hold[146] +"\n")
sleep(1)
file.write(hold[147] + ", " + mn + ", " + str(liegen.geocode(hold[147] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[147] + co + ", " + mn).longitude) + ", " + hold[148] 
           + ", " + hold[149] +"\n")
sleep(1)
file.write(hold[150] + ", " + mn + ", " + str(liegen.geocode(hold[150] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[150] + co + ", " + mn).longitude) + ", " + hold[151] 
           + ", " + hold[152] +"\n")
sleep(1)
file.write(hold[153] + ", " + mn + ", " + str(liegen.geocode(hold[153] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[153] + co + ", " + mn).longitude) + ", " + hold[154] 
           + ", " + hold[155] +"\n")
sleep(1)
file.write(hold[156] + ", " + mn + ", " + str(liegen.geocode(hold[156] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[156] + co + ", " + mn).longitude) + ", " + hold[157] 
           + ", " + hold[158] +"\n")
sleep(1)
file.write(hold[159] + ", " + mn + ", " + str(liegen.geocode(hold[159] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[159] + co + ", " + mn).longitude) + ", " + hold[160] 
           + ", " + hold[161] +"\n")
sleep(1)
file.write(hold[162] + ", " + mn + ", " + str(liegen.geocode(hold[162] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[162] + co + ", " + mn).longitude) + ", " + hold[163] 
           + ", " + hold[164] +"\n")
sleep(1)
file.write(hold[165] + ", " + mn + ", " + str(liegen.geocode(hold[165] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[165] + co + ", " + mn).longitude) + ", " + hold[166] 
           + ", " + hold[167] +"\n")
sleep(1)
file.write(hold[168] + ", " + mn + ", " + str(liegen.geocode(hold[168] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[168] + co + ", " + mn).longitude) + ", " + hold[169] 
           + ", " + hold[170] +"\n")
sleep(1)
file.write(hold[171] + ", " + mn + ", " + str(liegen.geocode(hold[171] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[171] + co + ", " + mn).longitude) + ", " + hold[172] 
           + ", " + hold[173] +"\n")
sleep(1)
file.write(hold[174] + ", " + mn + ", " + str(liegen.geocode(hold[174] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[174] + co + ", " + mn).longitude) + ", " + hold[175] 
           + ", " + hold[176] +"\n")
sleep(1)
file.write(hold[177] + ", " + mn + ", " + str(liegen.geocode(hold[177] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[177] + co + ", " + mn).longitude) + ", " + hold[178] 
           + ", " + hold[179] +"\n")
sleep(1)
file.write(hold[180] + ", " + mn + ", " + str(liegen.geocode(hold[180] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[180] + co + ", " + mn).longitude) + ", " + hold[181] 
           + ", " + hold[182] +"\n")
sleep(1)
file.write(hold[183] + ", " + mn + ", " + str(liegen.geocode(hold[183] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[183] + co + ", " + mn).longitude) + ", " + hold[184] 
           + ", " + hold[185] +"\n")
sleep(1)
file.write(hold[186] + ", " + mn + ", " + str(liegen.geocode(hold[186] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[186] + co + ", " + mn).longitude) + ", " + hold[187] 
           + ", " + hold[188] +"\n")
sleep(1)
file.write(hold[189] + ", " + mn + ", " + str(liegen.geocode(hold[189] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[189] + co + ", " + mn).longitude) + ", " + hold[190] 
           + ", " + hold[191] +"\n")
sleep(1)
file.write(hold[192] + ", " + mn + ", " + str(liegen.geocode(hold[192] + co + ", " + mn).latitude) 
           + ", " + str(liegen.geocode(hold[192] + co + ", " + mn).longitude) + ", " + hold[193] 
           + ", " + hold[194] +"\n")
sleep(1)

file.close()

if hold[0] == 'Anoka' and hold[192] == 'Yellow Medicine':
    print("Minnesota scraper is complete.")
else:
    print("ERROR: Must fix Minnesota scraper.")


