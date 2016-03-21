using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace MyFirstChallenge
{
    public partial class MyFirstChallenge : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void fortuneButton_Click(object sender, EventArgs e)
        {
            string ageOfPerson = ageBox.Text;
            string moneyOfPerson = moneyBox.Text;

            string result = "At " + ageOfPerson + " years old, I would have expected you to have more than " + moneyOfPerson + " in your pocket.";

            resultLabel.Text = result;
        }
    }
}