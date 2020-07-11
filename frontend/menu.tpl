<!DOCTYPE html>
<html>
    <head>
        <title>Edit Menu</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous"/>
<link rel="stylesheet" type="text/css" href=../style.css />
    </head>
    <body>
        <div>
            <h2>{{name}} &nbsp; <button type="button" class="btn btn-danger">change name</button></h2>
            <hr>
            %for item in items.keys():
            <div class = "row, padding-left">
                <h4>{{item}} &nbsp; <button type="button" class="btn btn-danger">delete section</button></h4>
            </div>
                <ul style="list-style: none;" class = "padding-bottom">
                    %for vals in items[item]:
                    <li class = "padding-bottom">{{vals[0]}} ... {{vals[1]}}
                        <br>&nbsp; &nbsp; &nbsp;<span>{{vals[2]}}</span> <button type="button" class="btn btn-danger">delete {{vals[0]}}</button></li>
                    %end
                    <li><form>
                        <label>Item: 
                            <input type="text" name="item-{{vals[0]}}"/>
                        </label>
                        <label>Cost:
                                <input type="text" name="Price-{{vals[0]}}"/>
                        </label>
                        <br>
                        <label>Description:
                                <input type="text" name="Desc-{{vals[0]}}"/>
                        </label>
                        <button class="btn btn-success" type= "submit">Add New Item</button>
                        </form>
                    </li>
                </ul>
                <hr>
            %end
                <h4><form>
                    <label>
                    Section Header:<input type="text" name="section"/>
                    </label>
                    <button class="btn btn-success" type= "submit">Add New Section</button>
                </form></h4>
            <div>
                <button type="button" class="btn btn-success">Save</button>
            </div>
        </div>
    </body>
</html>
