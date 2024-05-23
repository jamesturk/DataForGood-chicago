document.addEventListener('DOMContentLoaded', function() {
    var multiYearSubtableField = {{ multi_year_subtable_field|safe }};
    var subgroupChartData = {{ subgroup_chart_data|safe }};
    console.log(subgroupChartData, 'subgroupChartData');
    var currentView = 'tract';
    document.querySelector('.con3').classList.add('hidden');

    function updateSubgroupTable(year) {
        var subtableData = multiYearSubtableField[year];
        document.getElementById('subtable-year').textContent = year;
        document.getElementById('subtable-headers').innerHTML = '';
        document.getElementById('subtable-rows').innerHTML = '';

        subtableData.headers.forEach(function(header) {
            var th = document.createElement('th');
            th.textContent = header;
            document.getElementById('subtable-headers').appendChild(th);
        });

        subtableData.rows.forEach(function(row) {
            var tr = document.createElement('tr');
            row.forEach(function(value) {
                var th = document.createElement('th');
                th.textContent = value;
                tr.appendChild(th);
            });
            document.getElementById('subtable-rows').appendChild(tr);
        });

        updateChart(year, subtableData);
    }

    function updateChart(year, subtableData) {
        var tractCategories = subtableData.rows.map(function(row) {
            return row[0];
        });

        var raceGroups = subtableData.headers.slice(1);

        var seriesData;

        if (currentView === 'tract') {
            seriesData = raceGroups.map(function(raceGroup, index) {
                return {
                    name: raceGroup,
                    data: subtableData.rows.map(function(row) {
                        return parseFloat(row[index + 1]) || null;
                    })
                };
            });
        } else {
            seriesData = tractCategories.map(function(tract, index) {
                var tractData = subtableData.rows[index].slice(1).map(function(value) {
                    return parseFloat(value) || null;
                });

                return {
                    name: tract,
                    data: tractData
                };
            });
        }

        var chartOptions = {
            chart: {
                type: 'column'
            },
            title: {
                text: 'Subgroup Data for ' + year
            },
            xAxis: {
                categories: currentView === 'tract' ? tractCategories : raceGroups
            },
            yAxis: {
                min: 0,
                title: {
                    text: 'Value'
                },
                stackLabels: {
                    enabled: true
                }
            },
            legend: {
                align: 'right',
                verticalAlign: 'top',
                floating: true,
                backgroundColor: 'white',
                borderColor: '#CCC',
                borderWidth: 1,
                shadow: false
            },
            tooltip: {
                headerFormat: '<b>{point.x}</b><br/>',
                pointFormat: '{series.name}: {point.y}<br/>Total: {point.stackTotal}'
            },
            plotOptions: {
                column: {
                    stacking: 'normal',
                    dataLabels: {
                        enabled: true
                    }
                }
            },
            series: seriesData
        };

        Highcharts.chart('subtable-chart-container', chartOptions);
    }

    document.getElementById('subgroup-form').addEventListener('submit', function(event) {
        event.preventDefault();
        var selectedYear = document.getElementById('id_subgroup_year').value;
        updateSubgroupTable(selectedYear);
    });

    document.getElementById('toggle-view').addEventListener('click', function() {
        currentView = currentView === 'tract' ? 'raceGroup' : 'tract';
        var selectedYear = document.getElementById('id_subgroup_year').value;
        var subtableData = multiYearSubtableField[selectedYear];
        updateChart(selectedYear, subtableData);
    });
});
