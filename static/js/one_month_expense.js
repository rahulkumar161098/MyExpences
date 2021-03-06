
const json_data = expense_graph_data;
data_key = Object.keys(json_data);
data_value = Object.values(json_data);

const ctx1 = document.getElementById('oneMonthChart').getContext('2d');
const myChart1 = new Chart(ctx1, {
  type: 'line',
  data: {
    labels: data_key,
    datasets: [{
      label: 'Per Month Expenses Data',
      data: data_value,
      backgroundColor: [
        'rgba(0, 128, 128, .3)',

      ],
      borderColor: [
        'rgba(0, 128, 128, 1)',
        // 'rgba(54, 162, 235, 1)',
        // 'rgba(255, 206, 86, 1)',
        // 'rgba(75, 192, 192, 1)',
        // 'rgba(153, 102, 255, 1)',
        // 'rgba(255, 159, 64, 1)'
      ],
      borderWidth: 1,
      pointBackgroundColor: 'tomato',
      axis:'x'
    }]
  },
  options: {
    scales: {
      y: {
        beginAtZero: true
      },
      xAxes: [{
        ticks: {
          maxRotation: 50,
          minRotation: 30,
          padding: 5,
          autoSkip: false,
          fontSize: 12
        }
      }]
    },
    legend: {
      fullSize:true,
      display: true,
      position: 'bottom',

      labels: {
        boxWidth: 10,
        padding: 10,
      }

    },
  },
});
