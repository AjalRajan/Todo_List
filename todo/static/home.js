function myfun() {

    document.getElementById('added').innerHTML ='List Added'

    var title = document.forms['myform']['title'].value;
    if (title ==''){
        alert('input must be filled out');
        return window.location.href = 'http://127.0.0.1:8000/home/';
    }
    console.log(title)
}