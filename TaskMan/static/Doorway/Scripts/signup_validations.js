const regName = /^[a-zA-Z ]{1,30}$/;
const regEmail = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/
const regUserName = /^[a-zA-Z]+[a-zA-Z0-9_@+.]{2,16}$/
const regPassword = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#^])[A-Za-z\d@$!%*?&#^]{8,20}$/

const mainForm = document.getElementById("mainForm");


const firstName = mainForm.firstName
const lastName = mainForm.lastName
const email = mainForm.email
const username = mainForm.username
const password = mainForm.password;
const rePassword = mainForm.rePassword;
const submitBtn = document.querySelector("#submitBtn")

const firstNameErr = document.getElementById('firstName');
const lastNameErr = document.getElementById('lastName');
const emailErr = document.getElementById('email');
const userNameErr = document.getElementById('username')
const passErr = document.getElementById('password')
const passMissErr = document.getElementById('passwordmis')

let checkError = [false];


mainForm.addEventListener('submit', (e) => {
	e.preventDefault();
    

    checkError[0] = regName.test(firstName.value.trim())
    
    if(!checkError[0]){
        firstNameErr.classList.add('errshow');
    }
    else{
        firstNameErr.classList.remove('errshow');
    }
    
    checkError[1] = regName.test(lastName.value.trim())
    
    if(!checkError[1]){
        lastNameErr.classList.add('errshow')
    }
    else{
        lastNameErr.classList.remove('errshow')
    }

    checkError[2] = regEmail.test(email.value);
    
    if(!checkError[2]){
        emailErr.classList.add('errshow')
    }
    else{
        emailErr.classList.remove('errshow')
    }

    checkError[3] = regUserName.test(username.value)


    if(!checkError[3]){
        userNameErr.classList.add('errshow')
    }
    else{
        userNameErr.classList.remove('errshow')
    }

    password.value === rePassword.value? checkError[4] = true : checkError[4] = false;

    if(!checkError[4]){
        passMissErr.classList.add('errshow')
        }

    else{
        passMissErr.classList.remove('errshow')
        checkError[4] = regPassword.test(password.value)
        
        if(!checkError[4]){
            passErr.classList.add('errshow')
        }
    
        else{
            passErr.classList.remove('errshow')
        }
    }


    if(checkError.every(value => value === true)){
        console.log("no error")
        mainForm.submit();
    }
    
});
