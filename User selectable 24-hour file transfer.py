import os
import wx
import shutil
import time
import wx.lib.agw.multidirdialog as MDD

wildcard = "All files (*.*)|*.*"

class MyForm(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY,
                          "File and Folder Dialogs Tutorial")
        panel = wx.Panel(self, wx.ID_ANY)
        self.currentDirectory = os.getcwd()

        # create the buttons and bindings
        openFileDlgBtn = wx.Button(panel, label="Show Select FILE window")
        openFileDlgBtn.Bind(wx.EVT_BUTTON, self.onOpenFile)
 
        saveFileDlgBtn = wx.Button(panel, label="Show Save/as window")
        saveFileDlgBtn.Bind(wx.EVT_BUTTON, self.onSaveFile)
 
        actBtn = wx.Button(panel, label="Transfer the file")
        actBtn.Bind(wx.EVT_BUTTON, self.onDir)

        #put the buttons in a sizer
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(openFileDlgBtn, 0, wx.ALL|wx.CENTER,5)
        sizer.Add(saveFileDlgBtn, 0, wx.ALL|wx.CENTER,5)
        sizer.Add(actBtn, 0, wx.ALL|wx.CENTER,5)
        panel.SetSizer(sizer)
        

    def onDir(self,event):
        #Shows the DirDialog and prints the user's choice to stdout
        src=filePath
        dst=savePath

        print file  # testing
        st=os.stat(src)
        ctime=st.st_ctime
        mtime=(time.time() - ctime)/3600
        if mtime>24:
            shutil.move(src, dst)
            print dst
        else:
            print "file are: '%d' hours, since creation/modification" %mtime
        
        #assert not os.path.isabs(srcfile)
        #dstdir = os.path.join(dstroot, os.path.dirname(srcfile))

        shutil.copy(src, dst)
        
    def onOpenFile(self,event):
        # Create and show the Open FileDialog
       
        dlg = wx.FileDialog(
            self, message="Select FILE",
            defaultDir=self.currentDirectory,
            defaultFile="",
            wildcard=wildcard,
            style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR
            )
        if dlg.ShowModal() == wx.ID_OK:
            paths=dlg.GetPaths()
            print "You chose the following file(s):"
            for path in paths:
                 print path
                 global filePath
                 filePath=path
        dlg.Destroy()

    def onSaveFile(self, event):
        #Create/Show the SAVE FileDialog
        
        dlg = wx.DirDialog(self, "Choose a directory:")
            
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPath()
            print "You chose %s" % dlg.GetPath()
            for path in paths:
                global savePath
                savePath=dlg.GetPath()
        dlg.Destroy()

#Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()
    
        
