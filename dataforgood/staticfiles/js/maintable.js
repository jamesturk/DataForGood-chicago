document.addEventListener('DOMContentLoaded', function () {
    var chartData = {{ chart_data|safe }};
    var currentView = 'category'; // Initialize the current view to 'category'

    function updateMainChart() {
        var categories = chartData.categories;
        var series = chartData.series;

        var seriesData;

        if (currentView === 'category') {
            seriesData = series;
        } else {
            seriesData = categories.map(function(category, index) {
                var categoryData = series.map(function(serie) {
                    return serie.data[index];
                });

                return {
                    name: category,
                    data: categoryData
                };
            });
        }

        var chartOptions = {
            chart: {
                type: 'bar'
            },
            title: {
                text: '{{ table_title }}'
            },
            xAxis: {
                categories: currentView === 'category' ? categories : series.map(function(serie) {
                    return serie.name;
                })
            },
            yAxis: {
                min: 0,
                title: {
                    text: 'Value'
                }
            },
            legend: {
                reversed: true
            },
            plotOptions: {
                series: {
                    stacking: 'normal'
                }
            },
            series: seriesData
        };

        Highcharts.chart('chart-container', chartOptions);
    }

    updateMainChart();

    document.getElementById('toggle-main-view').addEventListener('click', function() {
        currentView = currentView === 'category' ? 'series' : 'category';
        updateMainChart();
    });
});
