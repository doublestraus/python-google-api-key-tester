#!/usr/bin/python3

import argparse
import json
import requests
import sys

def AbusiveexperiencereportAPI( api_key ):
    site = 'abusiveexperiencereport.googleapis.com' 
    url = 'https://abusiveexperiencereport.googleapis.com/v1/violatingSites?key=' + api_key
    response = requests.get( url )
    response_code = response.status_code
    # We try to get reason
    if response_code == 200:
        print( site + " " + str( response_code ) )
        return
    if response_code == 400:
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['details'][0]['reason']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None
    elif response_code == 403:
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['details'][1]['reason']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['status']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None

def AcceleratedmobilepageurlAPI( api_key ):
    site = "acceleratedmobilepageurl.googleapis.com"
    url = 'https://acceleratedmobilepageurl.googleapis.com/v1/ampUrls:batchGet?alt=json&key=' + api_key
    response = requests.post( url )
    response_code = response.status_code
    # We try to get reason
    if response_code == 200:
        print( site + " " + str( response_code ) )
        return
    if response_code == 400:
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['details'][0]['reason']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None
    elif response_code == 403:
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['details'][1]['reason']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['status']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None

def AdexperiencereportAPI( api_key ):
    site = 'adexperiencereport.googleapis.com' 
    url = 'https://adexperiencereport.googleapis.com/v1/violatingSites?key=' + api_key
    response = requests.get( url )
    response_code = response.status_code
    # We try to get reason
    if response_code == 200:
        print( site + " " + str( response_code ) )
        return
    if response_code == 400:
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['details'][0]['reason']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None
    elif response_code == 403:
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['details'][1]['reason']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['status']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None

def ApikeysAPI( api_key ):
    site = 'apikeys.googleapis.com' 
    url = 'https://apikeys.googleapis.com/v2/keys:lookupKey?key=' + api_key
    response = requests.get( url )
    response_code = response.status_code
    # We try to get reason
    if response_code == 200:
        print( site + " " + str( response_code ) )
        return
    if response_code == 400:
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['details'][0]['reason']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None
    elif response_code == 403:
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['details'][1]['reason']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['status']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None

def ChromeuxreportAPI( api_key ):
    site = "chromeuxreport.googleapis.com"
    url = 'https://chromeuxreport.googleapis.com/v1/records:queryRecord?alt=json&key=' + api_key
    response = requests.post( url )
    response_code = response.status_code
    # We try to get reason
    if response_code == 200:
        print( site + " " + str( response_code ) )
        return
    if response_code == 400:
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['details'][0]['reason']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None
    elif response_code == 403:
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['details'][1]['reason']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['status']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None

def CloudbuildAPI( api_key ):
    site = "cloudbuild.googleapis.com"
    url = 'https://cloudbuild.googleapis.com/v1/webhook?key=' + api_key
    response = requests.post( url )
    response_code = response.status_code
    # We try to get reason
    if response_code == 200:
        print( site + " " + str( response_code ) )
        return
    if response_code == 400:
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['details'][0]['reason']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None
    elif response_code == 403:
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['details'][0]['reason']
            print( site + " " + str( response_code ) + " " + reason )
            return 
        except:
            None
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['details'][1]['reason']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['status']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None

def DlpAPI( api_key ):
    site = 'dlp.googleapis.com' 
    url = 'https://dlp.googleapis.com/v2/infoTypes?key=' + api_key
    response = requests.get( url )
    response_code = response.status_code
    # We try to get reason
    if response_code == 200:
        print( site + " " + str( response_code ) )
        return
    if response_code == 400:
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['details'][0]['reason']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None
    elif response_code == 403:
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['details'][1]['reason']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['status']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None

def LanguageAPI( api_key ):
    site = "language.googleapis.com"
    url = 'https://language.googleapis.com/v1beta2/documents:analyzeEntities?key=' + api_key
    response = requests.post( url )
    response_code = response.status_code
    # We try to get reason
    if response_code == 200:
        print( site + " " + str( response_code ) )
        return
    if response_code == 400:
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['details'][0]['reason']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None
    elif response_code == 403:
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['details'][1]['reason']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['status']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None

