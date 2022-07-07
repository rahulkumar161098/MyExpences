'use strict';

const data1 = graph_data
const gr_keys= Object.keys(data1)
const gr_values= Object.values(data1)


// const sum_key=summary_key;

// let s=sum_key.split(",")

const ctx = document.getElementById('myChart').getContext('2d');
const myChart = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: gr_keys,
        datasets: [{
            label: 'Your Expences',
            data: gr_values,
            borderColor: "rgba(0,0,0,0.1)",
            backgroundColor: [
                'rgba(255, 99, 132)',
                'rgba(54, 162, 235)',
                'rgba(255, 206, 86)',
                'rgba(75, 192, 192)',
                'rgba(153, 102, 255)',
                'rgba(255, 159, 64)'
            ],
            borderColor: [
                'rgba(255, 255, 255, 2)',
                // 'rgba(54, 162, 235, 1)',
                // 'rgba(255, 206, 86, 1)',
                // 'rgba(75, 192, 192, 1)',
                // 'rgba(153, 102, 255, 1)',
                // 'rgba(255, 159, 64, 1)'
            ],
            
            borderWidth: 3
        }],
    },
    options: {
        display: true,
        responsive:false,
        legend:{
            display: true,
            position: 'bottom',
            
            labels:{
                boxWidth: 20,
                padding: 10,
            }
    
        },
    },
});
