function validateUser(loginForm){
    if(loginForm.userId.value== "Crispus"){
        if (loginForm.password.value== "password"){
            alert("Correct Input");
        }
        else{
            alert("Invalid password");
        }
    }
    else{
        alert("Invalid user id");
    }
}