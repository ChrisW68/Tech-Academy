<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Default.aspx.cs" Inherits="CS_006.Default" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
    <style type="text/css">
        .auto-style1 {
            color: #CCFF66;
        }
    </style>
</head>
<body>
    <form id="form1" runat="server">
    <div>
    
        <h1>Head Line 1&nbsp;&nbsp;&nbsp; </h1>
    
    </div>
        <h2>Head Line 2</h2>
        <p>
            &nbsp;</p>
        <h3>Head Line 3</h3>
        <h4>Hea<span class="auto-style1">d Line 4<asp:AdRotator ID="AdRotator1" runat="server" />
            </span></h4>
    </form>
</body>
</html>
