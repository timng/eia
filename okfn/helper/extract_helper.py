import urllib2
import re

# Extract text from hxs node, by xpath query and idx (th) result
def extract_text(hxs, xpaths, idx = 0):

    if isinstance(xpaths, list) == False:
        xpaths = [xpaths]

    for xpath in xpaths:
        
        # exec query
        els = hxs.xpath(xpath)

        if len(els) > idx and len(els) > 0:
            # check if xpath query on attribute of node
            # //a/@href
            end = xpath.split('/')[-1]
            if len(end) > 0 and ( end[0] == '@' or 'text()' in end ):
                return els[idx].extract().strip()
            else:
                # get all text of nodes in side els[idx]
                return '  '.join( els[idx].xpath('.//text()').extract() ).strip()
    return ''


def getwebcontent(url):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }

    req = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(req)
    return response.read()

def extract_text_re(pattern, text, group = 1 ):
    match = re.search( pattern, text)

    if match != None:
        return match.group(group)
    else:
        return ''