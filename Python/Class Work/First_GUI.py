import wx, dbprogram


class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None,\
          title=title, size=(300,200))
        self.exitProgram = None
        panel = wx.Panel(self)

        # Create menu bar
        menuBar = wx.MenuBar()
        # Create wx menus
        fileMenu = wx.Menu()
        editMenu = wx.Menu()
        exitItem = fileMenu.Append(wx.NewId(), "Exit")
        menuBar.Append(fileMenu, "File")

        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU,          self.exitProgram, exitItem)
        self.CreateStatusBar()


    def exit(self, event):
        self.Destroy()

app = wx.App()
frame = Frame("Python GUI")
frame.Show()
app.MainLoop()