def SpeechAPI( api_key ):
    site = 'speech.googleapis.com' 
    url = 'https://speech.googleapis.com/v1p1beta1/operations?key=' + api_key
    response = requests.get( url )
    response_code = response.status_code
    # We try to get reason
    if response_code == 200:
        print( site + " " + str( response_code ) )
        return
    if response_code == 400:
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['details'][0]['reason']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None
    elif response_code == 403:
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['details'][1]['reason']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['status']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None

def TexttospeechAPI( api_key ):
    site = 'texttospeech.googleapis.com' 
    url = 'https://texttospeech.googleapis.com/v1beta1/voices?key=' + api_key
    response = requests.get( url )
    response_code = response.status_code
    # We try to get reason
    if response_code == 200:
        print( site + " " + str( response_code ) )
        return
    if response_code == 400:
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['details'][0]['reason']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None
    elif response_code == 403:
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['details'][1]['reason']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['status']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None

def VideointelligenceAPI( api_key ):
    site = "videointelligence.googleapis.com"
    url = 'https://videointelligence.googleapis.com/v1/videos:annotate?key=' + api_key
    response = requests.post( url )
    response_code = response.status_code
    # We try to get reason
    if response_code == 200:
        print( site + " " + str( response_code ) )
        return
    if response_code == 400:
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['details'][0]['reason']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None
    elif response_code == 403:
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['details'][1]['reason']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['status']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None

def VisionAPI( api_key ):
    site = "vision.googleapis.com"
    url = 'https://vision.googleapis.com/v1/files:annotate?key=' + api_key
    response = requests.post( url )
    response_code = response.status_code
    # We try to get reason
    if response_code == 200:
        print( site + " " + str( response_code ) )
        return
    if response_code == 400:
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['details'][0]['reason']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None
    elif response_code == 403:
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['details'][1]['reason']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['status']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None

def DomainsrdapAPI( api_key ):
    site = 'domainsrdap.googleapis.com' 
    url = 'https://domainsrdap.googleapis.com/v1/ip?key=' + api_key
    response = requests.get( url )
    response_code = response.status_code
    # We try to get reason
    if response_code == 200:
        print( site + " " + str( response_code ) )
        return
    if response_code == 400:
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['details'][0]['reason']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None
    elif response_code == 403:
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['details'][1]['reason']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['status']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None

def HomegraphAPI( api_key ):
    site = "homegrapgh.googleapis.com"
    url = 'https://homegraph.googleapis.com/v1/devices:query?key=' + api_key
    response = requests.post( url )
    response_code = response.status_code
    # We try to get reason
    if response_code == 200:
        print( site + " " + str( response_code ) )
        return
    if response_code == 400:
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['details'][0]['reason']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None
    elif response_code == 403:
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['details'][1]['reason']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['status']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None

def KgsearchAPI( api_key ):
    site = 'kgsearch.googleapis.com' 
    url = 'https://kgsearch.googleapis.com/v1/entities:search?key=' + api_key
    response = requests.get( url )
    response_code = response.status_code
    # We try to get reason
    if response_code == 200:
        print( site + " " + str( response_code ) )
        return
    if response_code == 400:
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['details'][0]['reason']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None
    elif response_code == 403:
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['details'][1]['reason']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['status']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None

def SafebrowsingAPI( api_key ):
    site = 'safebrowsing.googleapis.com' 
    url = 'https://safebrowsing.googleapis.com/v4/threatLists?key=' + api_key
    response = requests.get( url )
    response_code = response.status_code
    # We try to get reason
    if response_code == 200:
        print( site + " " + str( response_code ) )
        return
    if response_code == 400:
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['details'][0]['reason']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None
    elif response_code == 403:
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['details'][1]['reason']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['status']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None

def SearchconsoleAPI( api_key ):
    site = "searchconsole.googleapis.com"
    url = 'https://searchconsole.googleapis.com/v1/urlTestingTools/mobileFriendlyTest:run?key=' + api_key
    response = requests.post( url )
    response_code = response.status_code
    # We try to get reason
    if response_code == 200:
        print( site + " " + str( response_code ) )
        return
    if response_code == 400:
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['details'][0]['reason']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None
    elif response_code == 403:
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['details'][1]['reason']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['status']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None

