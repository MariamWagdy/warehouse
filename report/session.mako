<html>
<head>
<style type="text/css">${css}</style>
</head>
<body>
<h1>${_("Stock Report")}</h1>
% for session in objects:
<h3>${"Stock Name :"} ${session.stockName}</h3>
<h3>${"Quantity :"} ${session.quantity}</h3>
<h3>${"Notes :"} ${session.notes}</h3>
% endfor
</body>
</html>