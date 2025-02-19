document.addEventListener("DOMContentLoaded", function () {
    var ctx = document.getElementById("stockChart").getContext("2d");
    
    var itemNames = JSON.parse(document.getElementById("stockChart").dataset.names);
    var itemStocks = JSON.parse(document.getElementById("stockChart").dataset.stocks);

    new Chart(ctx, {
        type: "bar",
        data: {
            labels: itemNames,
            datasets: [{
                label: "Stok Barang",
                data: itemStocks,
                backgroundColor: "rgba(54, 162, 235, 0.6)",
                borderColor: "rgba(54, 162, 235, 1)",
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false, // Ubah menjadi false agar bisa dikendalikan dengan CSS
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        stepSize: 1 // Biar nilai stok tidak ada angka desimal
                    }
                }
            }
        }
    });
});
