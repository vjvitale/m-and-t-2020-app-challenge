<html>
    <head>
        <title>Edit Menu</title>
        <script src="ajax.js"></script>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous"/>
        <link rel="stylesheet" type="text/css" href=../style.css />
    </head>
    <body>
        <div id="sections">
            <h2>{{name}} &nbsp; <button type="button" onclick= "changeName({{restaurant_id}})" class="btn btn-danger">change name</button></h2>
            <p>{{description}}</p><span><button type="button" onclick= "changeDescription({{restaurant_id}})" class="btn btn-danger">Edit Description</button></span>
            <hr>
            %for item in items.keys():
            <div class = "row, padding-left">
                <h4>{{item}} &nbsp; <button id={{section[item]}} type="button" class="btn btn-danger">delete section</button></h4>
            </div>
                <ul id="list-{{section[item]}}" style="list-style: none;" class = "padding-bottom">
                    %for vals in items[item]:
                    <li id={{vals[3]}} class = "padding-bottom">{{vals[0]}} ... {{vals[1]}}
                        <br>&nbsp; &nbsp; &nbsp;<span>{{vals[2]}}</span> <button type="button" onclick='deleteItem({{vals[3]}}); return false;' class="btn btn-danger">delete {{vals[0]}}</button></li>
                    %end
                    <li><form id = "item-{{section[item]}}">
                        <label>Item: 
                            <input type="text" name="item"/>
                        </label>
                        <label>Cost:
                                <input type="text" name="Price"/>
                        </label>
                        <br>
                        <label>Description:
                                <input type="text" name="Desc"/>
                        </label>
                        <label style="display: none"> <input type="text" name="sid" value="{{section[item]}}"></label>
                        <button class="btn btn-success"  onclick = "addItem({{section[item]}}); return false;" type= "submit">Add New Item</button> 
                        </form>
                    </li>
                </ul>
                <hr>
            %end
            </div>
            <div>
                <h4><form id = "section-form">
                    <label>
                    Section Header:<input type="text" name="section"/>
                    </label>
                     <label style="display: none"> <input type="text" name="rid" value="{{restaurant_id}}"></label>
                    <button class="btn btn-success" onclick= "addSection()" type= "submit">Add New Section</button>
                </form></h4>
        </div>
    </body>
</html>
