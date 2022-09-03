
__all__ = ["ModList", "NexusLink", "ManualNexusLink"]

def NexusLink(game:str, modID:int):
    return str(f'nexusmods.com/{game}/mods/{modID}')

def ManualNexusLink(game:str, modID:int, fileID:int):
    return str(f'nexusmods.com/{game}/mods/{modID}?tab=files&file_id={fileID}')

class ModList:
    
    def __init__(self, URL:str, DESC:str, text:str|bool, version:int, author:str, filename:str, link, title:str, subtitle:str):
        self.ModPage            = URL
        self.DESC               = DESC
        self.Text               = text
        self.Version            = version
        self.Author             = author
        self.FileName           = filename
        self.ManualLink         = link
        self.Title              = title
        self.Subtitle           = subtitle
    
    @property
    def ModPage(self):
        return self.ModPage
    
    @property
    def DESC(self):
        return self.DESC
    
    @property
    def Text(self):
        return self.Text
    
    @property
    def Title(self):
        return self.Title
    
    @property
    def Subtitle(self):
        return self.Subtitle
    
    @property
    def Author(self):
        return self.Author
    
    @property
    def Version(self):
        return self.Version
    
    @property
    def FileName(self):
        return self.FileName
    
    @property
    def ManualLink(self):
        return self.ManualLink
    


Generator = ModList

def ParseMod(game:str, modID:int, fileID:int, note:list):
    Generator.DESC          = None
    Generator.ManualLink    = None
    
    # details = {
    #     game    : "witcher3",
    #     modID   : 3652,
    #     fileID  : 24139
    # }
    
    # Define all properties, in order of use
    Generator.Title         = "Community Patch - Base"
    Generator.ModPage       = NexusLink(game, modID)
    Generator.Subtitle      = [note[0], note[1], note[2]]
    Generator.Author        = "wghost81"
    Generator.Version       = 1.0
    Generator.FileName      = "CommunityPatch-Base"
    Generator.ManualLink    = ManualNexusLink(game, modID, fileID)
    # Generator.DESC          = ""
    
    print(
        f'[url={Generator.ModPage}]{Generator.Title}[/url]'
    )

    if Generator.Subtitle[0]:
        print(f'{Generator.Subtitle[1]}: {Generator.Subtitle[2]}')
    
    print(
        f'Author: {Generator.Author}\n' \
        f'Mod Version: {Generator.Version}'
    )
    
    if Generator.ManualLink is None:
        print(f'File Name: {Generator.FileName}')
    elif Generator.ManualLink is not None:
        print(f'File Name: [url={Generator.ManualLink}]{Generator.FileName}[/url]')
    
    if Generator.DESC is not None and not str(""):
        print(f'\n[spoiler]\n{Generator.DESC}\n[/spoiler]')

ParseMod("witcher3", 3652, 24139, note=[True, "Required", "Yes"])