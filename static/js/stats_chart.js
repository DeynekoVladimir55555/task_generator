$(document).ready(function() {
  success_total = $('#success_total').val();
  fail_total = $('#fail_total').val();
  skip_total = $('#skip_total').val();

  const ctx = document.getElementById('stats_chart');

  new Chart(ctx, {
    type: 'pie',
    data: {
      labels: ['Решено верно', 'Решено неверно', 'Пропущено'],
      datasets: [{
        label: 'Статистика задач',
        data: [success_total, fail_total, skip_total],
        backgroundColor: [
          'rgb(0, 255, 0)',
          'rgb(255, 0, 0)',
          'rgb(200, 200, 200)'
      ],
        borderWidth: 0
      }]
    },
    options: {
      responsive: true,
    }
  });
});

