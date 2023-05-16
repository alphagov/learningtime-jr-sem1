async function fetchData() {
    const response = await fetch('http://localhost:4000/api/response-times');
    return response.json();
}

async function createChart() {
    const responseTimes = await fetchData();

    const chartData = {
        labels: responseTimes.map(rt => new Date(rt.checked_at)),
        datasets: [{
            label: 'Response Time (ms)',
            data: responseTimes.map(rt => rt.response_time_ms),
            borderColor: 'rgb(75, 192, 192)',
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            tension: 0.1
        }]
    };

    const chartConfig = {
        type: 'line',
        data: chartData,
        options: {
            scales: {
                x: {
                    type: 'time',
                    time: {
                        unit: 'minute',
                        displayFormats: {
                            minute: 'h:mm a'
                        }
                    },
                    title: {
                        display: true,
                        text: 'Time Checked At'
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'Response Time (ms)'
                    }
                }
            }
        }
    };

    const responseTimeChart = new Chart(
        document.getElementById('responseTimeChart'),
        chartConfig
    );
}

createChart();
