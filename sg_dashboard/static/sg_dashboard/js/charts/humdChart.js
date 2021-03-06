/**
 * Create Humidity chart
 */
function createHumdChart(data) {

    var humdCanvas = document.getElementById('humdCanvas').getContext('2d');

    return new Chart(humdCanvas, {
        type: 'bar',
        data: {
            labels: data.labels,
            datasets: [{
                label: 'Relative Humidity',
                data: data.data,
                backgroundColor: createColors(data.data),
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
 * Generate colors for Bar chart
 * Colors are relative to humidity value
 * @param {} values 
 */
function createColors(values) {
    const a = 0.8;
    var colors = [];
    for (const value in values) {
        var red = 60;
        var green = 160;
        var blue = 250;
        colors.push('rgba(' + red + ',' + green + ',' + blue + ',' + a + ')');
    }
    return colors;
}


/**
 * Update Humidity chart
 */
function updateHumidity(value) {
    charts.humdChart.data.labels.push("Test");
    console.log(charts.humdChart.data.datasets[0].data.push(value));
    charts.humdChart.update();
}