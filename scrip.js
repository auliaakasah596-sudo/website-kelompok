// Menunggu hingga seluruh konten halaman dimuat
document.addEventListener('DOMContentLoaded', function() {

    // Mengambil semua tombol dengan class 'btn-pesan'
    const tombolPesan = document.querySelectorAll('.btn-pesan');

    // Menambahkan event listener untuk setiap tombol
    tombolPesan.forEach(function(tombol) {
        tombol.addEventListener('click', function() {
            // Menampilkan pesan sederhana saat tombol diklik
            alert('Terima kasih! Silakan hubungi kami melalui email di kontak@digitalkreatif.com untuk pemesanan.');
        });
    });

});