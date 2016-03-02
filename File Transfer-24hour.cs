using System;
using System.IO;


class Exercise46
{
    public static void Main(string[] args)
    {
        try
        {
            CreationDate();
            Console.ReadKey();
            
        }
        catch (Exception e)
        {
            Console.WriteLine("The process failed: {0}", e.ToString());
        }
    }
    public static void CreationDate()

    {
        string fileName = "*.txt";
        string sourcePath = @"C:\Users\wise_\Desktop\Folder A";
        string targetPath = @"C:\Users\wise_\Desktop\Folder B";

        // Use Path class to manipulate file and directory paths.
        string sourceFile = System.IO.Path.Combine(sourcePath, fileName);
        string destFile = System.IO.Path.Combine(targetPath, fileName);


        // To copy all the files in one directory to another directory.
        // Get the files in the source folder.
        if (System.IO.Directory.Exists(sourcePath))
        {
            string[] files = System.IO.Directory.GetFiles(sourcePath);

            // Copy the files and overwrite destination files if they already exist.
            foreach (string s in files)
            {
                // Use static Path methods to extract only the file name from the path.
                FileInfo ageInfo = new FileInfo(s);
                if (ageInfo.CreationTime < DateTime.Now.AddDays(-1))
                {
                    fileName = System.IO.Path.GetFileName(s);
                    destFile = System.IO.Path.Combine(targetPath, fileName);
                    System.IO.File.Move(s, destFile);

                }
                else
                {
                    Console.WriteLine("File is not old enough");
                    Console.WriteLine("File is: " + ageInfo.CreationTimeUtc);
                    Console.ReadLine();
                }

            }
        }
        else
        {
            Console.WriteLine("Source path does not exist!");
        }

        // Keep console window open in debug mode.
        Console.WriteLine("Press any key to exit.");
        Console.ReadKey();
    }

}


