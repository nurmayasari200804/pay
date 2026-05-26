function copy(text, label) {
    navigator.clipboard.writeText(text).then(() => {
        const toast = document.getElementById('toast');
        toast.innerText = "✨ " + label + " berhasil disalin!";
        toast.style.opacity = '1';
        setTimeout(() => {
            toast.style.opacity = '0';
        }, 2000);
    }).catch(err => {
        console.error('Gagal menyalin text: ', err);
    });
}