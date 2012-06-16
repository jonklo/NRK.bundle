# -*- coding: utf-8 -*-

LIVE_TV_STATIONS = (
    {
        'title': 'NRK 1', 
        #'url': 'http://nrk1-i.akamaihd.net/hls/live/201543/nrk1/master.m3u8',
        'url': 'http://nrk1-i.akamaihd.net/hls/live/201543/nrk1/master_Layer3.m3u8',
        'desc': u'Bredt og variert programtilbud. Norges største tv-kanal.', 
        'img': 'nrk1.png'
    },
    {
        'title': 'NRK 2', 
        #'url': 'http://nrk2-i.akamaihd.net/hls/live/201544/nrk2/master.m3u8',
        'url': 'http://nrk2-i.akamaihd.net/hls/live/201544/nrk2/master_Layer3.m3u8',
        'desc': u'Fordypningskanalen. Bakgrunns-, dokumentar og nyhetskanal.', 
        'img': 'nrk2.png'
    }, 
    {
        'title': 'NRK Super / NRK 3', 
        #'url': 'http://nrk3-i.akamaihd.net/hls/live/201545/nrk3/master.m3u8',
        'url': 'http://nrk3-i.akamaihd.net/hls/live/201545/nrk3/master_Layer3.m3u8',
        'desc': u'Den tredje kanalen tilbyr vekselsvis et barnetilbud og et tilbud for unge voksne med serier, humor film.', 
        'img': 'nrk3.png'
    }
)


def LiveTVMenu(sender):
    """
    Show the live TV menu.
    """
    dir = MediaContainer(viewGroup='Details', title2=sender.itemTitle)
    
    for station in LIVE_TV_STATIONS:
        url = station['url']
        Log('Added %s' % url)
        
        dir.Append(VideoItem(url, title=station['title'], summary=station['desc'], thumb=R('nrk-nett-tv.png'))) 
    
    return dir
