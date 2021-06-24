# coding=utf-8
import requests
import urllib3
import json
import datetime

def test():
    url = "http://www.ceair.com/otabooking/flight-search!doFlightSearch.shtml"
    cookies = {
		"_ga":"GA1.2.1499015740.1598351258",
		# "_gat_UA-80008755-11":"1",
		# "_gat":"1",
		"_gid":"GA1.2.938159633.1598953018",
		"84bb15efa4e13721_gr_session_id_51eaa57b-7e78-4a38-9eee-5c86906565db":"true",
		"84bb15efa4e13721_gr_session_id":"51eaa57b-7e78-4a38-9eee-5c86906565db",
		"ecrmWebtrends":"116.228.213.70.1598351257696",
		"gr_user_id":"8e737683-09fe-4ca3-a9b1-0712c65c2ef8",
		"grwng_uid":"d1e07a55-3424-4de7-8681-a58c78c77de7",
		"JSESSIONID":"RCPU-MCKBTnv+skPDuocjihC.laputaServer2",
		"language":"zh_CN",
		"td_cookie":"1402754587",
        "user_cookie": "true",
        "Webtrends": "4fe5d36e.5adb126dd18dd"
	}
    headers = {
		"Connection":"keep-alive",
        "Content-Length":"440",
        "Accept":"application/json, text/javascript, */*; q=0.01",
        "X-Requested-With":"XMLHttpRequest",
        "xmvrc":"4de948be",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
        "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
        "Origin":"http://www.ceair.com",
        "Referer":"http://www.ceair.com/booking/syx-sha-200927_CNY.html?seriesid=bd7a7610ec3611eab5654b70b6c88a75",
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language":"zh-CN,zh;q=0.9"
	}

    form_data = {
        'searchCond':'{"adtCount":1,"chdCount":0,"infCount":0,"currency":"CNY","tripType":"OW","recommend":false,"reselect":"","page":"0","sortType":"a","sortExec":"a","seriesid":"bd7a7610ec3611eab5654b70b6c88a75","segmentList":[{"deptCd":"SYX","arrCd":"SHA","deptDt":"2020-09-27","deptAirport":"","arrAirport":"","deptCdTxt":"三亚","arrCdTxt":"上海","deptCityCode":"SYX","arrCityCode":"SHA"}],"version":"A.1.0"}',
        '_':'bd7a7610ec3611eab5654b70b6c88a75'
    }

    print(form_data)
    urllib3.disable_warnings()
    res_post = requests.post(url, cookies=cookies, data=form_data, headers=headers, verify=False).json()
    print(json.dumps(res_post, indent=4, ensure_ascii=False))

test()

# while True:
#     time_now = datetime.datetime.now().strftime('%Y_%m_%d_%H:%M:%S.%f') # 刷新
#     if time_now >= "2020_08_28_20:00:00.000000": #此处设置每天定时的时间
#         test()
#         print(time_now)
#     # time.sleep(0.1) # 因为以秒定时，所以暂停2秒，使之不会在1秒内执行多次