document.getElementById('map-select').addEventListener('change', function() {
    var selectedPath = this.value;
    var mapDivs = document.getElementById('map-display').children;

    for (var i = 0; i < mapDivs.length; i++) {
        if (mapDivs[i].id === selectedPath) {
        mapDivs[i].style.display = 'block';
        } else {
        mapDivs[i].style.display = 'none';
        }
    }
    });
