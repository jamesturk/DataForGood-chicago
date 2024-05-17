$(document).ready(function() {
    $('#id_geographic_level').change(function() {
        var selectedValue = $(this).val();
        if (selectedValue === 'Community') {
            $('#community_field').show();
            $('#tract_field').hide();
            $('#zipcode_field').hide();
        } else if (selectedValue === 'Zipcode') {
            $('#community_field').hide();
            $('#tract_field').hide();
            $('#zipcode_field').show();
        } else if (selectedValue === 'Tract') {
            $('#community_field').hide();
            $('#tract_field').show();
            $('#zipcode_field').hide();
        } else {
            $('#community_field').hide();
            $('#tract_field').hide();
            $('#zipcode_field').hide();
        }
    });

    function capitalizeText(text) {
        return text.toLowerCase().replace(/(?:^|\s)\S/g, function(a) { return a.toUpperCase(); });
    }

    document.addEventListener('DOMContentLoaded', function() {
        const labels = document.querySelectorAll('#community-list label');
        labels.forEach(function(label) {
            label.textContent = capitalizeText(label.textContent);
        });
    });
});

document.addEventListener('DOMContentLoaded', function() {
const geoLevelSelect = document.getElementById('id_geographic_level');
const tractField = document.getElementById('tract_field');
const zipcodeField = document.getElementById('zipcode_field');
const communityField = document.getElementById('community_field');

const categorySelect = document.getElementById('id_category');
const economicField = document.getElementById('economic_field');
const educationField = document.getElementById('education_field');
const healthField = document.getElementById('health_field');
const housingField = document.getElementById('housing_field');
const populationField = document.getElementById('population_field');



function handleGeoLevelChange() {
const selectedValue = geoLevelSelect.value;
// Hide all fields initially
tractField.style.display = 'none';
zipcodeField.style.display = 'none';
communityField.style.display = 'none';
// Show relevant field based on the selection
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
const selectedValue = categorySelect.value;
// Hide all fields initially
economicField.style.display = 'none';
educationField.style.display = 'none';
healthField.style.display = 'none';
housingField.style.display = 'none';
populationField.style.display = 'none';
// Show relevant field based on the selection
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

// function to select/remove all for years
function toggleYearSelection(source) {
checkboxes = document.querySelectorAll('[name="year"]');
for(var i = 0, n = checkboxes.length; i < n; i++) {
checkboxes[i].checked = source.checked;
}
};

// function to select/remove all for tracts
function toggleTractSelection(source) {
var checkboxes = document.querySelectorAll('input[name="tract"]');
for (var i = 0, n = checkboxes.length; i < n; i++) {
checkboxes[i].checked = source.checked;
}
};

// function to select/remove all for zipcodes
function toggleZipcodeSelection(source) {
var checkboxes = document.querySelectorAll('input[name="zipcode"]');
for (var i = 0, n = checkboxes.length; i < n; i++) {
checkboxes[i].checked = source.checked;
}
};

$(document).ready(function() {
// Show/hide search input based on selected geographic level
$('#id_geographic_level').change(function() {
var selectedValue = $(this).val();
if (selectedValue === 'Tract' || selectedValue === 'Zipcode' || selectedValue === 'Community') {
    $('#search-container').show();
} else {
    $('#search-container').hide();
}
});

$('#search-input').on('input', function() {
var searchTerm = $(this).val().toLowerCase();
var selectedValue = $('#id_geographic_level').val();

if (selectedValue === 'Tract') {
    $('#tract-list .checkbox').each(function() {
        var label = $(this).find('label').text().toLowerCase();
        if (label.includes(searchTerm)) {
            $(this).show();
        } else {
            $(this).hide();
        }
    });
} else if (selectedValue === 'Zipcode') {
    $('#zipcode-list .checkbox').each(function() {
        var label = $(this).find('label').text().toLowerCase();
        if (label.includes(searchTerm)) {
            $(this).show();
        } else {
            $(this).hide();
        }
    });
} else if (selectedValue === 'Community') {
    $('#community-list .checkbox').each(function() {
        var label = $(this).find('label').text().toLowerCase();
        if (label.includes(searchTerm)) {
            $(this).show();
        } else {
            $(this).hide();
        }
    });
}
});
});