def get_headers():
    headers = {
        'authority': 'api2.realtor.ca',
        'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
        'accept': '*/*',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
        'sec-ch-ua-platform': '"Linux"',
        'origin': 'https://www.realtor.ca',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.realtor.ca/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cookie': 'visid_incap_2269415=FMo6C9O/QEKQwoLjDYC+UiwHYmEAAAAAQUIPAAAAAAA0bAWaghrJjcdZjNJtuCaG; nlbi_2269415=n7yseQgPb3UbqzCtkG5lugAAAAAlbM7vXjXDp7mmcXv3aiNz; incap_ses_677_2269415=MYkFMBO+qyXVZn36HDBlCS0HYmEAAAAAS5HbldD+aAM1rzc9f+d6ig==; _gid=GA1.2.941576838.1633814320; _fbp=fb.1.1633814319858.1393045798; gig_bootstrap_3_mrQiIl6ov44s2X3j6NGWVZ9SDDtplqV7WgdcyEpGYnYxl7ygDWPQHqQqtpSiUfko=gigya-pr_ver4; ASP.NET_SessionId=0s022tvey40byp350v0e3etq; visid_incap_2271082=RyOgGeq3RVen6ArI92pdpVYIYmEAAAAAQUIPAAAAAABiZOCyev48hty+wRcG/hNG; nlbi_2271082=I+0wMG3m5mSNknHVcbDG1QAAAAAZGiA1wGlAgDTGr+pp/KPF; incap_ses_677_2271082=esqNdtC2tB/jln36HDBlCVYIYmEAAAAA1VmJdVggACw4VucbxySc6A==; nlbi_2269415_2147483646=EOHZclWCoCNFI/WfkG5lugAAAACYWLkAGZHSv7B7jP4oDaKg; _ga=GA1.2.712508816.1633814319; reese84=3:pZdIGtngzi2dsB6Nf7uueA==:jOA8ak4O7XxlJmrgl4chAmbptCEptWfvLj/zjUQwzvdjkoHb7VmyPFJCVZNZGkC2wLdSlcAI71Xe9YctmK1osoDJSzn+v7pDa/D6TMKVPam67BvKVyNxS9+Ttzxs0S+u7+ghgXF/AeJYKOp7pmJop77FFMG7F6Y2Z0QQlCZMKHsjroH9IhtcqtA3KsiiptY7hpPX6Cenm+8LIEdfMkkJ/sBsrRROW7rUBvkKoSHbVkUZ69ikgup9gf1TP4QyAAnIOzgL0m9Q+gnW7y4leCmTIKHL1ulHP9rpFJBX5IuzWf6C9YkdVj4UPIssto7f+6f7ZStVPWPiBnOxjUrJt3Ewv1/+ymv+2ZoYjHWNvCqvJTs+1H8jTLtskRiyhEbJK9VZGXldROJ6N3RrhLnDyzamV++L1zHRbsIFqsmrYxxpcXSsoFZqiZRsIk+Wd/9mQRey:RpyWe5SeNV9aGmeqeHo5V27dkGdHihdPvFcsgu8GpeI=; _4c_=fVNba9swFP4rRaN5qh1Llm%2BBPLQOlEA2ytrtYS9Bto5j0cQyshw3G%2F3vO%2FKcZKwwg4XOd75zP%2FpFhhoasqBxGKaUpyFPMnpHXuHUkcUvUrbuPLqjN3uyILW1bbeYz4dh8A2IvdXGL8X8INpPP7Q%2BbOAI%2ByWlsxwaC2bJM59FScyjW5Z7lIU%2B%2FlEazDbCKttL%2BCzeHCdMswBB3ewuKLKZn7Asjq5k1TgyZVHG%2FyIjOrqOaBLR2bM2dhl7q9nTI%2Bi17Ja7MNiWrGDNENYzxL6IAyy%2Fi6bU%2FREM5nXLgod89mR0C8aeXk4tPBrdt%2BvVkl7QZxCmrJ1uLRF%2BMaLpRGmVbiaMzfLeGGjK0zK%2FX5E7UmoJ2C%2Ba%2BZkfoGx%2FouRx5u7QYEdJayTeH%2B%2B339YrFBOsK0hTGvvTLEKaob41Wval3VqMg6wBiptOvqJCwlGVsB2UtPUYaHQ9oTWoXW0dHKQj3Bon4DBQGFQj9XC15El6RS%2BWSeTCb0Sz68VuLMWJercDebPGjSGV2HeAGPboqJrSUR6Msqqrb3K97w%2BFEqjNdd9Yc0JlLhohHfQVOiVxP5TYa5PrwwGMKoXbLnPVIK8weujAJZ7XRh%2FgJgsR1biYZKOa%2Fg0FAxVg280%2Fm3nSve0L8Et9mCOrUxZG7%2Bd9nTDc8ivsjXDrJuPC7DWm5KzwdSAbxmFf2eT9jrz9eTZZQAMWRDTEIVusIo154D5kGCWn90Oqime45dwLBQePyyTwBBTSYzwTVRBnQpQlmXxyGmUBjj%2FhFJ0c1dkHryoZVlHqVUkYezxD84Jz5iVJFUdRULCkEOSSV%2BocZRh1youm57Ta%2FeSRXsksTTBgHJzJ%2FFJEe5zY4YeS2ceSJXSvVrdTm%2F5j%2B6Fd7%2B%2B%2FAQ%3D%3D; _ga_Y07J3B53QP=GS1.1.1633814319.1.1.1633814883.3',
    }
    return headers

def get_data():
    data = {
      'ZoomLevel': '11',
      'LatitudeMax': '49.38900',
      'LongitudeMax': '-122.72965',
      'LatitudeMin': '49.12594',
      'LongitudeMin': '-123.51751',
      'Sort': '6-D',
      'PropertyTypeGroupID': '1',
      'PropertySearchTypeId': '1',
      'TransactionTypeId': '2',
      'Currency': 'CAD',
      'RecordsPerPage': '12',
      'ApplicationId': '1',
      'CultureId': '1',
      'Version': '7.0',
      'CurrentPage': None,
    }
    return data