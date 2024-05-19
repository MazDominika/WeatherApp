var ctx= document.getElementById('myChart');
let myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: null,
        datasets: [
        {
        label: 'Temperature',
        data: null,
        borderWidth: 1,
        borderColor: 'rgb(86, 117, 143)',
        fill: true
        },
        {
        label: 'Humidity',
        data: null,
        borderWidth: 1,
        borderColor: 'rgb(250, 222, 63)',
        fill: true
        }]
    },
    options: {
        scales: {
          y: {
      beginAtZero: true
    }}
    }});   

async function refreshData()
{
    const response = await fetch('/get_json');
    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    let checkedValue = checkValue();
    
    if(checkedValue == 'TH')
    {
        if (myChart.data.datasets.length < 2){
            let newDataset = {
                label: null,
                data: null,
                borderWidth: 1,
                borderColor: 'rgb(250, 222, 63)',
                fill: true
            }
            myChart.data.datasets.push(newDataset);
        }
        myChart.data.datasets[0].data = data.temperature.reverse();
        myChart.data.datasets[1].data = data.humidity.reverse();
        myChart.data.datasets[0].label = "Temperature";
        myChart.data.datasets[1].label = "Humidity";
        myChart.data.labels = data.date.reverse();
    }
    else
    {
        myChart.data.datasets[0].data = data.pressure.reverse();
        myChart.data.datasets[0].label = "Pressure";
        myChart.data.datasets.splice(1, 1);
        myChart.data.labels = data.date.reverse();
    }
    myChart.update();
    processData(data);      
    setTimeout(refreshData, 1000);      
}

function processData(jsonData) {
        var table = document.getElementById("measurmentsTable");
        var date = jsonData["date"];
        var temperature = jsonData["temperature"];
        var pressure = jsonData["pressure"];
        var humidity = jsonData["humidity"];

        if (table.rows.length < 2)
        {
            for (var i = 0; i < 15; i++)
            {                
                table.innerHTML+= "<tr><td>"+date[i]+"</td><td>"+temperature[i]+"</td><td>"+pressure[i]+"</td><td>"+humidity[i]+"</td></tr>"
            }
        }
        else
        {
            for (var i = 1; i < 15 + 1; i++)
            {                
                table.rows[i].cells[1].innerHTML = date[i-1];
                table.rows[i].cells[1].innerHTML  = temperature[i-1];
                table.rows[i].cells[2].innerHTML  = pressure[i-1];
                table.rows[i].cells[3].innerHTML = humidity[i-1];
            }
        }
    }

function checkValue()
{
  var radioButtons = document.getElementsByName('inlineRadioOptions');
  var checkedValue;
  for (var i = 0; i < radioButtons.length; i++) {
    if (radioButtons[i].checked) 
    {
        checkedValue = radioButtons[i].value;
        break;
    }
}

  if (checkedValue == undefined) {
     checkedValue = radioButtons[0].value;
    }

  return checkedValue;
}

refreshData();