def StoragetransferAPI( api_key ):
    site = 'storagetransfer.googleapis.com' 
    url = 'https://storagetransfer.googleapis.com/v1/transferJobs?key=' + api_key
    response = requests.get( url )
    response_code = response.status_code
    # We try to get reason
    if response_code == 200:
        print( site + " " + str( response_code ) )
        return
    if response_code == 400:
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['details'][0]['reason']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None
    elif response_code == 403:
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['details'][1]['reason']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['status']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None

def WebfontsAPI( api_key ):
    site = 'www.googleapis.com/webfonts' 
    url = 'https://www.googleapis.com/webfonts/v1/webfonts?key=' + api_key
    response = requests.get( url )
    response_code = response.status_code
    # We try to get reason
    if response_code == 200:
        print( site + " " + str( response_code ) )
        return
    if response_code == 400:
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['details'][0]['reason']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None
    elif response_code == 403:
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['details'][1]['reason']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['status']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None

def WebriskAPI( api_key ):
    site = "webrisk.googleapis.com"
    url = 'https://webrisk.googleapis.com/v1eap1:evaluateUri?key=' + api_key
    response = requests.post( url )
    response_code = response.status_code
    # We try to get reason
    if response_code == 200:
        print( site + " " + str( response_code ) )
        return
    if response_code == 400:
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['details'][0]['reason']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None
    elif response_code == 403:
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['details'][1]['reason']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['status']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None

def GeolocationAPI( api_key ):
    site = "www.googleapis.com/geolocation"
    url = 'https://www.googleapis.com/geolocation/v1/geolocate?key=' + api_key
    response = requests.post( url )
    response_code = response.status_code
    # We try to get reason
    if response_code == 200:
        print( site + " " + str( response_code ) )
        return
    if response_code == 400:
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['details'][0]['reason']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None
    elif response_code == 403:
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['details'][1]['reason']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['status']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None
    elif response_code == 404:
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['status']
            print( site + " " + str( response_code ) + " " + reason + " (may be interesting)" )
            return
        except:
            None

def MapsAPI( api_key ):
    site = 'maps.googleapis.com' 
    url = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins=40.6655101%2C-73.89188969999998&destinations=40.659569%2C-73.933783%7C40.729029%2C-73.851524%7C40.6860072%2C-73.6334271%7C40.598566%2C-73.7527626&key=' + api_key
    response = requests.get( url )
    response_code = response.status_code
    # We try to get reason
    if response_code == 200:
        try:
            response_json = json.loads( response.content )
            status = response_json['status']
            msg = response_json['error_message']
            print( site + " " + str( response_code ) + " " + status + " `" + msg + "`")
            return
        except:
            None
    if response_code == 400:
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['details'][0]['reason']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None
    elif response_code == 403:
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['details'][1]['reason']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None
        try:
            response_json = json.loads( response.content )
            reason = response_json['error']['status']
            print( site + " " + str( response_code ) + " " + reason )
            return
        except:
            None

def ProcessApiKey( api_key ):
    print( 'API key: ' + api_key )
    # Call API functions
    AbusiveexperiencereportAPI( api_key )
    AcceleratedmobilepageurlAPI( api_key )
    AdexperiencereportAPI( api_key )
    ApikeysAPI( api_key )
    ChromeuxreportAPI( api_key )
    CloudbuildAPI( api_key )
    DlpAPI( api_key )
    LanguageAPI( api_key ) 
    SpeechAPI( api_key )
    TexttospeechAPI( api_key )
    VideointelligenceAPI( api_key )
    VisionAPI( api_key )
    DomainsrdapAPI( api_key )
    HomegraphAPI( api_key )
    KgsearchAPI( api_key )
    SafebrowsingAPI( api_key )
    SearchconsoleAPI( api_key )
    StoragetransferAPI( api_key )
    WebfontsAPI( api_key )
    WebriskAPI( api_key )
    GeolocationAPI( api_key )
    MapsAPI( api_key )

# Define parser
parser = argparse.ArgumentParser( description = 'GOOGLE API key tester' )
parser.add_argument( '-k', '--key', action = 'store', help = 'Specify API key to test' )
api_key = parser.parse_args( ).key

try:
    assert( api_key != None )
except:
    sys.exit( 'Enter -h or --help to see options' )

ProcessApiKey( api_key )
