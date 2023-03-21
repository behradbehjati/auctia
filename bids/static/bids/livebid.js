
bidpk= document.getElementById('bidpk').textContent.trim()
 submitBtn= document.getElementById('submit-btn')

bidPrice= document.getElementById('bid-price')

userId= document.getElementById('user-id').textContent.trim()

socket=new WebSocket(
    'ws://127.0.0.1:8001/ws/'+bidpk+'/');
console.log(socket)
socket.onmessage=function(e){


let {sender,message}=JSON.parse(e.data)



updateChart()


};
submitBtn.addEventListener('click',()=>{

        let Price=bidPrice.value

        socket.send(JSON.stringify({
         'message':Price,
         'sender':userId


    }));



});
tbody=document.getElementById('tbody');


fetchChartData=async()=>{
    let response=await fetch('http://127.0.0.1:8001/livebid/'+bidpk+'/chart/')
    let data= await response.json()




    return data
    };
highest=document.getElementById('highest')
makeChart= async()=>{
    let data=await fetchChartData()
    console.log(data)
    highest.innerHTML=data.highest





    data.top10.forEach(function(item) {
      let row = document.createElement('tr');
      let id = document.createElement('td');
      let  price = document.createElement('td');
      let  time = document.createElement('td');

      id.innerText = item[0];
      price.innerText = item[1]
      time.innerText = item[2]

      row.appendChild(id);
      row.appendChild(price);
      row.appendChild(time);

      tbody.appendChild(row);
   });
    };


updateChart = async () => {
  let  trList = document.getElementsByTagName('tr');
  for(let i = trList.length - 1; i >= 0; i--) {
    trList[i].remove();
  }
  await makeChart();
}

socket.onopen=function(e){
updateChart()
};

