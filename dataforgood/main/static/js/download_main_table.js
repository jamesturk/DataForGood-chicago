function downloadTableAsExcel() {
    var table = document.getElementById("main-table");
    var wb = XLSX.utils.table_to_book(table);
    XLSX.writeFile(wb, "main-table.xlsx");
}

function downloadTableAsCSV() {
    var table = document.getElementById("main-table");
    var csv = [];
    var rows = table.querySelectorAll("tr");

    for (var i = 0; i < rows.length; i++) {
        var row = [], cols = rows[i].querySelectorAll("td, th");

        for (var j = 0; j < cols.length; j++) {
            row.push(cols[j].innerText);
        }

        csv.push(row.join(","));
    }

    var csvString = csv.join("\n");
    var blob = new Blob([csvString], { type: "text/csv;charset=utf-8;" });

    if (navigator.msSaveBlob) { // IE 10+
        navigator.msSaveBlob(blob, "main-table.csv");
    } else {
        var link = document.createElement("a");
        if (link.download !== undefined) {
            var url = URL.createObjectURL(blob);
            link.setAttribute("href", url);
            link.setAttribute("download", "main-table.csv");
            link.style.visibility = 'hidden';
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        }
    }
}