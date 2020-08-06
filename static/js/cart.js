var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		console.log('productId:', productId, 'actions:', action)
		console.log('User---',user)
		if(user == 'AnonymousUser'){
			alert('Login')
		}else{
			updateUserOrder(productId,action)
		}

	})
}

function updateUserOrder(productId,action){
	console.log('User is logged in, sending data..')
// url to which we will send data
	var url = '/updateitem/'
// fetch for sending data 
	fetch(url,{
		method:'POST',
		headers:{
			'Content-Type':'application/json',
			'X-CSRFToken':csrftoken,
	},
	 body :JSON.stringify( {'productId':productId,'action':action})

	})
	.then((response)=>{
		return response.json( )
	})
	.then((data)=>{
		console.log('data:',data)
	})
}
