using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public void TransDirectory(string[] source, string target)
    {
        var stack = new Stack<Folders>();
        stack.Push(new Folders(source[0], target));
        while (stack.Count > 0)
        {
            var folders = stack.Pop();
            Directory.CreateDirectory(folders.Target);
            foreach (var file in Directory.GetFiles(folders.Source, "*.*"))
            {
                string targetFile = Path.Combine(folders.Target, Path.GetFileName(file));
                if (File.Exists(targetFile)) File.Delete(targetFile); File.Move(file, targetFile);
            }
            foreach (var folder in Directory.GetDirectories(folders.Source))
            {
                stack.Push(new Folders(folder, Path.Combine(folders.Target, Path.GetFileName(folder))));
            }
        }
        Directory.Delete(source[0], true);
    } 



public class Folders { 
    public string Source { 
        get; private set; 
    } 
    public string Target { 
        get; private set; 
    } 
    public Folders(string source, string target) { 
        Source = @"C:\Users\wise_\Desktop\Folder A"; 
        Target = @"C:\Users\wise_\Desktop\Folder A"; 
    } 
}
