# -*- coding: utf-8 -*-
from live_radio import LiveRadioMenu
from live_tv import LiveTVMenu
from podcasts import *
from web_tv import *

NRK_PREFIX = '/video/nrk'

ART = 'art-default.jpg'
ICON = 'icon-default.png'


def Start():
    """
    Initiates the plugin.
    """
    Plugin.AddPrefixHandler(NRK_PREFIX, MainMenu, L('title'), ICON, ART)
    
    Plugin.AddViewGroup("Details", viewMode="InfoList", mediaType="items")
    
    MediaContainer.content = 'Items'
    
    # Set defaults
    MediaContainer.art = R(ART)
    MediaContainer.title1 = L('title')
    DirectoryItem.thumb = R(ICON)



def MainMenu():
    """
    Sets up the main menu. All the menu functions are in separate files.
    """
    dir = MediaContainer(viewGroup="Details")
    
    dir.Append(Function(DirectoryItem(
                            WebTVMenu, 
                            title=L('webtv_title'), 
                            summary=L('webtv_description'), 
                            thumb=R('nrk-nett-tv.png'))))
    
    dir.Append(Function(DirectoryItem(
                            LiveTVMenu, 
                            title=L('livetv_title'), 
                            summary=L('livetv_description'), 
                            thumb=R('nrk-nett-tv.png'))))
    
    dir.Append(Function(DirectoryItem(
                            LiveRadioMenu, 
                            title=L('liveradio_title'), 
                            summary=L('liveradio_description'), 
                            thumb=R('nrk-nettradio.png'))))
    
    dir.Append(Function(DirectoryItem(
                            PodcastVideoMenu, 
                            title=L('podcast_video_title'), 
                            summary=L('podcast_video_description'), 
                            thumb=R('nrk-no.png'))))
    
    dir.Append(Function(DirectoryItem(
                            PodcastAudioMenu, 
                            title=L('podcast_audio_title'), 
                            summary=L('podcast_audio_description'), 
                            thumb=R('nrk-no.png'))))
    
    return dir
