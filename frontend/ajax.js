function submitSearch(){
    var text = document.getElementById("searchbar").value;
    // console.log(text);
}

function login(){
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    // console.log(username + " and " + password);
    var request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200){
            console.log(this.response);
            
        }
    }
}

// function deletItem(){

// }

// function deleteSection(){

// }

function addItem(){
    var form = document.getElementById("item-form");
    console.log(form);
}

function addSection(){
    var form = document.getElementById("section-form");
    console.log(form);

}