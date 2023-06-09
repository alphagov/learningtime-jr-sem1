async function fetchData() {
    const response = await fetch('http://localhost:4000/api/response-times');
    return response.json();
}

async function createChart() {
    const data = await fetchData(); 
    const chartData = data.map(datum => ({
      x: new Date(datum.checked_at.replace(' ', 'T')), 
      y: datum.response_time_ms
    }));

    new Chart(document.getElementById("myChart"), {
      type: 'line',
      data: {
        datasets: [{
          label: 'Response Time (ms)',
          data: chartData,
          borderColor: 'rgb(255, 99, 132)',
          backgroundColor: 'rgba(255, 99, 132, 0.5)'
        }]
      },
      options: {
        scales: {
          x: {
            type: 'time',
            time: {
              unit: 'minute'
            }
          }
        }
      }
    });
}

createChart();
