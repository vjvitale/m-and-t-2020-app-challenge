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

function loadEditPage(){
    console.log("loading edit page")
}

function deletItem(){

}

function deleteSection(){

}

function addItem(){
    var text = document.getElementById("itemForm");
    console.log(text);
}

function addSection(){
    var form = document.getElementById("section-form");
    console.log(form);

}