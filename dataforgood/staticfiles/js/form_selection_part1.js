document.addEventListener('DOMContentLoaded', function() {
    var geoLevelSelect = document.getElementById('id_geographic_level');
    var communityField = document.getElementById('community_field');
    var tractField = document.getElementById('tract_field');
    var zipcodeField = document.getElementById('zipcode_field');

    geoLevelSelect.addEventListener('change', function() {
        var selectedValue = this.value;
        if (selectedValue === 'Community') {
            communityField.style.display = 'block';
            tractField.style.display = 'none';
            zipcodeField.style.display = 'none';
        } else if (selectedValue === 'Zipcode') {
            communityField.style.display = 'none';
            tractField.style.display = 'none';
            zipcodeField.style.display = 'block';
        } else if (selectedValue === 'Tract') {
            communityField.style.display = 'none';
            tractField.style.display = 'block';
            zipcodeField.style.display = 'none';
        } else {
            communityField.style.display = 'none';
            tractField.style.display = 'none';
            zipcodeField.style.display = 'none';
        }
    });

    function capitalizeText(text) {
        return text.toLowerCase().replace(/(?:^|\s)\S/g, function(a) { return a.toUpperCase(); });
    }

    var labels = document.querySelectorAll('#community-list label');
    labels.forEach(function(label) {
        label.textContent = capitalizeText(label.textContent);
    });
});

document.addEventListener('DOMContentLoaded', function() {
    var geoLevelSelect = document.getElementById('id_geographic_level');
    var tractField = document.getElementById('tract_field');
    var zipcodeField = document.getElementById('zipcode_field');
    var communityField = document.getElementById('community_field');

    var categorySelect = document.getElementById('id_category');
    var economicField = document.getElementById('economic_field');
    var educationField = document.getElementById('education_field');
    var healthField = document.getElementById('health_field');
    var housingField = document.getElementById('housing_field');
    var populationField = document.getElementById('population_field');

    function handleGeoLevelChange() {
        var selectedValue = geoLevelSelect.value;
        tractField.style.display = 'none';
        zipcodeField.style.display = 'none';
        communityField.style.display = 'none';
        if (selectedValue === 'Tract') {
            tractField.style.display = 'block';
        } else if (selectedValue === 'Zipcode') {
            zipcodeField.style.display = 'block';
        } else if (selectedValue == 'Community') {
            communityField.style.display = 'block';
        }
    }
    geoLevelSelect.addEventListener('change', handleGeoLevelChange);
    handleGeoLevelChange();

    function handleIndicatorChange() {
        var selectedValue = categorySelect.value;
        economicField.style.display = 'none';
        educationField.style.display = 'none';
        healthField.style.display = 'none';
        housingField.style.display = 'none';
        populationField.style.display = 'none';
        if (selectedValue === 'Economic') {
            economicField.style.display = 'block';
        } else if (selectedValue === 'Education') {
            educationField.style.display = 'block';
        } else if (selectedValue === 'Health') {
            healthField.style.display = 'block';
        } else if (selectedValue == 'Housing') {
            housingField.style.display = 'block';
        } else if (selectedValue == 'Population') {
            populationField.style.display = 'block';
        }
    }
    categorySelect.addEventListener('change', handleIndicatorChange);
    handleIndicatorChange();
});

function toggleYearSelection(source) {
    var checkboxes = document.querySelectorAll('[name="year"]');
    for(var i = 0, n = checkboxes.length; i < n; i++) {
        checkboxes[i].checked = source.checked;
    }
}

function toggleTractSelection(source) {
    var checkboxes = document.querySelectorAll('input[name="tract"]');
    for (var i = 0, n = checkboxes.length; i < n; i++) {
        checkboxes[i].checked = source.checked;
    }
}

function toggleZipcodeSelection(source) {
    var checkboxes = document.querySelectorAll('input[name="zipcode"]');
    for (var i = 0, n = checkboxes.length; i < n; i++) {
        checkboxes[i].checked = source.checked;
    }
}

document.addEventListener('DOMContentLoaded', function() {
    var geoLevelSelect = document.getElementById('id_geographic_level');
    var searchContainer = document.getElementById('search-container');
    var searchInput = document.getElementById('search-input');

    geoLevelSelect.addEventListener('change', function() {
        var selectedValue = this.value;
        if (selectedValue === 'Tract' || selectedValue === 'Zipcode' || selectedValue === 'Community') {
            searchContainer.style.display = 'block';
        } else {
            searchContainer.style.display = 'none';
        }
    });

    searchInput.addEventListener('input', function() {
        var searchTerm = this.value.toLowerCase();
        var selectedValue = geoLevelSelect.value;

        if (selectedValue === 'Tract') {
            var checkboxes = document.querySelectorAll('#tract-list .checkbox');
            checkboxes.forEach(function(checkbox) {
                var label = checkbox.querySelector('label').textContent.toLowerCase();
                if (label.includes(searchTerm)) {
                    checkbox.style.display = 'block';
                } else {
                    checkbox.style.display = 'none';
                }
            });
        } else if (selectedValue === 'Zipcode') {
            var checkboxes = document.querySelectorAll('#zipcode-list .checkbox');
            checkboxes.forEach(function(checkbox) {
                var label = checkbox.querySelector('label').textContent.toLowerCase();
                if (label.includes(searchTerm)) {
                    checkbox.style.display = 'block';
                } else {
                    checkbox.style.display = 'none';
                }
            });
        } else if (selectedValue === 'Community') {
            var checkboxes = document.querySelectorAll('#community-list .checkbox');
            checkboxes.forEach(function(checkbox) {
                var label = checkbox.querySelector('label').textContent.toLowerCase();
                if (label.includes(searchTerm)) {
                    checkbox.style.display = 'block';
                } else {
                    checkbox.style.display = 'none';
                }
            });
        }
    });
});
