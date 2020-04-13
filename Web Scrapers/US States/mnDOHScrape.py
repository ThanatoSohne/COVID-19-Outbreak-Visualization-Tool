from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from geopy import Nominatim
from time import sleep
import geocoder
import addfips

mnDOH = 'https://www.health.state.mn.us/diseases/coronavirus/situation.html'

mnClient = req(mnDOH)

site_parse = soup(mnClient.read(), "lxml")
mnClient.close()

tables = site_parse.find("div", {"class": "clearfix"}).findAll("tbody")[9]

tags = tables.findAll('td')

liegen = Nominatim(user_agent = 'combiner-atomeundwolke@gmail.com')
mn = "MINNESOTA"
co = ' County'
fips = addfips.AddFIPS()

csvfile = "COVID-19_cases_mndoh.csv"
headers = "County,State,FIPS,Latitude,Longitude,Confirmed Cases,Deaths\n"

hold = []

for td in tags:
    take = td.get_text()
    hold.append(take)
    
if hold[0] == 'Anoka' and hold[207] == 'Yellow Medicine':    
    
    file = open(csvfile, "w")
    file.write(headers)
    
    file.write(hold[0] + ", " + mn + ", " + fips.get_county_fips(hold[0],state=mn) + ", "
               + str(geocoder.opencage(hold[0] + co + ", " + mn, key='').latlng).strip('[]') + ", " 
               + hold[1] + ", " + hold[2] + "\n")
    #sleep(1)
    file.write(hold[3] + ", " + mn + ", " + fips.get_county_fips(hold[3],state=mn) + ", "
               + str(geocoder.opencage(hold[3] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[4] 
               + ", " + hold[5] +"\n")
    #sleep(1)
    file.write(hold[6] + ", " + mn + "," + fips.get_county_fips(hold[6],state=mn) + ", "
               + str(geocoder.opencage(hold[6] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[7] 
               + ", " + hold[8] +"\n")
    #sleep(1)
    file.write(hold[9] + ", " + mn + ", " + fips.get_county_fips(hold[9],state=mn) + ", "
               + str(geocoder.opencage(hold[9] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[10] 
               + ", " + hold[11] +"\n")
    #sleep(1)
    file.write(hold[12] + ", " + mn + ", " + fips.get_county_fips(hold[12],state=mn) + ", "
               + str(geocoder.opencage(hold[12] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[13] 
               + ", " + hold[14] +"\n")
    #sleep(1)
    file.write(hold[15] + ", " + mn + ", " + fips.get_county_fips(hold[15],state=mn) + ", "
               + str(geocoder.opencage(hold[15] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[16] 
               + ", " + hold[17] +"\n")
    #sleep(1)
    file.write(hold[18] + ", " + mn + ", " + fips.get_county_fips(hold[18],state=mn) + ", "
               + str(geocoder.opencage(hold[18] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[19] 
               + ", " + hold[20] +"\n")
    #sleep(1)
    file.write(hold[21] + ", " + mn + ", " + fips.get_county_fips(hold[21],state=mn) + ", "
               + str(geocoder.opencage(hold[21] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[22] 
               + ", " + hold[23] +"\n")
    #sleep(1)
    file.write(hold[24] + ", " + mn + ", "  + fips.get_county_fips(hold[24],state=mn) + ", "
               + str(geocoder.opencage(hold[24] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[25] 
               + ", " + hold[26] +"\n")
    #sleep(1)
    file.write(hold[27] + ", " + mn + ", " + fips.get_county_fips(hold[27],state=mn) + ", "
               + str(geocoder.opencage(hold[27] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[28] 
               + ", " + hold[29] +"\n")
    #sleep(1)
    file.write(hold[30] + ", " + mn + ", " + fips.get_county_fips(hold[30],state=mn) + ", "
               + str(geocoder.opencage(hold[30] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[31] 
               + ", " + hold[32] +"\n")
    #sleep(1)
    file.write(hold[33] + ", " + mn + ", " + fips.get_county_fips(hold[33],state=mn) + ", "
               + str(geocoder.opencage(hold[33] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[34] 
               + ", " + hold[35] +"\n")
    #sleep(1)
    file.write(hold[36] + ", " + mn + ", "  + fips.get_county_fips(hold[36],state=mn) + ", "
               + str(geocoder.opencage(hold[36] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[37] 
               + ", " + hold[38] +"\n")
    #sleep(1)
    file.write(hold[39] + ", " + mn + ", " + fips.get_county_fips(hold[39],state=mn) + ", "
               + str(geocoder.opencage(hold[39] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[40] 
               + ", " + hold[41] +"\n")
    #sleep(1)
    file.write(hold[42] + ", " + mn + ", " + fips.get_county_fips(hold[42],state=mn) + ", "
               + str(geocoder.opencage(hold[42] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[43] 
               + ", " + hold[44] +"\n")
    #sleep(1)
    file.write(hold[45] + ", " + mn + ", "  + fips.get_county_fips(hold[45],state=mn) + ", "
               + str(geocoder.opencage(hold[45] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[46] 
               + ", " + hold[47] +"\n")
    #sleep(1)
    file.write(hold[48] + ", " + mn + ", " + fips.get_county_fips(hold[48],state=mn) + ", "
               + str(geocoder.opencage(hold[48] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[49] 
               + ", " + hold[50] +"\n")
    #sleep(1)
    file.write(hold[51] + ", " + mn + ", " + fips.get_county_fips(hold[51],state=mn) + ", "
               + str(geocoder.opencage(hold[51] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[52] 
               + ", " + hold[53] +"\n")
    #sleep(1)
    file.write(hold[54] + ", " + mn + ", "  + fips.get_county_fips(hold[54],state=mn) + ", "
               + str(geocoder.opencage(hold[54] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[55] 
               + ", " + hold[56] +"\n")
    #sleep(1)
    file.write(hold[57] + ", " + mn + ", "  + fips.get_county_fips(hold[57],state=mn) + ", "
               + str(geocoder.opencage(hold[57] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[58] 
               + ", " + hold[59] +"\n")
    #sleep(1)
    file.write(hold[60] + ", " + mn + ", " + fips.get_county_fips(hold[60],state=mn) + ", "
               + str(geocoder.opencage(hold[60] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[61] 
               + ", " + hold[62] +"\n")
    #sleep(1)
    file.write(hold[63] + ", " + mn + ", " + fips.get_county_fips(hold[63],state=mn) + ", "
               + str(geocoder.opencage(hold[63] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[64] 
               + ", " + hold[65] +"\n")
    #sleep(1)
    file.write(hold[66] + ", " + mn + ", " + fips.get_county_fips(hold[66],state=mn) + ", "
               + str(geocoder.opencage(hold[66] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[67] 
               + ", " + hold[68] +"\n")
    #sleep(1)
    file.write(hold[69] + ", " + mn + ", "  + fips.get_county_fips(hold[69],state=mn) + ", "
               + str(geocoder.opencage(hold[69] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[70] 
               + ", " + hold[71] +"\n")
    #sleep(1)
    file.write(hold[72] + ", " + mn + ", " + fips.get_county_fips(hold[72],state=mn) + ", "
               + str(geocoder.opencage(hold[72] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[73] 
               + ", " + hold[74] +"\n")
    #sleep(1)
    file.write(hold[75] + ", " + mn + ", "  + fips.get_county_fips(hold[75],state=mn) + ", "
               + str(geocoder.opencage(hold[75] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[76] 
               + ", " + hold[77] +"\n")
    #sleep(1)
    file.write(hold[78] + ", " + mn + ", " + fips.get_county_fips(hold[78],state=mn) + ", "
               + str(geocoder.opencage(hold[78] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[79] 
               + ", " + hold[80] +"\n")
    #sleep(1)
    file.write(hold[81] + ", " + mn + ", "  + fips.get_county_fips(hold[81],state=mn) + ", "
               + str(geocoder.opencage(hold[81] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[82] 
               + ", " + hold[83] +"\n")
    #sleep(1)
    file.write(hold[84] + ", " + mn + ", " + fips.get_county_fips(hold[84],state=mn) + ", "
               + str(geocoder.opencage(hold[84] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[85] 
               + ", " + hold[86] +"\n")
    #sleep(1)
    file.write(hold[87] + ", " + mn + ", " + fips.get_county_fips(hold[87],state=mn) + ", "
               + str(geocoder.opencage(hold[87] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[88] 
               + ", " + hold[89] +"\n")
    #sleep(1)
    file.write(hold[90] + ", " + mn + ", " + fips.get_county_fips(hold[90],state=mn) + ", "
               + str(geocoder.opencage(hold[90] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[91] 
               + ", " + hold[92] +"\n")
    #sleep(1)
    file.write(hold[93] + ", " + mn + ", " + fips.get_county_fips(hold[93],state=mn) + ", "
               + str(geocoder.opencage(hold[93] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[94] 
               + ", " + hold[95] +"\n")
    #sleep(1)
    file.write(hold[96] + ", " + mn + ", "  + fips.get_county_fips(hold[96],state=mn) + ", "
               + str(geocoder.opencage(hold[96] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[97] 
               + ", " + hold[98] +"\n")
    #sleep(1)
    file.write(hold[99] + ", " + mn + ", " + fips.get_county_fips(hold[99],state=mn) + ", "
               + str(geocoder.opencage(hold[99] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[100] 
               + ", " + hold[101] +"\n")
    #sleep(1)
    file.write(hold[102] + ", " + mn + ", " + fips.get_county_fips(hold[102],state=mn) + ", "
               + str(geocoder.opencage(hold[102] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[103] 
               + ", " + hold[104] +"\n")
    #sleep(1)
    file.write(hold[105] + ", " + mn + ", " + fips.get_county_fips(hold[105],state=mn) + ", "
               + str(geocoder.opencage(hold[105] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[106] 
               + ", " + hold[107] +"\n")
    #sleep(1)
    file.write(hold[108] + ", " + mn + ", " + fips.get_county_fips(hold[108],state=mn) + ", "
               + str(geocoder.opencage(hold[108] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[109] 
               + ", " + hold[110] +"\n")
    #sleep(1)
    file.write(hold[111] + ", " + mn + ", "  + fips.get_county_fips(hold[111],state=mn) + ", "
               + str(geocoder.opencage(hold[111] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[112] 
               + ", " + hold[113] +"\n")
    #sleep(1)
    file.write(hold[114] + ", " + mn + ", "  + fips.get_county_fips(hold[114],state=mn) + ", "
               + str(geocoder.opencage(hold[114] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[115] 
               + ", " + hold[116] +"\n")
    #sleep(1)
    file.write(hold[117] + ", " + mn + ", "  + fips.get_county_fips(hold[117],state=mn) + ", "
               + str(geocoder.opencage(hold[117] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[118] 
               + ", " + hold[119] +"\n")
    #sleep(1)
    file.write(hold[120] + ", " + mn + ", " + fips.get_county_fips(hold[120],state=mn) + ", "
               + str(geocoder.opencage(hold[120] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[121] 
               + ", " + hold[122] +"\n")
    #sleep(1)
    file.write(hold[123] + ", " + mn + ", " + fips.get_county_fips(hold[123],state=mn) + ", "
               + str(geocoder.opencage(hold[123] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[124] 
               + ", " + hold[125] +"\n")
    #sleep(1)
    file.write(hold[126] + ", " + mn + ", "  + fips.get_county_fips(hold[126],state=mn) + ", "
               + str(geocoder.opencage(hold[126] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[127] 
               + ", " + hold[128] +"\n")
    #sleep(1)
    file.write(hold[129] + ", " + mn + ", " + fips.get_county_fips(hold[129],state=mn) + ", "
               + str(geocoder.opencage(hold[129] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[130] 
               + ", " + hold[131] +"\n")
    #sleep(1)
    file.write(hold[132] + ", " + mn + ", "  + fips.get_county_fips(hold[132],state=mn) + ", "
               + str(geocoder.opencage(hold[132] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[133] 
               + ", " + hold[134] +"\n")
    #sleep(1)
    file.write(hold[135] + ", " + mn + ", " + fips.get_county_fips(hold[135],state=mn) + ", "
               + str(geocoder.opencage(hold[135] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[136] 
               + ", " + hold[137] +"\n")
    #sleep(1)
    file.write(hold[138] + ", " + mn + ", "  + fips.get_county_fips(hold[138],state=mn) + ", "
               + str(geocoder.opencage(hold[138] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[139] 
               + ", " + hold[140] +"\n")
    #sleep(1)
    file.write(hold[141] + ", " + mn + ", "  + fips.get_county_fips(hold[141],state=mn) + ", "
               + str(geocoder.opencage(hold[141] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[142] 
               + ", " + hold[143] +"\n")
    #sleep(1)
    file.write(hold[144] + ", " + mn + ", "  + fips.get_county_fips(hold[144],state=mn) + ", "
               + str(geocoder.opencage(hold[144] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[145] 
               + ", " + hold[146] +"\n")
    #sleep(1)
    file.write(hold[147] + ", " + mn + ", "  + fips.get_county_fips(hold[147],state=mn) + ", "
               + str(geocoder.opencage(hold[147] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[148] 
               + ", " + hold[149] +"\n")
    #sleep(1)
    file.write(hold[150] + ", " + mn + ", "  + fips.get_county_fips(hold[150],state=mn) + ", "
               + str(geocoder.opencage(hold[150] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[151] 
               + ", " + hold[152] +"\n")
    #sleep(1)
    file.write(hold[153] + ", " + mn + ", "  + fips.get_county_fips(hold[153],state=mn) + ", "
               + str(geocoder.opencage(hold[153] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[154] 
               + ", " + hold[155] +"\n")
    #sleep(1)
    file.write(hold[156] + ", " + mn + ", " + fips.get_county_fips(hold[156],state=mn) + ", "
               + str(geocoder.opencage(hold[156] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[157] 
               + ", " + hold[158] +"\n")
    #sleep(1)
    file.write(hold[159] + ", " + mn + ", "  + fips.get_county_fips(hold[159],state=mn) + ", "
               + str(geocoder.opencage(hold[159] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[160] 
               + ", " + hold[161] +"\n")
    #sleep(1)
    file.write(hold[162] + ", " + mn + ", "  + fips.get_county_fips(hold[162],state=mn) + ", "
               + str(geocoder.opencage(hold[162] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[163] 
               + ", " + hold[164] +"\n")
    #sleep(1)
    file.write(hold[165] + ", " + mn + ", "  + fips.get_county_fips(hold[165],state=mn) + ", "
               + str(geocoder.opencage(hold[165] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[166] 
               + ", " + hold[167] +"\n")
    #sleep(1)
    file.write(hold[168] + ", " + mn + ", " + fips.get_county_fips(hold[168],state=mn) + ", "
               + str(geocoder.opencage(hold[168] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[169] 
               + ", " + hold[170] +"\n")
    #sleep(1)
    file.write(hold[171] + ", " + mn + ", " + fips.get_county_fips(hold[171],state=mn) + ", "
               + str(geocoder.opencage(hold[171] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[172] 
               + ", " + hold[173] +"\n")
    #sleep(1)
    file.write(hold[174] + ", " + mn + ", " + fips.get_county_fips(hold[174],state=mn) + ", "
               + str(geocoder.opencage(hold[174] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[175] 
               + ", " + hold[176] +"\n")
    #sleep(1)
    file.write(hold[177] + ", " + mn + ", " + fips.get_county_fips(hold[177],state=mn) + ", "
               + str(geocoder.opencage(hold[177] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[178] 
               + ", " + hold[179] +"\n")
    #sleep(1)
    file.write(hold[180] + ", " + mn + ", " + fips.get_county_fips(hold[180],state=mn) + ", "
               + str(geocoder.opencage(hold[180] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[181] 
               + ", " + hold[182] +"\n")
    #sleep(1)
    file.write(hold[183] + ", " + mn + ", "  + fips.get_county_fips(hold[183],state=mn) + ", "
               + str(geocoder.opencage(hold[183] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[184] 
               + ", " + hold[185] +"\n")
    #sleep(1)
    file.write(hold[186] + ", " + mn + ", "  + fips.get_county_fips(hold[186],state=mn) + ", "
               + str(geocoder.opencage(hold[186] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[187] 
               + ", " + hold[188] +"\n")
    #sleep(1)
    file.write(hold[189] + ", " + mn + ", " + fips.get_county_fips(hold[189],state=mn) + ", "
               + str(geocoder.opencage(hold[189] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[190] 
               + ", " + hold[191] +"\n")
    #sleep(1)
    file.write(hold[192] + ", " + mn + ", "  + fips.get_county_fips(hold[192],state=mn) + ", "
               + str(geocoder.opencage(hold[192] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[193] 
               + ", " + hold[194] +"\n")
    #sleep(1)
    file.write(hold[195] + ", " + mn + ", "  + fips.get_county_fips(hold[195],state=mn) + ", "
               + str(geocoder.opencage(hold[195] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[196] 
               + ", " + hold[197] +"\n")
    file.write(hold[198] + ", " + mn + ", "  + fips.get_county_fips(hold[198],state=mn) + ", "
               + str(geocoder.opencage(hold[198] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[199] 
               + ", " + hold[200] +"\n")
    file.write(hold[201] + ", " + mn + ", "  + fips.get_county_fips(hold[201],state=mn) + ", "
               + str(geocoder.opencage(hold[201] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[202] 
               + ", " + hold[203] +"\n")
    file.write(hold[204] + ", " + mn + ", "  + fips.get_county_fips(hold[204],state=mn) + ", "
               + str(geocoder.opencage(hold[204] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[205] 
               + ", " + hold[206] +"\n")
    file.write(hold[207] + ", " + mn + ", "  + fips.get_state_fips(mn) + ", "
               + str(geocoder.opencage(hold[207] + co + ", " + mn, key='').latlng).strip('[]') + ", " + hold[208] 
               + ", " + hold[209] +"\n")
    
    file.close()

    print("Minnesota scraper is complete.")
else:
    print("ERROR: Must fix Minnesota scraper.")

