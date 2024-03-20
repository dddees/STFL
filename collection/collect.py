import urllib.request
import re

start=1420066800000
end=1420153200000
url="https://www.pse.pl/dane-systemowe/funkcjonowanie-kse/raporty-dobowe-z-pracy-kse/zapotrzebowanie-mocy-kse?p_p_id=danekse_WAR_danekserbportlet&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=1&_danekse_WAR_danekserbportlet_type=kse&_danekse_WAR_danekserbportlet_target=csv&_danekse_WAR_danekserbportlet_from={start}&_danekse_WAR_danekserbportlet_to={end}"

period=365*10
for i in range (0,period):
	try:
		
		url_mod=url.format(start=start,end=end)
		response=urllib.request.urlopen(url_mod)
		text = str(response.read())
		response.close()
		
		
		x=re.sub("b'Data;Godz.;Dobowa prognoza zapotrzebowania KSE;Rzeczywiste zapotrzebowanie KSE",'',text)
		x=re.sub("'",'',x)

		x=x.split('\\n')
		with open ('demandd.csv','a') as f:
			for line in x:
				f.write(line+'\n')
		print(i/period)
		start=start+3600*24*1000
		end=start+3600*24*1000

	except Exception as e:	
		print('error on step',i,e)
