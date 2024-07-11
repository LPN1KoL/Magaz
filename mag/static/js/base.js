function showsearch(value){
    if (value != ''){
        document.getElementById('mod').style.display = 'block'
        const xhr = new XMLHttpRequest()
        xhr.open('GET', '/get_search')
        xhr.responseType = 'json'
        xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            const status = xhr.status
            if (status === 0 || (status >= 200 && status < 400)) {
                const products = xhr.response["products"]
                let div = document.getElementById("products")
                div.innerHTML = ''
                for (let i = 0; i < products.length; i++){
                    let product = products[i]
                    if (product.name.startsWith(value)) {
                        div.innerHTML += ''
                        }
                    else{
                        for(let k = 0; k < product.tags.length;k++){
                            let tag = product.tags[k]
                            if(tag.startsWith(value)){
                                div.innerHTML += ''
                            }
                        }
                        }
                    }
                }
            }
          }
        xhr.send();
        }
    }


document.addEventListener('mousedown', evt => {
    if (evt.target.classList.contains('modal')) {
        evt.preventDefault()
    }
    else {
        document.getElementById('mod').style.display = 'none'
        document.getElementById('search').value = ''
        }
})