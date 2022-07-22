const income_source_data = six_month_data
const income_keys= Object.keys(income_source_data);
const income_values= Object.values(income_source_data);

const incomes = document.getElementById('incomeChart').getContext('2d');
const incomeChart = new Chart(incomes, {
    type: 'pie',
    data: {
        labels: income_keys,
        datasets: [{
            label: 'Your Expences',
            data: income_values,
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
