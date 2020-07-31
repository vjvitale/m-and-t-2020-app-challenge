function submitSearch(){
    var text = document.getElementById("searchbar").value;
    // console.log(text);
}

function test(){
    console.log("Test");
}

function login(){
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    input = {"username": username, "password": password};
    $.ajax({
        type: "POST",
        url: "/server.py", //Fix where it sends the data to cause
        data: { param: input },
        success: loadEditPage
    });
    // console.log(username + " and " + password);
    // var request = new XMLHttpRequest();
    // request.onreadystatechange = function(){
    //     if (this.readyState === 4 && this.status === 200){
    //         console.log(this.response);
            
    //     }
    // }
}



function deletItem(item_id){

    var request = new XMLHttpRequest();

    request.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            var elem = document.getElementById(item_id);
            elem.parentNode.removeChild(elem);
        }
    }

    request.open("POST", "/removeItem")
    request.send(JSON.stringify(item_id))
}

function deleteSection(section_id){

    var request = new XMLHttpRequest();

    request.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            var elem = document.getElementById(section_id);
            elem.parentNode.removeChild(elem);
        }
    }

    request.open("POST", "/removeSection")
    request.send(JSON.stringify(section_id))


}

function addItem(section_id){
    var request = new XMLHttpRequest();
    var text = document.getElementById("item-" + section_id);

    request.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            console.log(this.response)
            resp = JSON.parse(this.response)
            item_list = document.getElementById("list-" + section_id)

            li = document.createElemnt("LI")

            li.innerHTML = resp["item"] + "..." resp["price"] + "<br>&nbsp; &nbsp; &nbsp;<span>" + resp["description"] + "</span> <button type='button' onclick='deleteItem("+ resp["item_id"] + "); return false;' class='btn btn-danger'>delete" + resp["item"] + "</button>"

            item_list.prepend(li)

        }
    }
    request.open("POST", "/addItem");
    request.send(new FormData(text))

    return false;
}

function addSection(){
    var request = new XMLHttpRequest();
    var form = document.getElementById("section-form");
    request.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            console.log(this.response)
            resp = JSON.parse(this.response)
            sect = document.getElementById("sections")

            div = document.createElemnt("DIV")

            basehtml = "<h4>" + resp["section"] + " &nbsp; <button id=" + resp["sid"] + " type='button' class='btn btn-danger'>delete section</button></h4>" + "<br> <ul id='list-" + resp["sid"] +"' style='list-style: none;' class = 'padding-bottom'>"

            basehtml += "<li><form id = 'item-" + resp["sid"] + "'><label>Item: <input type='text' name='item'/></label><label>Cost:<input type='text' name='Price'/></label><br><label>Description:<input type='text' name='Desc'/></label><label style='display: none'> <input type='text' name='sid' value='" + resp["sid"] + "'></label><button class='btn btn-success'  onclick = 'addItem(" + resp["sid"] + "); return false;' type= 'submit'>Add New Item</button> </form></li> </ul><hr>"
            
            div.insertAdjacentHTML("beforeend", basehtml)
        }
    }
    request.open("POST", "/addSection");
    request.send(new FormData(text))
}