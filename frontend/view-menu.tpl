<!DOCTYPE html>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
<link rel="stylesheet" href=/style.css>
<html>
    <head>
        <title>Edit Menu</title>
    </head>
    <body>
        <div>
            <h2>{{name}}</h2>
            %for item in items.keys():
            <div class = "row, padding-left">
                <h4>{{item}}</h4>
            </div>
                <ul style="list-style: none;" class = "padding-bottom">
                    %for vals in items[item]:
                    <li class = "padding-bottom">{{vals[0]}} ... {{vals[1]}}
                        <br><span>{{vals[2]}}</span></li>
                    %end
                </ul>
            %end
        </div>
    </body>
</html>