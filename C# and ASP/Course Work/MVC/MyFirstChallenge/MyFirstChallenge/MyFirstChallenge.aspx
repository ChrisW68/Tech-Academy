<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="MyFirstChallenge.aspx.cs" Inherits="MyFirstChallenge.MyFirstChallenge" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
    
        How old are you?&nbsp;
        <asp:TextBox ID="ageBox" runat="server">age</asp:TextBox>
        <br />
        <br />
        How much money do you have in your pocket?&nbsp;
        <asp:TextBox ID="moneyBox" runat="server">money in your pocket</asp:TextBox>
        <br />
        <br />
        <asp:Button ID="fortuneButton" runat="server" OnClick="fortuneButton_Click" Text="Click Me to see your Fortune." />
        <br />
        <br />
&nbsp;<asp:Label ID="resultLabel" runat="server"></asp:Label>
&nbsp;</div>
    </form>
</body>
</html>
