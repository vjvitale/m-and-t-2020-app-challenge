<html>
    <head>
        <title>Edit Menu</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous"/>
        <link rel="stylesheet" type="text/css" href=../style.css />
    </head>
    <body>
        <div>
            <h2>{{name}}</h2>
            <p>{{description}}</p>
            <hr>
            %for item in items.keys():
            <div class = "row, padding-left">
                <h4>{{item}}</h4>
            </div>
                <ul style="list-style: none;" class = "padding-bottom">
                    %for vals in items[item]:
                    <li class = "padding-bottom">{{vals[0]}} ... {{vals[1]}}
                        <br>&nbsp; &nbsp; &nbsp;<span>{{vals[2]}}</span>
                    </li>
                    %end
                </ul>
                <hr>
            %end
        </div>
    </body>
</html>