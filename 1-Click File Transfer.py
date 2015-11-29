import os
import wx
import shutil
import wx.lib.agw.multidirdialog as MDD

wildcard = "All files (*.txt)|*.*"

class MyForm(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY,
                          "File and Folder Dialogs Tutorial")
        panel = wx.Panel(self, wx.ID_ANY)
        self.currentDirectory = os.getcwd()
 
        actBtn = wx.Button(panel, label="Transfer the file")
        actBtn.Bind(wx.EVT_BUTTON, self.onDir)

        #put the buttons in a sizer
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(actBtn, 0, wx.ALL|wx.CENTER,5)
        panel.SetSizer(sizer)
        

    def onDir(src,dst):
        src = 'C:\\Users\\wise_\\Desktop\\Folder A'
        dst = 'C:\\Users\\wise_\\Desktop\\Folder B'

        for file in os.listdir(src):
            print file  # testing
            src_file = os.path.join(src, file)
            dst_file = os.path.join(dst, file)
            shutil.move(src_file, dst_file)
            print dst_file



#Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()
    
        
