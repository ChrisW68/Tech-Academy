using System;
using System.Collections.Generic;
using System.Data.Entity;



namespace EF_Code_First
{
    public class Student
    {
        public Student()
        {

        }
        public int StudentID { get; set; }
        public string StudentName { get; set; }
        public DateTime DateofBirth { get; set; }
        public byte[] Photo { get; set; }
        public decimal Height { get; set; }
        public float Weight { get; set; }

        public Teacher Teacher { get; set; }

        public Standard Standard { get; set; }
    }

    public class Teacher
    {
        public Teacher()
        {

        }
        public int TeacherId { get; set; }
        public string TeacherName { get; set; }
    }

    public class Standard
    {
        public Standard()
        {

        }
        public int StandardId { get; set; }
        public string StandardName { get; set; }

        public ICollection<Student> Students { get; set; }

    }

    class Program
    {
        static void Main(string[] args)
        {
            using (var ctx = new SchoolContext())
            {
                Student stud = new Student() { StudentName = "New Student" };

                ctx.Students.Add(stud);
                ctx.SaveChanges();
            }
        }
    }
    public class SchoolContext : DbContext
    {
        public SchoolContext(): base()
        {

        }
        public DbSet<Student> Students { get; set; }
        public DbSet<Standard> Standards { get; set; }
    }

}
