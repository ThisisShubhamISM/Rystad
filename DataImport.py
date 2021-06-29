import requests
dls = "https://www.eia.gov/dnav/pet/xls/PET_PNP_INPT_A_EPC0_YIR_MBBLPD_M.xls"
resp = requests.get(dls)
output = open('test.xls', 'wb')
output.write(resp.content)
output.close()



