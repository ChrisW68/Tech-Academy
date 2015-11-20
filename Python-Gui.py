import wx

class windowClass(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs)

        self.basicGUI()

    def basicGUI(self):

        panel = wx.Panel(self)
        
        menuBar = wx.MenuBar()
        
        fileButton = wx.Menu()
        editButton = wx.Menu()

        importItem = wx.Menu()

        importItem.Append(wx.ID_ANY, 'Import Document ..')
        importItem.Append(wx.ID_ANY, 'Import picture ..')
        importItem.Append(wx.ID_ANY, 'Import video ..')

        fileButton.AppendMenu(wx.ID_ANY, 'Import',importItem)

        toolBar =self.CreateToolBar()
        quitToolButton = fileButton.Append(wx.ID_ANY, 'Document')
        

        toolBar.Realize()
        self.Bind(wx.EVT_TOOL, self.Quit, quitToolButton)
        
        exitItem = fileButton.Append(wx.ID_EXIT, 'Exit\tCtrl+Q','status msg..') # |tCtrl+Q allows you to use a specific short cut key
        
        menuBar.Append(fileButton, 'File')
        menuBar.Append(editButton, 'Edit')

        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.Quit, exitItem)
        
        nameBox = wx.TextEntryDialog(None, 'What is your name?', 'Good Afternoon','name')

        if nameBox.ShowModal() == wx.ID_OK:
            userName = nameBox.GetValue()
     
        wx.TextCtrl(panel, pos=(10,20), size=(50,20))  #text box
        aweText = wx.StaticText(panel, -1, "Rent", (3,3))
        aweText.SetForegroundColour('Blue')
        aweText.SetBackgroundColour('green')

        wx.TextCtrl(panel, pos=(3,60), size=(50,20))  #text box
        relAweText = wx.StaticText(panel,-1,"Utilities-Electric", (3,40))
        relAweText.SetForegroundColour('black')
        relAweText.SetBackgroundColour('white')

        wx.TextCtrl(panel, pos=(3,110), size=(50,20))  #text box
        relAweText = wx.StaticText(panel,-1,"Utilities-Gas", (3,90))
        relAweText.SetForegroundColour('black')
        relAweText.SetBackgroundColour('grey')

        wx.TextCtrl(panel, pos=(120,20), size=(50,20))  #text box
        relAweText = wx.StaticText(panel,-1,"Utilities-Internet", (120,3))
        relAweText.SetForegroundColour('white')
        relAweText.SetBackgroundColour('black')

        wx.TextCtrl(panel, pos=(120,60), size=(50,20))  #text box
        relAweText = wx.StaticText(panel,-1,"Misc", (120,40))
        relAweText.SetForegroundColour('blue')
       

        self.SetTitle('Please enter your expenses this month '+userName)
        self.Show(True)

    def Quit(self, e):
        self.Close()

def main():
    app = wx.App()
    windowClass(None)

    app.MainLoop()

main()
