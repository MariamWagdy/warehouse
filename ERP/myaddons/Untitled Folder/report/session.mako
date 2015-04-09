<html>
<head>
    <style type="text/css">${css}</style>
</head>
<body>
    <h1>${_("Session Report")}</h1>
        % for session in objects:
             <h2>${ session.name }</h2>
     % endfor
</body>
</html>