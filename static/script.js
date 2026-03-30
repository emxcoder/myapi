

document.getElementById('year').textContent = new Date().getFullYear();
document.getElementById('vbu').addEventListener('click', clicked)

async function clicked() {
    const res = await fetch('/products', {
        method: 'GET'
    })
    const data = await res.json()

    document.getElementById('nome').innerText = 'EMXCODER'
}

