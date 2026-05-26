function copyToClipboard(number, bankName) {
    navigator.clipboard.writeText(number).then(() => {
        showToast(`Nomor ${bankName} berhasil disalin!`);
    }).catch(err => {
        console.error('Gagal menyalin: ', err);
    });
}

function showToast(message) {
    let toast = document.getElementById('toast');
    if (!toast) {
        toast = document.createElement('div');
        toast.id = 'toast';
        toast.className = 'toast';
        document.body.appendChild(toast);
    }
    toast.innerText = message;
    toast.style.opacity = '1';
    
    setTimeout(() => {
        toast.style.opacity = '0';
    }, 2000);
}