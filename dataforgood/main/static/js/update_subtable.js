$(document).ready(function() {
    var multiYearSubtableField = {{ multi_year_subtable_field|safe }};
    var subgroupChartData = {{ subgroup_chart_data|safe }};
    console.log(subgroupChartData,'subgroupChartData')
    var currentView = 'tract';
    $('.con3').hide();  //maybe deletion needed
    function updateSubgroupTable(year) {
        var subtableData = multiYearSubtableField[year];
        $('#subtable-year').text(year);
        $('#subtable-headers').empty();
        $('#subtable-rows').empty();

        subtableData.headers.forEach(function(header) {
            $('#subtable-headers').append('<th>' + header + '</th>');
        });

        subtableData.rows.forEach(function(row) {
            var rowHtml = '<tr>';
            row.forEach(function(value) {
                rowHtml += '<th>' + value + '</th>';
            });
            rowHtml += '</tr>';
            $('#subtable-rows').append(rowHtml);
        });

        // Update the subtable chart based on the current view
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
                    enabled: true,
                    style: {
                        fontWeight: 'bold',
                        color: ( // theme
                            Highcharts.defaultOptions.title.style &&
                            Highcharts.defaultOptions.title.style.color
                        ) || 'gray'
                    }
                }
            },
            legend: {
                align: 'right',
                x: -30,
                verticalAlign: 'top',
                y: 25,
                floating: true,
                backgroundColor:
                    Highcharts.defaultOptions.legend.backgroundColor || 'white',
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

    $('#subgroup-form').submit(function(event) {
        event.preventDefault();
        var selectedYear = $('#id_subgroup_year').val();
        updateSubgroupTable(selectedYear);
    });

    $('#toggle-view').click(function() {
        currentView = currentView === 'tract' ? 'raceGroup' : 'tract';
        var selectedYear = $('#id_subgroup_year').val();
        var subtableData = multiYearSubtableField[selectedYear];
        updateChart(selectedYear, subtableData);
    });
});