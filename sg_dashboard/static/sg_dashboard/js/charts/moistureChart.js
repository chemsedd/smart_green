/**
 * Create Soil moisture chart
 */
function createMoistureChart(data) {

    var moistureCanvas = document.getElementById('moistureCanvas').getContext('2d');

    return new Chart(moistureCanvas, {
        type: 'bar',
        data: {
            labels: data.labels,
            datasets: [{
                label: data.datalabel,
                data: data.data,
                //backgroundColor: bgcolor,
                borderWidth: 3,
            }]
        },
        options: {
            scales: {
                yAxes: {
                    ticks: {
                        min: 0,
                        max: 70,
                    },
                }
            }
        }
    });
}



/**
 * Update Soil Moisture chart
 */
function updateMoisture(value) {
    charts.moistureChart.data.labels.push("Test");
    console.log(charts.moistureChart.data.datasets[0].data.push(value));
    charts.moistureChart.update();
}