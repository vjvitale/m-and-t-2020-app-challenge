<html>
    <head>
        <title>Results</title>
        <script src="ajax.js"></script>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous"/>
        <link rel="stylesheet" type="text/css" href=../style.css />
    </head>
    <body>
        <div>
            <h2>Search Results</h2>
            <hr>
                <ul style="list-style: none;" class = "padding-bottom">
                    %for resturant in resturant:
                    <li class = "padding-bottom" href=/m/{{restaurant[1]}}> <h4>{{restaurant[0]}}</h4> 
                    <br>
                    {{resturant[2]}}
                    </li>
                    %end
                </ul>
                <hr>
        </div>
        <div>
            <h4 href="/">New Search</h4>
        </div>
    </body>
</html>
